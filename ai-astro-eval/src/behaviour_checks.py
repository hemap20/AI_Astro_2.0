"""
Phrase-level checks for prompt iterations, next to the event-judge metrics:
gated teaser questions, what the bot says in the last minute, and where the
session-2 callback to the previous chat lands.

  python src/behaviour_checks.py v1 i1 i2
"""

import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.sitara_orchestrator import RESULTS_ROOT, TIME_LOW_SEC

GATED_TEASER = re.compile(
    r"(jaan(na|ne|a)?\s*chah|sunna\s*chah|aur\s*jaan|bat(a|aa)(u|un|oon|aun|o)n?\s*\?|bataoon\b|bataun\b)",
    re.I)
RECHARGE = re.compile(r"(recharge|extend|minute|pay|time\s*thoda\s*kam|aur\s*time|time\s*(badha|add))", re.I)
KUNDLI_HOOK = re.compile(r"(kundli|chart|dikh)", re.I)
# a statement about the user's past/present (trust line)
PAST_PRESENT = re.compile(r"(raha hoga|rahi hogi|raha hai na|rahi hai na|pichle (saal|kuch)|202[2-5]|ho raha hoga|hua hoga|aaj kal|abhi aap)", re.I)
# IF MARRIED-only content; every test persona is unmarried
MARRIED_ONLY = re.compile(r"(divorce|talaq|extramarital|doosri shaadi|second marriage|shaadi ke baad.*jhagde kam)", re.I)


def sessions(version):
    for path in sorted(glob.glob(os.path.join(RESULTS_ROOT, version, "*", "*", "run_*", "session_*", "transcript.json"))):
        with open(path) as f:
            yield path, json.load(f)


def check(version):
    astro = gated = 0
    low_lines, low_recharge, low_kundli = 0, 0, 0
    callbacks = []
    trust_sessions = married_only = n_sessions = 0
    for path, msgs in sessions(version):
        a_msgs = [m for m in msgs if m["role"] == "ASTRO"]
        astro += len(a_msgs)
        n_sessions += 1
        trust_sessions += any(PAST_PRESENT.search(m["text"]) for m in a_msgs[:3])
        married_only += sum(bool(MARRIED_ONLY.search(m["text"])) for m in a_msgs)
        gated += sum(bool(GATED_TEASER.search(m["text"])) for m in a_msgs)
        for m in a_msgs:
            if m["sec"] >= TIME_LOW_SEC:
                low_lines += 1
                low_recharge += bool(RECHARGE.search(m["text"]))
                low_kundli += bool(KUNDLI_HOOK.search(m["text"]))
        if path.endswith(os.path.join("session_2", "transcript.json")):
            summary_path = os.path.join(os.path.dirname(path), "memory_summary.json")
            with open(summary_path) as f:
                summary = json.load(f)
            terms = _summary_terms(summary)
            first = next((i for i, m in enumerate(a_msgs, 1) if any(t in m["text"].lower() for t in terms)), None)
            callbacks.append((path.split(os.sep)[-4], first))
    return {
        "astro_msgs": astro,
        "gated_teaser_questions": gated,
        "last_minute_msgs": low_lines,
        "last_minute_recharge_or_time": low_recharge,
        "last_minute_kundli_hook": low_kundli,
        "s2_callback_astro_msg_no": callbacks,
        "trust_line_in_first_3": f"{trust_sessions}/{n_sessions}",
        "married_only_lines": married_only,
    }


def _summary_terms(summary):
    """Topic words from the previous-chat summary (concerns, predictions)."""
    text = json.dumps(summary, ensure_ascii=False).lower()
    words = {"shaadi", "marriage", "rishta", "paisa", "career", "job", "family", "ghar", "pichli", "last time", "pehle"}
    return [w for w in words if w in text] + ["pichli", "last time", "pichhli"]


if __name__ == "__main__":
    for v in sys.argv[1:]:
        print(v, json.dumps(check(v), ensure_ascii=False))
