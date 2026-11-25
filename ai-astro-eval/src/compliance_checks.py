"""
Scores a prompt version against the measurable items in prompts/requirements_checklist.md,
from saved transcripts, event-judge labels and metrics. Item ids match the checklist.

  python src/compliance_checks.py i29 i30
"""

import collections
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.sitara_orchestrator import RESULTS_ROOT

DATE = re.compile(r"\b((?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s*20\d\d|mid-?20\d\d|20\d\d)\b", re.I)
GREETING = re.compile(r"\b(namaste|hello|hi|kaise ho|kaise hain|swagat)\b", re.I)
RETURN_HOOK = re.compile(r"(agli baar|next time|zaroor aana|phir (aana|milte)|wapas aana|detail mein dekhenge|(bhi|aur bhi) (kaafi|bahut|bohot) kuch (likha|dikh)|baare mein bhi [^.?!]{0,40}(likha|dikh|saaf))", re.I)
HEDGE = re.compile(r"\b(ho sakta hai|ho sakti hai|mushkil hai)\b", re.I)
PAST = re.compile(r"(202[2-5]|college|pichle (saal|kuch))[^?]*\?", re.I)
MARRIED_ONLY = re.compile(r"(divorce|talaq|extramarital|doosri shaadi|second marriage)", re.I)
GATED = re.compile(r"(jaan(na|ne)?\s*chah|aur\s*kya\s*jaan|bat(a|aa)(u|un|oon)n?\s*\?)", re.I)
PATTERN = re.compile(r"\b(dono|ek hi (wajah|jagah|reason)|tabhi se)\b", re.I)
SCAPEGOAT = re.compile(r"(galti nahi|grahon ka (khel|asar)|kismat ka khel)", re.I)
REMEDY = re.compile(r"(mantra|namah|chalisa|daan|donate|108 baar|vrat)", re.I)
CALLBACK = re.compile(r"(pichli baar|last time|(tumne|aapne) bataya tha|humne baat|yaad (hai|rakhti)|maine bataya tha|maine [^.?!]{0,40}(bataya|kaha) tha|upay shuru|mantra shuru ki|pehle baat ki thi)", re.I)
DENIAL = re.compile(r"(abhi mile|pehli baar mil|kisi aur se baat)", re.I)
NEGATIVE = re.compile(r"(nahi hoga|nahi hogi|chances? nahi|kam chance|nahi milegi|nahi milega|mushkil hai|no chance|nahi dikh)", re.I)
TUM = re.compile(r"\b(tum|tumhe|tumhare|tumhari|tumhara|tumne)\b", re.I)
THEATRICAL = re.compile(r"(sahi disha|disha dikha|raasta dikhayenge|zindagi ke aane wale|kismat ka khel|bhagya)", re.I)
TEEN = re.compile(r"(\bhii+\b|\barre\b|\byaar\b|😊|🙂|❤|sitare|taare|universe|jaadu|magic|!!)", re.I)
HARD = re.compile(r"\b(aarthik|sthiti|parivaar|parivar|swabhaa?v|aamdani|sudhaa?r|mehsoos|prabhav|safalta|shuruaa?t|shuruwat|jeevan|kathin|badlaa?v|tanaa?v|stability|traditional|reserved|guarded|communication|financial|profile|direction|growth|personal|comfortable)\b", re.I)
ECHO = re.compile(r"^[^.?!]{0,40}(ki|ke) (baat|baare mein) (hai|dekhte)", re.I)
ABBR = re.compile(r"\b(\d{1,2}[HL]|AD|MD|PD|SAV|D9)\b")
VAGUE_OPENER = re.compile(r"^\W*(hi+|hello|namaste|future|kundli|love life|mujhe jan+a hai[^?]*|janna hai[^?]*)\W*$", re.I)
SHANI = re.compile(r"\b(shani|saturn|sade sati|dhaiya)\b(?!var)", re.I)


