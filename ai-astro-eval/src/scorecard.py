"""
Scorecard v2 for one prompt version: raw metric values (no 1-10 scores, no
composite) aggregated over cases × persona variants × runs, the simulated
user's VERDICT rates, and — with a baseline version — metrics_v2.DECISION_RULE.
For every DRIVER that misses its target, prints its prompt lever and two
example message pairs from the labels. Writes results/<version>/scorecard_v2.md.
"""

import csv
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from metrics import metrics_v2 as M
from src.sitara_orchestrator import RESULTS_ROOT

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Numeric form of each metric's target string in metrics_v2 (op, value), for
# met/missed checks. Booleans are averaged into rates first.
TARGET_VALUE = {
    "first_q_answered": (">=", 1.0),
    "questions_answered_rate": (">=", 0.90),
    "time_or_pay_before_answer": ("<=", 0.0),
    "time_or_pay_lines": ("<=", 1.0),
    "refusals": ("<=", 0.0),
    "user_frustrated": ("<=", 0.0),
    "timing_answered_with_window_rate": (">=", 0.80),
    "jargon_per_msg": ("<=", 0.30),
    "teases": ("<=", 2.0),
    "remedy_given": (">=", 1.0),
    "distress_handling": (">=", 1.0),
    "asks_known_info": ("<=", 0.0),
    "early_goodbye": ("<=", 0.0),
}
SCORED = [m for m in M.METRICS if m["tier"] in ("DRIVER", "LEAD", "GUARDRAIL") and m["key"] in TARGET_VALUE]
VERDICT_KEYS = [("answered", "answered / understood"), ("would_continue", "would continue"), ("would_return", "would return")]


def load_runs(prompt_version):
    """One row per (case, variant, run, session)."""
    rows = []
    pattern = os.path.join(RESULTS_ROOT, prompt_version, "*", "*", "run_*", "session_*", "metrics.json")
    for path in sorted(glob.glob(pattern)):
        d = os.path.dirname(path)
        session, run, variant, case = d.split(os.sep)[-1], d.split(os.sep)[-2], d.split(os.sep)[-3], d.split(os.sep)[-4]
        verdict = _read(os.path.join(d, "verdict.json")) or {}
        if "understood" in verdict:
            verdict["answered"] = verdict["understood"]
        rows.append({"case": case, "variant": variant, "run": run, "session": session, "dir": d,
                     "metrics": _read(path), "verdict": verdict})
    return rows


def summarize(rows):
    """{metric_key: (mean, n, run_min, run_max)} plus verdict yes-rates."""
    out = {}
    for m in SCORED:
        vals = [float(r["metrics"][m["key"]]) for r in rows if r["metrics"].get(m["key"]) is not None]
        out[m["key"]] = (sum(vals) / len(vals), len(vals), min(vals), max(vals)) if vals else (None, 0, None, None)
    for key, _ in VERDICT_KEYS:
        vals = [r["verdict"][key].lower().startswith("y") for r in rows if r["verdict"].get(key)]
        out["verdict." + key] = (sum(vals) / len(vals), len(vals), None, None) if vals else (None, 0, None, None)
    return out


def meets(key, mean):
    op, target = TARGET_VALUE[key]
    return mean >= target if op == ">=" else mean <= target


def better(key, a, b):
    """True if value a is better than b for this metric's direction."""
    return a > b if M.METRICS_BY_KEY[key]["direction"] == "higher_is_better" else a < b


def decide(cand, base):
    """Applies metrics_v2.DECISION_RULE on pooled values. Returns (decision, reasons)."""
    reasons = []
    for m in SCORED:
        if m["tier"] != "GUARDRAIL":
            continue
        c, b = cand[m["key"]][0], base[m["key"]][0]
        if c is not None and b is not None and better(m["key"], b, c):
            reasons.append(f"GUARDRAIL worse: {m['key']} {b:.2f} -> {c:.2f}")
    toward, away = [], []
    for m in SCORED:
        if m["tier"] != "DRIVER":
            continue
        c, b = cand[m["key"]][0], base[m["key"]][0]
        if c is None or b is None:
            continue
        spread = (base[m["key"]][3] or 0) - (base[m["key"]][2] or 0)
        if better(m["key"], c, b):
            toward.append(m["key"])
        elif abs(c - b) > spread:
            away.append(m["key"])
    if len(toward) < 2:
        reasons.append(f"only {len(toward)} DRIVER(s) moved toward target ({', '.join(toward) or 'none'})")
    for k in away:
        reasons.append(f"DRIVER moved away beyond run-to-run spread: {k}")
    for key, _ in VERDICT_KEYS[1:]:
        c, b = cand["verdict." + key][0], base["verdict." + key][0]
        if c is not None and b is not None and c < b:
            reasons.append(f"VERDICT {key} dropped {b:.0%} -> {c:.0%}")
    return ("CANDIDATE for live A/B" if not reasons else "REJECT"), reasons


