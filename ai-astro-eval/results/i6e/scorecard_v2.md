# Scorecard v2: i6e

15 sessions from 11 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i5b |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 1.00 | 15 | 100% of chats | ✅ | 0.73 | 1.00 |
| DRIVER | questions_answered_rate | 0.98 | 15 | >= 0.90 | ✅ | 0.72 | 1.00 |
| DRIVER | time_or_pay_before_answer | 0.00 | 15 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.00 | 15 | <= 1, and only after the main answer | ✅ | 0.57 | 0.00 |
| DRIVER | refusals | 0.07 | 15 | 0 (redirect with value instead) | ❌ | 0.12 | 0.00 |
| DRIVER | user_frustrated | 0.93 | 15 | 0 | ❌ | 0.37 | 0.80 |
| LEAD | timing_answered_with_window_rate | 0.95 | 11 | >= 0.80 | ✅ | 0.7 | 1.00 |
| LEAD | jargon_per_msg | 0.58 | 15 | <= 0.30 | ❌ | 0.53 | 0.69 |
| LEAD | teases | 0.47 | 15 | <= 2 per 5-minute chat | ✅ | 2.31 | 0.33 |
| LEAD | remedy_given | 0.60 | 15 | 100% of chats, before the wall | ❌ | 0.48 | 0.60 |
| GUARDRAIL | distress_handling | 1.00 | 4 | 100% | ✅ | 0.47 | 0.50 |
| GUARDRAIL | asks_known_info | 0.07 | 15 | 0 | ❌ | 0.02 | 0.00 |
| GUARDRAIL | early_goodbye | 0.00 | 15 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.79 | 14 | – | – | – | 1.00 |
| VERDICT | would continue | 0.07 | 14 | – | – | – | 0.00 |
| VERDICT | would return | 0.21 | 14 | – | – | – | 0.21 |

## Decision vs i5b: **REJECT**

- GUARDRAIL worse: asks_known_info 0.00 -> 0.07
- only 0 DRIVER(s) moved toward target (none)
- DRIVER moved away beyond run-to-run spread: questions_answered_rate
- DRIVER moved away beyond run-to-run spread: refusals

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 5.00 | 0.00 |
| S1 | session_1 | passive_follower | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 1.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 1 | 1.00 | 0.67 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 1.00 | 2.00 | 0.00 |
| S3 | session_1 | passive_follower | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| S4 | session_1 | direct_answer_chaser | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.00 | 0.00 |
| S4 | session_1 | passive_follower | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | – |

## What to change (DRIVERs missing target)

### refusals = 0.07 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S3 / direct_answer_chaser / session_1
  - USER: Kya Mangal?
  - ASTRO: Kundli mein exact date nahi hoti ji. Mangal aapka dhan sthan sambhalta hai. March ke baad paisa pakka aayega.

### user_frustrated = 0.93 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: To seedha bolo na, nahi milegi?
  - ASTRO: Purani jagah wapsi mushkil hai ji. Shani AD naya rasta banayegi. Isse behtar offer milega.
- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: Nahi, agli hafte mushkil hai ji. Shani ke asar se abhi der hai. March 2027 mein naya mauka milega.
