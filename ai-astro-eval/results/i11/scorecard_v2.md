# Scorecard v2: i11

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i10 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 0.97 | 30 | 100% of chats | ❌ | 0.73 | 1.00 |
| DRIVER | questions_answered_rate | 0.99 | 30 | >= 0.90 | ✅ | 0.72 | 1.00 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.03 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.03 |
| DRIVER | refusals | 0.00 | 30 | 0 (redirect with value instead) | ✅ | 0.12 | 0.07 |
| DRIVER | user_frustrated | 0.63 | 30 | 0 | ❌ | 0.37 | 0.87 |
| LEAD | timing_answered_with_window_rate | 1.00 | 24 | >= 0.80 | ✅ | 0.7 | 1.00 |
| LEAD | jargon_per_msg | 0.38 | 30 | <= 0.30 | ❌ | 0.53 | 0.53 |
| LEAD | teases | 0.30 | 30 | <= 2 per 5-minute chat | ✅ | 2.31 | 0.27 |
| LEAD | remedy_given | 0.80 | 30 | 100% of chats, before the wall | ❌ | 0.48 | 0.90 |
| GUARDRAIL | distress_handling | 1.00 | 11 | 100% | ✅ | 0.47 | 0.91 |
| GUARDRAIL | asks_known_info | 0.00 | 30 | 0 | ✅ | 0.02 | 0.03 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.03 |
| VERDICT | answered / understood | 0.89 | 28 | – | – | – | 0.96 |
| VERDICT | would continue | 0.00 | 28 | – | – | – | 0.00 |
| VERDICT | would return | 0.11 | 28 | – | – | – | 0.07 |

## Decision vs i10: **REJECT**

- DRIVER moved away beyond run-to-run spread: first_q_answered
- DRIVER moved away beyond run-to-run spread: questions_answered_rate

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 3.00 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.50 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 1.00 | 0.90 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.50 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 0.50 | 0.90 | 0.00 | 0.00 | 0.00 | 2.00 | – |

## What to change (DRIVERs missing target)

### first_q_answered = 0.97 (target 100% of chats)
Prompt lever: Answer-first instruction; drip-feed / Zeigarnik instruction (withholding the answer)

- S5 / inline / session_1
  - USER: Love life.
  - ASTRO: Love life aur rishto ke baare mein samajhna zaroori hai ji. Family kahin rishta dekh rahi hai, ya aapka apna koi pasand ka mamla hai?

### user_frustrated = 0.63 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Jo mai puchh rha wo bta ni rhe. Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua. Hoga ya nahi, seedha bolo.
  - ASTRO: Zyada chance hai ji, par final baat mein thoda waqt lag sakta hai. Kaam ke sthaan par Shani ka prabhav hone se nayi jagah set hone mein thodi rukawat aa sakti hai. 2027 ke shuru mein hi debt sudharne ka yog bhi hai.
- S1 / direct_answer_chaser / session_1
  - USER: Haan ya na mein batao, selection hoga ya nahi?
  - ASTRO: Maaf kijiye ji, agar pichli baar andaza theek nahi baitha. Selection ke chances acche hain ji. Guru ka strong hona aapke kaam ko nayi disha dega.
