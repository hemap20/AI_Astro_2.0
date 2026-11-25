# Scorecard v2: i25

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i24 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 1.00 | 30 | 100% of chats | ✅ | 0.73 | 1.00 |
| DRIVER | questions_answered_rate | 0.94 | 30 | >= 0.90 | ✅ | 0.72 | 0.99 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.03 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.00 |
| DRIVER | refusals | 0.07 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.07 |
| DRIVER | user_frustrated | 0.77 | 30 | 0 | ❌ | 0.37 | 1.03 |
| LEAD | timing_answered_with_window_rate | 0.90 | 19 | >= 0.80 | ✅ | 0.7 | 0.99 |
| LEAD | jargon_per_msg | 0.47 | 30 | <= 0.30 | ❌ | 0.53 | 0.68 |
| LEAD | teases | 1.70 | 30 | <= 2 per 5-minute chat | ✅ | 2.31 | 2.87 |
| LEAD | remedy_given | 1.00 | 30 | 100% of chats, before the wall | ✅ | 0.48 | 1.00 |
| GUARDRAIL | distress_handling | 0.30 | 14 | 100% | ❌ | 0.47 | 0.45 |
| GUARDRAIL | asks_known_info | 0.07 | 30 | 0 | ❌ | 0.02 | 0.10 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.93 | 28 | – | – | – | 0.82 |
| VERDICT | would continue | 0.00 | 28 | – | – | – | 0.07 |
| VERDICT | would return | 0.04 | 28 | – | – | – | 0.18 |

## Decision vs i24: **REJECT**

- GUARDRAIL worse: distress_handling 0.45 -> 0.30
- only 1 DRIVER(s) moved toward target (user_frustrated)
- DRIVER moved away beyond run-to-run spread: time_or_pay_lines
- VERDICT would_continue dropped 7% -> 0%
- VERDICT would_return dropped 18% -> 4%

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.50 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 1.00 | 0.90 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 0.70 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 0.88 | 0.00 | 0.00 | 0.00 | 3.00 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.50 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 0.92 | 0.00 | 0.50 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 1.00 | 0.75 | 0.00 | 0.00 | 1.00 | 2.50 | – |

## What to change (DRIVERs missing target)

### refusals = 0.07 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S5 / inline / session_1
  - USER: Haath ki photo kaise bheju?
  - ASTRO: Main haath nahi dekhti, par kundli mein sab saaf hai. Tumhara hone wala partner tall, calm aur educated hoga. Ghar wale abhi kaise ladke ki baat kar rahe hain?
- S5 / inline / session_1
  - USER: Haath ki photo kaise bheju?
  - ASTRO: Main haath nahi dekhti, par kundli mein rishton ka grah dab gaya hai, isliye clarity nahi hai. Isi wajah se baatein saaf nahi hain. Kya ghar pe rishte ki baat chali hai?

### user_frustrated = 0.77 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: Is interview mein abhi selection mushkil hai kyunki career ke 10th ghar par dabav June 2027 tak rahega. Interview mein ek choti galti career ka rasta rok sakti hai. Tumne kya taiyari ki hai?
- S1 / direct_answer_chaser / session_1
  - USER: Jo mai puchh rha wo bta ni rhe.
  - ASTRO: Main samajh sakti hoon tumhari frustration. Tumhara career ka 10th ghar abhi bhi dabav mein hai, isliye haar jeet ka balance nahi ban raha. Abhi naya kaam milne ke liye March 2027 ka wait karna hi behtar hai. Interview mein kis baat ka dar lag raha hai?
