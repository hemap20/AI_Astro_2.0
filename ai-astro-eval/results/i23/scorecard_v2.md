# Scorecard v2: i23

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i22m |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 1.00 | 30 | 100% of chats | ✅ | 0.73 | 1.00 |
| DRIVER | questions_answered_rate | 1.00 | 30 | >= 0.90 | ✅ | 0.72 | 1.00 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.03 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.03 |
| DRIVER | refusals | 0.07 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.07 |
| DRIVER | user_frustrated | 1.03 | 30 | 0 | ❌ | 0.37 | 1.07 |
| LEAD | timing_answered_with_window_rate | 0.97 | 18 | >= 0.80 | ✅ | 0.7 | 0.98 |
| LEAD | jargon_per_msg | 0.47 | 30 | <= 0.30 | ❌ | 0.53 | 0.63 |
| LEAD | teases | 2.23 | 30 | <= 2 per 5-minute chat | ❌ | 2.31 | 2.27 |
| LEAD | remedy_given | 1.00 | 30 | 100% of chats, before the wall | ✅ | 0.48 | 1.00 |
| GUARDRAIL | distress_handling | 0.43 | 14 | 100% | ❌ | 0.47 | 0.50 |
| GUARDRAIL | asks_known_info | 0.17 | 30 | 0 | ❌ | 0.02 | 0.10 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.03 |
| VERDICT | answered / understood | 0.86 | 28 | – | – | – | 0.79 |
| VERDICT | would continue | 0.00 | 28 | – | – | – | 0.00 |
| VERDICT | would return | 0.07 | 28 | – | – | – | 0.11 |

## Decision vs i22m: **REJECT**

- GUARDRAIL worse: distress_handling 0.50 -> 0.43
- GUARDRAIL worse: asks_known_info 0.10 -> 0.17
- VERDICT would_return dropped 11% -> 7%

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.50 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.50 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.50 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.00 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.50 | 1.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.50 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.50 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 1.00 | 3.00 | – |

## What to change (DRIVERs missing target)

### refusals = 0.07 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S5 / inline / session_1
  - USER: Haath ki photo kaise bheju?
  - ASTRO: Main haath nahi dekhti, par kundli mein sab saaf hai. Tumhare partner lambe aur shant honge, par thode reserve rahenge. Kya tumne aise kisi se baat ki hai?
- S5 / inline / session_1
  - USER: Haath ki photo kaise bheju? Hindi mein likho na.
  - ASTRO: Main haath nahi dekhti, par tumhari kundli se rishton ka grah thoda dab gaya hai, isliye clarity nahi mil rahi hai. Iske liye mantra roz 108 baar padhna shuru karo, jisse confusion door ho. Partner ki nature thodi reserved hogi; kya tumhare mann mein koi specific insaan hai ya bas shaadi ki chinta hai?

### user_frustrated = 1.03 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: Agle hafte selection ke chances kam hain kyunki abhi career ka daur thoda dheema chal raha hai. Selection ke liye tumhe thodi aur mehnat karni hogi, kyunki asli badlav March 2027 se aayega. Tumhari kundli mein ek chhoti si kami hai jo interview mein tumhari baat ko dabane ka asar dikha rahi hai, isliye Hanuman Chalisa roz padhna shuru karo. Interview ke waqt tumhe kis cheez se sabse zyada darr lagta hai?
- S1 / direct_answer_chaser / session_1
  - USER: Hoga ya nahi, seedha batao.
  - ASTRO: Purani job par wapas bulaye jaane ke chances toh kam hi hain. Kaam ka grah toh majboot hai, par career ki jagah par abhi ek dheema daur chal raha hai jo June 2027 tak rahega. Ye job kab chhuti thi aur wapas jaane ka khayal kyun aa raha hai?
