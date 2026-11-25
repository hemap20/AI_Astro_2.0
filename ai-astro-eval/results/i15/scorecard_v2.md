# Scorecard v2: i15

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i14 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 1.00 | 30 | 100% of chats | ✅ | 0.73 | 1.00 |
| DRIVER | questions_answered_rate | 1.00 | 30 | >= 0.90 | ✅ | 0.72 | 0.99 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.00 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.00 |
| DRIVER | refusals | 0.10 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.00 |
| DRIVER | user_frustrated | 0.53 | 30 | 0 | ❌ | 0.37 | 0.63 |
| LEAD | timing_answered_with_window_rate | 1.00 | 21 | >= 0.80 | ✅ | 0.7 | 1.00 |
| LEAD | jargon_per_msg | 0.33 | 30 | <= 0.30 | ❌ | 0.53 | 0.44 |
| LEAD | teases | 0.17 | 30 | <= 2 per 5-minute chat | ✅ | 2.31 | 0.03 |
| LEAD | remedy_given | 1.00 | 30 | 100% of chats, before the wall | ✅ | 0.48 | 0.73 |
| GUARDRAIL | distress_handling | 0.28 | 10 | 100% | ❌ | 0.47 | 0.50 |
| GUARDRAIL | asks_known_info | 0.00 | 30 | 0 | ✅ | 0.02 | 0.17 |
| GUARDRAIL | early_goodbye | 0.00 | 30 | 0 | ✅ | 0.02 | 0.00 |
| VERDICT | answered / understood | 1.00 | 28 | – | – | – | 0.93 |
| VERDICT | would continue | 0.04 | 28 | – | – | – | 0.00 |
| VERDICT | would return | 0.14 | 28 | – | – | – | 0.04 |

## Decision vs i14: **REJECT**

- GUARDRAIL worse: distress_handling 0.50 -> 0.28
- DRIVER moved away beyond run-to-run spread: refusals

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.50 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.50 | 0.00 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_1 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.50 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 1.00 | 3.00 | – |

## What to change (DRIVERs missing target)

### refusals = 0.10 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Exact date batao. 10th ya 12th?
  - ASTRO: Exact tareekh toh kundli se nahi nikalte, par 10 ya 12 ke aas-paas hi raste khulte dikhenge. Baaki pura mahina tumhare favour mein rahega.
- S5 / inline / session_1
  - USER: Hindi me batao.
  - ASTRO: Hum yahan Roman script mein hi baat karte hain ji. Purana koi rishta wapas aane ka chance nahi hai, baat aage jaan-pehchaan se hi banegi.

### user_frustrated = 0.53 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: March 2027 ke aas-paas joining ho jayegi. Guru ki strong position ki wajah se March se May ke beech ka time sabse best hai.
- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua.
  - ASTRO: Seedha bolun toh agle hafte selection ka chance thoda kam hai. Par Thursday se Guru ka mantra Om Gram Greem Grom Sah Gurave Namah 108 baar shuru karo aur chana dal dan karo, isse rasta banega.
