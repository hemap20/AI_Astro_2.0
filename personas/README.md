# Simulated user personas for testing the AI Astro

Two BEHAVIOUR prompts for an LLM that plays the USER in a first chat with the AI Astro. They define only how the user writes, asks, answers, discloses, reacts, paces and leaves. The situation (who the user is, their question, birth details, other people involved, facts they hold back) comes from a separate scenario list and is inserted at `{scenario}` at the end of each prompt.

Both are drawn from the users of **Astro Sitara** (`sitara(6 nov onw.)/`: 107 files, 96 users with a first chat).

| File | Behaviour type | Share of Sitara users |
|---|---|---|
| `sitara_1_direct_answer_chaser.md` | Asks one concrete question (when / which month / yes or no), narrows every window, repeats the question each time it is dodged, escalates to "Faltu" / "Not satisfied" | 44% ask for precise timing; 28% ask a when-question 3+ times |
| `sitara_2_passive_follower.md` | Opens vaguely ("Kundli", "future"), replies "Ji / Ok / Ha / Kya / Haan bataiye", says yes to every teaser, drifts across life areas, says "Kya" to jargon | 32% send 3+ one-word go-along replies; 18% reply "Kya / Matlab / Samji nahi" to jargon |

## What Sitara first chats look like

| Behaviour | Value |
|---|---|
| Consultations per user | 1 for 84% (only 16% came back) |
| First chat length | ~5 minutes (the free time) |
| User messages | ~11.5 (median 11) |
| Words per message | 4.3 (median 3.7) |
| Replies of 1–2 words | 46% |
| Shares another person's name or DOB | 17% |
| Emotional or self-blaming lines | 9% |

Patterns in Sitara's own replies that these users react to: heavy chart terms (house numbers, nakshatra, D9), repeated teasers ("Ek aur cheez hai, jaanna chahenge?"), dodging exact timing, and "Time thoda kam reh gaya hai" near the end. Both personas have explicit reactions to each.

## What a scenario should contain
- The user's app details message (Name, Gender, DOB, TOB, POB), which is the first USER turn.
- The main question (the direct-answer chaser needs a concrete one) and any other life areas the user may drift to.
- Details of other people involved, if any.
- Held-back facts, each with what makes the user reveal it.
- Optional: language, if not Hinglish.

## How to use
1. Put one persona file in the simulator's system prompt with `{scenario}` replaced.
2. After each AI Astro reply, send the simulator the reply plus the elapsed time as `[mm:ss]` if you track it.
3. The simulator ends with `[LEAVE]` and one `[VERDICT]` line (answered/understood, would continue, would return, reason).
4. Score the transcript with the judge (`judge/run_judge.py`) like any other chat.
