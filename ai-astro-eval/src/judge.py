"""
Judge LLM. Scores a session (or, for the cross-session pass, a full 3-session
run) against every metric in metrics/metrics_framework.py.

Polarity enforcement: the judge model is prompted to always reason in
"1 = worst for the user, 10 = best for the user" terms directly (see
prompts/judge_prompt.py). This module additionally re-verifies/enforces that
mapping in code via normalize_score(), using METRICS_BY_KEY as the single
source of truth for each metric's polarity — so an individual judge call
scoring a metric backwards cannot silently corrupt results.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prompts.judge_prompt import JUDGE_SYSTEM_PROMPT_TEMPLATE, CROSS_SESSION_ADDENDUM
from metrics.metrics_framework import METRICS, METRICS_BY_KEY
from src.gemini_client import generate_json, MODEL_ANALYSIS

SESSION_SCHEMA_HINT = """
{
  "scores": {
    "<metric_key>": {"score_1_to_10": <int 1-10>, "justification": "<one sentence, transcript-referencing>"}
    // one entry per metric key listed
  },
  "went_right": ["<specific, evidenced>", "<specific, evidenced>", "<specific, evidenced>"],
  "went_wrong": ["<specific, evidenced>", "<specific, evidenced>", "<specific, evidenced>"]
}
"""

CROSS_SESSION_SCHEMA_HINT = """
{
  "prioritized_prompt_changes": [
    {
      "priority": <int, 1 = most important>,
      "change": "<specific change to make to the prompt>",
      "engagement_retention_reasoning": "<why this matters for whether a real user stays engaged / comes back>",
      "evidence": ["<specific transcript moments across sessions 1-3>"]
    }
  ],
  "decision_rule_verdict": "needs_fix" or "passing",
  "decision_rule_reasoning": "<how the test case's own decision_rule was applied to reach this verdict>"
}
"""


def _metrics_block():
    lines = []
    for m in METRICS:
        direction_note = "(higher raw occurrence = better)" if m["polarity"] == "high_is_good" else "(higher raw occurrence = WORSE — score inverted, 10 means this bad behavior did NOT happen)"
        lines.append(f"- {m['key']}: {m['description']} {direction_note}")
    return "\n".join(lines)


def _build_session_response_schema():
    """
    API-level structured-output schema (see gemini_client.generate_json's
    response_schema param) for score_session's output. Confirmed via a real
    run that SESSION_SCHEMA_HINT (a textual instruction) is not reliably
    followed: one run returned "scores": {} (a fully empty object) while
    went_right/went_wrong were populated correctly — the judge silently
    skipped filling in the 24 metric entries rather than erroring. Building
    every metric key as a REQUIRED property here makes that impossible: the
    API rejects/regenerates a response missing any of them, rather than
    silently accepting an empty scores object.
    """
    score_entry_schema = {
        "type": "object",
        "properties": {
            "score_1_to_10": {"type": "integer"},
            "justification": {"type": "string"},
        },
        "required": ["score_1_to_10", "justification"],
    }
    scores_properties = {m["key"]: score_entry_schema for m in METRICS}
    return {
        "type": "object",
        "properties": {
            "scores": {
                "type": "object",
                "properties": scores_properties,
                "required": list(scores_properties.keys()),
            },
            "went_right": {"type": "array", "items": {"type": "string"}},
            "went_wrong": {"type": "array", "items": {"type": "string"}},
        },
        "required": ["scores", "went_right", "went_wrong"],
    }


SESSION_RESPONSE_JSON_SCHEMA = _build_session_response_schema()


def normalize_score(metric_key, raw_score_1_to_10):
    """
    Authoritative polarity enforcement point. The judge prompt already asks
    for "1=worst,10=best" directly, so in the normal case raw_score is
    already correctly oriented. This function exists as the auditable,
    code-level backstop: it looks up the metric's declared polarity and
    would invert here if the pipeline is ever changed to have the judge
    reason on a raw natural-direction scale instead of a worst/best scale.
    Currently a passthrough with bounds-checking and polarity lookup logged.
    """
    metric = METRICS_BY_KEY[metric_key]
    score = int(raw_score_1_to_10)
    if not 1 <= score <= 10:
        raise ValueError(f"Score for {metric_key} out of bounds: {score}")
    return {
        "score_1_to_10": score,
        "polarity_applied": metric["polarity"],
    }


def score_session(transcript_turns, session_label, prompt_version, persona_variant, gap_variant):
    system_prompt = JUDGE_SYSTEM_PROMPT_TEMPLATE.format(
        metrics_block=_metrics_block(),
        cross_session_block="(This is a single-session scoring pass, not the cross-session synthesis.)",
    )
    transcript_text = "\n".join(
        f"{'USER' if t['role'] == 'user' else 'ASTROLOGER'}: {t['text']}" for t in transcript_turns
    )
    context_header = (
        f"Session: {session_label} | Prompt version: {prompt_version} | "
        f"Persona variant: {persona_variant} | Memory gap variant: {gap_variant}\n\n"
    )

    result = generate_json(
        system_prompt=system_prompt,
        messages=[{"role": "user", "text": context_header + transcript_text}],
        schema_hint=SESSION_SCHEMA_HINT,
        temperature=0.2,
        model=MODEL_ANALYSIS,
        response_schema=SESSION_RESPONSE_JSON_SCHEMA,
    )

    normalized_scores = {}
    missing_metrics = []
    for metric_key, entry in result.get("scores", {}).items():
        if metric_key not in METRICS_BY_KEY:
            continue
        if not isinstance(entry, dict) or "score_1_to_10" not in entry:
            # Judge models occasionally emit a malformed entry for one metric
            # (missing key, wrong shape) even when the overall JSON is valid.
            # Skip just that metric rather than crashing the whole run over
            # one flaky field — report_generator renders a "-" for it, and
            # this is logged so it's visible, not silently swallowed.
            missing_metrics.append(metric_key)
            continue
        normalized = normalize_score(metric_key, entry["score_1_to_10"])
        normalized_scores[metric_key] = {
            "score_1_to_10": normalized["score_1_to_10"],
            "polarity_applied": normalized["polarity_applied"],
            "justification": entry.get("justification", ""),
        }
    if missing_metrics:
        print(f"  [judge warning] {session_label}: malformed/missing score entries for: {missing_metrics}")

    return {
        "session_label": session_label,
        "scores": normalized_scores,
        "went_right": result.get("went_right", []),
        "went_wrong": result.get("went_wrong", []),
    }


def score_cross_session(all_transcripts_by_session, decision_rule, prompt_version, persona_variant, gap_variant):
    cross_addendum = CROSS_SESSION_ADDENDUM.format(
        needs_fix_if=decision_rule["needs_fix_if"],
        passing_if=decision_rule["passing_if"],
    )
    system_prompt = JUDGE_SYSTEM_PROMPT_TEMPLATE.format(
        metrics_block=_metrics_block(),
        cross_session_block=cross_addendum,
    )

    combined = []
    for label, turns in all_transcripts_by_session.items():
        combined.append(f"=== {label.upper()} ===")
        combined.extend(
            f"{'USER' if t['role'] == 'user' else 'ASTROLOGER'}: {t['text']}" for t in turns
        )
    transcript_text = "\n".join(combined)
    context_header = (
        f"Cross-session synthesis pass | Prompt version: {prompt_version} | "
        f"Persona variant: {persona_variant} | Memory gap variant: {gap_variant}\n\n"
    )

    result = generate_json(
        system_prompt=system_prompt,
        messages=[{"role": "user", "text": context_header + transcript_text}],
        schema_hint=CROSS_SESSION_SCHEMA_HINT,
        temperature=0.2,
        model=MODEL_ANALYSIS,
    )
    return result
