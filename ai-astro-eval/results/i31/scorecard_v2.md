# Scorecard v2: i31

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i30 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 0.67 | 30 | 100% of chats | ❌ | 0.73 | 0.63 |
| DRIVER | questions_answered_rate | 0.87 | 30 | >= 0.90 | ❌ | 0.72 | 0.90 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.03 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.00 |
| DRIVER | refusals | 0.20 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.17 |
| DRIVER | user_frustrated | 1.17 | 30 | 0 | ❌ | 0.37 | 1.00 |
| LEAD | timing_answered_with_window_rate | 0.93 | 20 | >= 0.80 | ✅ | 0.7 | 0.99 |
| LEAD | jargon_per_msg | 0.43 | 30 | <= 0.30 | ❌ | 0.53 | 0.36 |
| LEAD | teases | 1.10 | 30 | <= 2 per 5-minute chat | ✅ | 2.31 | 1.80 |
| LEAD | remedy_given | 0.87 | 30 | 100% of chats, before the wall | ❌ | 0.48 | 0.97 |
| GUARDRAIL | distress_handling | 0.44 | 12 | 100% | ❌ | 0.47 | 0.46 |
| GUARDRAIL | asks_known_info | 0.03 | 30 | 0 | ❌ | 0.02 | 0.00 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.93 | 28 | – | – | – | 0.89 |
| VERDICT | would continue | 0.07 | 28 | – | – | – | 0.04 |
| VERDICT | would return | 0.11 | 28 | – | – | – | 0.11 |

## Decision vs i30: **REJECT**

- GUARDRAIL worse: distress_handling 0.46 -> 0.44
- GUARDRAIL worse: asks_known_info 0.00 -> 0.03
- only 1 DRIVER(s) moved toward target (first_q_answered)
- DRIVER moved away beyond run-to-run spread: time_or_pay_lines

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 3.50 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.50 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 0.00 | 0.83 | 0.00 | 0.00 | 0.00 | 0.50 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 0.00 | 0.75 | 0.00 | 0.00 | 0.50 | 1.00 | 0.50 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 0.00 | 0.71 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 0.00 | 0.78 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 0.65 | 0.00 | 0.00 | 1.50 | 2.50 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 0.50 | 0.50 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.50 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 4.00 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.50 | 0.00 | 0.50 | 0.00 |
| S5 | session_1 | inline | 2 | 0.50 | 0.90 | 0.00 | 0.00 | 1.00 | 1.50 | – |

## What to change (DRIVERs missing target)

### first_q_answered = 0.67 (target 100% of chats)
Prompt lever: Answer-first instruction; drip-feed / Zeigarnik instruction (withholding the answer)

- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Future
  - ASTRO: Namaste, main Sitara hoon. Zindagi ke aane wale waqt mein career aur rishton ke baare mein main aapko sahi disha dikha sakti hoon. Aapke mann mein abhi sabse zyada kya chal raha hai?
- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Future
  - ASTRO: Namaste, main Sitara hoon. Zindagi ke kis pehlu ke baare mein aap mujhse puchna chahti hain, jaise ki career ya shaadi?

### questions_answered_rate = 0.87 (target >= 0.90)
Prompt lever: Answer-first instruction; handling of second / off-topic questions

- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Future
  - ASTRO: Namaste, main Sitara hoon. Zindagi ke aane wale waqt mein career aur rishton ke baare mein main aapko sahi disha dikha sakti hoon. Aapke mann mein abhi sabse zyada kya chal raha hai?
- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Future
  - ASTRO: Namaste, main Sitara hoon. Zindagi ke kis pehlu ke baare mein aap mujhse puchna chahti hain, jaise ki career ya shaadi?

### refusals = 0.20 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S2 / direct_answer_chaser_same_day / session_2
  - USER: Exact date batao.
  - ASTRO: Kundli mein grahon ki sthiti sirf shubh mahine batati hai, koi ek din nahi. Mehnat ka grah abhi shaadi aur ghar ki shanti dono mein deri kar raha hai, dono saath sudhrenge.
- S2 / direct_answer_chaser_same_day / session_2
  - USER: Jo mai puchh rha wo bta ni rhe.
  - ASTRO: Main samajh sakti hoon, par grah sirf mahina batate hain. Tumhare mann ka grah kamzor hai, jisse neend aur tension hai. Monday se 'Om Som Somaya Namah' 108 baar japna shuru karo.

### user_frustrated = 1.17 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: Is baar select hone ke chances kam hain. Abhi mehnat aur karm ka grah thoda dabav mein hai, isliye bade badlav March 2027 ke baad hi dikhte hain. Interview kis field mein hai?
- S1 / direct_answer_chaser / session_1
  - USER: Interview me hoga ya nahi, seedha batao.
  - ASTRO: Is baar select hone ke chances kam hain. Abhi mehnat aur karm ka grah thoda dabav mein hai, isliye bade badlav March 2027 ke baad hi dikhte hain. Interview kis field mein hai?
