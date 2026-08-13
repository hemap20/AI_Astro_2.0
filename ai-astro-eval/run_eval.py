"""
CLI entrypoint for the AI Astro memory evaluation suite.

Examples:
  python run_eval.py --prompt-version v1 --test-case M1
  python run_eval.py --prompt-version v1 --all
  python run_eval.py --prompt-version v1 --test-case M3 --persona-variant alt --gap-variant same_day
"""

import argparse
import os
import sys
import traceback

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv

# .env lives one directory up (repo root), alongside this ai-astro-eval/ folder.
load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env"))

from test_cases.memory_test_cases import MEMORY_TEST_CASES
from src.orchestrator import run_single, RESULTS_ROOT
from src.report_generator import write_rollup_summary

# Alternate-persona style shifts applied on top of a test case's given
# ("primary") persona text to satisfy the mandatory 2-persona-variant
# requirement. The situation/facts stay identical — only formality,
# directness, and regional/language style shift — so a finding that
# replicates across both variants is a real finding, not an artifact of
# one persona's phrasing.
ALT_PERSONA_STYLE_SHIFT = """

ALTERNATE PERSONA STYLE OVERLAY (apply on top of the situation above):
Keep the exact same situation, facts, and goals described above, but change
HOW you communicate:
- Be noticeably more formal and hesitant than the primary persona - use "aap"
  consistently, soften direct requests ("agar aap bata sakein to..."), and
  take longer to get to the point.
- Use a slightly different regional/language flavor (lean more Punjabi-inflected
  Hinglish, or more English-mixed depending on what feels natural) rather than
  a straight copy of the primary persona's phrasing.
- Where the primary persona escalates bluntly, you escalate by going quieter
  and more indirect instead, then only becoming blunt as an occasional single
  short line, not a sustained tone shift.
"""

GAP_VARIANTS = ["same_day", "genuine_return"]


def persona_text_for_variant(session_def, persona_variant):
    base = session_def.get("persona")
    if base is None:
        # sessions 2/3 don't carry their own persona block in the test case
        # data; the persona identity carries over from session_1, so callers
        # must pass session_1's (possibly overlaid) persona text through.
        return None
    if persona_variant == "alt":
        return base + ALT_PERSONA_STYLE_SHIFT
    return base


def build_persona_text_by_session(test_case, persona_variant):
    """
    The test case schema only defines a `persona` block on session_1 (the
    persona identity is established there and simply continues through
    sessions 2/3). Resolve that here once, with the alt-variant overlay
    applied if requested, and reuse it for every session in the run.
    """
    session_1_persona = persona_text_for_variant(test_case["sessions"]["session_1"], persona_variant)
    return {
        "session_1": session_1_persona,
        "session_2": session_1_persona,
        "session_3": session_1_persona,
    }


def resolve_gap_variants(test_case, requested_gap_variant):
    declared = test_case["memory_gap_variant"]
    if requested_gap_variant:
        return [requested_gap_variant]
    if declared == "BOTH":
        return GAP_VARIANTS
    return [declared]


def resolve_persona_variants(test_case, requested_persona_variant):
    if requested_persona_variant:
        return [requested_persona_variant]
    n_required = test_case.get("persona_variants_required", 1)
    variants = ["primary"]
    if n_required >= 2:
        variants.append("alt")
    return variants


def run_test_case(test_case, prompt_version, persona_variant_arg, gap_variant_arg, runs_override):
    persona_variants = resolve_persona_variants(test_case, persona_variant_arg)
    gap_variants = resolve_gap_variants(test_case, gap_variant_arg)
    n_runs = runs_override or test_case["runs"]

    results = []
    for persona_variant in persona_variants:
        persona_text_by_session = build_persona_text_by_session(test_case, persona_variant)
        for gap_variant in gap_variants:
            for run_number in range(1, n_runs + 1):
                print(
                    f"[{test_case['id']}] persona={persona_variant} gap={gap_variant} "
                    f"run={run_number}/{n_runs} ...",
                    flush=True,
                )
                try:
                    result = run_single(
                        test_case=test_case,
                        prompt_version=prompt_version,
                        persona_variant_label=persona_variant,
                        persona_text_by_session=persona_text_by_session,
                        gap_variant=gap_variant,
                        run_number=run_number,
                    )
                    results.append(result)
                    print(f"  -> wrote {result['run_dir']}", flush=True)
                except FileExistsError as e:
                    print(f"  -> SKIPPED (already exists): {e}", flush=True)
                except Exception:
                    print(f"  -> FAILED: {test_case['id']} {persona_variant} {gap_variant} run {run_number}", flush=True)
                    traceback.print_exc()
    return results


def main():
    parser = argparse.ArgumentParser(description="AI Astro memory evaluation suite runner")
    parser.add_argument("--prompt-version", required=True, help="e.g. v1 (loads prompts/astro_system_prompt_v1.py)")
    parser.add_argument("--test-case", help="Test case id, e.g. M1. Omit with --all to run everything.")
    parser.add_argument("--all", action="store_true", help="Run every test case in MEMORY_TEST_CASES")
    parser.add_argument("--persona-variant", choices=["primary", "alt"], help="Restrict to one persona variant")
    parser.add_argument("--gap-variant", choices=GAP_VARIANTS, help="Restrict to one memory gap variant")
    parser.add_argument("--runs", type=int, help="Override the test case's configured run count")
    args = parser.parse_args()

    if not args.all and not args.test_case:
        parser.error("Specify --test-case <id> or --all")

    if os.environ.get("GEMINI_API_KEY") is None:
        parser.error("GEMINI_API_KEY is not set in the environment (.env).")

    test_cases_to_run = MEMORY_TEST_CASES
    if args.test_case:
        test_cases_to_run = [tc for tc in MEMORY_TEST_CASES if tc["id"] == args.test_case]
        if not test_cases_to_run:
            parser.error(f"Unknown test case id: {args.test_case}")

    for test_case in test_cases_to_run:
        run_test_case(
            test_case=test_case,
            prompt_version=args.prompt_version,
            persona_variant_arg=args.persona_variant,
            gap_variant_arg=args.gap_variant,
            runs_override=args.runs,
        )

    prompt_version_dir = os.path.join(RESULTS_ROOT, args.prompt_version)
    write_rollup_summary(prompt_version_dir, args.prompt_version)
    print(f"\nRollup summary written to {os.path.join(prompt_version_dir, 'summary.md')}")


if __name__ == "__main__":
    main()
