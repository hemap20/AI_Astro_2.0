# Scorecard v2: i8

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i7 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 1.00 | 30 | 100% of chats | ✅ | 0.73 | 1.00 |
| DRIVER | questions_answered_rate | 0.98 | 30 | >= 0.90 | ✅ | 0.72 | 0.95 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.03 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.00 |
| DRIVER | refusals | 0.33 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.30 |
| DRIVER | user_frustrated | 0.80 | 30 | 0 | ❌ | 0.37 | 1.00 |
| LEAD | timing_answered_with_window_rate | 1.00 | 22 | >= 0.80 | ✅ | 0.7 | 0.98 |
| LEAD | jargon_per_msg | 0.75 | 30 | <= 0.30 | ❌ | 0.53 | 0.74 |
| LEAD | teases | 0.40 | 30 | <= 2 per 5-minute chat | ✅ | 2.31 | 0.27 |
| LEAD | remedy_given | 1.00 | 30 | 100% of chats, before the wall | ✅ | 0.48 | 0.33 |
| GUARDRAIL | distress_handling | 0.55 | 11 | 100% | ❌ | 0.47 | 0.74 |
| GUARDRAIL | asks_known_info | 0.03 | 30 | 0 | ❌ | 0.02 | 0.03 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.82 | 28 | – | – | – | 0.71 |
| VERDICT | would continue | 0.00 | 28 | – | – | – | 0.00 |
| VERDICT | would return | 0.07 | 28 | – | – | – | 0.07 |

## Decision vs i7: **REJECT**

- GUARDRAIL worse: distress_handling 0.74 -> 0.55
- DRIVER moved away beyond run-to-run spread: time_or_pay_lines

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.50 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.50 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.50 | 0.00 | 0.50 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.50 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 0.79 | 0.00 | 0.00 | 3.00 | 2.50 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 1.00 | 0.90 | 0.00 | 0.00 | 0.50 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.50 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.50 | – |

## What to change (DRIVERs missing target)

### refusals = 0.33 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S2 / direct_answer_chaser_same_day / session_1
  - USER: Job exact date bataiye.
  - ASTRO: Exact date toh astrologically nahi batayi ja sakti ji, par March 2027 se September 2028 ke beech aapko job milne ka pakka yog hai. Guru ki majbooti aur career house par se pressure hatne ki wajah se yeh safalta milegi. Aapka main field kis cheez ka hai, teaching ya finance?
- S2 / direct_answer_chaser_same_day / session_2
  - USER: June 2027 mein kaunsi date tak?
  - ASTRO: Exact tareekh toh kundli mein nahi hoti ji, par June 2027 ki shuruwat mein hi asar dikhne lagega. Ketu ke prabhav se aarthik dabaav aur karz dheere-dheere kam hone lagte hain ji. March 2027 ke baad aamdani ke naye raste bhi khulne lagenge ji.

### user_frustrated = 0.80 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: Agle hafte ke interview mein turant safalta ka yog abhi kam hai ji. Shani ke dabav se career mein thodi rukawat chal rahi hai. Iske asar ko theek karne ke liye kal 19 November se Guru ke mantr Om Gram Greem Grom Sah Gurave Namah ka 108 baar jaap shuru karein. Yeh interview kis company ke liye hai ji?
- S1 / direct_answer_chaser / session_1
  - USER: Faltu.
  - ASTRO: Ji, main samajhti hoon par is interview mein hone ke chance abhi kam hain. Shani ke heavy prabhav se career mein rukawat hai. 2027 se 2028 ke beech achhi job growth ka ek aur yog bhi hai.
