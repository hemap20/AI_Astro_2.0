# Integration guide: metrics v2, event judge, Sitara test cases

For: Claude (or an engineer) integrating these pieces into the existing AI Astro evaluation framework, the one that has `metrics_framework.py`, `src/judge.py` (with `normalize_score()`), `report_generator.py`, test cases in the `MEMORY_TEST_CASES` format, and per-version results under `results/<version>/`.

Read this whole file before changing code. Keep the existing framework working; add the new pieces next to it.

---

## 1. What the pieces are and how they connect

```
test case (sitara_test_cases.py)
   + behaviour persona (personas/*.md, with {scenario} filled from the case)
        │
        ▼
simulator LLM  ⇄  AI Astro bot (prompt version under test)      ← existing harness
        │  transcript + [VERDICT] line
        ▼
event judge (judge/event_judge.py)  → per-message labels (JSON)
        │
        ▼
metric functions (event_judge.metrics)  → raw metric values per run
        │
        ▼
metrics_v2 (judge/metrics_v2.py)  → tier, target, direction, prompt lever
        │
        ▼
scorecard per prompt version + DECISION_RULE  → accept / reject + which instruction to change
```

| File (source repo: `judge_llm_astro/`) | Role | Depends on |
|---|---|---|
| `judge/event_judge.py` | Labels every message with fixed yes/no events (one Gemini call per transcript) and computes metrics from the labels by script | `google-genai`, `pandas`, `judge/chat_parser.py` (`render_transcript`, `load_first_chat`) |
| `judge/metrics_v2.py` | Metric definitions: tier, definition, direction, target, evidence, prompt lever; `DECISION_RULE`; `V1_MAPPING` from the old metrics | nothing |
| `sitara_test_cases.py` | 5 test cases (S1–S5): persona, scenario, pressure points, runs, decision rule, `metrics_v2` keys + `case_specific` checks | `personas/` |
| `personas/sitara_1_direct_answer_chaser.md`, `personas/sitara_2_passive_follower.md` | Behaviour-only simulator prompts; the situation goes in at `{scenario}` | nothing |
| `results/events_sitara/baseline_scorecard.csv` | Current Sitara values for every metric (the bar to beat) | — |
| `results/events_sitara/validation.csv` | Evidence: each metric's AUC vs real first→second chat return | — |

---

## 2. Core rules (do not change these while integrating)

1. **No 1–10 opinion scores for these metrics.** Each metric is a raw count, rate or yes/no computed by script from labels. Report the raw value next to its target.
2. **The judge labels; it does not score.** If you need a new metric, add a label field to the event judge prompt and compute the metric in code. Do not ask the LLM for a number.
3. **No composite score.** A prompt version is accepted or rejected by `metrics_v2.DECISION_RULE` (scorecard), not by an average.
4. **Tiers decide what counts:**
   - DRIVER metrics decide between versions.
   - LEAD metrics are reported but do not decide alone.
   - GUARDRAIL metrics must not get worse.
   - DIAGNOSTIC metrics only explain failures; never optimise for them.
5. **Temperature 0, seed 42, model `gemini-3.1-flash-lite`** for the event judge, so labels are repeatable.
6. **Offline results are a filter, not proof.** A version that passes still needs a live A/B test on first→second chat return.

---

## 3. Data formats

### 3.1 Transcript in (what the event judge needs)
A list of messages in order:
```json
[
  {"role": "USER",  "text": "Shadi kb hogi meri", "sec": 0},
  {"role": "ASTRO", "text": "Namaste Aradhana ji...", "sec": 6}
]
```
- `role` is `USER` or `ASTRO` (map the bot to `ASTRO`; drop system messages, or keep them as `SYSTEM`; they are ignored).
- `sec` = seconds since the chat started. Needed for timing metrics (`first_answer_sec`, `remedy_sec`). If the harness has no real timing, use the simulated clock passed to the simulator as `[mm:ss]`.
- The judge adds `idx` (position) itself when loading JSON transcripts.

`render_transcript()` turns this into lines like `#3 [00:42] ASTRO: text`, which is what the judge prompt expects. Reuse it rather than writing a new format.

### 3.2 Labels out (per transcript, saved as JSON)
```json
{
 "user_questions": [{"idx": 0, "kind": "timing", "repeat_of": null, "answered_idx": 4, "answer_has_window": true}],
 "astro": [{"idx": 1, "reading": false, "personal": false, "question": false, "tease": false,
            "tease_delivered_idx": null, "jargon_unexplained": 0, "remedy": false, "time_or_pay": false,
            "refusal": false, "generic": false, "empathy": false, "asks_known_info": false, "goodbye": false}],
 "user": [{"idx": 0, "confused": false, "frustrated": false, "disclosure": false, "distress": false}]
}
```
Store these with every run (see §6). They are the audit trail for every metric.

