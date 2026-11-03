"""
Runs every test case once (primary persona, same_day gap, 3 sessions) with the
astrologer role on each model below. User simulator, summarizer and judge stay
on their usual Gemini models so only the astrologer model varies.

  python run_model_sweep.py --prompt-version v1                 # all models
  python run_model_sweep.py --prompt-version v1 --models claude-sonnet-5-5 gemini-3.5-flash
  python run_model_sweep.py --prompt-version v1 --smoke-test    # one bot turn per model
"""

import argparse
import json
import os
import sys
import traceback
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env"))

from test_cases.memory_test_cases import MEMORY_TEST_CASES
from src.astro_bot import AstroBot
from src.orchestrator import run_single, RESULTS_ROOT
from src.report_generator import write_rollup_summary
from run_eval import build_persona_text_by_session

# Text-chat models listed by each API (2026-10-29). TTS/image/audio/robotics/
# research models and "-latest" aliases are excluded, as are the gemma-4
# models (0 quota on this API key).
CLAUDE_MODELS = [
    "claude-fable-5-1", "claude-opus-5-5", "claude-sonnet-5-5", "claude-haiku-5-5",
    "claude-opus-5", "claude-sonnet-5", "claude-fable-5",
    "claude-opus-4-8", "claude-opus-4-7", "claude-opus-4-6", "claude-sonnet-4-6",
    "claude-opus-4-5-20251101", "claude-sonnet-4-5-20250929", "claude-haiku-4-5-20251001",
]
GEMINI_MODELS = [
    "gemini-4-argon", "gemini-3.8-flash", "gemini-3.7-flash", "gemini-3.6-flash",
    "gemini-3.5-flash", "gemini-3.5-flash-lite", "gemini-3.1-pro-preview",
    "gemini-3.1-flash-lite", "gemini-3-flash-preview",
    "gemini-2.5-pro", "gemini-2.5-flash", "gemini-2.5-flash-lite",
]
ALL_MODELS = CLAUDE_MODELS + GEMINI_MODELS


def smoke_test(prompt_version, model):
    try:
        bot = AstroBot(prompt_version=prompt_version, model=model)
        reply = bot.respond_to("Namaste, meri shaadi kab hogi?")
        return model, True, reply[:80]
    except Exception as e:  # noqa: BLE001
        return model, False, str(e)[:200]


def run_test_case(prompt_version, model, test_case):
    print(f"[{model}] {test_case['id']} ...", flush=True)
    try:
        run_single(
            test_case=test_case,
            prompt_version=prompt_version,
            persona_variant_label="primary",
            persona_text_by_session=build_persona_text_by_session(test_case, "primary"),
            gap_variant="same_day",
            run_number=1,
            astro_model=model,
        )
        print(f"[{model}] {test_case['id']} done", flush=True)
    except FileExistsError:
        print(f"[{model}] {test_case['id']} SKIPPED (already exists)", flush=True)
    except Exception:
        print(f"[{model}] {test_case['id']} FAILED", flush=True)
        traceback.print_exc()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt-version", required=True)
    parser.add_argument("--models", nargs="+", default=ALL_MODELS)
    parser.add_argument("--smoke-test", action="store_true")
    parser.add_argument("--workers", type=int, default=20, help="(model, test case) runs in parallel")
    args = parser.parse_args()

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        if args.smoke_test:
            results = list(pool.map(lambda m: smoke_test(args.prompt_version, m), args.models))
            for model, ok, info in results:
                print(f"{'OK  ' if ok else 'FAIL'} {model}: {info}")
            print(json.dumps([m for m, ok, _ in results if ok]))
            return
        jobs = [(m, tc) for tc in MEMORY_TEST_CASES for m in args.models]
        list(pool.map(lambda job: run_test_case(args.prompt_version, *job), jobs))

    for model in args.models:
        model_dir = os.path.join(RESULTS_ROOT, args.prompt_version, model)
        write_rollup_summary(model_dir, f"{args.prompt_version} / {model}")


if __name__ == "__main__":
    main()
