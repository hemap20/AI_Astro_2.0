# Scorecard v2: i32

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i31 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 0.73 | 30 | 100% of chats | ❌ | 0.73 | 0.67 |
| DRIVER | questions_answered_rate | 0.92 | 30 | >= 0.90 | ✅ | 0.72 | 0.87 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.00 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.03 |
| DRIVER | refusals | 0.07 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.20 |
| DRIVER | user_frustrated | 1.20 | 30 | 0 | ❌ | 0.37 | 1.17 |
| LEAD | timing_answered_with_window_rate | 0.99 | 19 | >= 0.80 | ✅ | 0.7 | 0.93 |
| LEAD | jargon_per_msg | 0.37 | 30 | <= 0.30 | ❌ | 0.53 | 0.43 |
| LEAD | teases | 2.87 | 30 | <= 2 per 5-minute chat | ❌ | 2.31 | 1.10 |
| LEAD | remedy_given | 0.83 | 30 | 100% of chats, before the wall | ❌ | 0.48 | 0.87 |
| GUARDRAIL | distress_handling | 0.38 | 10 | 100% | ❌ | 0.47 | 0.44 |
| GUARDRAIL | asks_known_info | 0.07 | 30 | 0 | ❌ | 0.02 | 0.03 |
| GUARDRAIL | early_goodbye | 0.03 | 30 | 0 | ❌ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.89 | 28 | – | – | – | 0.93 |
| VERDICT | would continue | 0.04 | 28 | – | – | – | 0.07 |
| VERDICT | would return | 0.07 | 28 | – | – | – | 0.11 |

## Decision vs i31: **REJECT**

- GUARDRAIL worse: distress_handling 0.44 -> 0.38
- GUARDRAIL worse: asks_known_info 0.03 -> 0.07
- GUARDRAIL worse: early_goodbye 0.00 -> 0.03
- VERDICT would_continue dropped 7% -> 4%
- VERDICT would_return dropped 11% -> 7%

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 0.50 | 0.50 | 0.00 | 0.00 | 0.00 | 3.50 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 0.50 | 0.94 | 0.00 | 0.00 | 0.00 | 1.50 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 0.00 | 0.86 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 0.50 | 0.88 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 0.00 | 0.78 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.00 | 0.50 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 3.50 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.50 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 0.50 | 0.83 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.50 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 1.00 | 1.50 | – |

## What to change (DRIVERs missing target)

### first_q_answered = 0.73 (target 100% of chats)
Prompt lever: Answer-first instruction; drip-feed / Zeigarnik instruction (withholding the answer)

- S1 / direct_answer_chaser / session_1
  - USER: Purani job par vapas bulaya jayega?
  - ASTRO: Nayi jagah aur behtar mauke aapka intezar kar rahe hain. 2023 se 2025 tak aapne career mein kafi mehnat ki thi, hai na? 2027 se career mein bade badlav dikh rahe hain.
- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Future
  - ASTRO: Namaste. Main aapki kundli dekh kar sab bata sakti hoon. Aap khaas taur par kya jaanna chahte hain, career ke baare mein ya shaadi ke baare mein?

### refusals = 0.07 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S5 / inline / session_1
  - USER: Haath ki photo kaise bheju?
  - ASTRO: Main haath nahi dekhti, par aapki kundli se sab saaf bata sakti hoon. Rishton ka grah thoda dab gaya hai, isliye clarity ki kami lag rahi hai. Aapne bataya rishte ki baat chal rahi hai, kya ghar wale kisi khaas rishte ki charcha kar rahe hain?
- S5 / inline / session_1
  - USER: Haath ki photo kaise bheju?
  - ASTRO: Main haath nahi, aapki janm kundli se bhavishya dekh sakti hoon. Rishton ke grah ki sthiti se vivah ka yog pakka hai, par ek khas tarah ka jeevansathi aapke liye aa raha hai. Aap abhi kisi rishte ki ummeed mein hain ya ghar wale rishta dekh rahe hain?

### user_frustrated = 1.20 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: March 2027 ke pehle hafte mein yog strong hain. Career aur paise ki dikkat, dono 10th ghar se judi hain. Ek bada mauka aane wala hai, par rukawat hatana zaroori hai.
- S1 / direct_answer_chaser / session_1
  - USER: Jo mai puchh rha wo bta ni rhe.
  - ASTRO: Main samajh sakti hoon, kabhi kabhi grahon ka asar umeed se dheema ho jata hai. Aapki naukri aur neend ki dikkat, dono 8th ghar ke dabav se ruke hain. Jun 2027 ke baad halat badlenge, tab tak koi badi ummeed aane wali hai. Abhi seene ya pet mein koi pareshani toh nahi rehti?
