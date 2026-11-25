"""
Cliffhanger payoff test. Each case starts the chat at about 02:00 with a cliffhanger of one type
already said by the bot, then the user either asks about it ("Kya baat hai?") or does not ("Ok").
The bot replies for 3 turns; a judge checks whether the cliffhanger was paid off within 2 replies
with a concrete detail from the data, whether a remedy followed the payoff, and any "agli baar".

  python src/cliffhanger_test.py i33 i34 --runs 2
"""

import argparse
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", ".env"))

from src.astro_bot import AstroBot
from src.gemini_client import generate_json
from src.sitara_orchestrator import CHART_PROFILE, RESULTS_ROOT

# (type, user's opening question, bot's earlier answer + cliffhanger, the data line it is built on)
CASES = [
    ("person", "Meri shaadi kab hogi?",
     "Shaadi ka yog March 2027 se ban raha hai, rishta jaan-pehchaan se aayega. Shaadi se pehle ek rishta aayega jise pehchanna zaroori hai.",
     "Likely an arranged match, possibly through known circles."),
    ("hidden nature", "Mera hone wala partner kaisa hoga?",
     "Partner padhe-likhe aur shaant nature ke honge. Par unka ek chupa hua pehlu bhi hai jo jaanna zaroori hai.",
     "Partner: tall, calm, educated and warm, with a guarded side."),
    ("mistake", "Paisa haath mein kyun nahi rukta?",
     "Paisa abhi tight hai, 2028 tak halat behtar hogi. Paise ke liye kundli mein ek chhoti si galti dikh rahi hai jo aap baar baar kar rahe hain.",
     "Money doesn't stay because the 2H is low and Chandra is weak."),
    ("opportunity", "Naukri kab lagegi?",
     "Naukri ka achha yog March 2027 se ban raha hai. Career mein ek bada mauka aane wala hai, bas ek galti se bachna hoga.",
     "Going abroad: 2027-2028 is possible."),
    ("decision", "Job change karun ya nahi?",
     "Abhi wali jagah mein thoda aur tikna sahi rahega. 2027 mein ek decision aapki naukri pakki kar sakta hai.",
     "Job first, then business in trade or services."),
    ("sign to watch", "Ghar ki tension kab khatam hogi?",
     "Ghar ka mahaul dheere dheere shaant hoga. Tension khatam hone se pehle ek sanket milega, use pehchanna zaroori hai.",
     "Mixed now; 2027 brings relief after Feb and Jun."),
    ("new field", "Mere liye kaunsa kaam sahi hai?",
     "Aapke liye mehnat wala kaam achha rahega. Career mein ek naya raasta khulne wala hai jiska aapko andaaza nahi.",
     "Best fields: teaching, finance, communication, tech and media."),
]
USER_MODES = {"asks": "Kya baat hai? Batao.", "ignores": "Ok."}
FOLLOW_UPS = ["Achha.", "Theek hai."]

JUDGE_PROMPT = """You check one astrology chat. The ASTRO made a cliffhanger (a hint that holds back a detail)
in the message marked CLIFFHANGER. It was most likely built on this data line (the payoff may use another fact): {line}
Read the ASTRO replies after it (R1, R2, R3) and answer literally:
- payoff_reply: the first reply (1, 2 or 3) that resolves the cliffhanger: it says what the hinted thing actually is
  (which rishta/person, what hidden side, what mistake, what opportunity, what decision, what sign, what field),
  concretely, not another hint and not just general talk on the topic; null if none.
- payoff_concrete: true if that payoff states a concrete fact (it may use any astrology fact, not only the line above).
- remedy_reply: the first reply (1, 2 or 3) that gives a remedy (mantra, daan, fast, practice) with what it helps; null if none.
- agli_baar: true if any reply defers something to a later chat ("agli baar", "next time", "agle session").
Return JSON: {{"payoff_reply": int|null, "payoff_concrete": bool, "remedy_reply": int|null, "agli_baar": bool}}"""


def run_case(version, case, mode, run):
    kind, question, cliffhanger, line = case
    bot = AstroBot(prompt_version=version, user_profile=dict(CHART_PROFILE, elapsed_time="02:00"))
    bot._history = [{"role": "user", "text": question}, {"role": "model", "text": cliffhanger}]
    replies = []
    for i, user_text in enumerate([USER_MODES[mode]] + FOLLOW_UPS):
        bot.user_profile["elapsed_time"] = f"02:{30 * (i + 1):02d}" if i < 1 else f"03:{30 * (i - 1):02d}"
        replies.append(bot.respond_to(user_text))
    transcript = "\n".join(
        [f"USER: {question}", f"ASTRO (CLIFFHANGER): {cliffhanger}"]
        + [f"USER: {u}\nASTRO R{i + 1}: {r}" for i, (u, r) in enumerate(zip([USER_MODES[mode]] + FOLLOW_UPS, replies))]
    )
    verdict = generate_json(JUDGE_PROMPT.format(line=line), [{"role": "user", "text": transcript}],
                            temperature=0, model="gemini-3.1-flash-lite", role="judge")
    return {"version": version, "type": kind, "mode": mode, "run": run, "transcript": transcript, **verdict}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("versions", nargs="+")
    ap.add_argument("--runs", type=int, default=2)
    args = ap.parse_args()
    jobs = [(v, c, m, r) for v in args.versions for c in CASES for m in USER_MODES for r in range(1, args.runs + 1)]
    with ThreadPoolExecutor(14) as pool:
        results = list(pool.map(lambda j: run_case(*j), jobs))
    for v in args.versions:
        out = os.path.join(RESULTS_ROOT, v, "cliffhanger_test.json")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        rows = [r for r in results if r["version"] == v]
        with open(out, "w") as f:
            json.dump(rows, f, ensure_ascii=False, indent=2)

    print("| Version | Type | User | Paid off ≤2 replies | Concrete | Remedy after payoff | 'agli baar' |")
    print("|---|---|---|---|---|---|---|")
    for v in args.versions:
        for kind, *_ in CASES:
            for mode in USER_MODES:
                rows = [r for r in results if r["version"] == v and r["type"] == kind and r["mode"] == mode]
                paid = [r for r in rows if r.get("payoff_reply") and r["payoff_reply"] <= 2]
                conc = [r for r in paid if r.get("payoff_concrete")]
                rem = [r for r in paid if r.get("remedy_reply") and r["remedy_reply"] in (r["payoff_reply"], r["payoff_reply"] + 1)]
                agli = sum(bool(r.get("agli_baar")) for r in rows)
                print(f"| {v} | {kind} | {mode} | {len(paid)}/{len(rows)} | {len(conc)}/{len(rows)} | {len(rem)}/{len(rows)} | {agli} |")
    for v in args.versions:
        rows = [r for r in results if r["version"] == v]
        paid = [r for r in rows if r.get("payoff_reply") and r["payoff_reply"] <= 2]
        rem = [r for r in paid if r.get("remedy_reply") and r["remedy_reply"] in (r["payoff_reply"], r["payoff_reply"] + 1)]
        print(f"{v} TOTAL: paid off {len(paid)}/{len(rows)}, concrete {sum(bool(r.get('payoff_concrete')) for r in paid)}/{len(rows)}, "
              f"remedy after payoff {len(rem)}/{len(rows)}, 'agli baar' {sum(bool(r.get('agli_baar')) for r in rows)}")


if __name__ == "__main__":
    main()
