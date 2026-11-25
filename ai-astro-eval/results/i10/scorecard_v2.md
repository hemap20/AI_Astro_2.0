# Scorecard v2: i10

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i9 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 1.00 | 30 | 100% of chats | ✅ | 0.73 | 1.00 |
| DRIVER | questions_answered_rate | 1.00 | 30 | >= 0.90 | ✅ | 0.72 | 0.97 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.03 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.00 |
| DRIVER | refusals | 0.07 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.60 |
| DRIVER | user_frustrated | 0.87 | 30 | 0 | ❌ | 0.37 | 1.17 |
| LEAD | timing_answered_with_window_rate | 1.00 | 24 | >= 0.80 | ✅ | 0.7 | 0.99 |
| LEAD | jargon_per_msg | 0.53 | 30 | <= 0.30 | ❌ | 0.53 | 0.63 |
| LEAD | teases | 0.27 | 30 | <= 2 per 5-minute chat | ✅ | 2.31 | 0.40 |
| LEAD | remedy_given | 0.90 | 30 | 100% of chats, before the wall | ❌ | 0.48 | 0.87 |
| GUARDRAIL | distress_handling | 0.91 | 8 | 100% | ❌ | 0.47 | 0.91 |
| GUARDRAIL | asks_known_info | 0.03 | 30 | 0 | ❌ | 0.02 | 0.00 |
| GUARDRAIL | early_goodbye | 0.03 | 30 | 0 | ❌ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.96 | 28 | – | – | – | 0.82 |
| VERDICT | would continue | 0.00 | 28 | – | – | – | 0.04 |
| VERDICT | would return | 0.07 | 28 | – | – | – | 0.07 |

## Decision vs i9: **REJECT**

- GUARDRAIL worse: asks_known_info 0.00 -> 0.03
- GUARDRAIL worse: early_goodbye 0.00 -> 0.03
- DRIVER moved away beyond run-to-run spread: time_or_pay_lines
- VERDICT would_continue dropped 4% -> 0%

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.50 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 1.00 | 1.50 | 0.50 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.50 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.50 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.50 | – |

## What to change (DRIVERs missing target)

### refusals = 0.07 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S2 / direct_answer_chaser_genuine_return / session_2
  - USER: Jo mai puchh rha wo bta ni rhe. Exact date btao.
  - ASTRO: Pareshani samajh sakti hoon ji, par taare exact calendar ki tareek nahi, samay ka bada daaur batate hain. March 2027 ke pehle hafte ka wo samay hai jab nayi shuruaat pakki hai ji.
- S2 / direct_answer_chaser_genuine_return / session_2
  - USER: Faltu. Aap exact date bta ni pa rhe ho.
  - ASTRO: Sahi keh rahe hain aap ji, taaron ki chaal se exact din nahi, bas mahina hi pata chalta hai. Banking ke field mein Guru ka prabhav hi us samay aapko nayi shuruaat dega ji. October 2028 ke baad isi line mein bade labh ka yog bhi banega ji.

### user_frustrated = 0.87 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: March 2027 ka pehla hafta hi sabse pakka lag raha hai ji, kyunki tabhi naye grah ka prabhav shuru hota hai. Career ke grah apni sthiti badal kar aapka rasta saaf karenge ji. Isi dauran 2027 se 2028 ke beech videsh jane ka yog bhi khul sakta hai ji.
- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: Agle hafte selection ke chances thode kam hi lag rahe hain ji, kyunki abhi samay thoda intezaar karne wala hai. Career ke sthaan par chal dheemi hone ki wajah se baat final hone mein thoda waqt lagega. March ke baad finance aur debt sudharne ka yog bhi shuru ho raha hai ji.
