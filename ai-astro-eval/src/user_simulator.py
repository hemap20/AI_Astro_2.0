"""
Simulated user (Gemini). Generates each user turn dynamically, in-character,
reacting to what the astro bot actually said — never plays back scripted
lines verbatim.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prompts.user_simulator_guide import USER_STYLE_GUIDE
from src.gemini_client import generate_text, MODEL_CONVERSATIONAL

MIN_TURNS_PER_SESSION = 10


class UserSimulator:
    def __init__(self, persona_text, pressure_points, memory_gap_variant, session_label,
                 max_turns, persona_variant_label="primary", temperature=0.85):
        self.persona_text = persona_text
        self.pressure_points = list(pressure_points)
        self.memory_gap_variant = memory_gap_variant
        self.session_label = session_label
        self.target_turns = max(max_turns, MIN_TURNS_PER_SESSION)
        self.persona_variant_label = persona_variant_label
        self.temperature = temperature
        self._history = []  # list of {"role": "user"|"model", "text": ...} from the simulator's POV

    def _gap_framing(self):
        if self.memory_gap_variant == "same_day":
            return (
                "CONTINUATION CONTEXT: You are continuing the SAME conversation/day as before "
                "(less than 1 hour has passed since your last session). You are picking the "
                "conversation back up almost immediately, not returning after time away."
            )
        return (
            "RETURN CONTEXT: A genuine gap of at least 24 hours has passed since your last "
            "session. You are returning after being away, the way a real user reopens a chat "
            "the next day or later — not mid-conversation."
        )

    def _system_prompt(self):
        remaining_points = "\n".join(f"- {p}" for p in self.pressure_points)
        return f"""{USER_STYLE_GUIDE}

{self._gap_framing()}

YOUR PERSONA FOR THIS TEST CASE:
{self.persona_text}

GOALS/INTENTS FOR THIS SESSION ({self.session_label}) — work these into the
conversation in ROUGHLY this order, but you are simulating a real person, not
reading a script:
{remaining_points}

CRITICAL: these are goals and intents, not lines to output verbatim. At every
turn, read what the astrologer actually just said and respond in-character to
THAT — if they already answered something a later goal was going to ask about,
skip it, react to it, or rephrase naturally instead of robotically asking it
anyway. If a goal doesn't fit naturally where you expected, use your judgment
on when/how to bring it up, or drop it if it's been made moot by the
conversation.

This session should run at least {self.target_turns} user-bot exchanges. Once
your listed goals are covered, continue chatting naturally and in-character —
ask real follow-up questions, react to what the astrologer says, banter or
express feelings consistent with your persona — rather than stopping early or
repeating yourself. Do not mention that you are an AI, a simulation, a test,
or that you have a target number of turns; you are just a person texting.

When you believe the conversation has reached a natural close for this
session (goals covered, enough turns passed, conversation feels resolved for
now), end your message with the exact token [[SESSION_END]] on its own line
after your final in-character message.
"""

    def opening_message(self):
        text = generate_text(
            system_prompt=self._system_prompt(),
            messages=[{"role": "user", "text": "Begin the conversation with your opening message as this persona."}],
            temperature=self.temperature,
            model=MODEL_CONVERSATIONAL,
        )
        result = self._strip_end_token(text)
        self._remember_own_turn(result["text"])
        return result

    def respond_to(self, bot_message):
        self._history.append({"role": "user", "text": bot_message})
        prompt = (
            "The astrologer just said the above. Respond in-character as your next message(s). "
            "If you would naturally send this as multiple quick separate messages, put the literal "
            "marker [[MSG_BREAK]] on its own line between each separate message so the harness can "
            "split them into distinct bubbles. Do not use [[MSG_BREAK]] if you are sending only one message."
        )
        self._history.append({"role": "user", "text": prompt})
        text = generate_text(
            system_prompt=self._system_prompt(),
            messages=self._history,
            temperature=self.temperature,
            model=MODEL_CONVERSATIONAL,
        )
        result = self._strip_end_token(text)
        self._remember_own_turn(result["text"])
        return result

    def _remember_own_turn(self, text_with_msg_break):
        # Store the FULLY cleaned text (both control tokens removed) in
        # history — never the raw/[[SESSION_END]]-stripped-only text that
        # gets returned to the orchestrator. If [[MSG_BREAK]] (still present
        # in the returned text, needed downstream for bubble-splitting) were
        # also stored here, the model would see its own literal control
        # tokens echoed back in later turns and can get confused into
        # narrating about "receiving a token" instead of staying in
        # character (observed in practice with the lighter conversational
        # model). The model only ever needs to see clean in-character text.
        fully_clean = text_with_msg_break.replace("[[MSG_BREAK]]", " ").strip()
        self._history.append({"role": "model", "text": fully_clean})

    @staticmethod
    def _strip_end_token(text):
        ended = "[[SESSION_END]]" in text
        clean = text.replace("[[SESSION_END]]", "").strip()
        return {"text": clean, "session_end": ended}
