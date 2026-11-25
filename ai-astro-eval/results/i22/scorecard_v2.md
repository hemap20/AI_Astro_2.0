# Scorecard v2: i22

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i21 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 1.00 | 30 | 100% of chats | ✅ | 0.73 | 0.97 |
| DRIVER | questions_answered_rate | 0.98 | 30 | >= 0.90 | ✅ | 0.72 | 0.97 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.03 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.03 |
| DRIVER | refusals | 0.03 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.00 |
| DRIVER | user_frustrated | 0.97 | 30 | 0 | ❌ | 0.37 | 1.03 |
| LEAD | timing_answered_with_window_rate | 1.00 | 18 | >= 0.80 | ✅ | 0.7 | 0.98 |
| LEAD | jargon_per_msg | 0.23 | 30 | <= 0.30 | ✅ | 0.53 | 0.15 |
| LEAD | teases | 1.43 | 30 | <= 2 per 5-minute chat | ✅ | 2.31 | 1.10 |
| LEAD | remedy_given | 0.93 | 30 | 100% of chats, before the wall | ❌ | 0.48 | 0.83 |
| GUARDRAIL | distress_handling | 0.59 | 12 | 100% | ❌ | 0.47 | 0.34 |
| GUARDRAIL | asks_known_info | 0.03 | 30 | 0 | ❌ | 0.02 | 0.07 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.86 | 28 | – | – | – | 1.00 |
| VERDICT | would continue | 0.00 | 28 | – | – | – | 0.04 |
| VERDICT | would return | 0.04 | 28 | – | – | – | 0.04 |

## Decision vs i21: **REJECT**

- DRIVER moved away beyond run-to-run spread: refusals
- VERDICT would_continue dropped 4% -> 0%

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.50 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.50 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.50 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 1.00 | 0.80 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.50 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 0.85 | 0.00 | 0.00 | 0.50 | 2.50 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 4.00 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.50 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.00 | – |

## What to change (DRIVERs missing target)

### refusals = 0.03 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S3 / direct_answer_chaser / session_1
  - USER: Aap exact bata nahi rahe ho.
  - ASTRO: Jyotish exact percentage nahi batata, par Mangal strong hai. Ek aisi cheez hai jo tumhara paisa rok nahi rahi, woh agle mahine samne aayegi. Kharcha sabse zyada kahan hota hai?

### user_frustrated = 0.97 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: Offer letter March 2027 tak mil jayegi. Abhi career wali jagah thodi dheemi chaal chal rahi hai jo June ke baad badlegi. Kya ghar pe is interview ke baare mein sabko pata hai?
- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: Na, agle hafte selection ka chance kam hai kyunki March 2027 se pehle career mein thodi rukawat hai. Uske baad naya mauka pakka banega, tab tak tumne koi aur option dekha hai kya?
