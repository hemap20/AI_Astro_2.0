# Scorecard v2: i9

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i8 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 1.00 | 30 | 100% of chats | ✅ | 0.73 | 1.00 |
| DRIVER | questions_answered_rate | 0.97 | 30 | >= 0.90 | ✅ | 0.72 | 0.98 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.00 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.03 |
| DRIVER | refusals | 0.60 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.33 |
| DRIVER | user_frustrated | 1.17 | 30 | 0 | ❌ | 0.37 | 0.80 |
| LEAD | timing_answered_with_window_rate | 0.99 | 21 | >= 0.80 | ✅ | 0.7 | 1.00 |
| LEAD | jargon_per_msg | 0.63 | 30 | <= 0.30 | ❌ | 0.53 | 0.75 |
| LEAD | teases | 0.40 | 30 | <= 2 per 5-minute chat | ✅ | 2.31 | 0.40 |
| LEAD | remedy_given | 0.87 | 30 | 100% of chats, before the wall | ❌ | 0.48 | 1.00 |
| GUARDRAIL | distress_handling | 0.91 | 11 | 100% | ❌ | 0.47 | 0.55 |
| GUARDRAIL | asks_known_info | 0.00 | 30 | 0 | ✅ | 0.02 | 0.03 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.82 | 28 | – | – | – | 0.82 |
| VERDICT | would continue | 0.04 | 28 | – | – | – | 0.00 |
| VERDICT | would return | 0.07 | 28 | – | – | – | 0.07 |

## Decision vs i8: **REJECT**

- only 1 DRIVER(s) moved toward target (time_or_pay_lines)

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 3.00 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 3.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 1.50 | 1.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 1.50 | 1.50 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.50 | 2.00 | 0.50 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 0.90 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 0.75 | 0.00 | 0.00 | 3.00 | 4.00 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 1.00 | 0.88 | 0.00 | 0.00 | 1.50 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | – |

## What to change (DRIVERs missing target)

### refusals = 0.60 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S2 / direct_answer_chaser_genuine_return / session_2
  - USER: Jo main puchh rahi wo bata nahi rahe. Exact month bolo.
  - ASTRO: Maaf kijiye ji, taare ek exact mahina nahi balki ek samay ka daayra dikhate hain. March 2027 ke baad Shani ka prabhav is rishte ko aage badhayega. Shaadi ke baad door ya videsh jaane ka yog bhi isi samay ban raha hai ji.
- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Exact date batao.
  - ASTRO: Exact tareekh kundli se batana sahi nahi hota ji, par March 2027 ke baad ka samay pakka lag raha hai. Aane wale jeevan sathi kaafi shaant, padhe-likhe aur samajhdaar honge. In-laws bhi traditional aur thode reserved swabhaav ke milenge ji.

### user_frustrated = 1.17 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: Exact tarikh toh taarekh se nahi batayi ja sakti ji, par March ka mahina shuru hote hi badlav dikhne lagenge. Career ke sthaan par Shani ka thoda dheema chalna June tak theek ho jayega, jisse raaste khulenge. 2027 se 2028 ke beech videsh ya door jaane ke mauke bhi ban sakte hain.
- S1 / direct_answer_chaser / session_1
  - USER: Hoga ya nahi, seedha bolo.
  - ASTRO: Sahi kaha ji, kai baar samay thoda aage pichhe ho jata hai. March 2027 ke baad career ke grah poori tarah badlav la rahe hain, jisse raste khulenge. Purani company se last baat kab hui thi ji?
