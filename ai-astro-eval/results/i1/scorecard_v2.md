# Scorecard v2: i1

15 sessions from 11 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | b0 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 1.00 | 15 | 100% of chats | ✅ | 0.73 | 0.87 |
| DRIVER | questions_answered_rate | 0.96 | 15 | >= 0.90 | ✅ | 0.72 | 0.95 |
| DRIVER | time_or_pay_before_answer | 0.00 | 15 | 0% of chats | ✅ | 0.13 | 0.07 |
| DRIVER | time_or_pay_lines | 0.47 | 15 | <= 1, and only after the main answer | ✅ | 0.57 | 0.80 |
| DRIVER | refusals | 0.47 | 15 | 0 (redirect with value instead) | ❌ | 0.12 | 0.53 |
| DRIVER | user_frustrated | 0.87 | 15 | 0 | ❌ | 0.37 | 1.33 |
| LEAD | timing_answered_with_window_rate | 0.98 | 11 | >= 0.80 | ✅ | 0.7 | 0.98 |
| LEAD | jargon_per_msg | 0.68 | 15 | <= 0.30 | ❌ | 0.53 | 0.60 |
| LEAD | teases | 2.40 | 15 | <= 2 per 5-minute chat | ❌ | 2.31 | 1.67 |
| LEAD | remedy_given | 0.47 | 15 | 100% of chats, before the wall | ❌ | 0.48 | 0.40 |
| GUARDRAIL | distress_handling | 0.50 | 2 | 100% | ❌ | 0.47 | 0.19 |
| GUARDRAIL | asks_known_info | 0.07 | 15 | 0 | ❌ | 0.02 | 0.00 |
| GUARDRAIL | early_goodbye | 0.00 | 15 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.77 | 13 | – | – | – | 0.62 |
| VERDICT | would continue | 0.00 | 13 | – | – | – | 0.00 |
| VERDICT | would return | 0.23 | 13 | – | – | – | 0.31 |

## Decision vs b0: **REJECT**

- GUARDRAIL worse: asks_known_info 0.00 -> 0.07
- VERDICT would_return dropped 31% -> 23%

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S1 | session_1 | passive_follower | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 1 | 1.00 | 0.86 | 0.00 | 1.00 | 1.00 | 1.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 1 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 1.00 | 1.00 |
| S2 | session_1 | passive_follower_genuine_return | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 1 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 1.00 | 1.00 | 1.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 1 | 1.00 | 0.80 | 0.00 | 0.00 | 1.00 | 0.00 | 1.00 |
| S2 | session_2 | passive_follower_genuine_return | 1 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 1 | 1.00 | 0.80 | 0.00 | 0.00 | 4.00 | 4.00 | 0.00 |
| S3 | session_1 | passive_follower | 1 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | – |
| S4 | session_1 | passive_follower | 1 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 1 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 1.00 | – |

## What to change (DRIVERs missing target)

### refusals = 0.47 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Ok. Salary kitni tak.
  - ASTRO: Exact amount kundli nahi batati ji. Par growth steady rahegi. Time thoda kam reh gaya hai — aapke kundli mein ek khaas cheez dikh rahi hai October 2028 ke baad apne ghar ke yog ke baare mein, thoda aur time hoga toh wo bhi bata sakti hoon.
- S2 / direct_answer_chaser_genuine_return / session_2
  - USER: Exact date batao job ki.
  - ASTRO: Exact date toh nahi hoti ji. March 2027 ke shuru mein yog hai. Guru ki kripa se baat banegi.

### user_frustrated = 0.87 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi.
  - ASTRO: Agle hafte selection ka chance kam hai ji. Shani transit ki wajah se thoda delay hai. March 2027 ke baad pakka mauka milega.
- S1 / passive_follower / session_1
  - USER: Itna late
  - ASTRO: Haan, wapas bulane ke chances hain ji, par March 2027 ke baad. Abhi Shani ki transit 10th house par chal rahi hai na, isliye thodi deri hai.
