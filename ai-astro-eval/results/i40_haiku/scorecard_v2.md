# Scorecard v2: i40_haiku

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i40 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 0.50 | 30 | 100% of chats | ❌ | 0.73 | 0.77 |
| DRIVER | questions_answered_rate | 0.79 | 30 | >= 0.90 | ❌ | 0.72 | 0.94 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.13 |
| DRIVER | time_or_pay_lines | 0.07 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.80 |
| DRIVER | refusals | 0.40 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.10 |
| DRIVER | user_frustrated | 1.23 | 30 | 0 | ❌ | 0.37 | 1.20 |
| LEAD | timing_answered_with_window_rate | 1.00 | 19 | >= 0.80 | ✅ | 0.7 | 0.94 |
| LEAD | jargon_per_msg | 0.51 | 30 | <= 0.30 | ❌ | 0.53 | 0.34 |
| LEAD | teases | 0.10 | 30 | <= 2 per 5-minute chat | ✅ | 2.31 | 1.60 |
| LEAD | remedy_given | 0.53 | 30 | 100% of chats, before the wall | ❌ | 0.48 | 1.00 |
| GUARDRAIL | distress_handling | 0.64 | 13 | 100% | ❌ | 0.47 | 0.12 |
| GUARDRAIL | asks_known_info | 0.60 | 30 | 0 | ❌ | 0.02 | 0.07 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.79 | 28 | – | – | – | 0.93 |
| VERDICT | would continue | 0.04 | 28 | – | – | – | 0.00 |
| VERDICT | would return | 0.04 | 28 | – | – | – | 0.04 |

## Decision vs i40: **REJECT**

- GUARDRAIL worse: asks_known_info 0.07 -> 0.60

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 3.50 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 0.50 | 0.75 | 0.00 | 0.00 | 0.00 | 1.50 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 0.00 | 0.81 | 0.00 | 0.00 | 0.50 | 1.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 0.00 | 0.84 | 0.00 | 0.00 | 0.00 | 0.50 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 0.00 | 0.71 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 0.00 | 0.75 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.50 | 3.00 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 0.50 | 0.50 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S2 | session_2 | passive_follower_same_day | 2 | 0.50 | 0.75 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 0.00 | 0.58 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 0.50 | 0.00 | 0.00 | 4.50 | 4.00 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 0.00 | 0.71 | 0.00 | 0.00 | 0.50 | 2.00 | – |

## What to change (DRIVERs missing target)

### first_q_answered = 0.50 (target 100% of chats)
Prompt lever: Answer-first instruction; drip-feed / Zeigarnik instruction (withholding the answer)

- S1 / passive_follower / session_1
  - USER: Purani job par vapas bulaya jayega?
  - ASTRO: Namaste ji, main Sitara hoon. Purani job par wapas jaane ka sawal hai, to pehle yeh batayiye, kya aapne job kuch samay pehle chhodi thi?
- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Future
  - ASTRO: Ji, main aapka future dekh sakti hoon. Sabse pehle batayiye, aap kis baat ko lekar zyada soch rahi hain, kaam, shaadi, ya paise ki?

### questions_answered_rate = 0.79 (target >= 0.90)
Prompt lever: Answer-first instruction; handling of second / off-topic questions

- S1 / passive_follower / session_1
  - USER: Purani job par vapas bulaya jayega?
  - ASTRO: Namaste ji, main Sitara hoon. Purani job par wapas jaane ka sawal hai, to pehle yeh batayiye, kya aapne job kuch samay pehle chhodi thi?
- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Future
  - ASTRO: Ji, main aapka future dekh sakti hoon. Sabse pehle batayiye, aap kis baat ko lekar zyada soch rahi hain, kaam, shaadi, ya paise ki?

### refusals = 0.40 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Exact date bataiye tension kab khatam hogi
  - ASTRO: Ji, ghar ki tension ke liye sabse saaf samay Mar 2027 ke aas-paas ka hai. Mangal ki wajah se jhagde Mar 2027 se Sep 2028 ke beech dheere-dheere shant honge. Pakka exact din nahi bata sakti, par daur saaf dikhta hai.
- S2 / direct_answer_chaser_same_day / session_2
  - USER: Aap exact date kyu nahi bata pa rahe?
  - ASTRO: Ji, exact din ka hisaab kundli se nahi nikalti, isliye main sirf mahina aur samay bata sakti hoon. Feb 2027 ke aaspaas ghar ka bojh kam hota dikhta hai. Kya mummy ki baat par aapka mann sabse zyada bhari rehta hai?

### user_frustrated = 1.23 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: IT field. Selection hoga ya nahi? Jo mai puchh rha wo bta ni rhe.
  - ASTRO: Next week ke interview ka seedha jawab abhi pakka nahi bata sakti, par aapki padhai aur skill wali mehnat kaam aa sakti hai. Interview se pehle Budh ko majboot karne ke liye, roz "Om Budhaya Namah" ka jaap kijiye. Us interview mein aap ka kaam kis field ka hai?
- S1 / direct_answer_chaser / session_1
  - USER: Aap jo batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: Seedha jawab: IT interview mein selection ki sambhavna madhyam hai, pakka nahi kah sakti. Aapka Budh, jo baat-cheet aur buddhi ka grah hai, aapke favour mein dikhta hai. Interview se pehle aur baad mein Budh ka mantra jaari rakhiye.
