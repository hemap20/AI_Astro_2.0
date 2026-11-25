# Scorecard v2: i13

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i12 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 0.93 | 30 | 100% of chats | ❌ | 0.73 | 0.93 |
| DRIVER | questions_answered_rate | 0.96 | 30 | >= 0.90 | ✅ | 0.72 | 0.96 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.03 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.03 |
| DRIVER | refusals | 0.03 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.07 |
| DRIVER | user_frustrated | 0.93 | 30 | 0 | ❌ | 0.37 | 0.67 |
| LEAD | timing_answered_with_window_rate | 0.97 | 20 | >= 0.80 | ✅ | 0.7 | 1.00 |
| LEAD | jargon_per_msg | 0.43 | 30 | <= 0.30 | ❌ | 0.53 | 0.42 |
| LEAD | teases | 0.03 | 30 | <= 2 per 5-minute chat | ✅ | 2.31 | 0.13 |
| LEAD | remedy_given | 0.93 | 30 | 100% of chats, before the wall | ❌ | 0.48 | 0.87 |
| GUARDRAIL | distress_handling | 0.77 | 11 | 100% | ❌ | 0.47 | 0.92 |
| GUARDRAIL | asks_known_info | 0.10 | 30 | 0 | ❌ | 0.02 | 0.00 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.86 | 28 | – | – | – | 0.89 |
| VERDICT | would continue | 0.00 | 28 | – | – | – | 0.00 |
| VERDICT | would return | 0.04 | 28 | – | – | – | 0.07 |

## Decision vs i12: **REJECT**

- GUARDRAIL worse: distress_handling 0.92 -> 0.77
- GUARDRAIL worse: asks_known_info 0.00 -> 0.10
- only 1 DRIVER(s) moved toward target (refusals)
- VERDICT would_return dropped 7% -> 4%

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 3.50 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.50 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 0.80 | 0.00 | 0.00 | 0.00 | 0.50 | 0.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.00 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 0.75 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 0.00 | 0.84 | 0.00 | 0.00 | 0.50 | 1.50 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 3.00 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.50 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | – |

## What to change (DRIVERs missing target)

### first_q_answered = 0.93 (target 100% of chats)
Prompt lever: Answer-first instruction; drip-feed / Zeigarnik instruction (withholding the answer)

- S3 / direct_answer_chaser / session_1
  - USER: Mujhe janna hai meri future. Career aur paisa kaisa rahega?
  - ASTRO: Career aur paise ki fikar mat karo ji, waqt badlega. Aap abhi kahin kaam kar rahe hain ya naya try kar rahe hain?
- S3 / direct_answer_chaser / session_1
  - USER: Mujhe janna hai meri future. Career aur paise ko le k kaisa rahega ye saal?
  - ASTRO: Career aur paise ki baat hai ji, yeh sawal zaroori hai. Aap abhi kahin job kar rahe hain ya naya try kar rahe hain?

### refusals = 0.03 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S3 / direct_answer_chaser / session_1
  - USER: Exact date btao.
  - ASTRO: Exact din toh kundli mein nahi hota ji, par March 2027 ke pehle hafte mein sabse strong yog ban raha hai. Ussi samay nayi shuruwat ka rasta khulega.

### user_frustrated = 0.93 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua tha.
  - ASTRO: Haan ji, purani job milne ke poore chances hain. Kaam ke sthaan ka bal achha hone se wahan baat banegi. Wahan profile wahi purani rahegi ya kuch naya milega?
- S1 / direct_answer_chaser / session_1
  - USER: Selection hoga ya nahi, ye batao? Haan ya na mein.
  - ASTRO: Selection ka accha chance hai ji, bilkul pareshan mat ho. Do saal ka tajurba kaam aayega. Interview ki taiyari puri hai kya?
