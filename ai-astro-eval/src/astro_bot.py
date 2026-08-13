"""
The system under test: AI Astro ("Sitara"). Loads a versioned production
system prompt template from prompts/, fills in per-user/session variables
(birth data, marital status, Vedic expert data, memory), and logs the exact
assembled prompt used for each turn alongside the transcript.

Production returns structured JSON per turn ({"message", "marital_status"}),
not free text — this module calls generate_json() and extracts "message" for
the transcript while tracking "marital_status" across turns, since the prompt
re-assembles with the latest known status each turn (Step 2 of the prompt
asks up to 3 times, then assumes "unmarried").
"""

import datetime
import importlib
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.gemini_client import generate_json, MODEL_CONVERSATIONAL

BOT_RESPONSE_SCHEMA_HINT = """
{
  "message": "<chat reply text, following the persona's style rules>",
  "marital_status": "married" | "unmarried" | "unchanged"
}
"""

# Actual API-level structured-output schema (see gemini_client.generate_json's
# response_schema param) — enforces JSON structure as a hard constraint
# rather than a textual instruction the model can ignore (confirmed via live
# testing: under this persona's strong roleplay framing, the model
# occasionally returned plain in-character prose with zero JSON structure
# when only response_mime_type + a text instruction were used). "unchanged"
# is used instead of a nullable field — simpler than modeling nullability in
# this schema subset, and respond_to() below maps it back to "no update".
BOT_RESPONSE_JSON_SCHEMA = {
    "type": "object",
    "properties": {
        "message": {"type": "string"},
        "marital_status": {"type": "string", "enum": ["married", "unmarried", "unchanged"]},
    },
    "required": ["message", "marital_status"],
}


class _SafeFormatDict(dict):
    """
    format_map() backing dict that leaves unknown placeholders untouched
    instead of raising KeyError. The prompt template is under active
    iteration (placeholders get renamed/removed/hardcoded, e.g. "{parsed}"
    -> "{ASTRO_DATA}", "{marital_status}" hardcoded away) — this keeps
    _assemble_prompt() from breaking every time the template shape changes,
    while still substituting whichever placeholders ARE present.
    """

    def __missing__(self, key):
        return "{" + key + "}"


def load_astro_prompt(prompt_version):
    """
    prompt_version: e.g. "v1" -> prompts/astro_system_prompt_v1.py, which must
    define ASTRO_SYSTEM_PROMPT_TEMPLATE (a str.format() template).

    Returns (template, default_parsed). If the module also defines ASTRO_DATA
    (a real sample Vedic reading — PAST_EVENTS/EXPERT_DATA/REMEDIES), that is
    used as the default "parsed" value instead of "DATA_UNAVAILABLE", so a run
    actually exercises Phases 2-5 (predictions, past-event trust-building,
    remedies, retention hooks) rather than degrading to the no-data path on
    every test case. Falls back to "DATA_UNAVAILABLE" for prompt versions that
    don't define ASTRO_DATA.
    """
    module_name = f"prompts.astro_system_prompt_{prompt_version}"
    module = importlib.import_module(module_name)
    default_parsed = getattr(module, "ASTRO_DATA", "DATA_UNAVAILABLE")
    return module.ASTRO_SYSTEM_PROMPT_TEMPLATE, default_parsed


class AstroBot:
    def __init__(self, prompt_version, memory_object=None, user_profile=None, temperature=0.85):
        """
        user_profile: optional dict with date_of_birth/time_of_birth/
        place_of_birth/gender/parsed. Defaults to "unknown"/"DATA_UNAVAILABLE"
        — the eval harness has no birth-detail intake flow or astrological
        calculation engine of its own; test-case personas reveal birth
        details conversationally instead, matching how the placeholder
        values degrade gracefully per the prompt's own instructions.
        """
        self.prompt_template, self._default_parsed = load_astro_prompt(prompt_version)
        self.memory_object = memory_object
        self.user_profile = user_profile or {}
        self.temperature = temperature
        self.marital_status = "unknown"
        self._history = []  # from the bot's POV: role "user" = the human, "model" = the bot
        self.assembled_system_prompt = self._assemble_prompt()  # logged as of session start

    def _memory_summary_text(self):
        if not self.memory_object:
            return "(none - this is the user's first session)"
        consolidated = self.memory_object.get("consolidated_summary", {})
        concern = self.memory_object.get("concern_summary", {})
        return (
            "CONSOLIDATED SUMMARY:\n"
            f"{json.dumps(consolidated, indent=2)}\n\n"
            "CONCERN SUMMARY:\n"
            f"{json.dumps(concern, indent=2)}"
        )

    def _assemble_prompt(self):
        parsed_value = self.user_profile.get("parsed", self._default_parsed)
        values = _SafeFormatDict(
            current_date=self.user_profile.get("current_date", datetime.date.today().isoformat()),
            date_of_birth=self.user_profile.get("date_of_birth", "unknown"),
            time_of_birth=self.user_profile.get("time_of_birth", "unknown"),
            place_of_birth=self.user_profile.get("place_of_birth", "unknown"),
            gender=self.user_profile.get("gender", "unknown"),
            marital_status=self.marital_status,
            parsed=parsed_value,
            ASTRO_DATA=parsed_value,
            memory_summary=self._memory_summary_text(),
        )
        return self.prompt_template.format_map(values)

    def respond_to(self, user_message):
        self._history.append({"role": "user", "text": user_message})

        # Re-assemble each turn: marital_status may have been confirmed by
        # the previous turn, and the prompt's Step 2 behavior depends on it.
        self.assembled_system_prompt = self._assemble_prompt()

        result = generate_json(
            system_prompt=self.assembled_system_prompt,
            messages=self._history,
            schema_hint=BOT_RESPONSE_SCHEMA_HINT,
            temperature=self.temperature,
            model=MODEL_CONVERSATIONAL,
            response_schema=BOT_RESPONSE_JSON_SCHEMA,
        )
        message_text = result.get("message", "")
        new_status = result.get("marital_status")
        if new_status in ("married", "unmarried"):
            self.marital_status = new_status

        self._history.append({"role": "model", "text": message_text})
        return message_text
