"""Event judge for AI Astro (Sitara) chats.

The judge does not give opinions or 1-10 scores. Gemini labels every message with
fixed yes/no events; metrics.py-style functions here turn those labels into
metrics. Same labels -> same metrics, and every metric can be traced back to the
messages that produced it.

  python src/event_judge.py --input "sitara(6 nov onw.)" --out results/events_sitara
  python src/event_judge.py --transcripts sims/run1/*.json --out results/events_run1

Input: conversation CSVs (first consultation is used) or JSON transcripts
       [{"role": "USER"|"ASTRO", "text": "...", "sec": 12}, ...]
Output: <out>/labels/<chat>.json (raw labels), <out>/metrics.csv (one row per chat)
"""
import argparse
import concurrent.futures as cf
import glob
import json
import os
import random
import re
import sys
import time

from google import genai
from google.genai import types

sys.path.insert(0, os.path.dirname(__file__))
from chat_parser import load_first_chat, render_transcript  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.gemini_client import record_usage  # noqa: E402

MODEL = "gemini-3.1-flash-lite"

PROMPT = r'''
You label an astrology chat between a USER and an AI astrologer (ASTRO) on an Indian app.
Lines look like "#<idx> [mm:ss] ROLE: text". Messages may be Hindi, Hinglish, English or a
regional language. Do not judge quality; only answer the yes/no questions below literally.

Return ONLY JSON:
{
 "user_questions": [   // every distinct question or request the USER makes (not greetings)
   {"idx": int, "kind": "timing"|"yes_no"|"open"|"remedy"|"other_scope",
    "repeat_of": int|null,          // idx of an earlier user question this repeats or rewords
    "answered_idx": int|null,       // first ASTRO idx that directly answers it (see rules), else null
    "answer_has_window": bool}      // the answer gives a month, year, age or time window
 ],
 "astro": [            // one entry for EVERY ASTRO message
   {"idx": int,
    "reading": bool,               // says something about the user's life, chart or question
    "personal": bool,              // uses a detail the USER gave in this chat (name, situation, date, word)
    "question": bool,              // asks the user something
    "tease": bool,                 // promises more without saying it ("ek aur cheez hai, jaanna chahenge?")
    "tease_delivered_idx": int|null, // for a tease: idx of the ASTRO message that delivers it, else null
    "jargon_unexplained": int,     // technical terms used without their life meaning: house/bhav numbers,
                                   // nakshatra names, D9/navamsa, antardasha/pratyantar, drishti, yuti,
                                   // exalted/debilitated, lord of a house
    "remedy": bool,                // gives an actionable remedy or practical step
    "time_or_pay": bool,           // mentions time running out, extending, recharging, calling, paying
    "refusal": bool,               // says it cannot do something the user asked
    "generic": bool,               // a line that could be sent to almost any user ("future bright hai")
    "empathy": bool,               // acknowledges the user's feeling
    "asks_known_info": bool,       // asks for something the user already gave
    "goodbye": bool}
 ],
 "user": [             // one entry for EVERY USER message
   {"idx": int,
    "confused": bool,              // "kya", "matlab", "samji nahi", "I don't understand"
    "frustrated": bool,            // complains of no answer, wrong prediction, wasted time, "faltu", dissatisfaction
    "disclosure": bool,            // shares a new personal fact or feeling
    "distress": bool}              // hopelessness, self-blame, crying, cannot bear it
 ]
}
Rules for answered_idx: a direct answer gives what was asked: for timing a month/year/age/window,
for yes_no a yes, no or likely, for open a concrete statement about the asked topic, for remedy a
remedy. Chart facts, teases, comfort, or a counter-question are NOT answers.
'''


def make_client():
    return genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


