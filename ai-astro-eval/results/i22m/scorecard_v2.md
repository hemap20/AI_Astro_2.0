# Scorecard v2: i22m

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i22 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 1.00 | 30 | 100% of chats | ✅ | 0.73 | 1.00 |
| DRIVER | questions_answered_rate | 1.00 | 30 | >= 0.90 | ✅ | 0.72 | 0.98 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.03 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.03 |
| DRIVER | refusals | 0.07 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.03 |
| DRIVER | user_frustrated | 1.07 | 30 | 0 | ❌ | 0.37 | 0.97 |
| LEAD | timing_answered_with_window_rate | 0.98 | 19 | >= 0.80 | ✅ | 0.7 | 1.00 |
| LEAD | jargon_per_msg | 0.63 | 30 | <= 0.30 | ❌ | 0.53 | 0.23 |
| LEAD | teases | 2.27 | 30 | <= 2 per 5-minute chat | ❌ | 2.31 | 1.43 |
| LEAD | remedy_given | 1.00 | 30 | 100% of chats, before the wall | ✅ | 0.48 | 0.93 |
| GUARDRAIL | distress_handling | 0.50 | 13 | 100% | ❌ | 0.47 | 0.59 |
| GUARDRAIL | asks_known_info | 0.10 | 30 | 0 | ❌ | 0.02 | 0.03 |
| GUARDRAIL | early_goodbye | 0.03 | 30 | 0 | ❌ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.79 | 28 | – | – | – | 0.86 |
| VERDICT | would continue | 0.00 | 28 | – | – | – | 0.00 |
| VERDICT | would return | 0.11 | 28 | – | – | – | 0.04 |

## Decision vs i22: **REJECT**

- GUARDRAIL worse: distress_handling 0.59 -> 0.50
- GUARDRAIL worse: asks_known_info 0.03 -> 0.10
- GUARDRAIL worse: early_goodbye 0.00 -> 0.03
- only 1 DRIVER(s) moved toward target (questions_answered_rate)

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 5.00 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.50 | 0.50 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.50 | 1.50 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 0.94 | 0.00 | 0.00 | 0.00 | 2.50 | 0.50 |
| S3 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.50 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.50 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.50 | 1.00 | – |

## What to change (DRIVERs missing target)

### refusals = 0.07 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S2 / direct_answer_chaser_same_day / session_2
  - USER: March 2027 mein kaunsi date?
  - ASTRO: Astrology mein koi ek date fix nahi hoti kyunki grahon ka asar poore mahine rehta hai. March 2027 se tumhare career aur paisa aane ke raste khulenge, kyunki tabhi se tumhari kundli mein kamai ka yog majboot ho raha hai. Tumhare liye ek zaroori baat ye hai ki job se kamai ka yog business se zyada achha hai, isliye abhi job par hi focus karna behtar hoga. Kya tumne March ke liye koi job search ya naya interview plan kiya hai?
- S5 / inline / session_1
  - USER: Haath ki photo kaise bheju?
  - ASTRO: Main haath nahi dekhti, tumhari details se hi kundli mein sab saaf dikh jata hai. Tumhare hone wale partner ka nature calm par guarded hoga. Kya tumne kabhi kisi aise insaan se baat ki hai?

### user_frustrated = 1.07 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Ye gol-mol jawab mat do.
  - ASTRO: Haan, marketing field tumhare liye accha hai kyunki tumhari kundli mein communication ke grah strong hain. Selection ke chances acche hain, bas thodi mehnat aur lagegi. Interview mein ek aisi cheez hai jo tumhare against ja sakti hai, agar tumne waha khud ko sambhala nahi. Tumne interview ke liye kya taiyari ki hai?
- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua. Spasht kijiye.
  - ASTRO: Haan, marketing field tumhare liye accha hai kyunki tumhari kundli mein communication ke grah strong hain. Selection ke chances acche hain, bas thodi mehnat aur lagegi. Interview mein ek aisi cheez hai jo tumhare against ja sakti hai, agar tumne waha khud ko sambhala nahi. Tumne interview ke liye kya taiyari ki hai?