def examples(rows, key, limit=2):
    """Up to `limit` (user text, astro text) pairs showing a failure of `key`."""
    out = []
    for r in rows:
        msgs = _read(os.path.join(r["dir"], "transcript.json")) or []
        labels = _read(os.path.join(r["dir"], "labels.json")) or {}
        by_idx = {m["idx"]: m for m in msgs}

        def prev(i, role):
            return next((by_idx[j]["text"] for j in range(i - 1, -1, -1) if j in by_idx and by_idx[j]["role"] == role), "")

        def nxt(i, role):
            return next((m["text"] for m in msgs if m["idx"] > i and m["role"] == role), "")

        if key in ("first_q_answered", "questions_answered_rate"):
            qs = [q for q in labels.get("user_questions", []) if q.get("repeat_of") is None and q.get("answered_idx") is None]
            if key == "first_q_answered":
                qs = qs[:1] if qs and qs[0] == min(labels["user_questions"], key=lambda q: q["idx"]) else []
            pairs = [(by_idx.get(q["idx"], {}).get("text", ""), nxt(q["idx"], "ASTRO")) for q in qs]
        elif key in ("time_or_pay_before_answer", "time_or_pay_lines", "refusals"):
            flag = "refusal" if key == "refusals" else "time_or_pay"
            pairs = [(prev(a["idx"], "USER"), by_idx.get(a["idx"], {}).get("text", ""))
                     for a in labels.get("astro", []) if a.get(flag)]
        elif key == "user_frustrated":
            pairs = [(by_idx.get(u["idx"], {}).get("text", ""), prev(u["idx"], "ASTRO"))
                     for u in labels.get("user", []) if u.get("frustrated")]
        else:
            pairs = []
        for p in pairs:
            out.append((r["case"], r["variant"], r["session"], *p))
            if len(out) >= limit:
                return out
    return out


def _baseline_real():
    path = os.path.join(ROOT, "metrics", "baseline_scorecard.csv")
    with open(path) as f:
        return {row["metric"]: row["sitara_now"] for row in csv.DictReader(f)}


def _fmt(v):
    return "–" if v is None else f"{v:.2f}"


def write_scorecard(prompt_version, baseline_version=None):
    rows = load_runs(prompt_version)
    if not rows:
        raise SystemExit(f"no runs under results/{prompt_version}")
    pooled = summarize(rows)
    real = _baseline_real()
    base_pooled = summarize(load_runs(baseline_version)) if baseline_version else None

    L = [f"# Scorecard v2: {prompt_version}", "",
         f"{len(rows)} sessions from {len({(r['case'], r['variant'], r['run']) for r in rows})} runs. "
         "Raw values (booleans as share of sessions); `n` = sessions where the metric applied.", ""]

    head = "| Tier | Metric | Value | n | Target | Met | Real Sitara |" + (f" {baseline_version} |" if base_pooled else "")
    L += [head, "|" + "---|" * (head.count("|") - 1)]
    for m in SCORED:
        mean, n, _, _ = pooled[m["key"]]
        met = "–" if mean is None else ("✅" if meets(m["key"], mean) else "❌")
        line = f"| {m['tier']} | {m['key']} | {_fmt(mean)} | {n} | {m['target']} | {met} | {real.get(m['key'], '–')} |"
        if base_pooled:
            line += f" {_fmt(base_pooled[m['key']][0])} |"
        L.append(line)
    for key, name in VERDICT_KEYS:
        mean, n, _, _ = pooled["verdict." + key]
        line = f"| VERDICT | {name} | {_fmt(mean)} | {n} | – | – | – |"
        if base_pooled:
            line += f" {_fmt(base_pooled['verdict.' + key][0])} |"
        L.append(line)

    if base_pooled:
        decision, reasons = decide(pooled, base_pooled)
        L += ["", f"## Decision vs {baseline_version}: **{decision}**", ""]
        L += [f"- {r}" for r in reasons] or ["- all DECISION_RULE checks passed"]

    L += ["", "## Per case", ""]
    keys = [m["key"] for m in SCORED if m["tier"] == "DRIVER"]
    L += ["| Case | Session | Variant | n runs | " + " | ".join(keys) + " | would return |",
          "|" + "---|" * (len(keys) + 5)]
    groups = sorted({(r["case"], r["session"], r["variant"]) for r in rows})
    for case, session, variant in groups:
        g = summarize([r for r in rows if (r["case"], r["session"], r["variant"]) == (case, session, variant)])
        n_runs = sum(1 for r in rows if (r["case"], r["session"], r["variant"]) == (case, session, variant))
        L.append(f"| {case} | {session} | {variant} | {n_runs} | " + " | ".join(_fmt(g[k][0]) for k in keys)
                 + f" | {_fmt(g['verdict.would_return'][0])} |")

    L += ["", "## What to change (DRIVERs missing target)", ""]
    for m in SCORED:
        mean = pooled[m["key"]][0]
        if m["tier"] != "DRIVER" or mean is None or meets(m["key"], mean):
            continue
        L += [f"### {m['key']} = {mean:.2f} (target {m['target']})", f"Prompt lever: {m['prompt_lever']}", ""]
        for case, variant, session, user, astro in examples(rows, m["key"]):
            L += [f"- {case} / {variant} / {session}", f"  - USER: {user}", f"  - ASTRO: {astro}"]
        L.append("")

    path = os.path.join(RESULTS_ROOT, prompt_version, "scorecard_v2.md")
    with open(path, "w") as f:
        f.write("\n".join(L))
    return path


def _read(path):
    if not os.path.isfile(path):
        return None
    with open(path) as f:
        return json.load(f)
