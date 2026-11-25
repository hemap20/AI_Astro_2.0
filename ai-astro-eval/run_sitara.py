"""
Sitara test cases (test_cases/memory_test_cases.py) with the two behaviour
personas, production memory between sessions, and event-judge metrics (v2).

  python run_sitara.py --prompt-version v1 --all
  python run_sitara.py --prompt-version v1 --test-case S2 --persona passive_follower --gap-variant same_day --runs 1
  python run_sitara.py --prompt-version v2 --scorecard-only --baseline v1
"""

import argparse
import os
import re
import sys
import traceback
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env"))

from test_cases.memory_test_cases import SITARA_TEST_CASES
from src.sitara_simulator import PERSONA_FILES, persona_name_in_case, build_persona_prompt
from src.sitara_orchestrator import run_case, case_sessions
from src.scorecard import write_scorecard

GAP_VARIANTS = ["same_day", "genuine_return"]

# Every prompt reads the same test chart (Nandyal, 1 Aug 2003, 4:30 AM), so each
# scenario's birth details are replaced with the chart's; name and gender stay.
CHART_BIRTH_DETAILS = "DOB - 1 August 2003, TOB - 4:30 AM, POB - Nandyal, Andhra Pradesh"
_BIRTH_RE = re.compile(r"DOB - .*?, TOB - .*?, POB - .*$", re.M)


def persona_variants(case):
    """[(persona_name, persona_prompt)]: the case's named persona first, then
    the other Sitara persona with the same scenario when the case asks for 2
    variants. Inline personas (S5) run as-is under the name "inline"."""
    persona_text = _BIRTH_RE.sub(CHART_BIRTH_DETAILS, case_sessions(case)[0][1]["persona"])
    named = persona_name_in_case(persona_text)
    if named is None:
        return [("inline", build_persona_prompt(persona_text, None))]
    names = [named]
    if case.get("persona_variants_required", 1) >= 2:
        names += [n for n in PERSONA_FILES if n != named]
    return [(n, build_persona_prompt(persona_text, n)) for n in names]


def gap_variants(case):
    if "sessions" not in case:
        return [None]
    return GAP_VARIANTS if case.get("memory_gap_variant") == "BOTH" else [case["memory_gap_variant"]]


def jobs_for(case, args):
    for name, prompt in persona_variants(case):
        if args.persona and name != args.persona:
            continue
        for gap in gap_variants(case):
            if args.gap_variant and gap and gap != args.gap_variant:
                continue
            for n in range(1, (args.runs or case["runs"]) + 1):
                yield case, name, prompt, gap, n


def run_job(job, prompt_version):
    case, name, prompt, gap, n = job
    tag = f"[{case['id']}] {name} {gap or ''} run {n}"
    try:
        print(f"{tag} -> {run_case(case, prompt_version, name, prompt, gap, n)}", flush=True)
    except FileExistsError:
        print(f"{tag} SKIPPED (already exists)", flush=True)
    except Exception:
        print(f"{tag} FAILED", flush=True)
        traceback.print_exc()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt-version", required=True)
    ap.add_argument("--test-case", help="e.g. S1; omit with --all")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--persona", choices=list(PERSONA_FILES) + ["inline"])
    ap.add_argument("--gap-variant", choices=GAP_VARIANTS)
    ap.add_argument("--runs", type=int, help="override each case's run count")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--baseline", help="prompt version to compare against with DECISION_RULE")
    ap.add_argument("--scorecard-only", action="store_true")
    args = ap.parse_args()

    if not args.scorecard_only:
        if not args.all and not args.test_case:
            ap.error("Specify --test-case <id> or --all")
        cases = [c for c in SITARA_TEST_CASES if args.all or c["id"] == args.test_case]
        if not cases:
            ap.error(f"Unknown test case id: {args.test_case}")
        jobs = [j for c in cases for j in jobs_for(c, args)]
        print(f"{len(jobs)} runs", flush=True)
        with ThreadPoolExecutor(args.workers) as pool:
            list(pool.map(lambda j: run_job(j, args.prompt_version), jobs))

    print("Scorecard:", write_scorecard(args.prompt_version, args.baseline))


if __name__ == "__main__":
    main()
