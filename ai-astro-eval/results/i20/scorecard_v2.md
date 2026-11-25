# Scorecard v2: i20

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i19 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 0.97 | 30 | 100% of chats | ❌ | 0.73 | 1.00 |
| DRIVER | questions_answered_rate | 0.97 | 30 | >= 0.90 | ✅ | 0.72 | 0.99 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.03 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.00 |
| DRIVER | refusals | 0.07 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.13 |
| DRIVER | user_frustrated | 0.83 | 30 | 0 | ❌ | 0.37 | 0.70 |
| LEAD | timing_answered_with_window_rate | 1.00 | 19 | >= 0.80 | ✅ | 0.7 | 0.99 |
| LEAD | jargon_per_msg | 0.17 | 30 | <= 0.30 | ✅ | 0.53 | 0.10 |
| LEAD | teases | 1.43 | 30 | <= 2 per 5-minute chat | ✅ | 2.31 | 1.00 |
| LEAD | remedy_given | 0.90 | 30 | 100% of chats, before the wall | ❌ | 0.48 | 0.97 |
| GUARDRAIL | distress_handling | 0.41 | 13 | 100% | ❌ | 0.47 | 0.59 |
| GUARDRAIL | asks_known_info | 0.07 | 30 | 0 | ❌ | 0.02 | 0.03 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 1.00 | 28 | – | – | – | 1.00 |
| VERDICT | would continue | 0.04 | 28 | – | – | – | 0.00 |
| VERDICT | would return | 0.14 | 28 | – | – | – | 0.04 |

## Decision vs i19: **REJECT**

- GUARDRAIL worse: distress_handling 0.59 -> 0.41
- GUARDRAIL worse: asks_known_info 0.03 -> 0.07
- only 1 DRIVER(s) moved toward target (refusals)
- DRIVER moved away beyond run-to-run spread: first_q_answered
- DRIVER moved away beyond run-to-run spread: time_or_pay_lines

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 3.50 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.50 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.50 | 0.50 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 0.92 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 0.50 | 0.83 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.50 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.50 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 1.00 | 4.00 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 0.88 | 0.00 | 0.50 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | – |

## What to change (DRIVERs missing target)

### first_q_answered = 0.97 (target 100% of chats)
Prompt lever: Answer-first instruction; drip-feed / Zeigarnik instruction (withholding the answer)

- S2 / passive_follower_genuine_return / session_2
  - USER: Pichli baar kuch batane wale the aap?
  - ASTRO: Pichli baar tumne shaadi ki deri aur paise ki tension ke baare mein bataya tha na? Wahi se aage baat karte hain, abhi ghar pe rishte ki baat kahan tak pahuchi hai?

### refusals = 0.07 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S4 / direct_answer_chaser / session_1
  - USER: In-laws ki baat mat karo.
  - ASTRO: Seedhe haan ya na kehna theek nahi, arranged yog hai par Shukra kamzor hai. 2027 aate hi ek aisi sachai samne aayegi jo faisla aasan kar degi. Kya ghar walon ne date pakki kar di hai?
- S4 / direct_answer_chaser / session_1
  - USER: Matlab hoga ya nahi ye rishta? Seedha bolo.
  - ASTRO: Seedha haan nahi bol sakte kyunki Shukra kamzor hai. 2027 shuru hote hi ek aisi baat saamne aayegi jo sab clear kar degi. Kya ghar wale bahut jaldi mein hain?

### user_frustrated = 0.83 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: March ka pehla hafta sabse strong hai, kyuki tabhi career wali jagah par badlav shuru hoga; baki pura saal bhi open hai. Tum waha same profile chahte ho?
- S1 / direct_answer_chaser / session_1
  - USER: Itna late kyun? Jaldi nahi ho sakta?
  - ASTRO: March ka pehla hafta sabse strong hai, kyuki tabhi career wali jagah par badlav shuru hoga; baki pura saal bhi open hai. Tum waha same profile chahte ho?
