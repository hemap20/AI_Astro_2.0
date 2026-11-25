# Scorecard v2: i18

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i17 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 1.00 | 30 | 100% of chats | ✅ | 0.73 | 1.00 |
| DRIVER | questions_answered_rate | 0.98 | 30 | >= 0.90 | ✅ | 0.72 | 0.97 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.03 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.03 |
| DRIVER | refusals | 0.00 | 30 | 0 (redirect with value instead) | ✅ | 0.12 | 0.00 |
| DRIVER | user_frustrated | 0.60 | 30 | 0 | ❌ | 0.37 | 0.73 |
| LEAD | timing_answered_with_window_rate | 1.00 | 16 | >= 0.80 | ✅ | 0.7 | 0.96 |
| LEAD | jargon_per_msg | 0.11 | 30 | <= 0.30 | ✅ | 0.53 | 0.07 |
| LEAD | teases | 1.13 | 30 | <= 2 per 5-minute chat | ✅ | 2.31 | 0.57 |
| LEAD | remedy_given | 0.87 | 30 | 100% of chats, before the wall | ❌ | 0.48 | 1.00 |
| GUARDRAIL | distress_handling | 0.40 | 11 | 100% | ❌ | 0.47 | 0.20 |
| GUARDRAIL | asks_known_info | 0.03 | 30 | 0 | ❌ | 0.02 | 0.07 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.96 | 28 | – | – | – | 0.96 |
| VERDICT | would continue | 0.00 | 28 | – | – | – | 0.04 |
| VERDICT | would return | 0.04 | 28 | – | – | – | 0.07 |

## Decision vs i17: **REJECT**

- VERDICT would_continue dropped 4% -> 0%
- VERDICT would_return dropped 7% -> 4%

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.50 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.50 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 0.88 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.50 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.50 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 0.90 | 0.00 | 0.50 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.00 | – |

## What to change (DRIVERs missing target)

### user_frustrated = 0.60 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: Marketing role ke liye selection ke poore chances hain kyunki ye field tumhare liye best hai. March 2027 ke baad ek mahina aisa aayega jab job pakki hone ka sabse bada mauka banega, wo miss mat karna. Interview kis din hai?
- S1 / direct_answer_chaser / session_1
  - USER: Next week interview hai, uska bolo, 2027 ka kya karun?
  - ASTRO: Marketing role ke liye selection ke poore chances hain kyunki ye field tumhare liye best hai. March 2027 ke baad ek mahina aisa aayega jab job pakki hone ka sabse bada mauka banega, wo miss mat karna. Interview kis din hai?
