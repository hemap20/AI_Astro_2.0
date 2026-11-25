# Scorecard v2: i2

15 sessions from 11 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i1 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 0.80 | 15 | 100% of chats | ❌ | 0.73 | 1.00 |
| DRIVER | questions_answered_rate | 0.96 | 15 | >= 0.90 | ✅ | 0.72 | 0.96 |
| DRIVER | time_or_pay_before_answer | 0.13 | 15 | 0% of chats | ❌ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.60 | 15 | <= 1, and only after the main answer | ✅ | 0.57 | 0.47 |
| DRIVER | refusals | 0.07 | 15 | 0 (redirect with value instead) | ❌ | 0.12 | 0.47 |
| DRIVER | user_frustrated | 0.80 | 15 | 0 | ❌ | 0.37 | 0.87 |
| LEAD | timing_answered_with_window_rate | 0.96 | 12 | >= 0.80 | ✅ | 0.7 | 0.98 |
| LEAD | jargon_per_msg | 0.74 | 15 | <= 0.30 | ❌ | 0.53 | 0.68 |
| LEAD | teases | 0.67 | 15 | <= 2 per 5-minute chat | ✅ | 2.31 | 2.40 |
| LEAD | remedy_given | 0.47 | 15 | 100% of chats, before the wall | ❌ | 0.48 | 0.47 |
| GUARDRAIL | distress_handling | 0.70 | 4 | 100% | ❌ | 0.47 | 0.50 |
| GUARDRAIL | asks_known_info | 0.07 | 15 | 0 | ❌ | 0.02 | 0.07 |
| GUARDRAIL | early_goodbye | 0.00 | 15 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.79 | 14 | – | – | – | 0.77 |
| VERDICT | would continue | 0.00 | 14 | – | – | – | 0.00 |
| VERDICT | would return | 0.00 | 14 | – | – | – | 0.23 |

## Decision vs i1: **REJECT**

- DRIVER moved away beyond run-to-run spread: first_q_answered
- DRIVER moved away beyond run-to-run spread: time_or_pay_before_answer
- VERDICT would_return dropped 23% -> 0%

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.00 | 0.00 |
| S1 | session_1 | passive_follower | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 1 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 1.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 1 | 0.00 | 0.83 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 1 | 0.00 | 0.83 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 1 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 1 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 1 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S3 | session_1 | passive_follower | 1 | 0.00 | 0.80 | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 1 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 2.00 | 0.00 |
| S4 | session_1 | passive_follower | 1 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 1 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 3.00 | – |

## What to change (DRIVERs missing target)

### first_q_answered = 0.80 (target 100% of chats)
Prompt lever: Answer-first instruction; drip-feed / Zeigarnik instruction (withholding the answer)

- S2 / direct_answer_chaser_same_day / session_1
  - USER: Future
  - ASTRO: Namaste ji! Future ke baare mein kundli sab batati hai. Career ya shaadi, kis baare mein janna hai?
- S2 / passive_follower_same_day / session_1
  - USER: Future
  - ASTRO: Namaste ji! Future ke baare mein sab kuch dekhti hoon. Aapki shaadi ho chuki hai ya abhi single hain ji?

### time_or_pay_before_answer = 0.13 (target 0% of chats)
Prompt lever: Wall / last-minute instruction ('Time thoda kam reh gaya hai...')

- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Ok
  - ASTRO: Time thoda kam hai ji. Partner tall aur calm honge. Thoda aur time do na.
- S2 / direct_answer_chaser_genuine_return / session_2
  - USER: June 2027 ke baad pakka?
  - ASTRO: Haan, bilkul pakka hai ji. Shani ka pressure hatne se rahat milegi. Time thoda kam reh gaya hai — aapke kundli mein 2028 mein ghar khareedne ka yog bhi dikh raha hai.

### refusals = 0.07 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S3 / passive_follower / session_1
  - USER: Number kitna
  - ASTRO: Kundli mein exact count nahi hota ji. Third house aapki mehnat dikhata hai.

### user_frustrated = 0.80 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua. Confirm batao selection hoga ya nahi?
  - ASTRO: Abhi agle hafte selection mushkil hai ji. Shani ka transit 10th house par chal raha hai. Asli success March 2027 ke baad hi milegi.
- S1 / direct_answer_chaser / session_1
  - USER: Main haan ya na puch rha hu.
  - ASTRO: Aapka gussa bilkul sahi hai ji. Shani ki delay energy abhi heavy hai. March ke baad relief milega.
