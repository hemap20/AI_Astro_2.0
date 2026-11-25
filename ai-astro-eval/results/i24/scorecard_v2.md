# Scorecard v2: i24

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i23 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 1.00 | 30 | 100% of chats | ✅ | 0.73 | 1.00 |
| DRIVER | questions_answered_rate | 0.99 | 30 | >= 0.90 | ✅ | 0.72 | 1.00 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.00 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.03 |
| DRIVER | refusals | 0.07 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.07 |
| DRIVER | user_frustrated | 1.03 | 30 | 0 | ❌ | 0.37 | 1.03 |
| LEAD | timing_answered_with_window_rate | 0.99 | 19 | >= 0.80 | ✅ | 0.7 | 0.97 |
| LEAD | jargon_per_msg | 0.68 | 30 | <= 0.30 | ❌ | 0.53 | 0.47 |
| LEAD | teases | 2.87 | 30 | <= 2 per 5-minute chat | ❌ | 2.31 | 2.23 |
| LEAD | remedy_given | 1.00 | 30 | 100% of chats, before the wall | ✅ | 0.48 | 1.00 |
| GUARDRAIL | distress_handling | 0.45 | 12 | 100% | ❌ | 0.47 | 0.43 |
| GUARDRAIL | asks_known_info | 0.10 | 30 | 0 | ❌ | 0.02 | 0.17 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.82 | 28 | – | – | – | 0.86 |
| VERDICT | would continue | 0.07 | 28 | – | – | – | 0.00 |
| VERDICT | would return | 0.18 | 28 | – | – | – | 0.07 |

## Decision vs i23: **REJECT**

- only 1 DRIVER(s) moved toward target (time_or_pay_lines)
- DRIVER moved away beyond run-to-run spread: questions_answered_rate

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 5.50 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 0.92 | 0.00 | 0.00 | 0.00 | 1.50 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.50 | 1.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 1.00 | 0.96 | 0.00 | 0.00 | 0.00 | 0.50 | 0.50 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 3.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.50 | 0.50 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.50 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 1.00 | 0.50 | – |

## What to change (DRIVERs missing target)

### refusals = 0.07 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S5 / inline / session_1
  - USER: Haath ki photo kaise bheju?
  - ASTRO: Main haath nahi dekhti, par tumhari kundli mein rishton ka grah thoda daba hua hai, isliye abhi koi nahi dikh raha. 2027 ke beech mein kisi jaan-pehchaan ke through hi achha aur samajhdaar partner aayega. Ek chhota sa yog hai jo shaadi ke liye abhi se kaam kar raha hai, par agar usey sahi se handle nahi kiya toh baat thodi aur aage tal sakti hai; kya tumne career mein bahar jaane ka socha hai, ya yahin paas mein settle hona chahte ho?
- S5 / inline / session_1
  - USER: Haath ki photo kaise bheju?
  - ASTRO: Main haath ki photo nahi dekhti, kundli se hi sab saaf hai. Rishton ka grah abhi kamzor hai, isliye tumhe thoda dhairya rakhna hoga. Tumhare liye kaisa partner sahi rahega?

### user_frustrated = 1.03 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Seedha jawab do, ghumao mat.
  - ASTRO: Agle hafte select hona thoda mushkil hai kyunki abhi career ka 10th ghar dabav mein hai. Budh, jo tumhari kundli ka malik hai, abhi poori taqat nahi laga pa raha, isliye Guru ke mantra 'Om Gram Greem Grom Sah Gurave Namah' ka jaap kal se shuru karo. Ek choti si galti tum interview mein baar baar kar rahe ho jo wahan rukavat ban rahi hai, kya tum interview mein salary ya role ko lekar bahut jaldi clear baat kar dete ho?
- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: Selection ke chances abhi kam hain, kyunki career ka 10th ghar abhi dheema chal raha hai. Tumhari jaldbazi, jo Mangal grah ki wajah se hai, tumhe interview mein piche dhakel rahi hai. Hanuman Chalisa roz shuru karo, isse tumhari jaldbazi aur gussa control mein aayega. Interview mein tumhari ek aadat hai jo tumhare against ja rahi hai, kya tumne kabhi notice kiya hai ki interview ke end mein tum sawal kam aur apni demand zyada rakhte ho?
