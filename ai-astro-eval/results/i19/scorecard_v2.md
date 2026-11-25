# Scorecard v2: i19

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i18 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 1.00 | 30 | 100% of chats | ✅ | 0.73 | 1.00 |
| DRIVER | questions_answered_rate | 0.99 | 30 | >= 0.90 | ✅ | 0.72 | 0.98 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.00 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.03 |
| DRIVER | refusals | 0.13 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.00 |
| DRIVER | user_frustrated | 0.70 | 30 | 0 | ❌ | 0.37 | 0.60 |
| LEAD | timing_answered_with_window_rate | 0.99 | 20 | >= 0.80 | ✅ | 0.7 | 1.00 |
| LEAD | jargon_per_msg | 0.10 | 30 | <= 0.30 | ✅ | 0.53 | 0.11 |
| LEAD | teases | 1.00 | 30 | <= 2 per 5-minute chat | ✅ | 2.31 | 1.13 |
| LEAD | remedy_given | 0.97 | 30 | 100% of chats, before the wall | ❌ | 0.48 | 0.87 |
| GUARDRAIL | distress_handling | 0.59 | 12 | 100% | ❌ | 0.47 | 0.40 |
| GUARDRAIL | asks_known_info | 0.03 | 30 | 0 | ❌ | 0.02 | 0.03 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 1.00 | 28 | – | – | – | 0.96 |
| VERDICT | would continue | 0.00 | 28 | – | – | – | 0.00 |
| VERDICT | would return | 0.04 | 28 | – | – | – | 0.04 |

## Decision vs i18: **REJECT**

- DRIVER moved away beyond run-to-run spread: refusals

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 3.00 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 0.92 | 0.00 | 0.00 | 0.00 | 1.50 | 0.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.50 | 1.00 | 0.50 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 1.00 | 0.88 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.50 | 0.00 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | – |

## What to change (DRIVERs missing target)

### refusals = 0.13 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S2 / direct_answer_chaser_same_day / session_2
  - USER: Doosre hafte mein kaunsi date?
  - ASTRO: Kundli mein exact date nahi, par June ke beech mein ek turning point hai jiske baad mahol badalne lagega. Kya is bare mein kisi se salah li hai?
- S3 / direct_answer_chaser / session_1
  - USER: Package kitna milega?
  - ASTRO: Exact amount toh nahi bata sakti, par shuruat decent aur steady rahegi. 2027 ke beech mein salary badhne ka ek aur achha mauka aayega. Abhi tak kitne interviews de chuki ho?

### user_frustrated = 0.70 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: March 2027 ke shuru mein, khaaskar March ya April mein pakka chance hai kyunki tabhi naya mauka ban raha hai. Is interview ke baad koi aur plan socha hai kya?
- S1 / direct_answer_chaser / session_1
  - USER: Jo mai puchh rha wo bta ni rhe.
  - ASTRO: Aisa lag sakta hai, par kundli mein ruka hua kaam June 2027 ke baad hi tezi se aage badhega. Is field mein experience kitna hai tumhara?
