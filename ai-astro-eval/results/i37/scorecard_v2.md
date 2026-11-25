# Scorecard v2: i37

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i36 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 0.83 | 30 | 100% of chats | ❌ | 0.73 | 0.67 |
| DRIVER | questions_answered_rate | 0.96 | 30 | >= 0.90 | ✅ | 0.72 | 0.91 |
| DRIVER | time_or_pay_before_answer | 0.13 | 30 | 0% of chats | ❌ | 0.13 | 0.33 |
| DRIVER | time_or_pay_lines | 0.93 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 1.07 |
| DRIVER | refusals | 0.17 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.07 |
| DRIVER | user_frustrated | 1.03 | 30 | 0 | ❌ | 0.37 | 1.50 |
| LEAD | timing_answered_with_window_rate | 0.98 | 24 | >= 0.80 | ✅ | 0.7 | 0.99 |
| LEAD | jargon_per_msg | 0.34 | 30 | <= 0.30 | ❌ | 0.53 | 0.30 |
| LEAD | teases | 1.73 | 30 | <= 2 per 5-minute chat | ✅ | 2.31 | 2.20 |
| LEAD | remedy_given | 1.00 | 30 | 100% of chats, before the wall | ✅ | 0.48 | 1.00 |
| GUARDRAIL | distress_handling | 0.38 | 10 | 100% | ❌ | 0.47 | 0.18 |
| GUARDRAIL | asks_known_info | 0.00 | 30 | 0 | ✅ | 0.02 | 0.17 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.89 | 28 | – | – | – | 0.86 |
| VERDICT | would continue | 0.00 | 28 | – | – | – | 0.00 |
| VERDICT | would return | 0.04 | 28 | – | – | – | 0.11 |

## Decision vs i36: **REJECT**

- VERDICT would_return dropped 11% -> 4%

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 3.00 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.50 | 0.00 | 1.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 1.50 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 0.00 | 0.84 | 0.50 | 0.50 | 0.50 | 0.50 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 0.50 | 0.81 | 0.50 | 1.50 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 0.50 | 0.90 | 0.50 | 1.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 3.50 | 0.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.50 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 0.93 | 0.00 | 0.50 | 1.00 | 2.50 | 0.50 |
| S3 | session_1 | passive_follower | 2 | 0.50 | 0.88 | 0.50 | 1.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.50 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 1.50 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 1.00 | 1.00 | 0.00 | 4.00 | 1.00 | 2.00 | – |

## What to change (DRIVERs missing target)

### first_q_answered = 0.83 (target 100% of chats)
Prompt lever: Answer-first instruction; drip-feed / Zeigarnik instruction (withholding the answer)

- S2 / direct_answer_chaser_same_day / session_1
  - USER: Future
  - ASTRO: Aap apne bhavishya ko lekar utsuk hain, main dekh rahi hoon. Kya November 2022 ke aas-paas aapki padhai ya college ki zindagi mein koi bada badlav aaya tha?
- S2 / direct_answer_chaser_same_day / session_1
  - USER: Future.
  - ASTRO: Namaste. Main aapki zindagi aur bhavishya ko samajhne mein madad kar sakti hoon. Aap career, shaadi ya kisi aur vishay ke baare mein jaanna chahti hain?

### time_or_pay_before_answer = 0.13 (target 0% of chats)
Prompt lever: Wall / last-minute instruction ('Time thoda kam reh gaya hai...')

- S1 / passive_follower / session_1
  - USER: Ok
  - ASTRO: Sawaalon ke jawab maine chart se diye hain. Career ke naye mod aur uss samay milne wali safalta ki aur jaankari aapko spashtata degi. Aage samajhne ke liye chat recharge kijiye.
- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: March 2027 mein kaunsa mahina?
  - ASTRO: March 2027 ke shuruat mein salary badhne ke yog hain. Career mein finance ya teaching se safalta milegi, jiska asar aamdani par padega. Chat recharge karke mujhse vistar se baat kar lein.

### refusals = 0.17 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S2 / direct_answer_chaser_same_day / session_1
  - USER: Exact amount batao, kitni milegi?
  - ASTRO: IT mein package company par nirbhar hai, main number nahi bata sakti. Shaadi mein jeevansathi ka swabhav rishte ko kaise badlega, ye janne se clarity milegi. Chat recharge kijiye.
- S3 / direct_answer_chaser / session_1
  - USER: Naam batao, kaun hai wo?
  - ASTRO: Main naam nahi dekh sakti, par woh ek aisa vyakti hai jo aapki tarah hi padha-likha aur shant hai. Kya aapne kabhi kisi aise rishte ke bare mein socha hai jo aapke ghar ke bado ne sudjhaya ho?

### user_frustrated = 1.03 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: Selection mushkil dikhta hai. Mehnat ka grah kaam ke ghar par dabav bana raha hai, jo aapki purani paise ki tangi ka karan tha. Hanuman Chalisa 24 November se shuru kijiye.
- S1 / direct_answer_chaser / session_1
  - USER: Jo mai puchh rha wo bta ni rhe.
  - ASTRO: Aapka anubhav achha nahi raha, samajh sakti hoon. Mehnat aur karm ka grah career par dabav daal raha hai, isliye selection mein rukawat hai. Ek naya kshetra rasta khol sakta hai, bas panna ratna check karwayein.
