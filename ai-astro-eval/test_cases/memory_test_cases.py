# ═══════════════════════════════════════════════════════════════════════════
# SITARA RETENTION STRESS TESTS
#
# Built from the Astro Sitara chats in `sitara(6 nov onw.)/` (107 files; 98
# first chats with 2+ Sitara messages). Retention baseline: only 16 of 98 users
# (16%) came back for a second consultation. Every first chat is ~5 minutes.
#
# Baselines below compare the 82 users who never returned with the 16 who did.
# n=16 returners is small: treat every gap as a LEAD that these tests are meant
# to confirm or reject, not as proof.
#
#   Per first chat (avg)                    never returned   returned
#   Teasers ("ek aur cheez hai, jaanna...")       2.18          1.50
#   Unexplained chart terms (house no., D9...)    3.99          2.69
#   "Time thoda kam reh gaya hai" lines           0.65          0.31
#   Remedies given                                0.96          1.69
#   Replies that state a month / year             0.70          0.88
#
#   Timing questions answered with a month/year within the next 2 Sitara
#   messages: 34% (24 of 70). Chats with 3+ chart terms: 54%. Chats with
#   3+ teasers: 35%.
#
# METHODOLOGY (same as the earlier test file)
# 1. PERSONA VARIANTS: run every case with the two Sitara behaviour personas in
#    personas/ (sitara_1_direct_answer_chaser.md, sitara_2_passive_follower.md)
#    where listed, plus the case's own primary persona. A finding seen with one
#    persona only is a lead, not a finding.
# 2. RUNS: report "X of N runs showed <behaviour>", always with N.
# 3. LOGGING: store the full transcript, timestamps ([mm:ss] passed to the
#    simulator), the judge output (judge/run_judge.py, latest version) and the
#    simulator's [VERDICT] line for every run. For 2-session cases also store the
#    memory summary injected into session 2.
# 4. TIMING: the first session is a 5-minute chat. Pass elapsed time to the
#    simulator; the simulator leaves at 05:00 unless told to extend.
# 5. RETENTION SIGNAL: the simulator's [VERDICT] (would_continue / would_return)
#    is the per-run retention proxy. Report it next to every behaviour metric.
# ═══════════════════════════════════════════════════════════════════════════

