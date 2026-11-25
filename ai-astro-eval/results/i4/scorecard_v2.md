# Scorecard v2: i4

15 sessions from 11 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i3b |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 0.93 | 15 | 100% of chats | ❌ | 0.73 | 1.00 |
| DRIVER | questions_answered_rate | 0.99 | 15 | >= 0.90 | ✅ | 0.72 | 0.96 |
| DRIVER | time_or_pay_before_answer | 0.00 | 15 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.00 | 15 | <= 1, and only after the main answer | ✅ | 0.57 | 0.40 |
| DRIVER | refusals | 0.00 | 15 | 0 (redirect with value instead) | ✅ | 0.12 | 0.33 |
| DRIVER | user_frustrated | 0.80 | 15 | 0 | ❌ | 0.37 | 0.73 |
| LEAD | timing_answered_with_window_rate | 1.00 | 10 | >= 0.80 | ✅ | 0.7 | 1.00 |
| LEAD | jargon_per_msg | 0.67 | 15 | <= 0.30 | ❌ | 0.53 | 0.66 |
| LEAD | teases | 0.40 | 15 | <= 2 per 5-minute chat | ✅ | 2.31 | 0.40 |
| LEAD | remedy_given | 0.33 | 15 | 100% of chats, before the wall | ❌ | 0.48 | 0.33 |
| GUARDRAIL | distress_handling | 0.28 | 5 | 100% | ❌ | 0.47 | 0.28 |
| GUARDRAIL | asks_known_info | 0.13 | 15 | 0 | ❌ | 0.02 | 0.00 |
| GUARDRAIL | early_goodbye | 0.00 | 15 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.93 | 14 | – | – | – | 0.82 |
| VERDICT | would continue | 0.07 | 14 | – | – | – | 0.00 |
| VERDICT | would return | 0.21 | 14 | – | – | – | 0.00 |

## Decision vs i3b: **REJECT**

- GUARDRAIL worse: asks_known_info 0.00 -> 0.13
- DRIVER moved away beyond run-to-run spread: first_q_answered

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S1 | session_1 | passive_follower | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 3.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| S2 | session_1 | passive_follower_genuine_return | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 1 | 0.00 | 0.80 | 0.00 | 0.00 | 0.00 | 3.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| S2 | session_2 | passive_follower_genuine_return | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S3 | session_1 | passive_follower | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.00 | 0.00 |
| S4 | session_1 | passive_follower | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.00 | – |

## What to change (DRIVERs missing target)

### first_q_answered = 0.93 (target 100% of chats)
Prompt lever: Answer-first instruction; drip-feed / Zeigarnik instruction (withholding the answer)

- S2 / direct_answer_chaser_genuine_return / session_2
  - USER: Rahat matlab exactly kya?
  - ASTRO: Shaadi March 2027 aur September 2028 ke beech hogi ji. Shani antardasha aane se saari rukawatein door ho jayengi.

### user_frustrated = 0.80 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / passive_follower / session_1
  - USER: Etna late
  - ASTRO: Purani job par wapas aane ka yog thoda kam hai ji. Lekin March 2027 ke baad naye mauke zaroor milenge. Guru ki kripa se naya rasta khulega.
- S1 / passive_follower / session_1
  - USER: vesa hota nahi
  - ASTRO: Sach hai ji, Shani ki chal aisi hi hai. March 2027 mein Shani AD aate hi badlav ayega.
