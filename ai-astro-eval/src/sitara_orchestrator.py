"""
Runs one Sitara test case (one persona variant, gap variant and run number):
simulator ⇄ astro bot per session, production summary chained into the next
session, event judge + metrics_v2 values per session. Writes

  results/<version>/<case>/<persona>[_<gap>]/run_<n>/
      meta.json
      session_<k>/transcript.json  transcript.md  labels.json  metrics.json  verdict.json  usage.json
      session_<k>/memory_summary.json   (session 2+: summary injected at its start)
"""

import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.astro_bot import AstroBot
from src.summarizer import summarize_session
from src.sitara_simulator import SitaraSimulator, clock_label
from src.gemini_client import MODEL_CONVERSATIONAL, MODEL_SIMULATOR, ASTRO_THINKING_LEVEL, start_usage
from src import event_judge
from src.chat_parser import render_transcript

RESULTS_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results")

# Simulated clock: user messages at t, astro reply at t+15s, next user turn at t+30s
# (about 10 exchanges in the 5-minute first chat).
ASTRO_DELAY_SEC = 15
EXCHANGE_SEC = 30
CHAT_END_SEC = 300
TIME_LOW_SEC = 240

# Birth details of the test chart in the prompts' data (personas use the same, see run_sitara.py).
CHART_PROFILE = {
    "current_date": "18 Nov 2026",
    "date_of_birth": "1 Aug 2003",
    "time_of_birth": "4:30 am",
    "place_of_birth": "Nandyal, Andhra Pradesh",
    "gender": "as stated by the user",
}


def case_sessions(case):
    """[(session_label, session_def)] for single- and multi-session cases."""
    if "sessions" in case:
        return sorted(case["sessions"].items())
    return [("session_1", {"persona": case["persona"], "pressure_points": case["pressure_points"]})]


def run_dir_for(prompt_version, case_id, persona_name, gap_variant, run_number):
    variant = persona_name + (f"_{gap_variant}" if gap_variant else "")
    return os.path.join(RESULTS_ROOT, prompt_version + os.environ.get("RESULTS_TAG", ""), case_id, variant, f"run_{run_number}")


def run_session(sim, bot, max_turns):
    """Returns (msgs, verdict). msgs use the event judge's format:
    {"idx", "role": "USER"|"ASTRO", "text", "sec"}."""
    msgs, clock = [], 0
    user_lines = sim.opening()
    for _ in range(max_turns):
        if not user_lines:
            break
        for line in user_lines:
            msgs.append({"role": "USER", "text": line, "sec": clock})
        # a burst of user lines goes to the bot as one turn
        # prompts with an {elapsed_time} placeholder see the chat clock as mm:ss
        bot.user_profile["elapsed_time"] = clock_label(clock).strip("[]")
        astro_text = bot.respond_to("\n".join(user_lines))
        msgs.append({"role": "ASTRO", "text": astro_text, "sec": clock + ASTRO_DELAY_SEC,
                     "raw_response": bot.last_raw_response})
        clock += EXCHANGE_SEC
        # prompts with a {time_running_out} placeholder see "True" for the last minute
        bot.user_profile["time_running_out"] = str(clock >= TIME_LOW_SEC)
        if sim.left:
            break
        user_lines = sim.reply(astro_text, clock)
        if sim.left:
            for line in user_lines:
                msgs.append({"role": "USER", "text": line, "sec": clock})
            break
    # the persona can leave without a [VERDICT] line; ask for it explicitly
    for _ in range(2):
        if sim.verdict:
            break
        sim.force_leave(max(clock, CHAT_END_SEC))
    for i, m in enumerate(msgs):
        m["idx"] = i
    return msgs, sim.verdict


def run_case(case, prompt_version, persona_name, persona_prompt, gap_variant, run_number):
    run_dir = run_dir_for(prompt_version, case["id"], persona_name, gap_variant, run_number)
    if os.path.isdir(run_dir) and os.listdir(run_dir):
        raise FileExistsError(run_dir)
    os.makedirs(run_dir, exist_ok=True)

    max_turns = case.get("max_turns") or case["max_turns_per_session"]
    judge_client = event_judge.make_client()
    _write_json(os.path.join(run_dir, "meta.json"), {
        "case_id": case["id"], "prompt_version": prompt_version, "persona": persona_name,
        "gap_variant": gap_variant, "run": run_number,
        "astro_model": MODEL_CONVERSATIONAL, "astro_thinking": ASTRO_THINKING_LEVEL or "budget 512", "simulator_model": MODEL_SIMULATOR,
        "event_judge_model": event_judge.MODEL,
        "event_judge_prompt_sha1": hashlib.sha1(event_judge.PROMPT.encode()).hexdigest()[:12],
    })

    memory = None
    sessions = case_sessions(case)
    for k, (label, session_def) in enumerate(sessions, start=1):
        session_dir = os.path.join(run_dir, label)
        os.makedirs(session_dir, exist_ok=True)
        if memory is not None:
            _write_json(os.path.join(session_dir, "memory_summary.json"), memory)

        usage = start_usage()
        sim = SitaraSimulator(persona_prompt, session_def["pressure_points"],
                              session_index=k, gap_variant=gap_variant)
        bot = AstroBot(prompt_version=prompt_version, memory_object=memory, user_profile=dict(CHART_PROFILE))
        msgs, verdict = run_session(sim, bot, max_turns)

        judge_msgs = [{k2: m[k2] for k2 in ("idx", "role", "text", "sec")} for m in msgs]
        labels = event_judge.call(judge_client, render_transcript(judge_msgs))
        values = event_judge.metrics(judge_msgs, labels)

        _write_json(os.path.join(session_dir, "transcript.json"), msgs)
        _write_json(os.path.join(session_dir, "labels.json"), labels)
        _write_json(os.path.join(session_dir, "metrics.json"), values)
        _write_json(os.path.join(session_dir, "verdict.json"), verdict)
        with open(os.path.join(session_dir, "transcript.md"), "w") as f:
            f.write(f"# {case['id']} {label}: {persona_name} {gap_variant or ''} run {run_number}\n\n")
            f.writelines(f"{clock_label(m['sec'])} **{m['role']}**: {m['text']}\n\n" for m in msgs)
            f.write(f"**VERDICT**: {json.dumps(verdict, ensure_ascii=False)}\n")

        if k < len(sessions):
            # production summary, chained: previous summary + this session only
            memory = summarize_session(memory, [
                {"role": "user" if m["role"] == "USER" else "model", "text": m["text"]} for m in msgs
            ])
        _write_json(os.path.join(session_dir, "usage.json"), usage)
    return run_dir


def _write_json(path, obj):
    with open(path, "w") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