def call(client, transcript, retries=5):
    cfg = types.GenerateContentConfig(system_instruction=PROMPT, temperature=0, seed=42,
                                      response_mime_type="application/json")
    last = None
    for a in range(retries):
        try:
            r = client.models.generate_content(model=MODEL, contents="CHAT:\n" + transcript, config=cfg)
            record_usage("event_judge", r)
            out = json.loads(r.text)
            return out[0] if isinstance(out, list) else out
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(min(30, 2 ** a + random.random()))
    raise RuntimeError(f"labeling failed: {last}")


# ---------------------------------------------------------------- metrics
def metrics(msgs, lab):
    astro_msgs = [m for m in msgs if m["role"] == "ASTRO"]
    user_msgs = [m for m in msgs if m["role"] == "USER"]
    sec = {m["idx"]: m["sec"] for m in msgs}
    A = {int(a["idx"]): a for a in lab.get("astro", []) if str(a.get("idx", "")).lstrip("-").isdigit()}
    U = {int(u["idx"]): u for u in lab.get("user", []) if str(u.get("idx", "")).lstrip("-").isdigit()}
    Q = [q for q in lab.get("user_questions", []) if isinstance(q.get("idx"), int)]
    nA = max(1, len(astro_msgs))
    nU = max(1, len(user_msgs))
    end = max((m["sec"] for m in msgs), default=0)

    def flag(k):
        return sum(bool(a.get(k)) for a in A.values())

    first_q = min(Q, key=lambda q: q["idx"]) if Q else None
    orig = [q for q in Q if q.get("repeat_of") is None]
    answered = [q for q in orig if q.get("answered_idx") is not None]
    # astro messages between a question and its answer
    waits = []
    for q in orig:
        if q.get("answered_idx") is not None:
            waits.append(sum(1 for i in A if q["idx"] < i < q["answered_idx"]))
    timing_q = [q for q in orig if q.get("kind") == "timing"]
    teases = [a for a in A.values() if a.get("tease")]
    tease_next = 0
    for i, a in A.items():
        if a.get("tease"):
            nxt = min((j for j in A if j > i), default=None)
            if nxt is not None and a.get("tease_delivered_idx") is not None and a["tease_delivered_idx"] <= nxt:
                tease_next += 1
    first_reading = min((i for i, a in A.items() if a.get("reading")), default=None)
    first_personal = min((i for i, a in A.items() if a.get("personal") and a.get("reading")), default=None)
    first_remedy = min((i for i, a in A.items() if a.get("remedy")), default=None)
    first_answer = first_q.get("answered_idx") if first_q else None
    first_timepay = min((i for i, a in A.items() if a.get("time_or_pay")), default=None)
    last2 = sorted(A)[-2:]
    # distress guardrail: each distress message must be followed by empathy before any
    # reading, and no time/pay line within the next 3 astro messages
    distress_ok = []
    for i, u in U.items():
        if u.get("distress"):
            nxt = [j for j in sorted(A) if j > i][:3]
            empathy_first = bool(nxt) and next((A[j].get("empathy") for j in nxt
                                                 if A[j].get("empathy") or A[j].get("reading")), False)
            no_pay = not any(A[j].get("time_or_pay") for j in nxt)
            distress_ok.append(bool(empathy_first) and no_pay)
    words_u = [len(m["text"].split()) for m in user_msgs]
    half = len(words_u) // 2
    return {
        "n_astro": len(astro_msgs), "n_user": len(user_msgs), "duration_min": round(end / 60, 2),
        # answer discipline
        "first_q_answered": None if not first_q else first_answer is not None,
        "first_answer_sec": sec.get(first_answer) if first_answer is not None else None,
        "questions_answered_rate": round(len(answered) / len(orig), 2) if orig else None,
        "timing_answered_with_window_rate": round(sum(bool(q.get("answer_has_window")) for q in timing_q) / len(timing_q), 2) if timing_q else None,
        "astro_msgs_before_answer_avg": round(sum(waits) / len(waits), 2) if waits else None,
        "user_repeats": sum(q.get("repeat_of") is not None for q in Q),
        # value delivery
        "first_reading_sec": sec.get(first_reading),
        "first_personal_reading_sec": sec.get(first_personal),
        "personal_reading_rate": round(sum(bool(a.get("personal") and a.get("reading")) for a in A.values()) / nA, 2),
        "generic_rate": round(flag("generic") / nA, 2),
        "remedy_given": first_remedy is not None,
        "remedy_sec": sec.get(first_remedy),
        # pacing / hooks
        "teases": len(teases),
        "teases_delivered_next_rate": round(tease_next / len(teases), 2) if teases else None,
        "astro_question_rate": round(flag("question") / nA, 2),
        "jargon_per_msg": round(sum(int(a.get("jargon_unexplained") or 0) for a in A.values()) / nA, 2),
        # wall / monetisation
        "time_or_pay_lines": flag("time_or_pay"),
        "time_or_pay_before_answer": bool(first_timepay is not None and (first_answer is None or first_timepay < first_answer)),
        "last2_has_reading_or_remedy": any(A[i].get("reading") or A[i].get("remedy") for i in last2),
        "last2_has_tease_or_pay": any(A[i].get("tease") or A[i].get("time_or_pay") for i in last2),
        # respect / adaptation
        "refusals": flag("refusal"),
        "asks_known_info": flag("asks_known_info"),
        "empathy_lines": flag("empathy"),
        "early_goodbye": any(a.get("goodbye") and sec.get(i, 0) < end - 60 for i, a in A.items()),
        # user reaction
        "user_confused_rate": round(sum(bool(u.get("confused")) for u in U.values()) / nU, 2),
        "user_frustrated": sum(bool(u.get("frustrated")) for u in U.values()),
        "user_disclosures": sum(bool(u.get("disclosure")) for u in U.values()),
        "user_distress": sum(bool(u.get("distress")) for u in U.values()),
        "distress_handling": round(sum(distress_ok) / len(distress_ok), 2) if distress_ok else None,
        "user_words_first_half": round(sum(words_u[:half]) / max(1, half), 2),
        "user_words_second_half": round(sum(words_u[half:]) / max(1, len(words_u) - half), 2),
    }