def sessions(version):
    pattern = os.path.join(RESULTS_ROOT, version, "*", "*", "run_*", "session_*", "transcript.json")
    for path in sorted(glob.glob(pattern)):
        d = os.path.dirname(path)
        with open(path) as f:
            msgs = json.load(f)
        with open(os.path.join(d, "metrics.json")) as f:
            metrics = json.load(f)
        yield d, msgs, metrics


def _first_real_answered(d, msgs):
    """A4: the first user question that is not a vague opener ("Future", "Hi") is answered by
    01:30, or in the very next reply when it was asked after 01:00."""
    with open(os.path.join(d, "labels.json")) as f:
        labels = json.load(f)
    by_idx = {x["idx"]: x for x in msgs}
    real = [q for q in sorted(labels.get("user_questions", []), key=lambda q: q["idx"])
            if q["idx"] in by_idx and not VAGUE_OPENER.match(by_idx[q["idx"]]["text"])]
    if not real:
        return True
    q = real[0]
    ans = q.get("answered_idx")
    if ans is None or ans not in by_idx:
        return False
    next_astro = next((x["idx"] for x in msgs if x["idx"] > q["idx"] and x["role"] == "ASTRO"), None)
    return by_idx[ans]["sec"] <= 90 or ans == next_astro


def check(version):
    c = collections.Counter()
    for d, msgs, m in sessions(version):
        astro = [x["text"] for x in msgs if x["role"] == "ASTRO"]
        if not astro:
            continue
        c["chats"] += 1
        c["replies"] += len(astro)
        c["A1 greeting first, no date"] += bool(GREETING.search(astro[0]) and not DATE.search(astro[0]))
        c["A4 first real question answered by 01:30 or next reply"] += _first_real_answered(d, msgs)
        c["A6 personal reading by 03:30"] += m.get("first_personal_reading_sec") is not None and m["first_personal_reading_sec"] <= 210
        c["A8 remedy by 04:15"] += m.get("remedy_sec") is not None and m["remedy_sec"] <= 255
        c["A9 early goodbye"] += bool(m.get("early_goodbye"))
        c["A10 return hook at close"] += any(RETURN_HOOK.search(t) for t in astro[-3:])
        c["C1 hedging lines"] += sum(bool(HEDGE.search(t)) for t in astro)
        dates = collections.Counter()
        for t in astro:
            dates.update(set(x.lower().replace(" ", "") for x in DATE.findall(t)))
        c["C2 repeated date mentions"] += sum(n - 1 for n in dates.values() if n > 1)
        c["C4 past-event line in first 3 replies"] += any(PAST.search(t) for t in astro[:3])
        c["C5 married-only lines"] += sum(bool(MARRIED_ONLY.search(t)) for t in astro)
        c["C8 refusals"] += m.get("refusals") or 0
        c["D1 replies with 2+ questions"] += sum(t.count("?") >= 2 for t in astro)
        c["D2 replies with a question"] += sum("?" in t for t in astro)
        c["D4 gated/generic questions"] += sum(bool(GATED.search(t)) for t in astro)
        c["D5 asks known info"] += m.get("asks_known_info") or 0
        c["E1 pattern lines"] += sum(bool(PATTERN.search(t)) for t in astro)
        c["E3 scapegoat lines"] += sum(bool(SCAPEGOAT.search(t)) for t in astro)
        c["E4 judge teasers"] += m.get("teases") or 0
        c["E5 remedy replies"] += sum(bool(REMEDY.search(t)) for t in astro)
        c["E6 time/pay lines"] += m.get("time_or_pay_lines") or 0
        if os.path.basename(d) == "session_2":
            c["returning chats"] += 1
            first = next((i + 1 for i, t in enumerate(astro) if CALLBACK.search(t)), None)
            c["F1 callback in reply 2-3"] += first in (2, 3)
            c["F1b callback in the first reply"] += first == 1
            c["F2 denials of the last chat"] += sum(bool(DENIAL.search(t)) for t in astro)
        c["G1 words"] += sum(len(t.split()) for t in astro)
        c["G2 teen/whimsical lines"] += sum(bool(TEEN.search(t)) for t in astro)
        c["G3 hard words"] += sum(len(HARD.findall(t)) for t in astro)
        c["G4 echo openings"] += sum(bool(ECHO.search(t)) for t in astro)
        c["G5 abbreviations"] += sum(len(ABBR.findall(t)) for t in astro)
        c["G6 Shani mentions"] += sum(len(SHANI.findall(t)) for t in astro)
        c["C9 negative predictions"] += sum(bool(NEGATIVE.search(t)) for t in astro)
        c["G8 replies using tum"] += sum(bool(TUM.search(t)) for t in astro)
        c["G9 theatrical lines"] += sum(bool(THEATRICAL.search(t)) for t in astro)
    return c


