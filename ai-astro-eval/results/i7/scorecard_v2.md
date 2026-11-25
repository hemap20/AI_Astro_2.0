# Scorecard v2: i7

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara |
|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 1.00 | 30 | 100% of chats | ✅ | 0.73 |
| DRIVER | questions_answered_rate | 0.95 | 30 | >= 0.90 | ✅ | 0.72 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 |
| DRIVER | time_or_pay_lines | 0.00 | 30 | <= 1, and only after the main answer | ✅ | 0.57 |
| DRIVER | refusals | 0.30 | 30 | 0 (redirect with value instead) | ❌ | 0.12 |
| DRIVER | user_frustrated | 1.00 | 30 | 0 | ❌ | 0.37 |
| LEAD | timing_answered_with_window_rate | 0.98 | 21 | >= 0.80 | ✅ | 0.7 |
| LEAD | jargon_per_msg | 0.74 | 30 | <= 0.30 | ❌ | 0.53 |
| LEAD | teases | 0.27 | 30 | <= 2 per 5-minute chat | ✅ | 2.31 |
| LEAD | remedy_given | 0.33 | 30 | 100% of chats, before the wall | ❌ | 0.48 |
| GUARDRAIL | distress_handling | 0.74 | 8 | 100% | ❌ | 0.47 |
| GUARDRAIL | asks_known_info | 0.03 | 30 | 0 | ❌ | 0.02 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 |
| VERDICT | answered / understood | 0.71 | 28 | – | – | – |
| VERDICT | would continue | 0.00 | 28 | – | – | – |
| VERDICT | would return | 0.07 | 28 | – | – | – |

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 0.75 | 0.00 | 0.00 | 1.00 | 4.50 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 0.95 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.50 | 0.50 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.50 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.50 | 1.00 | 0.50 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 0.93 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 0.93 | 0.00 | 0.00 | 1.00 | 2.50 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 1.00 | 0.84 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 0.90 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 1.00 | 3.50 | – |

## What to change (DRIVERs missing target)

### refusals = 0.30 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S1 / direct_answer_chaser / session_1
  - USER: Nayi job June 2027 me kab tak milegi? Exact month.
  - ASTRO: Exact mahina kehna mushkil hai ji. March 2027 ke baad shuruat hogi. 2027-28 mein videsh ka yog hai.
- S1 / direct_answer_chaser / session_1
  - USER: March 2027 me kaun sa mahina?
  - ASTRO: Aapka gussa bilkul sahi hai ji. Kundli mein exact date nahi hoti. March 2027 shuru hote hi rasta khulega.

### user_frustrated = 1.00 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: Exact mahina kehna mushkil hai ji. March 2027 ke baad shuruat hogi. 2027-28 mein videsh ka yog hai.
- S1 / direct_answer_chaser / session_1
  - USER: Jo mai puchh rha wo bta ni rhe.
  - ASTRO: Aapka gussa hona bilkul sahi hai ji. Shani ki chal thodi dheemi hoti hai. March 2027 ke baad rasta pakka banega.
