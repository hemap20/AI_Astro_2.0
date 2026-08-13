"""
Runs the production chat-summarization prompt over a just-completed session's
transcript to produce the memory object carried into the next session.

Confirmed production behavior (see prompts/summarizer_prompt.py): summarization
is INCREMENTAL. Each call receives the user's previous consolidated_summary and
previous concern_summary (each possibly empty/null on a user's first session)
plus ONLY the current session's chat, and returns updated versions of both,
merging duplicates and incrementing mention_count rather than re-deriving
everything from the full multi-session transcript. This module chains that way:
session_2's summary call is seeded with session_1's output + session_2's
transcript alone; session_3's summary call is seeded with the (session_1+2)
summary + session_3's transcript alone.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prompts.summarizer_prompt import CHAT_SUMMARY_SYSTEM_PROMPT, CHAT_SUMMARY_USER_PROMPT
from src.gemini_client import generate_json, MODEL_ANALYSIS

MEMORY_SCHEMA_HINT = """
{
  "consolidated_summary": {
    "primary_concern": ["..."],
    "secondary_concerns": ["..."],
    "remedies_mentioned": ["..."],
    "astro_solutions": "...",
    "user_description": "...",
    "recommendation": ["..."]
  },
  "concern_summary": {
    "title": "User Summary",
    "profile": {"age": null, "description": "..."},
    "data": [
      {
        "title": "Primary Concerns",
        "content": [
          {"title": "...", "description": "...", "mention_count": 1, "validated_prediction": null}
        ]
      }
    ]
  }
}
"""

EMPTY_CONSOLIDATED_SUMMARY = "(none - this is the user's first session)"
EMPTY_CONCERN_SUMMARY = "(none - this is the user's first session)"


def _transcript_to_text(transcript_turns):
    lines = []
    for turn in transcript_turns:
        speaker = "USER" if turn["role"] == "user" else "ASTROLOGER"
        lines.append(f"{speaker}: {turn['text']}")
    return "\n".join(lines)


def summarize_session(previous_memory_object, new_session_transcript):
    """
    previous_memory_object: dict with "consolidated_summary"/"concern_summary"
    keys (the output of a prior summarize_session call), or None for a user's
    first-ever session.
    new_session_transcript: transcript_turns list for ONLY the session just
    completed (not prior sessions — production summarization is incremental,
    it is never re-run over full history).
    """
    if previous_memory_object:
        prev_consolidated = previous_memory_object.get("consolidated_summary", {})
        prev_concern = previous_memory_object.get("concern_summary", {})
    else:
        prev_consolidated = EMPTY_CONSOLIDATED_SUMMARY
        prev_concern = EMPTY_CONCERN_SUMMARY

    user_prompt = CHAT_SUMMARY_USER_PROMPT.format(
        previous_consolidated_summary=prev_consolidated,
        previous_concern_summary=prev_concern,
    )
    user_prompt += "\n" + _transcript_to_text(new_session_transcript)

    result = generate_json(
        system_prompt=CHAT_SUMMARY_SYSTEM_PROMPT,
        messages=[{"role": "user", "text": user_prompt}],
        schema_hint=MEMORY_SCHEMA_HINT,
        temperature=0.2,
        model=MODEL_ANALYSIS,
    )
    return result
