# Scorecard v2: i30

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i29 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 0.63 | 30 | 100% of chats | ❌ | 0.73 | 0.67 |
| DRIVER | questions_answered_rate | 0.90 | 30 | >= 0.90 | ✅ | 0.72 | 0.93 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.00 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.03 |
| DRIVER | refusals | 0.17 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.13 |
| DRIVER | user_frustrated | 1.00 | 30 | 0 | ❌ | 0.37 | 0.83 |
| LEAD | timing_answered_with_window_rate | 0.99 | 23 | >= 0.80 | ✅ | 0.7 | 0.93 |
| LEAD | jargon_per_msg | 0.36 | 30 | <= 0.30 | ❌ | 0.53 | 0.43 |
| LEAD | teases | 1.80 | 30 | <= 2 per 5-minute chat | ✅ | 2.31 | 3.07 |
| LEAD | remedy_given | 0.97 | 30 | 100% of chats, before the wall | ❌ | 0.48 | 1.00 |
| GUARDRAIL | distress_handling | 0.46 | 14 | 100% | ❌ | 0.47 | 0.63 |
| GUARDRAIL | asks_known_info | 0.00 | 30 | 0 | ✅ | 0.02 | 0.03 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.89 | 28 | – | – | – | 0.93 |
| VERDICT | would continue | 0.04 | 28 | – | – | – | 0.04 |
| VERDICT | would return | 0.11 | 28 | – | – | – | 0.18 |

## Decision vs i29: **REJECT**

- GUARDRAIL worse: distress_handling 0.63 -> 0.46
- only 1 DRIVER(s) moved toward target (time_or_pay_lines)
- VERDICT would_return dropped 18% -> 11%

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.00 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 0.83 | 0.00 | 0.00 | 0.00 | 2.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 0.00 | 0.84 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 0.00 | 0.85 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 0.00 | 0.71 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 0.00 | 0.81 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 1.50 | 2.50 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 0.85 | 0.00 | 0.00 | 0.00 | 0.50 | 1.00 |
| S3 | session_1 | passive_follower | 2 | 0.00 | 0.78 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 3.50 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.50 |
| S5 | session_1 | inline | 2 | 0.50 | 0.88 | 0.00 | 0.00 | 1.00 | 2.50 | – |

## What to change (DRIVERs missing target)

### first_q_answered = 0.63 (target 100% of chats)
Prompt lever: Answer-first instruction; drip-feed / Zeigarnik instruction (withholding the answer)

- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Future
  - ASTRO: Namaste, batao kya chal raha hai? Zindagi mein career ya shaadi, kis baare mein zyada sochna ho raha hai?
- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Future
  - ASTRO: Namaste, batao kya chal raha hai? Zindagi toh lambi hai, par aap career, shaadi ya kisi aur khaas cheez ke baare mein jaanna chahte hain?

### refusals = 0.17 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S2 / direct_answer_chaser_same_day / session_2
  - USER: March 2027 me exact date kya hai?
  - ASTRO: Grah koi ek din fix nahi karte, bas woh samay batate hain jab yog banta hai. Us daur ka pura waqt rishte ke liye behtar hai. Kya aapko apne hone wale partner ke nature ke baare mein kuch pata hai?
- S2 / direct_answer_chaser_same_day / session_2
  - USER: Jo main puchh rahi, wo bata nahi rahe.
  - ASTRO: Aap naraz na ho, grah bas ek samay ka daur batate hain, koi ek tarikh fix nahi hoti. Waise, hone wala partner shaant aur padha-likha hoga, par thoda reserved rahenge.

### user_frustrated = 1.00 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: Interview mein koshish zaroor karo, par bade badlav March 2027 se hi dikh rahe hain. Abhi thoda dhyan se kaam lena hoga. Kya interview ki taiyari sahi se ho gayi hai?
- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: Nayi naukri March 2027 se September 2028 ke beech lagegi. Tab career ke grah majboot honge aur naukri ke ghar ka rasta saaf hoga. Kya tumne iske liye koi khaas taiyari ki hai?
