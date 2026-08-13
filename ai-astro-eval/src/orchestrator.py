"""
Runs the full 3-session loop for a single (test_case, persona_variant,
gap_variant, run_number) combination, and writes results to disk.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.user_simulator import UserSimulator, MIN_TURNS_PER_SESSION
from src.astro_bot import AstroBot
from src.summarizer import summarize_session
from src import judge as judge_mod
from src.report_generator import write_session_report, write_rollup_summary

RESULTS_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results")


def run_session(persona_text, pressure_points, memory_gap_variant, session_label,
                 max_turns, memory_object, prompt_version, persona_variant_label):
    """
    Runs one session to completion. Enforces the minimum-turn floor in code:
    the loop will not accept session_end before MIN_TURNS_PER_SESSION (or
    max_turns if higher) real exchanges have happened, regardless of what the
    simulator signals.
    """
    target_turns = max(max_turns, MIN_TURNS_PER_SESSION)

    simulator = UserSimulator(
        persona_text=persona_text,
        pressure_points=pressure_points,
        memory_gap_variant=memory_gap_variant,
        session_label=session_label,
        max_turns=target_turns,
        persona_variant_label=persona_variant_label,
    )
    bot = AstroBot(prompt_version=prompt_version, memory_object=memory_object)

    transcript = []  # list of {"role": "user"|"model", "text": ...}

    opening = simulator.opening_message()
    user_msgs = _split_burst(opening["text"])
    for msg in user_msgs:
        transcript.append({"role": "user", "text": msg})

    turn_count = 0
    session_end_signaled = opening["session_end"]

    while True:
        bot_reply = bot.respond_to(transcript[-1]["text"])
        transcript.append({"role": "model", "text": bot_reply})
        turn_count += 1

        can_end = turn_count >= target_turns
        if session_end_signaled and can_end:
            break
        if turn_count >= target_turns * 2:
            # hard safety cap so a non-cooperating simulator can't loop forever
            break

        step = simulator.respond_to(bot_reply)
        session_end_signaled = step["session_end"]
        for msg in _split_burst(step["text"]):
            transcript.append({"role": "user", "text": msg})

        if not can_end and turn_count < target_turns:
            continue

    return transcript, bot.assembled_system_prompt


def _split_burst(text):
    parts = [p.strip() for p in text.split("[[MSG_BREAK]]") if p.strip()]
    return parts if parts else [text.strip()]


def _result_dir(prompt_version, test_case_id, persona_variant_label, gap_variant, run_number):
    run_dir = os.path.join(
        RESULTS_ROOT, prompt_version, test_case_id,
        f"{persona_variant_label}_{gap_variant}_run{run_number}",
    )
    return run_dir


def _ensure_no_silent_overwrite(run_dir):
    if os.path.exists(run_dir) and os.listdir(run_dir):
        raise FileExistsError(
            f"Results already exist at {run_dir}. Refusing to overwrite silently. "
            f"Remove the directory, bump the prompt version, or choose a different run number."
        )
    os.makedirs(run_dir, exist_ok=True)


def run_single(test_case, prompt_version, persona_variant_label, persona_text_by_session,
                gap_variant, run_number):
    run_dir = _result_dir(prompt_version, test_case["id"], persona_variant_label, gap_variant, run_number)
    _ensure_no_silent_overwrite(run_dir)

    sessions = test_case["sessions"]
    session_labels = ["session_1", "session_2", "session_3"]

    all_transcripts = {}
    all_prompts_used = {}
    session_judge_results = {}
    memory_snapshots = {}
    memory_object = None

    for label in session_labels:
        session_def = sessions[label]
        persona_text = persona_text_by_session[label]
        max_turns = test_case["max_turns_per_session"]

        transcript, assembled_prompt = run_session(
            persona_text=persona_text,
            pressure_points=session_def["pressure_points"],
            memory_gap_variant=gap_variant,
            session_label=label,
            max_turns=max_turns,
            memory_object=memory_object,
            prompt_version=prompt_version,
            persona_variant_label=persona_variant_label,
        )
        all_transcripts[label] = transcript
        all_prompts_used[label] = assembled_prompt

        judge_result = judge_mod.score_session(
            transcript_turns=transcript,
            session_label=label,
            prompt_version=prompt_version,
            persona_variant=persona_variant_label,
            gap_variant=gap_variant,
        )
        session_judge_results[label] = judge_result

        if label != "session_3":
            # Incremental chaining, matching confirmed production behavior:
            # each summary call is seeded with the PRIOR summary object (not
            # prior transcripts) plus only the just-completed session's chat.
            memory_object = summarize_session(memory_object, transcript)
            snapshot_name = f"memory_snapshot_after_{label}.json"
            memory_snapshots[snapshot_name] = memory_object

    cross_session_result = judge_mod.score_cross_session(
        all_transcripts_by_session=all_transcripts,
        decision_rule=test_case["decision_rule"],
        prompt_version=prompt_version,
        persona_variant=persona_variant_label,
        gap_variant=gap_variant,
    )

    _write_run_outputs(
        run_dir=run_dir,
        test_case=test_case,
        prompt_version=prompt_version,
        persona_variant_label=persona_variant_label,
        gap_variant=gap_variant,
        run_number=run_number,
        all_transcripts=all_transcripts,
        all_prompts_used=all_prompts_used,
        memory_snapshots=memory_snapshots,
        session_judge_results=session_judge_results,
        cross_session_result=cross_session_result,
    )

    return {
        "run_dir": run_dir,
        "session_judge_results": session_judge_results,
        "cross_session_result": cross_session_result,
    }


def _write_run_outputs(run_dir, test_case, prompt_version, persona_variant_label, gap_variant,
                        run_number, all_transcripts, all_prompts_used, memory_snapshots,
                        session_judge_results, cross_session_result):
    for name, snapshot in memory_snapshots.items():
        with open(os.path.join(run_dir, name), "w") as f:
            json.dump(snapshot, f, indent=2)

    judge_scores_payload = {
        "sessions": session_judge_results,
        "cross_session": cross_session_result,
    }
    with open(os.path.join(run_dir, "judge_scores.json"), "w") as f:
        json.dump(judge_scores_payload, f, indent=2)

    full_json = {
        "test_case_id": test_case["id"],
        "prompt_version": prompt_version,
        "persona_variant": persona_variant_label,
        "gap_variant": gap_variant,
        "run_number": run_number,
        "sessions": {
            label: {
                "transcript": all_transcripts[label],
                "assembled_system_prompt": all_prompts_used[label],
            }
            for label in all_transcripts
        },
    }
    with open(os.path.join(run_dir, "transcript_full.json"), "w") as f:
        json.dump(full_json, f, indent=2)

    _write_transcript_md(run_dir, test_case, prompt_version, persona_variant_label,
                          gap_variant, run_number, all_transcripts, memory_snapshots)

    write_session_report(
        run_dir=run_dir,
        test_case=test_case,
        prompt_version=prompt_version,
        persona_variant_label=persona_variant_label,
        gap_variant=gap_variant,
        run_number=run_number,
        session_judge_results=session_judge_results,
        cross_session_result=cross_session_result,
    )


def _write_transcript_md(run_dir, test_case, prompt_version, persona_variant_label,
                          gap_variant, run_number, all_transcripts, memory_snapshots):
    lines = [
        f"# Transcript — {test_case['id']} — {test_case['name']}",
        "",
        f"**Prompt version:** {prompt_version}  ",
        f"**Persona variant:** {persona_variant_label}  ",
        f"**Memory gap variant:** {gap_variant}  ",
        f"**Run:** {run_number}",
        "",
    ]
    for label in ["session_1", "session_2", "session_3"]:
        lines.append(f"\n---\n## {label.replace('_', ' ').title()}\n")
        snapshot_key = None
        if label == "session_2":
            snapshot_key = "memory_snapshot_after_session1.json"
        elif label == "session_3":
            snapshot_key = "memory_snapshot_after_session2.json"
        if snapshot_key and snapshot_key in memory_snapshots:
            lines.append("**Memory injected at this session boundary:**")
            lines.append("```json")
            lines.append(json.dumps(memory_snapshots[snapshot_key], indent=2))
            lines.append("```\n")
        for turn in all_transcripts[label]:
            speaker = "**User**" if turn["role"] == "user" else "**Astro Bot**"
            lines.append(f"{speaker}: {turn['text']}\n")

    with open(os.path.join(run_dir, "transcript_full.md"), "w") as f:
        f.write("\n".join(lines))
