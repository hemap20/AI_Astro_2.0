"""
Scores saved chats with the First-Chat Rubric Framework
(/Users/hemapunyamoorty/Desktop/judge_llm_astro/personas/rubrics.md).

Judged rubrics and the gate come from one LLM call per chat that applies the rubric text.
Counted rubrics (1.3, 4.1, 4.3) are computed here from the transcript, using the judge's
per-message labels (question / reading) for 1.3.

  python src/rubric_judge.py i40 i40_haiku --workers 12
"""

import argparse
import collections
import glob
import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", ".env"))

from src.gemini_client import generate_json
from src.sitara_orchestrator import RESULTS_ROOT

RUBRIC_PATH = "/Users/hemapunyamoorty/Desktop/judge_llm_astro/personas/rubrics.md"
JUDGE_MODEL = os.environ.get("RUBRIC_JUDGE_MODEL", "gemini-3.1-flash-lite")
JUDGED = ["1.1", "1.2", "1.4", "2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7", "3.1", "3.2", "3.3", "4.2", "5.1"]
COUNTED = ["1.3", "4.1", "4.3"]
BUCKETS = {"1": "Understanding", "2": "Prediction", "3": "Momentum", "4": "Human feel", "5": "Difficult user"}
ALLOWED = {1, 3, 4, 6, 7, 8, 9, 10}

SYSTEM = """You are a strict judge applying the rubric framework below to ONE astrology chat.
Follow its fixed order exactly: skip check, Low rules first, otherwise the highest rule fully true
(start from 10 and go down), and every yes needs a quoted line from the chat (no quote means no).
Only the scores 1, 3, 4, 6, 7, 8, 9, 10 exist.

Score the gate checks G1-G4 and these judged rubrics: {judged}.
Do NOT score the counted rubrics 1.3, 4.1, 4.3; instead label every ASTRO message (by idx) as
"reading" (states something about the user's life, chart, an answer or guidance), "question" (only asks),
"both" (a reading and a question), or "other" (greeting, filler, close without reading).

<rubrics>
{rubrics}
</rubrics>"""

SCHEMA_HINT = """{"gate": {"G1": {"fail": bool, "quote": str}, "G2": {...}, "G3": {...}, "G4": {...}},
 "rubrics": {"1.1": {"skipped": bool, "score": int|null, "quote": str, "why": str}, ... one key per judged rubric},
 "labels": [{"idx": int, "type": "reading"|"question"|"both"|"other"}]}"""


def chats(version):
    for path in sorted(glob.glob(os.path.join(RESULTS_ROOT, version, "*", "*", "run_*", "session_*", "transcript.json"))):
        with open(path) as f:
            yield path, json.load(f)


def _words(t):
    return re.findall(r"\w+", t.lower())


def counted(msgs, labels):
    astro = [m for m in msgs if m["role"] == "ASTRO"]
    kinds = {l["idx"]: l["type"] for l in labels}
    out = {}

    # 1.3 Gets to the reading
    seq = [kinds.get(m["idx"], "other") for m in astro]
    is_q = [k in ("question", "both") for k in seq]
    is_r = [k in ("reading", "both") for k in seq]
    if not any(is_r):
        out["1.3"] = 1
    else:
        first_r = is_r.index(True)
        Q = sum(is_q[:first_r]) + (seq[first_r] == "both" and 0)
        T = sum(is_q)
        R = run = 0
        for k in seq:
            if k == "question":
                run += 1
            elif k in ("reading", "both"):
                run = 1 if k == "both" else 0
            R = max(R, run)
        if Q >= 5: s = 3
        elif Q == 4 or R >= 3: s = 4
        elif Q == 3: s = 6
        elif Q <= 1 and T <= 3 and R <= 1: s = 10
        elif T <= 3: s = 9
        elif T == 4: s = 8
        else: s = 7
        out["1.3"] = s

    # 4.1 Message shape (first 5 minutes)
    first5 = [m for m in astro if m["sec"] <= 300]
    wc = [len(m["text"].split()) for m in first5] or [0]
    M = len(first5)
    long_share = sum(w > 30 for w in wc) / max(M, 1)
    bursts, run = 0, 0
    for m in msgs:
        run = run + 1 if m["role"] == "ASTRO" else 0
        if run == 4:
            bursts += 1
    listy = any(re.search(r"^\s*(\d+[.)]|[-*•])\s", m["text"], re.M) for m in first5)
    if long_share > 0.5 or listy: s = 1
    elif long_share >= 0.25 or M > 24 or M < 5: s = 3
    elif max(wc) > 60 or 21 <= M <= 24: s = 4
    elif long_share >= 0.10 or 17 <= M <= 20 or 5 <= M <= 7 or bursts >= 2: s = 6
    elif max(wc) <= 25 and 10 <= M <= 14 and bursts == 0:
        s = 10 if sum(wc) / M <= 15 else 9
    elif long_share == 0: s = 8
    else: s = 7
    out["4.1"] = s
    out["_shape"] = {"M": M, "avg_words": round(sum(wc) / max(M, 1), 1), "long_share": round(long_share, 2)}

    # 4.3 Not repetitive
    sents = [_words(x) for m in astro for x in re.split(r"[.?!]+", m["text"]) if len(_words(x)) >= 4]
    rep = 0
    for i, a in enumerate(sents):
        for b in sents[:i]:
            if abs(len(a) - len(b)) <= 2 and len(set(a) ^ set(b)) <= 4 and len(set(a) - set(b)) <= 2:
                rep += 1
                break
    openers = collections.Counter(" ".join(_words(m["text"])[:2]) for m in astro)
    top = max(openers.values()) if openers else 0
    if rep >= 6: s = 1
    elif rep >= 4: s = 3
    elif rep == 3: s = 4
    elif rep == 2 or top >= 4: s = 6
    elif rep == 1: s = 7
    elif top == 3: s = 8
    elif top == 2: s = 9
    else: s = 10
    out["4.3"] = s
    out["_rep"] = {"rep": rep, "top_opener": top}
    return out


