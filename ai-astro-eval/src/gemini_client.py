"""
Thin shared wrapper around the Gemini API (google-genai SDK) used by all
three roles (user simulator, astro bot, judge). Kept in one place so model
name / retry / JSON-mode behavior is consistent across the pipeline.
"""

import json
import os
import time

from google import genai
from google.genai import types

DEFAULT_MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")

# Per-role model assignment: conversational roles (user simulator, astro bot)
# use the lighter/cheaper model since they run many turns per session; the
# judge (and summarizer, an analysis role like the judge rather than a
# conversational one) uses the stronger model since scoring/extraction
# accuracy matters more than per-call cost there.
MODEL_CONVERSATIONAL = os.environ.get("GEMINI_MODEL_CONVERSATIONAL", "gemini-3.5-flash-lite")
MODEL_ANALYSIS = os.environ.get("GEMINI_MODEL_ANALYSIS", "gemini-3.5-flash")

_client = None


def _get_client():
    global _client
    if _client is not None:
        return _client
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not set. Add it to your environment or .env file."
        )
    _client = genai.Client(api_key=api_key)
    return _client


def _to_contents(messages):
    """messages: list of {"role": "user"|"model", "text": "..."} in chronological order."""
    return [
        types.Content(role=m["role"], parts=[types.Part(text=m["text"])])
        for m in messages
    ]


# gemini-3.x models "think" by default (extended reasoning before the final
# answer). None of our three roles strictly need that — a chat reply, a JSON
# scoring object, and a JSON memory summary are all direct-answer tasks.
# thinking_budget=0 (fully off) is REJECTED by these models with a 400
# INVALID_ARGUMENT — confirmed via direct API test — so this uses a small
# bounded budget instead. Confirmed via live testing that under JSON mode
# with a long system prompt (astro bot's full persona + ASTRO_DATA + growing
# history), the model intermittently returns finish_reason=MALFORMED_RESPONSE
# (empty response.text, no exception) — a probabilistic Gemini-side
# structured-output glitch, not a bug in this retry loop. It's usually
# transient (a retry recovers), but a small thinking budget appears to make
# it more frequent, so this is set higher than the bare minimum (128) that
# was tried first, trading a little latency/cost for reliability.
THINKING_CONFIG_MINIMAL = types.ThinkingConfig(thinking_budget=512)
MAX_OUTPUT_TOKENS = 8192


def generate_text(system_prompt, messages, temperature=0.85, model=None, max_retries=4):
    """
    Returns the raw text of the model's reply.

    temperature defaults high (0.85) for the user-simulator/astro-bot roles so
    repeated runs of the same test case are NOT near-identical — this is a
    functional requirement (see run_eval.py docs / README), not a style choice.
    """
    client = _get_client()
    model = model or DEFAULT_MODEL
    contents = _to_contents(messages)

    last_err = None
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=model,
                contents=contents,
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    temperature=temperature,
                    thinking_config=THINKING_CONFIG_MINIMAL,
                    max_output_tokens=MAX_OUTPUT_TOKENS,
                ),
            )
            if not response.text:
                # Happens on safety filtering / non-STOP finish reasons (e.g.
                # MAX_TOKENS, RECITATION) or an empty-but-non-None string.
                # Treat as a retryable failure rather than propagating an
                # empty/None value into downstream string operations.
                candidates = getattr(response, "candidates", None) or []
                finish_reason = candidates[0].finish_reason if candidates else "unknown"
                raise RuntimeError(f"Gemini returned no text (finish_reason={finish_reason})")
            return response.text
        except Exception as e:  # noqa: BLE001 - retry any transient API failure
            last_err = e
            time.sleep(min(2 ** attempt, 10))
    raise RuntimeError(f"Gemini call failed after {max_retries} attempts: {last_err}")


def generate_json(system_prompt, messages, schema_hint="", temperature=0.4, model=None, max_retries=7,
                   response_schema=None):
    """
    Generate JSON output. schema_hint is appended to the prompt describing the
    exact JSON shape expected. Returns a parsed Python object.

    Used for summarizer and judge output, where we need structured, parseable
    results rather than free text.

    max_retries defaults higher than generate_text's (7 vs 4): this is the
    path that hits Gemini's intermittent MALFORMED_RESPONSE finish reason
    (see THINKING_CONFIG_MINIMAL comment above) — each retry is cheap relative
    to losing an entire multi-session test run to one flaky call deep into a
    long conversation.

    response_schema: optional JSON-Schema-shaped dict (OpenAPI 3.0 subset —
    see google.genai.types.GenerateContentConfig.response_schema). Confirmed
    via live testing that response_mime_type="application/json" ALONE is only
    a soft hint the model can ignore — under a strong roleplay persona system
    prompt, the astro bot occasionally returned plain in-character prose with
    no JSON structure at all, which no amount of retrying that exact request
    reliably fixes (it's a compliance failure, not a transient glitch).
    Passing response_schema makes JSON structure an API-level constraint
    instead of a textual instruction the model can override. Pass it whenever
    the caller has a small, fixed output shape (see astro_bot.py); omit it for
    schemas too complex/dynamic to express this way (e.g. the judge's 24
    metric keys) and rely on schema_hint + retries there instead.
    """
    client = _get_client()
    model = model or DEFAULT_MODEL
    full_system = (
        system_prompt
        + "\n\nRespond with ONLY valid JSON, no markdown fences, matching this shape:\n"
        + schema_hint
    )
    contents = _to_contents(messages)

    last_err = None
    for attempt in range(max_retries):
        try:
            config_kwargs = dict(
                system_instruction=full_system,
                temperature=temperature,
                response_mime_type="application/json",
                thinking_config=THINKING_CONFIG_MINIMAL,
                max_output_tokens=MAX_OUTPUT_TOKENS,
            )
            if response_schema is not None:
                config_kwargs["response_schema"] = response_schema
            response = client.models.generate_content(
                model=model,
                contents=contents,
                config=types.GenerateContentConfig(**config_kwargs),
            )
            if not response.text:
                candidates = getattr(response, "candidates", None) or []
                finish_reason = candidates[0].finish_reason if candidates else "unknown"
                raise RuntimeError(f"Gemini returned no text for JSON call (finish_reason={finish_reason})")
            text = response.text.strip()
            try:
                return json.loads(text)
            except json.JSONDecodeError as parse_err:
                raise RuntimeError(
                    f"Gemini JSON call returned non-JSON text (len={len(text)}): "
                    f"{text[:300]!r} ({parse_err})"
                ) from parse_err
        except Exception as e:  # noqa: BLE001
            last_err = e
            time.sleep(min(2 ** attempt, 10))
    raise RuntimeError(f"Gemini JSON call failed after {max_retries} attempts: {last_err}")
