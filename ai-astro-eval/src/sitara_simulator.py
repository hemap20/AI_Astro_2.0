"""
Simulated user for the Sitara test cases. The system prompt is a behaviour
persona from personas/ with {scenario} filled from the test case, plus the
case's pressure points. Each astro reply is sent with the elapsed chat time as
[mm:ss]; the persona leaves at 05:00 with [LEAVE] and one [VERDICT] line.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.gemini_client import generate_text, MODEL_SIMULATOR

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PERSONA_FILES = {
    "direct_answer_chaser": "personas/sitara_1_direct_answer_chaser.md",
    "passive_follower": "personas/sitara_2_passive_follower.md",
}
_FILE_TO_NAME = {os.path.basename(v): k for k, v in PERSONA_FILES.items()}
_BEHAVIOUR_RE = re.compile(r"Use behaviour prompt:\s*personas/(\S+\.md)")


def persona_name_in_case(persona_text):
    """Persona named by a case's 'Use behaviour prompt: personas/<file>.md'
    line, or None for an inline persona (S5)."""
    m = _BEHAVIOUR_RE.search(persona_text)
    return _FILE_TO_NAME[m.group(1)] if m else None


def build_persona_prompt(persona_text, persona_name):
    """persona_name: one of PERSONA_FILES, or None to use the case's inline
    persona text as-is."""
    if persona_name is None:
        return persona_text.strip()
    scenario = persona_text.split("SCENARIO:", 1)[-1].strip()
    with open(os.path.join(ROOT, PERSONA_FILES[persona_name])) as f:
        return f.read().replace("{scenario}", scenario)


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


def clock_label(sec):
    return f"[{sec // 60:02d}:{sec % 60:02d}]"


SESSION_FRAMING = {
    "same_day": (
        "This is your SECOND chat with the same astrologer, less than an hour after the first. "
        "Do not send your app details again."
    ),
    "genuine_return": (
        "This is your SECOND chat with the same astrologer, a day or more after the first. "
        "Do not send your app details again."
    ),
}


class SitaraSimulator:
    def __init__(self, persona_prompt, pressure_points, session_index=1, gap_variant=None, temperature=0.85):
        self.persona_prompt = persona_prompt
        self.pressure_points = list(pressure_points)
        self.session_index = session_index
        self.gap_variant = gap_variant
        self.temperature = temperature
        self._history = []  # simulator POV: "user" = astro + clock, "model" = own turns
        self.verdict = None
        self.left = False

    def _system_prompt(self):
        points = "\n".join(f"- {p}" for p in self.pressure_points)
        framing = SESSION_FRAMING[self.gap_variant] + "\n\n" if self.session_index > 1 else ""
        return f"""{self.persona_prompt}

# THIS CHAT
{framing}Work these beats into the chat roughly in order. They are intents, not lines to read out:
react to what the astrologer actually said first.
{points}
"""

    def _turn(self, incoming):
        self._history.append({"role": "user", "text": incoming})
        raw = generate_text(
            system_prompt=self._system_prompt(),
            messages=self._history,
            temperature=self.temperature,
            model=MODEL_SIMULATOR,
            role="simulator",
        )
        self._history.append({"role": "model", "text": raw})
        if "[LEAVE]" in raw or "[VERDICT]" in raw:
            self.left = True
            self.verdict = parse_verdict(raw) or self.verdict
        return _clean_lines(raw)

    def opening(self):
        """First USER turn(s): app details (session 1) and the opener."""
        return self._turn("[00:00] The chat has started. Send your first message(s).")

    def reply(self, astro_text, sec):
        return self._turn(f"{clock_label(sec)} {astro_text}")

    def force_leave(self, sec):
        """Asks for the [LEAVE]/[VERDICT] when the loop stops before the persona left."""
        self._turn(f"{clock_label(sec)} (The free chat time is over.) Output only [LEAVE] and your "
                   "[VERDICT] line in the exact format from your instructions.")


def _clean_lines(raw):
    """One USER message per line; drops [LEAVE]/[VERDICT] text."""
    text = raw.split("[VERDICT]", 1)[0].replace("[LEAVE]", "\n")
    return [line.strip() for line in text.splitlines() if line.strip()]