### 3.3 Metrics out
`event_judge.metrics(msgs, labels)` returns a flat dict, e.g.
`{"first_q_answered": true, "questions_answered_rate": 0.67, "time_or_pay_before_answer": false, "time_or_pay_lines": 1, "refusals": 0, "user_frustrated": 2, "teases": 3, "jargon_per_msg": 0.4, "remedy_given": true, "distress_handling": null, ...}`
`None` means "not applicable" (e.g. no timing question asked); exclude it from averages, do not count it as 0.

### 3.4 Simulator verdict
Each persona ends with `[LEAVE]` and one line:
```
[VERDICT] answered: yes; would_continue: no; would_return: no; reason: <text>
```
(the passive persona uses `understood` instead of `answered`). Parse with:
```python
import re
def parse_verdict(text):
    m = re.search(r"\[VERDICT\](.*)", text)
    if not m:
        return None
    out = {}
    for part in m.group(1).split(";"):
        if ":" in part:
            k, v = part.split(":", 1)
            out[k.strip()] = v.strip()
    return out
```
Remove the `[LEAVE]` / `[VERDICT]` text from the transcript before sending it to the event judge.

---

## 4. Integration steps

### Step 1: copy the files
Copy into the framework (adjust paths to its layout, e.g. `src/`):
- `judge/event_judge.py` → `src/event_judge.py`
- `judge/chat_parser.py` → only `render_transcript` is needed for simulated transcripts; copy the function if the framework has its own parser.
- `judge/metrics_v2.py` → `src/metrics_v2.py`
- `sitara_test_cases.py` → next to the existing test case file
- `personas/` → the framework's persona folder

Keep `metrics_framework.py` (v1) untouched so old results stay readable.

### Step 2: call the event judge from the framework's judge step
`event_judge.py` has a CLI, but inside the framework call the functions directly:
```python
from google import genai
from event_judge import call, metrics
from chat_parser import render_transcript   # or the copied function

client = genai.Client()   # reads GEMINI_API_KEY

def score_transcript_v2(msgs):
    for i, m in enumerate(msgs):
        m["idx"] = i
        m.setdefault("sec", 0)
    labels = call(client, render_transcript(msgs))
    return labels, metrics(msgs, labels)
```
Run it per session transcript. Keep the existing judge too if its gates are needed (G1–G4 come from the rubric judge in `judge/run_judge.py`, prompt v5; the `gates` guardrail refers to those).

### Step 3: register metrics_v2 in the framework's metric schema
The old schema has `key, description, raw_scale, polarity, is_gate, applies_to`, and `normalize_score()` maps everything to 1–10. For v2:
- **Preferred:** report raw values and targets; do not normalise. Add a separate report section ("Scorecard v2") instead of mixing v2 into the 1–10 category tables.
- **If the pipeline must have the old schema,** build entries from metrics_v2 like this (do not invent 1–10 values from opinions):
```python
import metrics_v2 as M
def to_v1_schema(m):
    return {
        "key": "v2_" + m["key"],
        "description": m["definition"],
        "raw_scale": "rate_good" if m["direction"] == "higher_is_better" else "count_bad",
        "polarity": "high_is_good" if m["direction"] == "higher_is_better" else "low_is_good",
        "is_gate": m["tier"] == "GUARDRAIL",
        "applies_to": "session",
        "tier": m["tier"], "target": m["target"], "prompt_lever": m["prompt_lever"],
    }
V2_FOR_V1 = [to_v1_schema(m) for m in M.METRICS if m["tier"] != "DIAGNOSTIC"]
```
Add a `"Scorecard v2"` category to `CATEGORY_ORDER` / `CATEGORY_BY_METRIC_KEY` so the existing assertion (every metric has a category) still passes.

### Step 4: run the Sitara test cases in the existing harness
`sitara_test_cases.py` follows the same shape as `MEMORY_TEST_CASES`, with these differences:
| Field | Meaning |
|---|---|
| `persona` (single-session cases S1, S3, S4, S5) | Text that starts with `Use behaviour prompt: personas/<file>.md` followed by `SCENARIO:`. Build the simulator system prompt by reading that persona file and replacing `{scenario}` with the SCENARIO text. S5 has a full inline persona instead (no file). |
| `sessions` (S2 only) | Two sessions like the memory cases; session 2 gets `memory_injected: "SUMMARY_FROM_SESSION_1"` from the production summariser. |
| `max_turns` / `max_turns_per_session` | Hard stop for the loop. |
| `persona_variants_required` | Also run with the persona named in the comment (the other Sitara persona or the described variant). |
| `metrics_v2` | Keys from `metrics_v2.py`, computed by the event judge. |
| `case_specific` | Checks for this case only, read from the transcript or the VERDICT (e.g. `narrowing_handled`, `language_switched`). Implement as small functions over the labels/transcript, or score by hand for the first batch. |
| `decision_rule` | Case-level needs-fix / passing rule, evaluated across all runs and persona variants. |

