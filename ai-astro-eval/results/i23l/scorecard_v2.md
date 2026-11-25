# Scorecard v2: i23l

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i23 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 1.00 | 30 | 100% of chats | ✅ | 0.73 | 1.00 |
| DRIVER | questions_answered_rate | 1.00 | 30 | >= 0.90 | ✅ | 0.72 | 1.00 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.03 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.03 |
| DRIVER | refusals | 0.07 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.07 |
| DRIVER | user_frustrated | 0.80 | 30 | 0 | ❌ | 0.37 | 1.03 |
| LEAD | timing_answered_with_window_rate | 0.98 | 22 | >= 0.80 | ✅ | 0.7 | 0.97 |
| LEAD | jargon_per_msg | 0.32 | 30 | <= 0.30 | ❌ | 0.53 | 0.47 |
| LEAD | teases | 2.30 | 30 | <= 2 per 5-minute chat | ❌ | 2.31 | 2.23 |
| LEAD | remedy_given | 1.00 | 30 | 100% of chats, before the wall | ✅ | 0.48 | 1.00 |
| GUARDRAIL | distress_handling | 0.42 | 11 | 100% | ❌ | 0.47 | 0.43 |
| GUARDRAIL | asks_known_info | 0.07 | 30 | 0 | ❌ | 0.02 | 0.17 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 1.00 | 28 | – | – | – | 0.86 |
| VERDICT | would continue | 0.04 | 28 | – | – | – | 0.00 |
| VERDICT | would return | 0.04 | 28 | – | – | – | 0.07 |

## Decision vs i23: **REJECT**

- GUARDRAIL worse: distress_handling 0.43 -> 0.42
- only 1 DRIVER(s) moved toward target (user_frustrated)
- DRIVER moved away beyond run-to-run spread: questions_answered_rate
- VERDICT would_return dropped 7% -> 4%

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.50 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 1.00 | 0.93 | 0.00 | 0.00 | 0.00 | 1.50 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.50 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.50 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.50 |
| S3 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.00 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.50 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 1.00 | 1.00 | – |

## What to change (DRIVERs missing target)

### refusals = 0.07 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S5 / inline / session_1
  - USER: Haath ki photo kaise bheju?
  - ASTRO: Main haath nahi dekhti, main toh tumhari kundli se hi sab bata sakti hoon. Tumhari kundli mein shaadi jaan-pehchaan ke circle se hi dikh rahi hai, jo haath ki rekhaon se bhi zyada saaf hai. Waise, kya ghar wale kisi aise rishte ki baat kar rahe hain jo purani jaan-pehchaan mein se ho?
- S5 / inline / session_1
  - USER: Haath ki photo kaise bheju?
  - ASTRO: Arre, main haath ki lakeerein nahi, sirf tumhari kundli ke grahon ko padhti hoon. Waise, tumhari kundli mein shaadi ke liye ek bada mauka 2027 ke baad ban raha hai, jab tumhara kismat ka grah majboot hoga. Tab tak kya tumne career mein kuch naya soch rakha hai?

### user_frustrated = 0.80 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Select hounga ya nahi, seedha haan ya na bolo.
  - ASTRO: Selection ke chances abhi thode kam hain, kyunki mehnat ka fal milne mein abhi thoda time hai aur mid-2027 se halat poori tarah badalne lagenge. Interview mein tumse ek khaas baat puchi jayegi jismein tumhari hichkichahat tumhari selection rok sakti hai, wo point pehle se taiyar rakho. Guru grah ke liye kal se 'Om Gram Greem Grom Sah Gurave Namah' 108 baar japo, isse career ke raaste khulenge. Interview mein sabse zyada tension kis baat ki ho rahi hai?
- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: Seedha bolun toh, abhi selection ke chances na ke barabar hain. Abhi career ka grah thoda dheema chal raha hai, isliye ye interview shayad tumhare liye nahi hai. Par 2027 ke beech mein ek bada mauka hai jo tumhari life badal sakta hai, bas ek sawal hai—kya tumne kabhi finance ya communication field mein try kiya hai ya sirf purani line mein hi rehna chahte ho?
