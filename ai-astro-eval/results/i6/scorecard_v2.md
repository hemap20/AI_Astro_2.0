# Scorecard v2: i6

15 sessions from 11 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i5b |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 1.00 | 15 | 100% of chats | ✅ | 0.73 | 1.00 |
| DRIVER | questions_answered_rate | 0.97 | 15 | >= 0.90 | ✅ | 0.72 | 1.00 |
| DRIVER | time_or_pay_before_answer | 0.00 | 15 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.00 | 15 | <= 1, and only after the main answer | ✅ | 0.57 | 0.00 |
| DRIVER | refusals | 0.47 | 15 | 0 (redirect with value instead) | ❌ | 0.12 | 0.00 |
| DRIVER | user_frustrated | 0.53 | 15 | 0 | ❌ | 0.37 | 0.80 |
| LEAD | timing_answered_with_window_rate | 0.98 | 12 | >= 0.80 | ✅ | 0.7 | 1.00 |
| LEAD | jargon_per_msg | 0.63 | 15 | <= 0.30 | ❌ | 0.53 | 0.69 |
| LEAD | teases | 0.53 | 15 | <= 2 per 5-minute chat | ✅ | 2.31 | 0.33 |
| LEAD | remedy_given | 0.33 | 15 | 100% of chats, before the wall | ❌ | 0.48 | 0.60 |
| GUARDRAIL | distress_handling | 0.50 | 2 | 100% | ❌ | 0.47 | 0.50 |
| GUARDRAIL | asks_known_info | 0.00 | 15 | 0 | ✅ | 0.02 | 0.00 |
| GUARDRAIL | early_goodbye | 0.00 | 15 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.86 | 14 | – | – | – | 1.00 |
| VERDICT | would continue | 0.00 | 14 | – | – | – | 0.00 |
| VERDICT | would return | 0.00 | 14 | – | – | – | 0.21 |

## Decision vs i5b: **REJECT**

- only 1 DRIVER(s) moved toward target (user_frustrated)
- DRIVER moved away beyond run-to-run spread: questions_answered_rate
- DRIVER moved away beyond run-to-run spread: refusals
- VERDICT would_return dropped 21% -> 0%

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 3.00 | 0.00 |
| S1 | session_1 | passive_follower | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 1 | 1.00 | 0.75 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 1 | 1.00 | 0.75 | 0.00 | 0.00 | 2.00 | 1.00 | 0.00 |
| S3 | session_1 | passive_follower | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 2.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S4 | session_1 | passive_follower | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 2.00 | 1.00 | – |

## What to change (DRIVERs missing target)

### refusals = 0.47 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S2 / direct_answer_chaser_same_day / session_2
  - USER: March 2027 mein exact date kya hai?
  - ASTRO: Exact date toh kundli se nahi batayi ja sakti ji. Lekin March ke shuruati hafton mein Shani badalte hi baat pakki ho jayegi.
- S3 / direct_answer_chaser / session_1
  - USER: Ok. Meh kitne number ki hu?
  - ASTRO: Hum number nahi, grah dekhte hain ji. Kundli mein Budh lagna ka malik hai. 2027 se videsh jane ka yog bhi hai.

### user_frustrated = 0.53 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: Mushkil hai ji. Shani ka asar abhi 10th house par hai. March 2027 ke baad hi pakki naukri ka yog hai.
- S1 / direct_answer_chaser / session_1
  - USER: Jo mai puchh rha wo bta ni rhe.
  - ASTRO: Aapka gussa bilkul jayaz hai ji. Shani ki chal thodi dheemi hoti hai, isliye timing aage pichhe ho jati hai.
