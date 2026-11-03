"""
Claude (Anthropic API) counterpart to gemini_client.generate_json(), used only
for the astro-bot role when it's run on a Claude model. Structured output is
enforced by forcing a single tool call whose input_schema is the bot's
response schema — the Claude equivalent of Gemini's response_schema.
"""

import json
import os
import time

import anthropic

MAX_OUTPUT_TOKENS = 4096

_client = None


def _get_client():
    global _client
    if _client is not None:
        return _client
    api_key = os.environ.get("CLAUDE_API_KEY") or os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("CLAUDE_API_KEY is not set. Add it to your environment or .env file.")
    _client = anthropic.Anthropic(api_key=api_key)
    return _client


def _to_messages(messages):
    """Gemini-style {"role": "user"|"model", "text"} -> Anthropic messages,
    merging consecutive same-role turns (Anthropic requires alternation)."""
    out = []
    for m in messages:
        role = "assistant" if m["role"] == "model" else "user"
        if out and out[-1]["role"] == role:
            out[-1]["content"] += "\n" + m["text"]
        else:
            out.append({"role": role, "content": m["text"]})
    return out


def generate_json(system_prompt, messages, schema_hint="", temperature=0.85, model=None, max_retries=7,
                  response_schema=None):
    client = _get_client()
    tool = {
        "name": "respond",
        "description": "Send your reply. Always call this tool with your full response.\n" + schema_hint,
        "input_schema": response_schema or {"type": "object"},
    }
    kwargs = dict(
        model=model,
        system=system_prompt,
        messages=_to_messages(messages),
        max_tokens=MAX_OUTPUT_TOKENS,
        tools=[tool],
        tool_choice={"type": "tool", "name": "respond"},
        temperature=temperature,
    )

    last_err = None
    for attempt in range(max_retries):
        try:
            response = client.messages.create(**kwargs)
            for block in response.content:
                if block.type == "tool_use":
                    return block.input
                if block.type == "text" and "output_config" in kwargs:
                    return json.loads(block.text)
            raise RuntimeError(f"Claude returned no structured output (stop_reason={response.stop_reason})")
        except anthropic.BadRequestError as e:
            # Newer models don't allow forced tool_choice; use JSON-schema output instead.
            if "tool_choice" in str(e) and "tools" in kwargs:
                kwargs.pop("tools")
                kwargs.pop("tool_choice")
                schema = dict(response_schema or {"type": "object"}, additionalProperties=False)
                kwargs["output_config"] = {"format": {"type": "json_schema", "schema": schema}}
                continue
            # Some newer models reject `temperature`; drop it once and retry.
            if "temperature" in str(e) and "temperature" in kwargs:
                kwargs.pop("temperature")
                continue
            raise
        except Exception as e:  # noqa: BLE001 - retry any transient API failure
            last_err = e
            time.sleep(min(2 ** attempt, 10))
    raise RuntimeError(f"Claude call failed after {max_retries} attempts: {last_err}")
