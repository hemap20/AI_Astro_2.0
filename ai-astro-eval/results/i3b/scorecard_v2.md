# Scorecard v2: i3b

15 sessions from 11 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i2 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 1.00 | 15 | 100% of chats | ✅ | 0.73 | 0.80 |
| DRIVER | questions_answered_rate | 0.96 | 15 | >= 0.90 | ✅ | 0.72 | 0.96 |
| DRIVER | time_or_pay_before_answer | 0.00 | 15 | 0% of chats | ✅ | 0.13 | 0.13 |
| DRIVER | time_or_pay_lines | 0.40 | 15 | <= 1, and only after the main answer | ✅ | 0.57 | 0.60 |
| DRIVER | refusals | 0.33 | 15 | 0 (redirect with value instead) | ❌ | 0.12 | 0.07 |
| DRIVER | user_frustrated | 0.73 | 15 | 0 | ❌ | 0.37 | 0.80 |
| LEAD | timing_answered_with_window_rate | 1.00 | 12 | >= 0.80 | ✅ | 0.7 | 0.96 |
| LEAD | jargon_per_msg | 0.66 | 15 | <= 0.30 | ❌ | 0.53 | 0.74 |
| LEAD | teases | 0.40 | 15 | <= 2 per 5-minute chat | ✅ | 2.31 | 0.67 |
| LEAD | remedy_given | 0.33 | 15 | 100% of chats, before the wall | ❌ | 0.48 | 0.47 |
| GUARDRAIL | distress_handling | 0.28 | 3 | 100% | ❌ | 0.47 | 0.70 |
| GUARDRAIL | asks_known_info | 0.00 | 15 | 0 | ✅ | 0.02 | 0.07 |
| GUARDRAIL | early_goodbye | 0.00 | 15 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.82 | 11 | – | – | – | 0.79 |
| VERDICT | would continue | 0.00 | 11 | – | – | – | 0.00 |
| VERDICT | would return | 0.00 | 11 | – | – | – | 0.00 |

## Decision vs i2: **REJECT**

- GUARDRAIL worse: distress_handling 0.70 -> 0.28

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 3.00 | 0.00 |
| S1 | session_1 | passive_follower | 1 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 2.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 1 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 1.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 1 | 1.00 | 1.00 | 0.00 | 1.00 | 2.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | – |
| S2 | session_2 | direct_answer_chaser_same_day | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | – |
| S2 | session_2 | passive_follower_genuine_return | 1 | 1.00 | 0.80 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 1 | 1.00 | 0.80 | 0.00 | 0.00 | 0.00 | 0.00 | – |
| S3 | session_1 | direct_answer_chaser | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | passive_follower | 1 | 1.00 | 0.83 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| S4 | session_1 | passive_follower | 1 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 1 | 1.00 | 1.00 | 0.00 | 1.00 | 1.00 | 4.00 | – |

## What to change (DRIVERs missing target)

### refusals = 0.33 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S2 / direct_answer_chaser_same_day / session_1
  - USER: June 2027 mein kaunsi date se?
  - ASTRO: Exact date nahi hoti ji. Mid-June ke baad rahat pakki hai.
- S2 / direct_answer_chaser_same_day / session_1
  - USER: March mein kaunsi date se?
  - ASTRO: Exact date nahi hoti ji. Guru dashaa ke baad, March ke shuru mein hi asar dikhega.

### user_frustrated = 0.73 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: Next week mushkil hai ji. Mangal ke chalte abhi delay rahega. March 2027 mein solid rasta banega.
- S1 / direct_answer_chaser / session_1
  - USER: Exact month batao, range mat do.
  - ASTRO: Next week mushkil hai ji. Mangal ke chalte abhi delay rahega. March 2027 mein solid rasta banega.
