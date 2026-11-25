"""Load a conversation CSV and cut out the user's first consultation."""
import os
import pandas as pd

SYSTEM_ID = 0
START_PREFIX = "Consultation started"


def user_id_from_path(path: str) -> str:
    # conversation_<userID>_<astroID>.csv (a "<folder>__" prefix may be present)
    name = os.path.basename(path).split("__")[-1]
    return name.split("_")[1]


def load_first_chat(path: str) -> list[dict]:
    """Return the first consultation as a chronological list of messages.

    Files are newest-first and several messages can share a second, so the
    file order is reversed before a stable sort on the timestamp.
    """
    uid = int(user_id_from_path(path))
    df = pd.read_csv(path, dtype={"Message": str}).iloc[::-1].reset_index(drop=True)
    df["ts"] = pd.to_datetime(df["Date"] + " " + df["Time"])
    df = df.sort_values("ts", kind="stable").reset_index(drop=True)
    df["Message"] = df["Message"].fillna("").astype(str)

    starts = df.index[df["Message"].str.startswith(START_PREFIX)].tolist()
    if not starts:
        return []
    lo = starts[0]
    hi = starts[1] if len(starts) > 1 else len(df)
    first = df.iloc[lo:hi]
    t0 = first["ts"].iloc[0]

    msgs = []
    for _, r in first.iterrows():
        sid = int(r["Sender ID"])
        if sid == SYSTEM_ID:
            role = "SYSTEM"
        elif sid == uid:
            role = "USER"
        else:
            role = "ASTRO"
        text = r["Message"].strip()
        if role == "SYSTEM" and text.startswith(START_PREFIX):
            continue
        msgs.append({
            "sec": int((r["ts"] - t0).total_seconds()),
            "role": role,
            "text": text if text else "[empty / media]",
        })
    for i, m in enumerate(msgs):
        m["idx"] = i
    return msgs


def render_transcript(msgs: list[dict]) -> str:
    lines = []
    for m in msgs:
        mm, ss = divmod(m["sec"], 60)
        lines.append(f"#{m['idx']} [{mm:02d}:{ss:02d}] {m['role']}: {m['text']}")
    return "\n".join(lines)
