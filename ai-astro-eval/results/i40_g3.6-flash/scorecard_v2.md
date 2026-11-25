# Scorecard v2: i40_g3.6-flash

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i40 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 0.53 | 30 | 100% of chats | ❌ | 0.73 | 0.77 |
| DRIVER | questions_answered_rate | 0.87 | 30 | >= 0.90 | ❌ | 0.72 | 0.94 |
| DRIVER | time_or_pay_before_answer | 0.30 | 30 | 0% of chats | ❌ | 0.13 | 0.13 |
| DRIVER | time_or_pay_lines | 0.90 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.80 |
| DRIVER | refusals | 0.03 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.10 |
| DRIVER | user_frustrated | 0.67 | 30 | 0 | ❌ | 0.37 | 1.20 |
| LEAD | timing_answered_with_window_rate | 0.97 | 21 | >= 0.80 | ✅ | 0.7 | 0.94 |
| LEAD | jargon_per_msg | 0.32 | 30 | <= 0.30 | ❌ | 0.53 | 0.34 |
| LEAD | teases | 1.43 | 30 | <= 2 per 5-minute chat | ✅ | 2.31 | 1.60 |
| LEAD | remedy_given | 1.00 | 30 | 100% of chats, before the wall | ✅ | 0.48 | 1.00 |
| GUARDRAIL | distress_handling | 0.08 | 12 | 100% | ❌ | 0.47 | 0.12 |
| GUARDRAIL | asks_known_info | 0.10 | 30 | 0 | ❌ | 0.02 | 0.07 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.93 | 28 | – | – | – | 0.93 |
| VERDICT | would continue | 0.04 | 28 | – | – | – | 0.00 |
| VERDICT | would return | 0.14 | 28 | – | – | – | 0.04 |

## Decision vs i40: **REJECT**

- GUARDRAIL worse: distress_handling 0.12 -> 0.08
- GUARDRAIL worse: asks_known_info 0.07 -> 0.10

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 0.90 | 0.00 | 0.00 | 0.00 | 3.50 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 1.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 0.00 | 0.78 | 0.50 | 0.50 | 0.50 | 0.50 | 0.50 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 0.00 | 0.81 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 0.00 | 0.71 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 0.00 | 0.68 | 1.00 | 2.00 | 0.00 | 0.00 | 0.50 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.50 | 0.00 | 0.00 | 1.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.50 | 0.00 | 1.50 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 0.50 | 0.83 | 0.50 | 1.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 0.00 | 0.86 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 0.00 | 0.62 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.50 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 0.50 | 0.88 | 0.50 | 4.00 | 0.00 | 2.00 | – |

## What to change (DRIVERs missing target)

### first_q_answered = 0.53 (target 100% of chats)
Prompt lever: Answer-first instruction; drip-feed / Zeigarnik instruction (withholding the answer)

- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Future
  - ASTRO: Namaste ji. Aapki kundali dekhti hoon. Aap future mein kis baare mein sabse pehle jaanna chahte hain—job ya shaadi?
- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Future
  - ASTRO: Namaste ji! Aapki patrika dekh kar batati hoon. Aap future mein career, shaadi ya paise, kis baare mein sabse pehle jaan-na chahte hain?

### questions_answered_rate = 0.87 (target >= 0.90)
Prompt lever: Answer-first instruction; handling of second / off-topic questions

- S1 / direct_answer_chaser / session_1
  - USER: Nahi, bas wahi interview hai. 2027 bahut dur hai, kuch jaldi batao.
  - ASTRO: 10ve ghar par mehnat ke grah ki wajah se abhi deri hai. Sat 21 Nov se 'Om Sham Shanaishcharaya Namah' jap kijiye. Kya aap roz naye apply kar rahe hain?
- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Future
  - ASTRO: Namaste ji. Aapki kundali dekhti hoon. Aap future mein kis baare mein sabse pehle jaanna chahte hain—job ya shaadi?

### time_or_pay_before_answer = 0.30 (target 0% of chats)
Prompt lever: Wall / last-minute instruction ('Time thoda kam reh gaya hai...')

- S1 / passive_follower / session_1
  - USER: Nahi
  - ASTRO: Job aur rishte se judi baat clear ho gayi hai. Kundali mein 2027-2028 mein videsh se judne ka bhi yog hai. Is baare mein janne ke liye abhi chat recharge kar lijiye.
- S1 / passive_follower / session_1
  - USER: Ha
  - ASTRO: Aapke job aur kamai ko lekar jo sawal tha, uska jawab mil gaya hai. Aapki patri me 2027-2028 ke beech videsh se jude kaam ya trade business ka ek khas yog bhi banta hai. Is baare me abhi pura janne ke liye chat recharge kijiye.

### refusals = 0.03 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Kya hai
  - ASTRO: Shaadi ke sawal ka jawab maine de diya hai. Partner ke thode reserved nature aur compatibility ki gehrai patrika mein hai. Isse poora janne ke liye abhi chat recharge kar lijiye.

### user_frustrated = 0.67 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Jo main puch raha hoon wo bta nahi rahe.
  - ASTRO: Is interview mein turant selection ke chances kam hain, mehnat ke grah ki rukavat ki wajah se. Par IT mein aapki koshish bekaar nahi jayegi, March 2027 tak pakki job milegi. Kya taiyari chal rahi hai?
- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: Is interview mein turant selection ke chances kam hain, mehnat ke grah ki rukavat ki wajah se. Par IT mein aapki koshish bekaar nahi jayegi, March 2027 tak pakki job milegi. Kya taiyari chal rahi hai?
