# Scorecard v2: i35

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i33 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 0.80 | 30 | 100% of chats | ❌ | 0.73 | 0.73 |
| DRIVER | questions_answered_rate | 0.91 | 30 | >= 0.90 | ✅ | 0.72 | 0.90 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.07 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.00 |
| DRIVER | refusals | 0.27 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.33 |
| DRIVER | user_frustrated | 1.53 | 30 | 0 | ❌ | 0.37 | 1.73 |
| LEAD | timing_answered_with_window_rate | 0.96 | 21 | >= 0.80 | ✅ | 0.7 | 0.97 |
| LEAD | jargon_per_msg | 0.39 | 30 | <= 0.30 | ❌ | 0.53 | 0.35 |
| LEAD | teases | 1.67 | 30 | <= 2 per 5-minute chat | ✅ | 2.31 | 1.77 |
| LEAD | remedy_given | 1.00 | 30 | 100% of chats, before the wall | ✅ | 0.48 | 0.87 |
| GUARDRAIL | distress_handling | 0.45 | 11 | 100% | ❌ | 0.47 | 0.17 |
| GUARDRAIL | asks_known_info | 0.13 | 30 | 0 | ❌ | 0.02 | 0.13 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.71 | 28 | – | – | – | 0.82 |
| VERDICT | would continue | 0.00 | 28 | – | – | – | 0.04 |
| VERDICT | would return | 0.04 | 28 | – | – | – | 0.07 |

## Decision vs i33: **REJECT**

- DRIVER moved away beyond run-to-run spread: time_or_pay_lines
- VERDICT would_continue dropped 4% -> 0%
- VERDICT would_return dropped 7% -> 4%

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 3.00 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 0.00 | 0.74 | 0.00 | 0.00 | 0.00 | 1.50 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 0.50 | 0.78 | 0.00 | 0.00 | 1.50 | 2.00 | 0.50 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 0.50 | 0.90 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 0.50 | 0.88 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.50 | 1.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 3.00 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 0.75 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 3.00 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 0.50 | 0.88 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 0.75 | 0.00 | 0.00 | 1.00 | 3.50 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 1.00 | 3.00 | – |

## What to change (DRIVERs missing target)

### first_q_answered = 0.80 (target 100% of chats)
Prompt lever: Answer-first instruction; drip-feed / Zeigarnik instruction (withholding the answer)

- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Future
  - ASTRO: Namaste, main Sitara hoon. Zindagi ke aane wale waqt ke baare mein aap mujhse kuch bhi puch sakti hain. Kya aap career, rishton ya kisi khaas vishay ko lekar chinta mein hain?
- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Future
  - ASTRO: Namaste. Main samajh sakti hoon ki aap apne aane wale waqt ke baare mein jaanna chahte hain. Aap career, shaadi ya kisi aur vishay par baat karna chahenge?

### refusals = 0.27 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S2 / direct_answer_chaser_genuine_return / session_2
  - USER: March mein konsi date?
  - ASTRO: Jyotish mein exact taareekh nahi, samay ka daur hota hai. March 2027 ka pura mahina shubh hai. Career aur shaadi dono tabhi sudhrenge. Aapki kundli mein ghar ke sukh ke baare mein bhi likha hai.
- S2 / direct_answer_chaser_same_day / session_1
  - USER: March 2027 me kaunsa mahina, date batao.
  - ASTRO: March 2027 ke baad se yog banta hai, par koi ek tareekh pakka nahi hoti. Aapki naukri aur shaadi, dono mein deri ka ek hi karan hai: abhi ka mushkil daur. Kya aap abhi kaam ko lekar zyada pareshan hain?

### user_frustrated = 1.53 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: Interview mein chances acche hain. Wo baat ye hai ki wo rishta kisi jaan-pehchan ke zariye aayega, jo kaafi shant swabhav ka hoga. Guru ka mantra 108 baar roz padhein, kya taiyari puri hai?
- S1 / direct_answer_chaser / session_1
  - USER: Jo mai puchh rha wo bta ni rhe.
  - ASTRO: Selection ke acche chances hain, kyunki career ka grah abhi majboot hai. 2023 se 2025 tak ki paise ki pareshani ab khatam ho rahi hai. Guru ka mantra guruvaar se shuru kijiye.