def report(version):
    c = check(version)
    n, r = c["chats"], c["replies"]
    per_chat = lambda k: f"{c[k] / n:.2f}/chat"
    share = lambda k, base: f"{c[k]}/{base}"
    rows = [
        ("A1 greeting first, no date", share("A1 greeting first, no date", n)),
        ("A4 first real question answered by 01:30 or next reply", share("A4 first real question answered by 01:30 or next reply", n)),
        ("A6 personal reading by 03:30", share("A6 personal reading by 03:30", n)),
        ("A8 remedy by 04:15", share("A8 remedy by 04:15", n)),
        ("A9 early goodbye", share("A9 early goodbye", n)),
        ("A10 return hook at close", share("A10 return hook at close", n)),
        ("C1 hedging lines", per_chat("C1 hedging lines")),
        ("C2 repeated date mentions", per_chat("C2 repeated date mentions")),
        ("C4 past-event line in first 3 replies", share("C4 past-event line in first 3 replies", n)),
        ("C5 married-only lines", str(c["C5 married-only lines"])),
        ("C8 refusals", per_chat("C8 refusals")),
        ("D1 replies with 2+ questions", share("D1 replies with 2+ questions", r)),
        ("D2 replies with a question", f"{c['D2 replies with a question'] / r:.0%}"),
        ("D4 gated/generic questions", str(c["D4 gated/generic questions"])),
        ("D5 asks known info", per_chat("D5 asks known info")),
        ("E1 pattern lines", per_chat("E1 pattern lines")),
        ("E3 scapegoat lines", per_chat("E3 scapegoat lines")),
        ("E4 judge teasers", per_chat("E4 judge teasers")),
        ("E5 remedy replies", per_chat("E5 remedy replies")),
        ("E6 time/pay lines", per_chat("E6 time/pay lines")),
        ("F1 callback in reply 2-3", share("F1 callback in reply 2-3", c["returning chats"])),
        ("F1b callback in the first reply", share("F1b callback in the first reply", c["returning chats"])),
        ("F2 denials of the last chat", str(c["F2 denials of the last chat"])),
        ("G1 words per reply", f"{c['G1 words'] / r:.1f}"),
        ("G2 teen/whimsical lines", str(c["G2 teen/whimsical lines"])),
        ("G3 hard words per reply", f"{c['G3 hard words'] / r:.2f}"),
        ("G4 echo openings", str(c["G4 echo openings"])),
        ("G5 abbreviations", str(c["G5 abbreviations"])),
        ("G6 Shani mentions", str(c["G6 Shani mentions"])),
        ("C9 negative predictions", str(c["C9 negative predictions"])),
        ("G8 replies using tum", f"{c['G8 replies using tum']}/{r}"),
        ("G9 theatrical lines", str(c["G9 theatrical lines"])),
    ]
    return dict(rows)


if __name__ == "__main__":
    versions = sys.argv[1:]
    reports = {v: report(v) for v in versions}
    keys = list(next(iter(reports.values())))
    print("| Item | " + " | ".join(versions) + " |")
    print("|---|" + "---|" * len(versions))
    for k in keys:
        print(f"| {k} | " + " | ".join(reports[v][k] for v in versions) + " |")
