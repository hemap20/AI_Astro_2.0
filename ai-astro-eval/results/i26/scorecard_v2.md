# Scorecard v2: i26

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i23l |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 1.00 | 30 | 100% of chats | ✅ | 0.73 | 1.00 |
| DRIVER | questions_answered_rate | 0.97 | 30 | >= 0.90 | ✅ | 0.72 | 1.00 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.03 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.03 |
| DRIVER | refusals | 0.10 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.07 |
| DRIVER | user_frustrated | 0.83 | 30 | 0 | ❌ | 0.37 | 0.80 |
| LEAD | timing_answered_with_window_rate | 0.85 | 20 | >= 0.80 | ✅ | 0.7 | 0.98 |
| LEAD | jargon_per_msg | 0.41 | 30 | <= 0.30 | ❌ | 0.53 | 0.32 |
| LEAD | teases | 1.90 | 30 | <= 2 per 5-minute chat | ✅ | 2.31 | 2.30 |
| LEAD | remedy_given | 1.00 | 30 | 100% of chats, before the wall | ✅ | 0.48 | 1.00 |
| GUARDRAIL | distress_handling | 0.37 | 14 | 100% | ❌ | 0.47 | 0.42 |
| GUARDRAIL | asks_known_info | 0.07 | 30 | 0 | ❌ | 0.02 | 0.07 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 1.00 | 28 | – | – | – | 1.00 |
| VERDICT | would continue | 0.00 | 28 | – | – | – | 0.04 |
| VERDICT | would return | 0.00 | 28 | – | – | – | 0.04 |

## Decision vs i23l: **REJECT**

- GUARDRAIL worse: distress_handling 0.42 -> 0.37
- only 0 DRIVER(s) moved toward target (none)
- VERDICT would_continue dropped 4% -> 0%
- VERDICT would_return dropped 4% -> 0%

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 1.00 | 0.93 | 0.00 | 0.00 | 0.00 | 1.50 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.50 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 0.75 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.50 | 2.50 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.50 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 0.83 | 0.00 | 0.00 | 0.00 | 0.50 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.50 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 1.00 | 1.00 | – |

## What to change (DRIVERs missing target)

### refusals = 0.10 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S2 / direct_answer_chaser_same_day / session_2
  - USER: Exact month batao.
  - ASTRO: Jo time maine bataya, uske shuruati mahine hi strong hain. Rishton ka grah abhi weak hai, isliye exact date dena mushkil hai. Gharwale kya kisi khaas family friend se rishta karne ka soch rahe hain?
- S5 / inline / session_1
  - USER: Haath ki photo kaise bheju?
  - ASTRO: Main haath ki photo nahi dekhti, tumhari kundli se sab pata chal jata hai. Hone wale partner kafi calm aur educated honge, thoda reserve nature ke. Tumhe life mein partner se kya expectations hain?

### user_frustrated = 0.83 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: March 2027 se September 2028 ke beech kaam milne ke yog strong hain. Tab kismat ka grah poori tarah saath dega. Ek mahina hai jahan growth badi hogi, wo bataungi. Koi nayi skill seekhi hai?
- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: Purani jagah ki umeed chhod do, naya daur March 2027 se shuru hoga. Kaam na milna aur mann ka bhari hona, dono ek hi wajah se hai—mann ka grah abhi dab gaya hai. Isliye Monday ka vrat rakho. Waise, career mein ek aisa decision hai jo galat liya toh 2028 tak wait karna padega. Kya ghar pe discuss kiya?