Timing: the first session is a 5-minute chat. After each bot reply, send the simulator the reply prefixed with the elapsed time, e.g. `[02:35] <bot message>`. Advance the clock by real bot latency or by a fixed estimate (about 25–35 seconds per exchange). Personas leave at `[05:00]`.

Loop sketch:
```python
def run_case(case, persona_prompt, bot, simulator, max_turns):
    msgs, clock = [], 0
    user_text = simulator.start(persona_prompt)          # first USER turn (app details + opener)
    for _ in range(max_turns):
        if "[LEAVE]" in user_text:
            break
        msgs.append({"role": "USER", "text": strip_tags(user_text), "sec": clock})
        bot_text = bot.reply(msgs)
        clock += 30                                        # or real latency
        msgs.append({"role": "ASTRO", "text": bot_text, "sec": clock})
        user_text = simulator.reply(f"[{clock//60:02d}:{clock%60:02d}] {bot_text}")
    return msgs, parse_verdict(user_text)
```

### Step 5: aggregate per prompt version and apply the decision rule
For each prompt version, over all cases × runs × persona variants:
1. Mean (or share of runs) of every metric in each case's `metrics_v2` list; report `n` with it ("4 of 6 runs").
2. VERDICT rates: share of runs with `would_continue: yes` and `would_return: yes`.
3. Compare with the current production prompt run on the same cases (and with `baseline_scorecard.csv` for real-chat levels).
4. Apply `metrics_v2.DECISION_RULE`:
   - any GUARDRAIL worse → reject;
   - at least two DRIVER metrics move toward target and none moves away by more than the current version's run-to-run spread → candidate;
   - VERDICT rates do not drop;
   - candidate → live A/B.
5. For every DRIVER that misses its target, print its `prompt_lever` and two example message pairs from the labels (the user question and the bot reply that failed). That is the "what to change" output.

Run-to-run spread: run the current production prompt at least 5 times per case first; use the min–max range of each metric as the noise band.

### Step 6: store per run
`results/<version>/<case_id>/<persona_variant>/run_<n>/`:
- `transcript.json` (with `sec`)
- `labels.json` (event judge output)
- `metrics.json` (computed metrics)
- `verdict.json`
- `memory_summary.txt` (session 2+ only, as in the old methodology)
- `meta.json` (bot prompt version, simulator model, event judge model + prompt hash)

---

## 5. Checks before trusting results

1. **Smoke test:** run the event judge on 3 real Sitara chats from `sitara(6 nov onw.)/` and compare the metrics with the same chats in `results/events_sitara/metrics.csv`. They should match exactly (same model, temperature 0, seed 42).
2. **Label spot-check:** read the labels of about 15 transcripts by hand, especially `distress`, `answered_idx` and `tease`. If a label type is wrong more than ~1 time in 10, fix its wording in the event judge prompt (that is a new judge version; rerun the baseline).
3. **Simulator realism:** compare simulated users with real Sitara users: average words per user message (real: about 4.3) and share of 1–2 word replies (real: about 46%). If the simulator writes much longer or cleaner messages, tighten the persona before trusting any result.
4. **Baseline reproduction:** run the current production prompt through all 5 cases. Its metric levels should be in the same direction as `baseline_scorecard.csv` (e.g. `first_q_answered` well below 100%, `teases` around 2+). If the offline baseline looks much better than real chats, the simulation is too easy.

---

## 6. Extending

- **New metric:** add a label field to `PROMPT` in `event_judge.py`, compute it in `metrics()`, add an entry to `metrics_v2.METRICS` with tier `LEAD` (or `GUARDRAIL` if it is a policy rule), then validate it on real chats with outcomes before promoting it to `DRIVER`.
- **Re-validation:** when more Sitara chats with return outcomes are available, run `event_judge.py --input <folder>` and recompute AUC per metric (as in `results/events_sitara/validation.csv`). Promote/demote tiers based on that, and record the change in `metrics_v2.py`.
- **New test case:** follow the S1–S5 structure: real-data baseline in the header comment, persona from `personas/` + scenario, pressure points, `runs`, `decision_rule`, `metrics_v2` keys, `case_specific` checks.

---

## 7. Known limits

- Evidence for the DRIVER tier comes from 98 chats with only 16 returners: treat it as leads.
- Event labels are deterministic but not yet human-validated.
- `gates` needs the rubric judge (`judge/run_judge.py`, prompt v5); the event judge does not check G1–G4.
- `distress` may be over-labelled (28 of 98 real chats); spot-check before using `distress_handling` as a hard gate.
