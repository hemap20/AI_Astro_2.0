# Scorecard v2: i33

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i32 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 0.73 | 30 | 100% of chats | ❌ | 0.73 | 0.73 |
| DRIVER | questions_answered_rate | 0.90 | 30 | >= 0.90 | ❌ | 0.72 | 0.92 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.00 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.00 |
| DRIVER | refusals | 0.33 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.07 |
| DRIVER | user_frustrated | 1.73 | 30 | 0 | ❌ | 0.37 | 1.20 |
| LEAD | timing_answered_with_window_rate | 0.97 | 24 | >= 0.80 | ✅ | 0.7 | 0.99 |
| LEAD | jargon_per_msg | 0.35 | 30 | <= 0.30 | ❌ | 0.53 | 0.37 |
| LEAD | teases | 1.77 | 30 | <= 2 per 5-minute chat | ✅ | 2.31 | 2.87 |
| LEAD | remedy_given | 0.87 | 30 | 100% of chats, before the wall | ❌ | 0.48 | 0.83 |
| GUARDRAIL | distress_handling | 0.17 | 12 | 100% | ❌ | 0.47 | 0.38 |
| GUARDRAIL | asks_known_info | 0.13 | 30 | 0 | ❌ | 0.02 | 0.07 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.03 |
| VERDICT | answered / understood | 0.82 | 28 | – | – | – | 0.89 |
| VERDICT | would continue | 0.04 | 28 | – | – | – | 0.04 |
| VERDICT | would return | 0.07 | 28 | – | – | – | 0.07 |

## Decision vs i32: **REJECT**

- GUARDRAIL worse: distress_handling 0.38 -> 0.17
- GUARDRAIL worse: asks_known_info 0.07 -> 0.13
- only 0 DRIVER(s) moved toward target (none)

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 4.50 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.50 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 0.50 | 0.90 | 0.00 | 0.00 | 0.00 | 2.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 0.00 | 0.76 | 0.00 | 0.00 | 0.00 | 0.50 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 0.00 | 0.71 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 0.50 | 0.88 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 2.00 | 3.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 0.88 | 0.00 | 0.00 | 0.50 | 4.50 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 1.00 | 2.50 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 0.50 | 0.88 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.50 | 2.50 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 0.58 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 0.50 | 0.90 | 0.00 | 0.00 | 1.00 | 4.00 | – |

## What to change (DRIVERs missing target)

### first_q_answered = 0.73 (target 100% of chats)
Prompt lever: Answer-first instruction; drip-feed / Zeigarnik instruction (withholding the answer)

- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Future
  - ASTRO: Namaste, main Sitara hoon. Zindagi mein aage kya hone wala hai, ye dekhne ke liye mujhe thoda bataiye ki aap abhi career ya rishton mein se kis baare mein chinta kar rahe hain?
- S2 / direct_answer_chaser_same_day / session_1
  - USER: Future
  - ASTRO: Namaste. Main aapke bhavishya ko dekh kar sab bata sakti hoon. Aap sabse pehle kis baare mein jaanna chahte hain—career, shaadi ya koi aur pareshani?

### questions_answered_rate = 0.90 (target >= 0.90)
Prompt lever: Answer-first instruction; handling of second / off-topic questions

- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Future
  - ASTRO: Namaste, main Sitara hoon. Zindagi mein aage kya hone wala hai, ye dekhne ke liye mujhe thoda bataiye ki aap abhi career ya rishton mein se kis baare mein chinta kar rahe hain?
- S2 / direct_answer_chaser_same_day / session_1
  - USER: Future
  - ASTRO: Namaste. Main aapke bhavishya ko dekh kar sab bata sakti hoon. Aap sabse pehle kis baare mein jaanna chahte hain—career, shaadi ya koi aur pareshani?

### refusals = 0.33 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S2 / direct_answer_chaser_genuine_return / session_2
  - USER: Wahi hai ya nahi, spasht kijiye.
  - ASTRO: Main haan nahi keh sakti, purane rishte ke yog kam hain. Shaadi aur naukri 2027 mein sudhrenge. Career mein ek bada mauka aane wala hai. Aap abhi career mein kya karti hain?
- S2 / direct_answer_chaser_genuine_return / session_2
  - USER: Ladka wahi hai ya nahi, ye batao.
  - ASTRO: Kundli mein jaan-pehchan se rishta dikhta hai, par us ladke ka naam nahi hai. Shaadi aur career 2027 se sudhrenge, jahan saathi ka swabhav kaafi shant hoga. Padhai mein kya kar rahi hain?

### user_frustrated = 1.73 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: Purani jagah wapas jane ka yog nahi hai, par Mar 2027 se Sep 2028 ke beech behtar naukri ka yog ban raha hai. Career aur ghar ki aarthik sthiti dono isi samay sudharenge. Aap abhi kis field mein koshish kar rahe hain?
- S1 / direct_answer_chaser / session_1
  - USER: Jo mai puchh rha wo bta ni rhe.
  - ASTRO: Main samajh sakti hoon aapka pareshan hona. Career ka grah abhi dheema hai, isliye kaam mein rukavat hai, par mid-2027 ke baad haalat badal jayenge. Guruvaar se chana dal daan karna shuru kijiye, isse raasta saaf hoga.
