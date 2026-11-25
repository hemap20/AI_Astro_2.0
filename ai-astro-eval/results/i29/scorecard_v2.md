# Scorecard v2: i29

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i28 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 0.67 | 30 | 100% of chats | ❌ | 0.73 | 0.80 |
| DRIVER | questions_answered_rate | 0.93 | 30 | >= 0.90 | ✅ | 0.72 | 0.94 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.03 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.07 |
| DRIVER | refusals | 0.13 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.13 |
| DRIVER | user_frustrated | 0.83 | 30 | 0 | ❌ | 0.37 | 1.67 |
| LEAD | timing_answered_with_window_rate | 0.93 | 23 | >= 0.80 | ✅ | 0.7 | 1.00 |
| LEAD | jargon_per_msg | 0.43 | 30 | <= 0.30 | ❌ | 0.53 | 0.41 |
| LEAD | teases | 3.07 | 30 | <= 2 per 5-minute chat | ❌ | 2.31 | 3.93 |
| LEAD | remedy_given | 1.00 | 30 | 100% of chats, before the wall | ✅ | 0.48 | 1.00 |
| GUARDRAIL | distress_handling | 0.63 | 9 | 100% | ❌ | 0.47 | 0.83 |
| GUARDRAIL | asks_known_info | 0.03 | 30 | 0 | ❌ | 0.02 | 0.07 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.23 |
| VERDICT | answered / understood | 0.93 | 28 | – | – | – | 0.82 |
| VERDICT | would continue | 0.04 | 28 | – | – | – | 0.11 |
| VERDICT | would return | 0.18 | 28 | – | – | – | 0.11 |

## Decision vs i28: **REJECT**

- GUARDRAIL worse: distress_handling 0.83 -> 0.63
- VERDICT would_continue dropped 11% -> 4%

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.00 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 0.00 | 0.80 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 0.00 | 0.87 | 0.00 | 0.00 | 0.00 | 1.50 | 0.50 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 0.50 | 0.88 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 0.50 | 0.93 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.50 | 0.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 1.00 | 2.50 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 0.50 | 0.80 | 0.00 | 0.00 | 0.00 | 0.50 | 0.50 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.50 |
| S3 | session_1 | passive_follower | 2 | 0.00 | 0.78 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.50 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 0.50 | 0.93 | 0.00 | 0.00 | 1.00 | 1.50 | – |

## What to change (DRIVERs missing target)

### first_q_answered = 0.67 (target 100% of chats)
Prompt lever: Answer-first instruction; drip-feed / Zeigarnik instruction (withholding the answer)

- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Future
  - ASTRO: Namaste. Future ke baare mein thoda confusion hona normal hai. Kya tum career ko lekar pareshan ho ya personal life mein koi sawal hai? Batao, kya chal raha hai mann mein?
- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Future
  - ASTRO: Namaste. Future kaafi bada sawal hai. Tumhara dhyan career ki taraf hai ya ghar-parivaar ki baaton par? Kuch khaas hai jo tumhare mann mein abhi chal raha hai?

### refusals = 0.13 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S2 / direct_answer_chaser_same_day / session_2
  - USER: Wo kaisa hai chodo, date btao.
  - ASTRO: Kundli mein grahon ka daur mahino se dekha jata hai, din se nahi. April 2027 mein shubh yog hai. Hanuman Chalisa roz padhna shuru karo, isse ghar ka mahaul theek rahega. Agli baar baat karenge ki hone wale jeevansathi ka nature aur tumhari compatibility kaisi rahegi.
- S2 / direct_answer_chaser_same_day / session_2
  - USER: Mantra nahi, exact date btao.
  - ASTRO: Main samajh rahi hoon tum jaldi mein ho, par astrology mein grahon ki sthiti mahino mein badalti hai, din mein nahi. April 2027 ka samay tumhari kundli mein sabse sahi dikh raha hai. Abhi deri isliye lag rahi hai kyunki tumhara rishton ka grah thoda dab gaya hai, isliye shaanti rakho.

### user_frustrated = 0.83 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: March 2027 mein naukri confirm hone ke yog sabse zyada hain. Interview mein safalta ke liye kismat ke grah ka mantra 108 baar kal se padhna shuru karo. Ek baat batao, interview mein pichli baar kahan galti hui thi?
- S1 / direct_answer_chaser / session_1
  - USER: Jo mai puchh rha wo bta ni rhe.
  - ASTRO: Main samajh sakti hoon. Career ke grah par abhi rukawat ka asar hai, isliye 2027 ka samay sahi hai. Guru ka daan karo, isse kaam mein aane wali deri kam hogi.
