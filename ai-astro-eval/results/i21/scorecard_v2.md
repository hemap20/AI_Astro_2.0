# Scorecard v2: i21

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i20 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 0.97 | 30 | 100% of chats | ❌ | 0.73 | 0.97 |
| DRIVER | questions_answered_rate | 0.97 | 30 | >= 0.90 | ✅ | 0.72 | 0.97 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.03 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.03 |
| DRIVER | refusals | 0.00 | 30 | 0 (redirect with value instead) | ✅ | 0.12 | 0.07 |
| DRIVER | user_frustrated | 1.03 | 30 | 0 | ❌ | 0.37 | 0.83 |
| LEAD | timing_answered_with_window_rate | 0.98 | 17 | >= 0.80 | ✅ | 0.7 | 1.00 |
| LEAD | jargon_per_msg | 0.15 | 30 | <= 0.30 | ✅ | 0.53 | 0.17 |
| LEAD | teases | 1.10 | 30 | <= 2 per 5-minute chat | ✅ | 2.31 | 1.43 |
| LEAD | remedy_given | 0.83 | 30 | 100% of chats, before the wall | ❌ | 0.48 | 0.90 |
| GUARDRAIL | distress_handling | 0.34 | 15 | 100% | ❌ | 0.47 | 0.41 |
| GUARDRAIL | asks_known_info | 0.07 | 30 | 0 | ❌ | 0.02 | 0.07 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 1.00 | 28 | – | – | – | 1.00 |
| VERDICT | would continue | 0.04 | 28 | – | – | – | 0.04 |
| VERDICT | would return | 0.04 | 28 | – | – | – | 0.14 |

## Decision vs i20: **REJECT**

- GUARDRAIL worse: distress_handling 0.41 -> 0.34
- only 1 DRIVER(s) moved toward target (refusals)
- VERDICT would_return dropped 14% -> 4%

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 0.50 | 0.90 | 0.00 | 0.00 | 0.00 | 2.50 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 1.00 | 0.88 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 1.00 | 0.88 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 0.92 | 0.00 | 0.00 | 0.00 | 2.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 4.00 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.50 | 0.00 | 1.50 | 0.00 |
| S5 | session_1 | inline | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.50 | – |

## What to change (DRIVERs missing target)

### first_q_answered = 0.97 (target 100% of chats)
Prompt lever: Answer-first instruction; drip-feed / Zeigarnik instruction (withholding the answer)

- S1 / direct_answer_chaser / session_1
  - USER: Purani job par vapas bulaya jayega?
  - ASTRO: Purani job chhoote hue kitna time ho gaya, aur wahan wapas jaane ki koi baat chal rahi hai kya?

### user_frustrated = 1.03 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: Na, agle hafte selection ka chance kam hai kyunki June tak thoda delay chal raha hai. Interview mein ek specific cheez par dhyan dena, warna baat ruk sakti hai. Ghar mein kis kis ko pata hai?
- S1 / direct_answer_chaser / session_1
  - USER: Seedha bolo, hoga ya nahi?
  - ASTRO: Main samajhti hoon, kabhi-kabhi timing thoda aage-peeche ho jaati hai kyunki abhi career wali jagah par thoda dabav chal raha hai. June ke baad halat tezi se badlenge. Kya tumne kisi aur jagah bhi apply kiya hai?