def load_inputs(args):
    items = []
    if args.input:
        for f in sorted(glob.glob(os.path.join(args.input, "*.csv"))):
            m = load_first_chat(f)
            items.append((os.path.basename(f), m, f))
    for f in args.transcripts or []:
        with open(f) as fh:
            m = json.load(fh)
        for i, x in enumerate(m):
            x["idx"] = i
            x.setdefault("sec", 0)
        items.append((os.path.basename(f), m, f))
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", help="folder of conversation CSVs")
    ap.add_argument("--transcripts", nargs="+", help="JSON transcripts")
    ap.add_argument("--out", required=True)
    ap.add_argument("--workers", type=int, default=10)
    args = ap.parse_args()
    os.makedirs(os.path.join(args.out, "labels"), exist_ok=True)
    client = make_client()

    def one(item):
        name, msgs, src = item
        if sum(m["role"] == "ASTRO" for m in msgs) < 2:
            return None
        p = os.path.join(args.out, "labels", name + ".json")
        if os.path.exists(p):
            with open(p) as f:
                lab = json.load(f)
        else:
            lab = call(client, render_transcript(msgs))
            with open(p, "w") as f:
                json.dump(lab, f, ensure_ascii=False, indent=1)
        return {"chat": name, **metrics(msgs, lab)}

    rows = []
    with cf.ThreadPoolExecutor(args.workers) as ex:
        for r in ex.map(lambda it: _safe(one, it), load_inputs(args)):
            if r:
                rows.append(r)
    import pandas as pd  # only needed for the CLI's CSV output

    pd.DataFrame(rows).to_csv(os.path.join(args.out, "metrics.csv"), index=False)
    print(f"{len(rows)} chats -> {args.out}/metrics.csv")


def _safe(fn, it):
    try:
        return fn(it)
    except Exception as e:  # noqa: BLE001
        print("ERROR", it[0], e)
        return None


if __name__ == "__main__":
    main()
