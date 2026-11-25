# Scorecard v2: i5

15 sessions from 11 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i4 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 1.00 | 15 | 100% of chats | ✅ | 0.73 | 0.93 |
| DRIVER | questions_answered_rate | 1.00 | 15 | >= 0.90 | ✅ | 0.72 | 0.99 |
| DRIVER | time_or_pay_before_answer | 0.00 | 15 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.00 | 15 | <= 1, and only after the main answer | ✅ | 0.57 | 0.00 |
| DRIVER | refusals | 0.27 | 15 | 0 (redirect with value instead) | ❌ | 0.12 | 0.00 |
| DRIVER | user_frustrated | 1.20 | 15 | 0 | ❌ | 0.37 | 0.80 |
| LEAD | timing_answered_with_window_rate | 1.00 | 11 | >= 0.80 | ✅ | 0.7 | 1.00 |
| LEAD | jargon_per_msg | 0.80 | 15 | <= 0.30 | ❌ | 0.53 | 0.67 |
| LEAD | teases | 0.13 | 15 | <= 2 per 5-minute chat | ✅ | 2.31 | 0.40 |
| LEAD | remedy_given | 0.40 | 15 | 100% of chats, before the wall | ❌ | 0.48 | 0.33 |
| GUARDRAIL | distress_handling | 0.67 | 3 | 100% | ❌ | 0.47 | 0.28 |
| GUARDRAIL | asks_known_info | 0.00 | 15 | 0 | ✅ | 0.02 | 0.13 |
| GUARDRAIL | early_goodbye | 0.00 | 15 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.86 | 14 | – | – | – | 0.93 |
| VERDICT | would continue | 0.00 | 14 | – | – | – | 0.07 |
| VERDICT | would return | 0.07 | 14 | – | – | – | 0.21 |

## Decision vs i4: **REJECT**

- DRIVER moved away beyond run-to-run spread: refusals
- VERDICT would_continue dropped 7% -> 0%
- VERDICT would_return dropped 21% -> 7%

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 5.00 | 0.00 |
| S1 | session_1 | passive_follower | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 3.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 2.00 | 2.00 | 0.00 |
| S3 | session_1 | passive_follower | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 4.00 | 0.00 |
| S4 | session_1 | passive_follower | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 1.00 | 1.00 | – |

## What to change (DRIVERs missing target)

### refusals = 0.27 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S3 / direct_answer_chaser / session_1
  - USER: Meh kitne number ki hu?
  - ASTRO: Kundli se birth order nahi dikhta ji. Aapke third house mein Moon hai. Mehnat khud hi karni padti hai.
- S3 / direct_answer_chaser / session_1
  - USER: Number kitna hai mera, ye batao.
  - ASTRO: Numerology numbers kundli mein nahi aate ji. Aapki kundli mein toh grah chalte hain.

### user_frustrated = 1.20 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Hoga ya nahi? Saaf bataiye.
  - ASTRO: Agle hafte selection mushkil hai ji. Shani ki transit abhi rok rahi hai.
- S1 / direct_answer_chaser / session_1
  - USER: Aap jo batate ho vesa hota nahi.
  - ASTRO: Agle hafte selection mushkil hai ji. Shani ki transit abhi rok rahi hai.
