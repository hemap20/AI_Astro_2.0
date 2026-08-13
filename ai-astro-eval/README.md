# ai-astro-eval

Multi-session memory evaluation suite for the AI Astro bot. Runs simulated
users (Gemini) against the production system prompt across 3 sessions per
test case, with real summarization between sessions, and scores every
session with a Judge LLM (also Gemini).

## Setup

```bash
cd ai-astro-eval
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

`GEMINI_API_KEY` is read from `../.env` (the repo root's `.env`) automatically
via `run_eval.py`. You can also export it directly in your shell.

## Before running for real

`prompts/astro_system_prompt_v1.py` is still a **placeholder** — replace
`ASTRO_SYSTEM_PROMPT` with the actual production system prompt text before
trusting any results; anything scored against the placeholder is not
meaningful.

`prompts/summarizer_prompt.py` is the **real production prompt**
(`CHAT_SUMMARY_SYSTEM_PROMPT` / `CHAT_SUMMARY_USER_PROMPT`), confirmed
incremental: each call takes the previous `consolidated_summary` +
`concern_summary` (merges duplicates, increments `mention_count`) plus only
the just-completed session's chat — never the full multi-session transcript.
`src/summarizer.py::summarize_session()` implements this chaining and is
verified working (mention_count correctly incremented across chained calls in
testing). `src/astro_bot.py::_assemble_prompt()`'s exact memory-injection
formatting (labels/structure around the JSON) is still a reasonable guess —
confirm it against production once the real astro system prompt is supplied.

## Running

```bash
# one test case, all its persona/gap variants, configured run count
python run_eval.py --prompt-version v1 --test-case M1

# everything
python run_eval.py --prompt-version v1 --all

# narrow to one persona/gap variant, override run count (useful for quick checks)
python run_eval.py --prompt-version v1 --test-case M3 --persona-variant alt --gap-variant same_day --runs 1
```

Results land in `results/<prompt_version>/<test_case_id>/<persona_variant>_<gap_variant>_run<N>/`:
- `transcript_full.md` / `.json` — full 3-session transcript, memory shown inline at each boundary
- `memory_snapshot_after_session1.json` / `after_session2.json` — exact summarizer output injected
- `judge_scores.json` — raw normalized scores + right/wrong lists + cross-session synthesis
- `judge_report.md` — screenshot-ready formatted report

A version-level rollup lands at `results/<prompt_version>/summary.md`.

**Results are never silently overwritten** — re-running an existing
`<persona_variant>_<gap_variant>_run<N>` combination raises `FileExistsError`.
Bump `--runs`, remove the old directory, or use a new `--prompt-version` to
test a new prompt.

## Design notes worth knowing

- **1–10 polarity** is enforced via `metrics/metrics_framework.py`'s explicit
  `polarity` field per metric (`high_is_good` / `low_is_good`), looked up in
  `src/judge.py::normalize_score()` — never inferred from a metric's name.
- **15-turn-per-session floor** is enforced in code in
  `src/orchestrator.py::run_session()` (`target_turns = max(max_turns, MIN_TURNS_PER_SESSION)`),
  not left to the simulator's judgment.
- **Non-determinism**: the user simulator runs at temperature 0.95 specifically
  so repeated runs of the same test case diverge — spot-check `transcript_full.md`
  across two runs of the same case to confirm this if you change models/temps.
- **Persona variants**: the test-case data only defines one persona per case.
  The required second ("alt") variant is derived in `run_eval.py` by applying
  a style-shift overlay (`ALT_PERSONA_STYLE_SHIFT`) on top of the same
  situation/facts — same content, different formality/directness/regional
  flavor — so a finding that replicates across both is a real finding.
