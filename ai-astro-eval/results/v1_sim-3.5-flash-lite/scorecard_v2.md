# Scorecard v2: v1

15 sessions from 11 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara |
|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 0.67 | 15 | 100% of chats | ❌ | 0.73 |
| DRIVER | questions_answered_rate | 0.87 | 15 | >= 0.90 | ❌ | 0.72 |
| DRIVER | time_or_pay_before_answer | 0.00 | 15 | 0% of chats | ✅ | 0.13 |
| DRIVER | time_or_pay_lines | 0.00 | 15 | <= 1, and only after the main answer | ✅ | 0.57 |
| DRIVER | refusals | 0.40 | 15 | 0 (redirect with value instead) | ❌ | 0.12 |
| DRIVER | user_frustrated | 0.87 | 15 | 0 | ❌ | 0.37 |
| LEAD | timing_answered_with_window_rate | 0.75 | 11 | >= 0.80 | ❌ | 0.7 |
| LEAD | jargon_per_msg | 0.88 | 15 | <= 0.30 | ❌ | 0.53 |
| LEAD | teases | 1.67 | 15 | <= 2 per 5-minute chat | ✅ | 2.31 |
| LEAD | remedy_given | 0.33 | 15 | 100% of chats, before the wall | ❌ | 0.48 |
| GUARDRAIL | distress_handling | 0.50 | 2 | 100% | ❌ | 0.47 |
| GUARDRAIL | asks_known_info | 0.00 | 15 | 0 | ✅ | 0.02 |
| GUARDRAIL | early_goodbye | 0.00 | 15 | 0 | ✅ | 0.02 |
| VERDICT | answered / understood | 0.50 | 14 | – | – | – |
| VERDICT | would continue | 0.21 | 14 | – | – | – |
| VERDICT | would return | 0.21 | 14 | – | – | – |

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 1.00 | 2.00 | 0.00 |
| S1 | session_1 | passive_follower | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 1 | 0.00 | 0.67 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 1 | 0.00 | 0.40 | 0.00 | 0.00 | 1.00 | 2.00 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 1 | 0.00 | 0.75 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 3.00 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| S2 | session_2 | passive_follower_same_day | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 1 | 0.00 | 0.83 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| S3 | session_1 | passive_follower | 1 | 0.00 | 0.80 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 1 | 1.00 | 0.67 | 0.00 | 0.00 | 2.00 | 2.00 | 0.00 |
| S4 | session_1 | passive_follower | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 1 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | – |

## What to change (DRIVERs missing target)

### first_q_answered = 0.67 (target 100% of chats)
Prompt lever: Answer-first instruction; drip-feed / Zeigarnik instruction (withholding the answer)

- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Future
  - ASTRO: Namaste ji! Future ke baare mein dekhte hain. Aap abhi unmarried hain na?
- S2 / direct_answer_chaser_same_day / session_1
  - USER: Future
  - ASTRO: Namaste ji, aapka swagat hai. Future ke baare mein sab batati hoon. Aap married hain ya unmarried ji?

### questions_answered_rate = 0.87 (target >= 0.90)
Prompt lever: Answer-first instruction; handling of second / off-topic questions

- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Future
  - ASTRO: Namaste ji! Future ke baare mein dekhte hain. Aap abhi unmarried hain na?
- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Konse month me
  - ASTRO: Aapka Rahu-Saturn sub-period chal raha hai ji. Is dauran Shani ka transit strong rahega. Partner kaise milenge, wo bataau?

### refusals = 0.40 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S1 / direct_answer_chaser / session_1
  - USER: Exact month batao
  - ASTRO: Exact month batana mushkil hota hai ji. Mercury aur Saturn ki chal dekho. Agle kuch hafto mein baat ban sakti hai.
- S2 / direct_answer_chaser_same_day / session_1
  - USER: Paisa kab aayega
  - ASTRO: Finance ya investment advice nahi deti ji. Ye mere daayre se baahar hai. Career gains zaroor dekh sakti hoon.

### user_frustrated = 0.87 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi
  - ASTRO: Exact month batana mushkil hota hai ji. Mercury aur Saturn ki chal dekho. Agle kuch hafto mein baat ban sakti hai.
- S1 / direct_answer_chaser / session_1
  - USER: Faltu
  - ASTRO: Spasht bolti hoon ji. Tenth lord Mercury active hai. Purani jagah se call aayegi.
