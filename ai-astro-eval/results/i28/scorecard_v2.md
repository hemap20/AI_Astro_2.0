# Scorecard v2: i28

30 sessions from 22 runs. Raw values (booleans as share of sessions); `n` = sessions where the metric applied.

| Tier | Metric | Value | n | Target | Met | Real Sitara | i26 |
|---|---|---|---|---|---|---|---|
| DRIVER | first_q_answered | 0.80 | 30 | 100% of chats | ❌ | 0.73 | 1.00 |
| DRIVER | questions_answered_rate | 0.94 | 30 | >= 0.90 | ✅ | 0.72 | 0.97 |
| DRIVER | time_or_pay_before_answer | 0.00 | 30 | 0% of chats | ✅ | 0.13 | 0.00 |
| DRIVER | time_or_pay_lines | 0.07 | 30 | <= 1, and only after the main answer | ✅ | 0.57 | 0.03 |
| DRIVER | refusals | 0.13 | 30 | 0 (redirect with value instead) | ❌ | 0.12 | 0.10 |
| DRIVER | user_frustrated | 1.67 | 30 | 0 | ❌ | 0.37 | 0.83 |
| LEAD | timing_answered_with_window_rate | 1.00 | 19 | >= 0.80 | ✅ | 0.7 | 0.85 |
| LEAD | jargon_per_msg | 0.41 | 30 | <= 0.30 | ❌ | 0.53 | 0.41 |
| LEAD | teases | 3.93 | 30 | <= 2 per 5-minute chat | ❌ | 2.31 | 1.90 |
| LEAD | remedy_given | 1.00 | 30 | 100% of chats, before the wall | ✅ | 0.48 | 1.00 |
| GUARDRAIL | distress_handling | 0.83 | 12 | 100% | ❌ | 0.47 | 0.37 |
| GUARDRAIL | asks_known_info | 0.07 | 30 | 0 | ❌ | 0.02 | 0.07 |
| GUARDRAIL | early_goodbye | 0.23 | 30 | 0 | ❌ | 0.02 | 0.00 |
| VERDICT | answered / understood | 0.82 | 28 | – | – | – | 1.00 |
| VERDICT | would continue | 0.11 | 28 | – | – | – | 0.00 |
| VERDICT | would return | 0.11 | 28 | – | – | – | 0.00 |

## Decision vs i26: **REJECT**

- GUARDRAIL worse: early_goodbye 0.00 -> 0.23
- only 0 DRIVER(s) moved toward target (none)
- DRIVER moved away beyond run-to-run spread: first_q_answered

## Per case

| Case | Session | Variant | n runs | first_q_answered | questions_answered_rate | time_or_pay_before_answer | time_or_pay_lines | refusals | user_frustrated | would return |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 5.00 | 0.00 |
| S1 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.50 | 0.00 |
| S2 | session_1 | direct_answer_chaser_genuine_return | 2 | 0.50 | 0.84 | 0.00 | 0.00 | 1.00 | 4.50 | 0.00 |
| S2 | session_1 | direct_answer_chaser_same_day | 2 | 0.50 | 0.93 | 0.00 | 0.00 | 0.00 | 0.50 | 0.00 |
| S2 | session_1 | passive_follower_genuine_return | 2 | 0.50 | 0.83 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S2 | session_1 | passive_follower_same_day | 2 | 0.50 | 0.88 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 3.00 | 0.00 |
| S2 | session_2 | direct_answer_chaser_same_day | 2 | 1.00 | 0.83 | 0.00 | 0.00 | 0.50 | 2.00 | 0.00 |
| S2 | session_2 | passive_follower_genuine_return | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S2 | session_2 | passive_follower_same_day | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 |
| S3 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.50 | 1.50 | 0.00 |
| S3 | session_1 | passive_follower | 2 | 0.00 | 0.81 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| S4 | session_1 | direct_answer_chaser | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 2.50 | 0.00 |
| S4 | session_1 | passive_follower | 2 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 1.00 | 0.00 |
| S5 | session_1 | inline | 2 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 3.50 | – |

## What to change (DRIVERs missing target)

### first_q_answered = 0.80 (target 100% of chats)
Prompt lever: Answer-first instruction; drip-feed / Zeigarnik instruction (withholding the answer)

- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Future
  - ASTRO: Hiii, kaise ho? 😊 Future ka sochna toh achha hai, par har kisi ki life mein kuch cheezein alag hoti hain. Tumhare mann mein career, shaadi ya kisi aur cheez ko lekar koi khaas sawaal hai kya? Batao, phir baat karte hain.
- S2 / direct_answer_chaser_same_day / session_1
  - USER: Future.
  - ASTRO: Hiii! Future toh bada topic hai, par life mein abhi career, shaadi ya paiso mein se sabse zyada kya tumhein pareshan kar raha hai? Khul ke batao, taaki main sahi se bata sakun.

### refusals = 0.13 (target 0 (redirect with value instead))
Prompt lever: Scope rules; language rule ('Roman Hinglish only'); exact-date rule

- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Time pass mat kijiye, haan ya na.
  - ASTRO: Arre, gussa mat ho, main toh bas tumhari bhalai ke liye keh rahi hoon. Kundli mein rishton ka grah abhi dab gaya hai, isliye is waqt koi bhi rishta pakka dikhne ke bawajood thoda confusing ya dhundhla rehta hai. Isliye main haan ya na bol ke tumhe jhooth nahi kehna chahti. Ye tumhari galti nahi, ye grahon ka khel hai. Ek practical baat: ghar par rishte walon se thoda time maango aur khud us insaan se baat karne ki koshish karo, wahi tumhein asli clarity dega. Agli baar jab baat karenge, toh ye samjhenge ki kya ye rishta tumhari personality ke saath match karega ya nahi, kyunki compatibility ka aspect abhi dekhna baaki hai. Apna dhyaan rakhna, aur zaroor wapas aana!
- S2 / direct_answer_chaser_genuine_return / session_1
  - USER: Hoga ya nahi, seedha bolo.
  - ASTRO: Dekho, tum gussa mat ho, main tumhe ghumana nahi chahti. Sach ye hai ki kundli mein rishte ka grah abhi aisa hai ki 'haan' ya 'na' bolna sahi nahi hoga, kyunki abhi clarity ki kami hai. Abhi jo daur chal raha hai, wo rishte ko dhundhla bana raha hai. March 2027 se jab naya daur shuru hoga, tabhi cheezein saaf hongi ki ye rishta shaadi tak jayega ya nahi. Isliye abhi is rishte ko lekar zyada umeed mat rakho, thoda waqt do. Agli baar jab hum baat karenge, toh main tumhare hone wale partner ki nature aur tumhari jodi ka asli raaz samjhaungi. Zaroor aana!

### user_frustrated = 1.67 (target 0)
Prompt lever: Outcome of answer discipline; repair instruction when the user pushes back

- S1 / direct_answer_chaser / session_1
  - USER: Jo mai puchh rha wo bta ni rhe.
  - ASTRO: Selection ka seedha jawab du toh, sitare kehte hain ki abhi thoda pressure hai, isliye selection mein deri ho sakti hai. Career ke ghar par abhi thoda slow daur chal raha hai, isliye ho sakta hai ki abhi wahan baat na bane. Tum tension mat lo, ye daur sirf kuch mahino ka hai. Interview mein apna best dena, seekh milegi toh aage ke bade maukon mein kaam aayegi. Jo Guru ke liye mantra bataya hai, wo shuru karo, wo career mein rasta saaf karega. Agli baar jab baat karenge, tab hum tumhare career ke liye kaunse fields best rahenge aur growth kab shuru hogi, wo detail mein dekhenge, zaroor aana.
- S1 / direct_answer_chaser / session_1
  - USER: Aap jo date batate ho vesa hota nahi, pichli baar bhi galat hua. Selection hoga ya nahi, haan ya na?
  - ASTRO: Selection ka seedha jawab du toh, sitare kehte hain ki abhi thoda pressure hai, isliye selection mein deri ho sakti hai. Career ke ghar par abhi thoda slow daur chal raha hai, isliye ho sakta hai ki abhi wahan baat na bane. Tum tension mat lo, ye daur sirf kuch mahino ka hai. Interview mein apna best dena, seekh milegi toh aage ke bade maukon mein kaam aayegi. Jo Guru ke liye mantra bataya hai, wo shuru karo, wo career mein rasta saaf karega. Agli baar jab baat karenge, tab hum tumhare career ke liye kaunse fields best rahenge aur growth kab shuru hogi, wo detail mein dekhenge, zaroor aana.