def judge(path, msgs, rubrics_text):
    out_path = os.path.join(os.path.dirname(path), "rubric_scores.json")
    if os.path.exists(out_path):
        with open(out_path) as f:
            return json.load(f)
    transcript = "\n".join(f"[{m['idx']}] [{m['sec'] // 60:02d}:{m['sec'] % 60:02d}] {m['role']}: {m['text']}" for m in msgs)
    v = generate_json(SYSTEM.format(judged=", ".join(JUDGED), rubrics=rubrics_text),
                      [{"role": "user", "text": transcript}], schema_hint=SCHEMA_HINT,
                      temperature=0, model=JUDGE_MODEL, role="judge")
    if isinstance(v, list):
        v = v[0]
    scores = {}
    for k in JUDGED:
        r = (v.get("rubrics") or {}).get(k) or {}
        sc = r.get("score")
        scores[k] = None if r.get("skipped") or sc not in ALLOWED else sc
    c = counted(msgs, v.get("labels") or [])
    scores.update({k: c[k] for k in COUNTED})
    gate_fail = [g for g, x in (v.get("gate") or {}).items() if isinstance(x, dict) and x.get("fail")]
    vals = [s for s in scores.values() if s is not None]
    overall = sum(vals) / len(vals)
    if gate_fail:
        overall = min(overall, 3)
    res = {"scores": scores, "gate_fail": gate_fail, "overall": round(overall, 2),
           "shape": c["_shape"], "rep": c["_rep"], "judge": v}
    with open(out_path, "w") as f:
        json.dump(res, f, ensure_ascii=False, indent=2)
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("versions", nargs="+")
    ap.add_argument("--workers", type=int, default=12)
    args = ap.parse_args()
    with open(RUBRIC_PATH) as f:
        rubrics_text = f.read()
    jobs = [(v, p, m) for v in args.versions for p, m in chats(v)]

    def run(j):
        try:
            return j[0], judge(j[1], j[2], rubrics_text)
        except Exception as e:  # noqa: BLE001
            print("FAILED", j[1], e, flush=True)
            return j[0], None

    with ThreadPoolExecutor(args.workers) as pool:
        results = list(pool.map(run, jobs))

    keys = sorted(JUDGED + COUNTED, key=lambda k: tuple(map(int, k.split("."))))
    print("| Rubric | " + " | ".join(args.versions) + " |")
    print("|---|" + "---|" * len(args.versions))
    table = {}
    for v in args.versions:
        rs = [r for vv, r in results if vv == v and r]
        table[v] = rs
    for k in keys:
        row = []
        for v in args.versions:
            xs = [r["scores"][k] for r in table[v] if r["scores"].get(k) is not None]
            row.append(f"{sum(xs) / len(xs):.1f} (n={len(xs)})" if xs else "–")
        print(f"| {k} | " + " | ".join(row) + " |")
    for b, name in BUCKETS.items():
        row = []
        for v in args.versions:
            xs = [r["scores"][k] for r in table[v] for k in keys if k.startswith(b + ".") and r["scores"].get(k) is not None]
            row.append(f"{sum(xs) / len(xs):.2f}" if xs else "–")
        print(f"| **Bucket {b} {name}** | " + " | ".join(row) + " |")
    print("| Gate fails | " + " | ".join(
        f"{sum(bool(r['gate_fail']) for r in table[v])}/{len(table[v])} "
        f"{dict(collections.Counter(g for r in table[v] for g in r['gate_fail']))}" for v in args.versions) + " |")
    print("| **Overall (gate-capped)** | " + " | ".join(
        f"**{sum(r['overall'] for r in table[v]) / len(table[v]):.2f}**" for v in args.versions) + " |")


if __name__ == "__main__":
    main()
