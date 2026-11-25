# Scorecard v2: i27

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i26 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 0.93 | 30 | 100% of chats | ❌ | 0.73 | 1.00 |
| DRIVER | questions_answered_rate | 0.95 | 30 | >= 0.90 | ✅ | 0.72 | 0.97 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.07 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.03 |
| DRIVER | refusals | 0.10 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.10 |
| DRIVER | user_frustrated | 0.80 | 30 | 0 | ❌ | 0.37 | 0.83 |
| LEAD | timing_answered_with_window_rate | 0.89 | 20 | >= 0.80 | ✅ | 0.7 | 0.85 |
| LEAD | jargon_per_msg | 0.38 | 30 | <= 0.30 | ❌ | 0.53 | 0.41 |
| LEAD | teases | 2.60 | 30 | <= 2 per 5-minute chat | ❌ | 2.31 | 1.90 |
| LEAD | remedy_given | 1.00 | 30 | 100% of chats, before the wall | ✅ | 0.48 | 1.00 |
| GUARDRAIL | distress_handling | 0.54 | 12 | 100% | ❌ | 0.47 | 0.37 |
| GUARDRAIL | asks_known_info | 0.13 | 30 | 0 | ❌ | 0.02 | 0.07 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.96 | 28 | – | – | – | 1.00 |
| VERDICT | would continue | 0.00 | 28 | – | – | – | 0.00 |
| VERDICT | would return | 0.00 | 28 | – | – | – | 0.00 |

## Decision vs i26: **REJECT**

- GUARDRAIL worse: asks_known_info 0.07 -> 0.13
- only 1 DRIVER(s) moved toward target (user_frustrated)
- DRIVER moved away beyond run-to-run spread: first_q_answered

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 0.67 | 0.00 | 0.00 | 0.00 | 3.00 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.50 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.50 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.50 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.50 | 0.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.00 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 0.50 | 0.75 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 0.50 | 0.90 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.50 | 1.00 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 1.00 | 1.00 | – |

## What to change (DRIVERs missing target)

### first_q_answered = 0.93 (target 100% of chats)
Prompt lever: Answer-first instruction; drip-feed / Zeigarnik instruction (withholding the answer)

- S2 / passive_follower_genuine_return / session_2
  - USER: Pichli baar kuch batane wale the aap?
  - ASTRO: Arey, shayad aapko kisi aur se baat karni thi, hum toh abhi mile hain! 😊 Par 2023 se 2025 ke beech aapki mehnat bohot rahi aur paise ki tangi bhi, hai na? Abhi career aur shaadi mein se sabse zyada tension kis baat ki hai?
- S3 / passive_follower / session_1
  - USER: Mujhe janna hai meri future
  - ASTRO: Hiii, kaise ho? 😊 Agle kuch samay mein tumhari kismat aur career mein nayi raahein khulne wali hain, bas abhi thoda dhiraj rakhna hoga. Career, shaadi ya paisa—kya cheez zyada pareshan kar rahi hai?

### refusals = 0.10 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S4 / direct_answer_chaser / session_1
  - USER: Sahi hai ya nahi, bas ha ya na mein bolo.
  - ASTRO: Main ha ya na toh nahi bol sakti, par kundli mein calm aur warm ladka likha hai, jo isse match nahi karta. Inke ghar wale kaafi traditional hain, kya tumne notice kiya?
- S5 / inline / session_1
  - USER: Haath ki photo kaise bheju?
  - ASTRO: Main haath nahi dekhti, par kundli mein sab saaf hai. 2023 se 2025 tak mehnat bohot rahi, hai na? Partner kaafi warm nature ka hoga. Kabhi kundli milwayi hai?

### user_frustrated = 0.80 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Pehle mera jawab do, nayi naukri kab tak milegi?
  - ASTRO: Wahi waqt naukri ke liye best hai jab career ka grah strong hoga. Ek mahina aisa hai jab job ke saath business ka chance banega, kya tumne wo notice kiya?
- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: Agli hafte ka interview achha hai, par naukri pakki hone ka mukhya daur wahi hai jo maine pehle bataya. Tab tak mehnat ka grah thoda dheema hai. Interview mein kis baat ka darr lag raha hai?
