# Scorecard v2: i17

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i16 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 1.00 | 30 | 100% of chats | ✅ | 0.73 | 1.00 |
| DRIVER | questions_answered_rate | 0.97 | 30 | >= 0.90 | ✅ | 0.72 | 0.99 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.03 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.00 |
| DRIVER | refusals | 0.00 | 30 | 0 (redirect with value instead) | ✅ | 0.12 | 0.00 |
| DRIVER | user_frustrated | 0.73 | 30 | 0 | ❌ | 0.37 | 0.57 |
| LEAD | timing_answered_with_window_rate | 0.96 | 18 | >= 0.80 | ✅ | 0.7 | 1.00 |
| LEAD | jargon_per_msg | 0.07 | 30 | <= 0.30 | ✅ | 0.53 | 0.21 |
| LEAD | teases | 0.57 | 30 | <= 2 per 5-minute chat | ✅ | 2.31 | 0.20 |
| LEAD | remedy_given | 1.00 | 30 | 100% of chats, before the wall | ✅ | 0.48 | 0.93 |
| GUARDRAIL | distress_handling | 0.20 | 12 | 100% | ❌ | 0.47 | 0.58 |
| GUARDRAIL | asks_known_info | 0.07 | 30 | 0 | ❌ | 0.02 | 0.00 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.96 | 28 | – | – | – | 0.93 |
| VERDICT | would continue | 0.04 | 28 | – | – | – | 0.07 |
| VERDICT | would return | 0.07 | 28 | – | – | – | 0.25 |

## Decision vs i16: **REJECT**

- GUARDRAIL worse: distress_handling 0.58 -> 0.20
- GUARDRAIL worse: asks_known_info 0.00 -> 0.07
- only 0 DRIVER(s) moved toward target (none)
- DRIVER moved away beyond run-to-run spread: time_or_pay_lines
- VERDICT would_continue dropped 7% -> 4%
- VERDICT would_return dropped 25% -> 7%

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 0.88 | 0.00 | 0.00 | 0.00 | 4.00 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 1.00 | 0.90 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 1.00 | 0.88 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.50 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.00 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 0.88 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.50 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | – |

## What to change (DRIVERs missing target)

### user_frustrated = 0.73 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pehle April bola ab June.
  - ASTRO: Purane logo ka touch kaam aayega, June 2027 ke baad wahi se bulawa aa sakta hai. Thursday se Om Gram Greem Grom Sah Gurave Namah ka jaap karo. Abhi ghar pe kiske sath rehte ho?
- S1 / direct_answer_chaser / session_1
  - USER: Sahi kya hai?
  - ASTRO: Purane logo ka touch kaam aayega, June 2027 ke baad wahi se bulawa aa sakta hai. Thursday se Om Gram Greem Grom Sah Gurave Namah ka jaap karo. Abhi ghar pe kiske sath rehte ho?