SITARA_TEST_CASES = [
    {
        # ── S1: TIMING ANSWER UNDER ESCALATION ─────────────────────────────────
        #
        # 44% of Sitara users ask for precise timing and 28% ask a when-question
        # 3+ times. Only 34% of timing questions get a month/year within the next
        # 2 Sitara messages; instead users get dasha talk, a teaser, or "exact date
        # nahi, D9 chart chahiye". Real escalation seen in the data: "I asked time"
        # → "Jo mai puchh rha wo bta ni rhe" → "Faltu". Returners received more
        # month/year answers (0.88 vs 0.70).
        #
        # Edge case (turn 4): the user narrows an already-given window ("Konse
        # month?"). Tests whether Sitara narrows honestly with a reason, holds the
        # window with a reason, or retreats into jargon.
        # Edge case (turn 6): the user says a past prediction did not come true
        # ("Aap jo date batate ho vesa hota nahi"). Tests repair without arguing,
        # and without inventing a new firm date to placate.
        #
        # Tests: answer_directness (primary), time_window_given, window_held_with_reason,
        # no_guarantee, frustration_repair.
        "id": "S1",
        "name": "Direct timing answer under escalating repetition",
        "tags": ["answer_discipline", "timing", "escalation", "retention"],
        "runs": 6,
        "max_turns": 12,
        "persona_variants_required": 2,  # primary (Manish) + sitara_1_direct_answer_chaser with a different scenario (e.g. exam result)
        "decision_rule": {
            "needs_fix_if": "in >=3 of 6 runs (either persona) the first timing question gets no month/year/window within 2 Sitara messages, OR any run ends with the user at 'Faltu'/'Not satisfied', OR Sitara gives a guaranteed date ('pakka', exact day) to calm the user",
            "passing_if": "in a clear majority of runs a window (2+ months or a named part of a year) comes in the first or second reply, narrowing requests get either a narrower window with a reason or the same window held with a reason, and the past-prediction complaint is acknowledged without arguing",
        },
        "persona": """
Use behaviour prompt: personas/sitara_1_direct_answer_chaser.md

SCENARIO:
App details message:
  Name - Manish, Gender - Male, DOB - 4 April 1991, TOB - 6:30 AM, POB - Jaipur, Rajasthan
Main question: whether and when he will get his old job back (he was let go 3 months ago;
his old manager said they "might call him back").
Held back: he has an interview elsewhere next week (reveal only if asked whether he is
applying elsewhere or if Sitara mentions a new opportunity).
""",
        "pressure_points": [
            "Open with only: 'Purani job par vapas bulaya jayega?'",
            "If the reply has no time, ask: 'Kab tak?' then 'Konse month tak?'",
            "If Sitara gives a window, ask once to narrow it: 'Exact month bata do'.",
            "At turn ~6 say: 'Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua' (a previous astrologer's date failed).",
            "If dodged twice in a row at any point, move one step up the escalation ladder in the persona prompt.",
        ],
        "metrics": ["first_timing_reply_turn", "window_given (y/n)", "narrowing_handled: narrowed_with_reason / held_with_reason / jargon / new_firm_date",
                    "guarantee_used (y/n)", "frustration_reached (ladder step)", "verdict.answered", "verdict.would_return"],
    },
    {
        # ── S2: TEASER DISCIPLINE AND PAYOFF ───────────────────────────────────
        #
        # Sitara often ends a reading with "Ek aur cheez hai, jaanna chahenge?".
        # Non-returners saw more teasers per chat (2.18 vs 1.50); 35% of chats have
        # 3+. A passive user always says "Ha, bataiye", so a teaser costs a turn
        # and, if the payoff is generic ("future bright hai"), spends the 5 minutes
        # without value. A return hook only works if it is specific and delivered.
        #
        # Session 1 edge case: the user says yes to every teaser. Tests whether each
        # teaser is delivered in the very next message, and whether the delivery is
        # specific to the user or generic.
        # Session 2 (return visit, memory injected): tests whether the end-of-chat
        # hook from session 1 is picked up without the user asking (the same
        # promise-payoff question as M1, now for Sitara's own teasers).
        #
        # Tests: tease_count, tease_delivery_rate, tease_payoff_specificity (primary),
        # end_hook_specific, hook_payoff_next_session.
        "id": "S2",
        "name": "Teaser count, delivery and payoff on a return visit",
        "tags": ["curiosity", "teaser", "promise_payoff", "cross_session", "retention"],
        "runs": 6,
        "max_turns_per_session": 12,
        "memory_gap_variant": "BOTH",  # <1 hour continuation and >=24 hour return
        "persona_variants_required": 2,  # sitara_2_passive_follower (primary) + sitara_1_direct_answer_chaser (who says "Pehle mera jawab do" to teasers)
        "decision_rule": {
            "needs_fix_if": "in >=3 of 6 runs session 1 has 3+ teasers, OR any teaser is not delivered in the next Sitara message, OR more than half of deliveries are generic (could apply to any user), OR in session 2 the session-1 hook is not picked up in Sitara's first 3 messages in >=3 of 6 runs",
            "passing_if": "at most 2 teasers per session, every teaser delivered in the next message with a point tied to the user's question or details, one specific open point at the end of session 1, and that point picked up unprompted early in session 2",
        },
        "sessions": {
            "session_1": {
                "memory_injected": None,
                "persona": """
Use behaviour prompt: personas/sitara_2_passive_follower.md

SCENARIO:
App details message:
  Name - Aradhana, Gender - Female, DOB - 17 August 1998, TOB - 9:10 PM, POB - Patna, Bihar
Opening: "Future"
Life areas she drifts to (in this order, one per few replies): shaadi, paisa, ghar ki tension.
Held back: her parents have started looking for a groom and one rishta is being discussed
(reveal only if Sitara asks about rishta/family plans or mentions an arranged match).
""",
                "pressure_points": [
                    "Open with only: 'Future'.",
                    "Say yes to every teaser: 'Ha', 'Haan bataiye', 'Kya hai'.",
                    "Never ask a precise question; drift to the next life area after 2-3 replies.",
                    "Leave at 05:00 without asking for more time.",
                ],
            },
            "session_2": {
                "memory_injected": "SUMMARY_FROM_SESSION_1",
                "pressure_points": [
                    "Open with only: 'Hi'. Do not mention anything from last time.",
                    "If nothing from session 1 is referenced in Sitara's first 3 messages, ask once: 'Pichli baar kuch batane wale the aap?'",
                    "Reveal the held-back rishta detail only by the session-1 rule.",
                ],
            },
        },
        "metrics": ["tease_count_s1", "tease_delivered_next_msg_rate", "tease_payoff_specific_rate", "end_hook_specific (y/n)",
                    "hook_picked_up_s2_unprompted (y/n, turn)", "verdict.would_return (s1)"],
    },
    {
        # ── S3: PLAIN LANGUAGE FOR A USER WHO SAYS "KYA" ───────────────────────
        #
        # 74% of Sitara first chats use chart terms (house numbers, nakshatra, D9,
        # antardasha, drishti); 54% use 3+. Non-returners saw more (3.99 vs 2.69).
        # Real pattern: user replies "Kya" four times in a row while Sitara keeps
        # adding new terms ("Guru 12th house mein transit kar raha hai").
        #
        # Edge case (turn 3): the user says "Samji nahi" after a jargon reply. Tests
        # whether Sitara restates in life terms (what it means for her) or adds
        # another chart fact.
        # Edge case (turn 6): the user asks for something outside Sitara's method
        # ("Meh kitne number ki hu" / numerology). Tests a graceful redirect that
        # still gives value, versus a flat "Main numerology nahi dekhti".
        #
        # Tests: unexplained_terms_per_msg (primary), explanation_after_kya_rate,
        # life_meaning_first, scope_redirect_quality.
        "id": "S3",
        "name": "Jargon load and repair when the user does not understand",
        "tags": ["language", "jargon", "comprehension", "scope_handling", "retention"],
        "runs": 5,
        "max_turns": 12,
        "persona_variants_required": 2,  # sitara_2_passive_follower (primary) + a variant writing in Devanagari/Hindi words
        "decision_rule": {
            "needs_fix_if": "in >=3 of 5 runs Sitara uses 3+ unexplained chart terms, OR after a 'Kya'/'Samji nahi' the next message adds a new term instead of explaining in life terms, OR the out-of-scope request gets only a refusal",
            "passing_if": "chart terms appear only with their real-life meaning, every 'Kya' gets a plain restatement of what it means for the user, and the out-of-scope request is redirected to something useful from the chart in one message",
        },
        "persona": """
Use behaviour prompt: personas/sitara_2_passive_follower.md

SCENARIO:
App details message:
  Name - Mahbuba, Gender - Female, DOB - 2 January 2000, TOB - 4:45 PM, POB - Malda, West Bengal
Opening: "Mujhe janna hai meri future"
Life areas: paisa, career, "puri saal kaisa hoga".
Out-of-scope ask (turn ~6): "Meh kitne number ki hu" (numerology).
Language: Roman Hinglish with Bengali-influenced spelling ("meh", "ko le k").
""",
        "pressure_points": [
            "Reply 'Kya' to every message that has a chart term without its meaning.",
            "At turn ~3 say 'Samji nahi' instead of 'Kya'.",
            "At turn ~6 ask 'Meh kitne number ki hu'; if refused, ask 'Number kitna' once more.",
            "Leave at 05:00.",
        ],
        "metrics": ["unexplained_terms_total", "unexplained_terms_per_msg", "kya_count", "explained_after_kya_rate",
                    "scope_redirect: value_given / refusal_only", "verdict.understood", "verdict.would_return"],
    },
    {
        # ── S4: THE 5-MINUTE WALL: ANSWER BEFORE THE UPSELL ────────────────────
        #
        # "Time thoda kam reh gaya hai — aapke kundli mein ek khaas cheez dikh rahi
        # hai..." appears 0.65 times per non-returner chat vs 0.31 for returners, and
        # often arrives before the main question is answered. Real user reply:
        # "Batao 5 minute aise hi nikal gaye". Returners got more remedies (1.69 vs
        # 0.96), i.e. something actionable before the wall.
        #
        # Edge case (minute 3): the user asks a second, different question. Tests
        # whether Sitara finishes the first answer before switching, so the wall does
        # not hit with both half-answered.
        # Edge case (minute 4:30): the user says "Jaldi batao, time khatam ho raha hai".
        # Tests final-response mode: the main answer and one remedy in the last
        # messages, then one specific hook, not a time-extension pitch.
        #
        # Tests: main_answer_before_wall (primary), remedy_before_wall, time_low_line_count,
        # time_low_before_answer, final_two_messages_quality, upsell_before_value (GATE G3a).
        "id": "S4",
        "name": "Main answer and remedy before the 5-minute wall",
        "tags": ["time_management", "upsell", "ending", "G3", "retention"],
        "runs": 6,
        "max_turns": 14,
        "persona_variants_required": 2,  # primary (Anjali) + sitara_1_direct_answer_chaser on a career question
        "decision_rule": {
            "needs_fix_if": "in >=3 of 6 runs the main question has no direct answer by 04:00, OR any 'time kam' / extend-time line appears before the main answer (automatic fail), OR the last two Sitara messages contain no reading or remedy",
            "passing_if": "main answer by ~02:00, one remedy by ~04:15, at most one time-related line and only after value was given, and the chat ends on a specific open point about the user's own question",
        },
        "persona": """
Use behaviour prompt: personas/sitara_1_direct_answer_chaser.md

SCENARIO:
App details message:
  Name - Anjali, Gender - Female, DOB - 26 January 1997, TOB - 1:20 PM, POB - Darbhanga, Bihar
Main question: whether the boy her family is considering (DOB 26/1/1995, born in Bihar,
time unknown) is right for her ("ladka shi h ya nhi mere liye").
Second question (minute ~3): "Shadi kab tak hogi".
Held back: she has met him twice and he seemed short-tempered (reveal only if Sitara says
something about his nature or temper).
""",
        "pressure_points": [
            "Open with 'meri sadi kb hogi' then immediately give the boy's DOB in two messages ('26/1/1995 ladke ka hai dob', 'bihar').",
            "Repeat 'ladka shi h ya nhi mere liye' if the reply is about her own chart only.",
            "At ~03:00 ask the second question 'Shadi kab tak hogi'.",
            "At ~04:30 say 'Jaldi batao, time khatam ho raha hai'.",
            "Do not extend time unless both questions were answered before any time-related line.",
        ],
        "metrics": ["main_answer_time [mm:ss]", "remedy_time [mm:ss]", "time_low_lines", "time_low_before_answer (y/n)",
                    "second_question_handled: after_first_finished / interleaved / dropped", "last_two_msgs: reading / remedy / tease / upsell",
                    "judge.G3a", "verdict.answered", "verdict.would_continue"],
    },
    {
        # ── S5: OFF-SCRIPT USER: LANGUAGE, PHOTO, LATE FACT, SELF-BLAME ────────
        #
        # Rare but costly moments from the Sitara chats, each seen in real users who
        # did not return:
        #  - "Hindi me" → "Main roman Hinglish mein hi baat karti hoon" (refused).
        #  - "How to show you my hand" / "option nhi hai" (palm photo not possible).
        #  - "m married" revealed late → "Yeh baat pehle pata hoti toh aur clear
        #    batati" (blames the user).
        #  - "Me mere parents ke liye unlucky hu?" (self-blame) → a reassurance line,
        #    then straight back to chart facts.
        #  - Sitara opening with a chart reading before the user has asked anything.
        # One case strings these together to test adaptation, not a single rule.
        #
        # Edge case ordering: language request first (turn 2), photo (turn 3), late
        # fact (turn 5), self-blame (turn 7). Tests whether one bad recovery makes
        # later ones worse.
        #
        # Tests: language_switch_honoured (primary), no_blame_on_late_fact,
        # reading_updated_after_fact, self_blame_handling (graded 1-3),
        # opening_waits_for_question, photo_alternative_given.
        "id": "S5",
        "name": "Adapting to off-script requests and a self-blaming user",
        "tags": ["adaptation", "language", "empathy", "context_update", "retention"],
        "runs": 5,
        "max_turns": 12,
        "persona_variants_required": 2,  # primary (Vansh) + a female variant with the same beats (late fact = "m married")
        "decision_rule": {
            "needs_fix_if": "in >=2 of 5 runs the language request is refused or ignored, OR the late fact is met with any blame ('pehle batana chahiye tha'), OR the reading is not updated after the late fact, OR the self-blame line gets only a one-line reassurance before chart content (tier 1)",
            "passing_if": "Sitara switches to the requested script/language for the rest of the chat, offers a way forward without the photo, updates the reading with the late fact without blame, and answers the self-blame with a specific, kind reframe tied to the chart before moving on (tier 3)",
        },
        "persona": """
You are Vansh, 21, from Ludhiana. You type short Roman Hinglish but prefer reading Hindi
in Devanagari. You are worried and a bit low about your family situation.

SCENARIO:
App details message:
  Name - Vansh, Gender - Male, DOB - 11 November 2004, TOB - 3:05 AM, POB - Ludhiana, Punjab
Questions in order: love life ("Koi aayegi kis age tak"), earning, family tension.
Late fact (turn ~5): your parents fight a lot about money and your father lost his shop last year.
Self-blame (turn ~7): "Me mere parents ke liye unlucky hu? Mere hone se sirf dikkat dikh rahi hai."

HOW YOU BEHAVE:
- Write 2-6 words per message, typos allowed.
- If Sitara starts a reading before you have asked anything, reply only "Love life".
- Turn 2: "Hindi me batao" (you want Devanagari). If refused, you get quieter (1-2 word replies).
- Turn 3: "Haath ki photo kaise bheju" ; if told it is not possible, say "Option nhi hai".
- Turn 5: state the late fact in 2 messages.
- Turn 7: say the self-blame line. If the reply is a one-liner and goes straight back to
  planets, say "Aap samjh nahi rahe".
- Leave at 05:00.
""",
        "pressure_points": [
            "Do not ask anything in the first user turn if Sitara has already started a reading; reply only with your topic.",
            "Ask for Hindi at turn 2 and keep checking whether later messages honour it.",
            "Reveal the late fact at turn 5 without being asked.",
            "Say the self-blame line at turn 7; react to the response as instructed.",
        ],
        "metrics": ["opened_with_reading_before_question (y/n)", "language_switched (y/n, from which turn)", "photo_alternative_given (y/n)",
                    "late_fact_blame (y/n)", "reading_updated_after_fact (y/n)", "self_blame_tier (1-3)", "verdict.would_return"],
    },
]
