# Scorecard v2: i14

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i13 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 1.00 | 30 | 100% of chats | ✅ | 0.73 | 0.93 |
| DRIVER | questions_answered_rate | 0.99 | 30 | >= 0.90 | ✅ | 0.72 | 0.96 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.00 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.03 |
| DRIVER | refusals | 0.00 | 30 | 0 (redirect with value instead) | ✅ | 0.12 | 0.03 |
| DRIVER | user_frustrated | 0.63 | 30 | 0 | ❌ | 0.37 | 0.93 |
| LEAD | timing_answered_with_window_rate | 1.00 | 16 | >= 0.80 | ✅ | 0.7 | 0.97 |
| LEAD | jargon_per_msg | 0.44 | 30 | <= 0.30 | ❌ | 0.53 | 0.43 |
| LEAD | teases | 0.03 | 30 | <= 2 per 5-minute chat | ✅ | 2.31 | 0.03 |
| LEAD | remedy_given | 0.73 | 30 | 100% of chats, before the wall | ❌ | 0.48 | 0.93 |
| GUARDRAIL | distress_handling | 0.50 | 10 | 100% | ❌ | 0.47 | 0.77 |
| GUARDRAIL | asks_known_info | 0.17 | 30 | 0 | ❌ | 0.02 | 0.10 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.93 | 28 | – | – | – | 0.86 |
| VERDICT | would continue | 0.00 | 28 | – | – | – | 0.00 |
| VERDICT | would return | 0.04 | 28 | – | – | – | 0.04 |

## Decision vs i13: **REJECT**

- GUARDRAIL worse: distress_handling 0.77 -> 0.50
- GUARDRAIL worse: asks_known_info 0.10 -> 0.17

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.50 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.50 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 1.00 | 0.88 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.50 | – |

## What to change (DRIVERs missing target)

### user_frustrated = 0.63 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi.
  - ASTRO: March 2027 ka mahina sabse pakka lag raha hai ji, kyunki tabhi naya samay shuru hota hai. Baaki thoda-bahut aage-peeche bhi ho sakta hai. Vahan salary ko lekar koi baat hui hai kya?
- S1 / direct_answer_chaser / session_1
  - USER: Zyada chance nahi, seedha bolo milegi ya nahi?
  - ASTRO: Zyada chance hai ji. Guru ki taqat se purani baat pakki hogi. Agle hafte ka interview kis role ke liye hai ji?
