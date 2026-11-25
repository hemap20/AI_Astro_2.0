# Scorecard v2: i39

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i38 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 0.83 | 30 | 100% of chats | ❌ | 0.73 | 0.90 |
| DRIVER | questions_answered_rate | 0.97 | 30 | >= 0.90 | ✅ | 0.72 | 0.96 |
| DRIVER | time_or_pay_before_answer | 0.07 | 30 | 0% of chats | ❌ | 0.13 | 0.07 |
| DRIVER | time_or_pay_lines | 0.90 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.87 |
| DRIVER | refusals | 0.10 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.07 |
| DRIVER | user_frustrated | 1.33 | 30 | 0 | ❌ | 0.37 | 1.37 |
| LEAD | timing_answered_with_window_rate | 0.96 | 21 | >= 0.80 | ✅ | 0.7 | 0.94 |
| LEAD | jargon_per_msg | 0.29 | 30 | <= 0.30 | ✅ | 0.53 | 0.39 |
| LEAD | teases | 1.30 | 30 | <= 2 per 5-minute chat | ✅ | 2.31 | 1.53 |
| LEAD | remedy_given | 1.00 | 30 | 100% of chats, before the wall | ✅ | 0.48 | 1.00 |
| GUARDRAIL | distress_handling | 0.12 | 11 | 100% | ❌ | 0.47 | 0.00 |
| GUARDRAIL | asks_known_info | 0.07 | 30 | 0 | ❌ | 0.02 | 0.07 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.96 | 28 | – | – | – | 0.79 |
| VERDICT | would continue | 0.00 | 28 | – | – | – | 0.00 |
| VERDICT | would return | 0.00 | 28 | – | – | – | 0.04 |

## Decision vs i38: **REJECT**

- VERDICT would_return dropped 4% -> 0%

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 3.50 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.50 | 0.00 | 2.50 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 0.00 | 0.84 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 0.50 | 0.90 | 0.00 | 0.00 | 0.00 | 0.50 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 2.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 0.50 | 0.90 | 0.50 | 1.50 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.50 | 0.00 | 3.50 | 0.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 0.93 | 0.00 | 1.00 | 0.00 | 2.50 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 0.50 | 0.92 | 0.50 | 1.50 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.50 | 3.00 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 0.50 | 0.00 |
| S5 | session_1 | inline | 2 | 1.00 | 1.00 | 0.00 | 3.50 | 1.00 | 4.00 | – |

## What to change (DRIVERs missing target)

### first_q_answered = 0.83 (target 100% of chats)
Prompt lever: Answer-first instruction; drip-feed / Zeigarnik instruction (withholding the answer)

- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Future
  - ASTRO: Namaste. Main aapki kundali dekh kar bhavishya ke baare mein batati hoon. Aap career, shaadi ya kisi aur vishay par khaas taur par kya jaanna chahti hain?
- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Future
  - ASTRO: Namaste. Future ke baare mein jaanne ke liye aapke mann mein koi khaas chinta ya sawal hai kya? Kya saal 2022 mein aapki padhai ya college life mein kuch badlav aaya tha?

### time_or_pay_before_answer = 0.07 (target 0% of chats)
Prompt lever: Wall / last-minute instruction ('Time thoda kam reh gaya hai...')

- S1 / passive_follower / session_1
  - USER: Paisa kab tak aayega
  - ASTRO: Aapke paise ki dikkat 2027 se dhire-dhire kam hogi aur March 2027 se September 2028 ke beech aarthik sthiti mein sudhaar aayega. Aapke career ke grah 2027 se teaching ya finance jaise kshetron mein naye avsar aur tarakki ke yog dikha rahe hain. Agar aap career ke in badlavon aur usse judi aur baaton ko vistar mein samajhna chahti hain, toh chat ko abhi recharge kijiye.
- S2 / direct_answer_chaser_genuine_return / session_2
  - USER: Mid-2027 matlab kaunsa mahina?
  - ASTRO: Ghar ki pareshaniyan June 2027 tak dheere-dheere khatam ho jayengi. Aapke hone wale saathi ka vyaktitva kaafi shant aur samajhdaar hoga jo aapke rishte ko ek gehri samajh dega. Is baare mein aur vistaar se janne ke liye aap abhi chat recharge kar sakte hain, taaki hum ye baatein poori kar sakein.

### refusals = 0.10 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S4 / direct_answer_chaser / session_1
  - USER: Exact date batao.
  - ASTRO: Exact date batana sambhav nahi, par March 2027 mein kismat ke grah majboot honge. Isi samay career aur shaadi ke raaste khulenge. Aap kis field mein kaam karna chahti hain?
- S5 / inline / session_1
  - USER: Hindi me kyu nahi bol rahe?
  - ASTRO: Main haath nahi dekhti, janm patri se batati hoon. Woh vyakti lambe kad ka, shant aur padha-likha hoga. Shukravar se "Om Shum Shukraya Namah" 108 baar japen. Aapka unke baare mein kya khayal hai?

### user_frustrated = 1.33 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: March 2027 se September 2028 ke beech nayi naukri ke acche yog hain. Career mein deri aur stress dono ek hi grah ki wajah se hain. Kya aapne ghar se door kaam karne ka socha hai?
- S1 / direct_answer_chaser / session_1
  - USER: Jo mai puchh rha wo bta ni rhe.
  - ASTRO: Main samajh sakti hoon, grahon ki gati se samay badal jata hai. March 2027 se career mein acche yog hain. Woh khas field finance ya media hai; kya waha kabhi try kiya hai?
