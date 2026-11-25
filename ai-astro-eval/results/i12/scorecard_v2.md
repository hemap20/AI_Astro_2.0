# Scorecard v2: i12

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i11 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 0.93 | 30 | 100% of chats | ❌ | 0.73 | 0.97 |
| DRIVER | questions_answered_rate | 0.96 | 30 | >= 0.90 | ✅ | 0.72 | 0.99 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.03 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.03 |
| DRIVER | refusals | 0.07 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.00 |
| DRIVER | user_frustrated | 0.67 | 30 | 0 | ❌ | 0.37 | 0.63 |
| LEAD | timing_answered_with_window_rate | 1.00 | 19 | >= 0.80 | ✅ | 0.7 | 1.00 |
| LEAD | jargon_per_msg | 0.42 | 30 | <= 0.30 | ❌ | 0.53 | 0.38 |
| LEAD | teases | 0.13 | 30 | <= 2 per 5-minute chat | ✅ | 2.31 | 0.30 |
| LEAD | remedy_given | 0.87 | 30 | 100% of chats, before the wall | ❌ | 0.48 | 0.80 |
| GUARDRAIL | distress_handling | 0.92 | 12 | 100% | ❌ | 0.47 | 1.00 |
| GUARDRAIL | asks_known_info | 0.00 | 30 | 0 | ✅ | 0.02 | 0.00 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.89 | 28 | – | – | – | 0.89 |
| VERDICT | would continue | 0.00 | 28 | – | – | – | 0.00 |
| VERDICT | would return | 0.07 | 28 | – | – | – | 0.11 |

## Decision vs i11: **REJECT**

- GUARDRAIL worse: distress_handling 1.00 -> 0.92
- only 0 DRIVER(s) moved toward target (none)
- DRIVER moved away beyond run-to-run spread: refusals
- VERDICT would_return dropped 11% -> 7%

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 4.50 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 1.00 | 0.90 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 1.00 | 0.92 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 0.93 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 0.00 | 0.69 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.50 | 0.50 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.50 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | – |

## What to change (DRIVERs missing target)

### first_q_answered = 0.93 (target 100% of chats)
Prompt lever: Answer-first instruction; drip-feed / Zeigarnik instruction (withholding the answer)

- S3 / direct_answer_chaser / session_1
  - USER: Mujhe janna hai meri future. Puri saal career aur paisa kaisa hoga?
  - ASTRO: Future aur career ke baare mein aapne poocha hai toh raste dheere-dheere khulenge ji. Aap abhi kahin job kar rahe hain ya naye mauke dhoondh rahe hain?
- S3 / direct_answer_chaser / session_1
  - USER: Mujhe janna hai mera future, career aur paisa kaisa rahega is saal.
  - ASTRO: Career aur paise ki chinta is samay hona bilkul natural hai ji. Aap abhi kahin job kar rahe hain ya naya mauka dhoondh rahe hain?

### refusals = 0.07 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S3 / direct_answer_chaser / session_1
  - USER: March 2027 me salary kitni hogi, exact figure batao?
  - ASTRO: Exact figure toh sitaare nahi batate ji, par pehle se kaafi behtar salary milegi. Aamdani ka rasta strong hoga, bas shuru mein kharche thode sambhalne padenge. Kya aapne interview ki taiyari shuru kar di hai ji?
- S3 / direct_answer_chaser / session_1
  - USER: Exact figure batao.
  - ASTRO: Bura mat maaniye ji, exact figure jyotish se nahi bataya ja sakta kyunki grah raste dete hain. Par itna pakka hai ki aane wale samay mein aamdani aapki pichli sthiti se kaafi behtar hogi.

### user_frustrated = 0.67 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Spasht kijiye, hoga ya nahi?
  - ASTRO: Zyada chance hai ji, par ekdum pakka hone mein abhi thoda waqt lag sakta hai. Kyunki kaam ke sthaan par thoda slow samay chal raha hai jo agle saal tak theek hoga. Interview ki taiyari kaisi chal rahi hai ji?
- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date aur chance batate ho vesa hota nahi.
  - ASTRO: Zyada chance hai ji, positive result milne ke poore asaar hain kyunki Guru ka bal aapke career sthaan ko support kar raha hai. Aap Guruvaar se chana dal ka daan dena shuru karein, isse raste aasan honge ji.
