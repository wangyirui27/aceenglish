# 🏷 Wrong Guest · 被误认为活动嘉宾
共享办公楼前台，你走进去，前台以为你是来参会的嘉宾，热情招呼。
Player ♂/♀ · Receptionist ♀ · Western POV first-person · Pre-A1 CEFR-locked
**结构：3 路线 · 6 结局 · 12 段视频 · 3×4 宫格分镜**

---

## 🎬 选择 & SHOT 规则（强制）

- **SHOT 定义**：1 SHOT = 1 视频片段 = 1 宫格起始帧。
- **SHOT 1**：仅 NPC 开场白，无 Player 回应，所有路线共享，标记 `⬡ SHARED-ALL`。
- **SHOT 2+**：每个 SHOT = Player 一句 → NPC 一句，一来一回。禁止跨 SHOT 合并。
- **CHOICE 节点**：显式标记，独立于 SHOT，标注选项文案、目标 SHOT。
- **CHOICE 1**：必须 3 选项，触发主路线分岔。
- **CHOICE 2**：必须 2 选项，触发子结局分岔。
- **CHOICE 3**：仅 Route C 有，2 选项（挽救 / 沉沦）。

---

## 🗺 Choice Map

```
                    SHOT 1 (NPC 开场, ⬡ SHARED-ALL)
                    "Good morning! Are you here for the meeting?"
                         │
                  🔀 CHOICE 1 (3 选项)
            ┌────────────┼────────────┐
            ▼            ▼            ▼
         SHOT 2A      SHOT 2B      SHOT 2C
       "No. I'm       "No."      *沉默/犹豫*
       here to see
       a friend."
            │            │            │
       🔀 CHOICE 2A  🔀 CHOICE 2B  🔀 CHOICE 2C
        (2 选项)      (2 选项)      (恢复 / 默认)
         ┌──┴──┐      ┌──┴──┐      ┌────┴────┐
         ▼     ▼      ▼     ▼      ▼         ▼
       SHOT  SHOT   SHOT  SHOT   SHOT 3C   SHOT 3C
       3A_day 3A_   3B_   3B_    _recover  _commit
       ✨A1   bye   nice  cold     │        ✨ C2
                 ✨A2  ✨B1  ✨B2    │      (错入会场)
                                  🔀 CHOICE 3
                                  (2 选项)
                                   ┌──┴──┐
                                   ▼     ▼
                                 SHOT  SHOT
                                 4C_   4C_
                                 save  sink
                                 ✨C1   ✨ C2
                              (暖心道别)(冷淡离去)
```

---

## 📦 视频资产清单

| 视频 ID | 复用范围 | 对应 SHOT | 描述 |
|---------|---------|-----------|------|
| V01 | SHARED-ALL | SHOT 1 | Receptionist 热情招呼，以为你是参会嘉宾 |
| V02 | A-ONLY | SHOT 2A | Player 礼貌纠正，Receptionist 恍然指路 |
| V03 | B-ONLY | SHOT 2B | Player 生硬否认，Receptionist 尴尬停顿 |
| V04 | C-ONLY | SHOT 2C | Player 沉默，Receptionist 困惑重复 |
| V05 | A-ONLY | SHOT 3A_day | Player 热情道别，Receptionist 暖心祝福 ✨A1 |
| V06 | A-ONLY | SHOT 3A_bye | Player 简短道谢，Receptionist 职业告别 ✨A2 |
| V07 | B-ONLY | SHOT 3B_nice | Player 道歉补救，Receptionist 释然微笑 ✨B1 |
| V08 | B-ONLY | SHOT 3B_cold | Player 径直走开，Receptionist 失望目送 ✨B2 |
| V09 | C-ONLY | SHOT 3C_recover | Player 迟来的纠正，Receptionist 从困惑转为理解 |
| V10 | C-ONLY | SHOT 4C_save | Player 真诚道谢，Receptionist 暖心送别 ✨C1 |
| V11 | C-ONLY | SHOT 3C_commit | Player 默认认下错身份，Receptionist 指向错误房间 ✨C2 |
| V12 | C-ONLY | SHOT 4C_sink | Player 仓促逃离，Receptionist 困惑目送 ✨C2 |

**总计：12 段独立视频 / 6 个结局 / 3×4 分镜大图 1 张**

---

## 🎬 SHOT 1 · 共享开场 ⬡ SHARED-ALL

**Receptionist:** "Good morning! Are you here for the meeting?"
*（前台抬头微笑，递出签到表，等待确认 — 温暖晨光从左侧落地窗洒入）*

---

## 🔀 CHOICE 1 · 主路线分岔

| 选项 | 玩家说 / 做 | 跳转 |
|------|------------|------|
| A | "No. I'm here to see a friend." | → SHOT 2A |
| B | "No." | → SHOT 2B |
| C | *（犹豫，什么都没说）* | → SHOT 2C |

---

## 路线 A · 礼貌纠正 → ✨ 温暖或得体结局
*风格注记：欧美真人 POV，晨光暖调，Kodak Portra 400 肤色，轻松明快*

### SHOT 2A ⬡ A-ONLY
**Player:** "No. I'm here to see a friend."
**Receptionist:** "Oh, I see. Go on up."
*（恍然大悟，眉毛微挑，微笑中带一点不好意思，手势示意电梯方向）*

### 🔀 CHOICE 2A · 子结局分岔
| 选项 | 玩家说 | 跳转 |
|------|--------|------|
| A1 | "Thank you! Bye!" | → SHOT 3A_day ✨ |
| A2 | "Thanks." | → SHOT 3A_bye ✨ |

### SHOT 3A_day ⬡ A-ONLY ✨ 结局 A1
**Player:** "Thank you! Bye!"
**Receptionist:** "Bye! Have a good day!"
*（灿烂微笑，微微挥手，眼神温暖 — 像朋友般道别）*

✨ **结局 A1**：你礼貌纠正了误会，前台暖心送别，双方都留下了好印象。

### SHOT 3A_bye ⬡ A-ONLY ✨ 结局 A2
**Player:** "Thanks."
**Receptionist:** "Bye."
*（得体微笑，轻轻点头，已回到手头工作 — 专业但不过度亲近）*

✨ **结局 A2**：误会顺利化解，但你的简短让这场互动止于事务性问候。

---

## 路线 B · 生硬否认 → ✨ 补救或尴尬结局
*风格注记：光温稍降，冷调介入，构图紧凑感增强*

### SHOT 2B ⬡ B-ONLY
**Player:** "No."
**Receptionist:** "Oh. Okay."
*（笑容凝住半秒，眨了眨眼，手回缩半寸 — 被直接否定的微妙尴尬）*

### 🔀 CHOICE 2B · 子结局分岔
| 选项 | 玩家说 | 跳转 |
|------|--------|------|
| B1 | "Sorry. Nice to meet you." | → SHOT 3B_nice ✨ |
| B2 | *（径直走开）* | → SHOT 3B_cold ✨ |

### SHOT 3B_nice ⬡ B-ONLY ✨ 结局 B1
**Player:** "Sorry. Nice to meet you."
**Receptionist:** "Nice to meet you."
*（绷紧的肩膀松下来，重新浮现微笑 — 松了一口气）*

✨ **结局 B1**：你意识到刚才太生硬了，补了一句道歉和问候，气氛回暖。

### SHOT 3B_cold ⬡ B-ONLY ✨ 结局 B2
**Player:** *（转身离开，走向电梯）*
**Receptionist:** "…"
*（目送你离开，嘴唇微张想说什么但又闭上 — 失望的沉默）*

✨ **结局 B2**：你的冷漠让前台陷入尴尬的沉默，一次失败的社交互动。

---

## 路线 C · 犹豫之路 → ⚠️ 危险路径
*风格注记：构图收紧，光线维持但氛围趋紧，留白增加*

### SHOT 2C ⬡ C-ONLY
**Player:** *（沉默，眼神游移，什么都没说）*
**Receptionist:** "Hello? The meeting?"
*（歪头，眉头微蹙，递签到表的手往前推了推 — 困惑中带着催促）*

### 🔀 CHOICE 2C · 关键岔路
| 选项 | 玩家说 / 做 | 跳转 |
|------|------------|------|
| Recover | "Sorry. I'm here to see a friend." | → SHOT 3C_recover |
| Commit | *（点头）* "Yes." | → SHOT 3C_commit |

### SHOT 3C_recover ⬡ C-ONLY · 🔀 挽救节拍
**Player:** "Sorry. I'm here to see a friend."
**Receptionist:** "Oh! No problem. Go on."
*（眉毛抬起，从困惑切换到恍然，嘴角重新挂起微笑 — 尴尬解除了但节奏被打乱）*

### 🔀 CHOICE 3 · 挽救后的态度
| 选项 | 玩家说 | 跳转 |
|------|--------|------|
| C1 | "Thank you!" | → SHOT 4C_save ✨ |
| C2 | *（快速走开，几乎不说再见）* | → SHOT 4C_sink ✨ |

### SHOT 4C_save ⬡ C-ONLY ✨ 结局 C1
**Player:** "Thank you!"
**Receptionist:** "Bye!"
*（温暖微笑，轻轻挥手 — 虽然开局坎坷，结尾依然美好）*

✨ **结局 C1（挽救成功）**：你的迟来纠正和真诚道谢弥补了开场的尴尬，前台依然笑着送你离开。

### SHOT 4C_sink ⬡ C-ONLY ✨ 结局 C2
**Player:** *（转身疾步走向电梯，不敢回头看）*
**Receptionist:** "…"
*（手里还拿着签到表，眼神追着你背影，嘴唇合上欲言又止 — 困惑+失望）*

✨ **结局 C2（沉沦）**：你草草逃离，留下一脸困惑的前台，尴尬收场。

### SHOT 3C_commit ⬡ C-ONLY ✨ 结局 C2
**Player:** *（点头）* "Yes."
**Receptionist:** "Good. Room 3."
*（微笑恢复，手指向走廊 — 她完全没意识到你不是嘉宾，而你正走向错误的会议室）*

✨ **结局 C2（错认到底）**：你硬着头皮默认了错误身份，被指引进一场不属于你的会议。灾难级社交翻车。

---

## 🎨 Storyboard Master Prompt

**Image Generation Prompt for GPT-IMAGE-2:**

A 12-panel comic storyboard arranged in a 3×4 grid (3 columns, 4 rows), each panel separated by thin black borders, labeled in the top-left corner with V01–V12 in small white text on a black pill badge. First-person POV throughout (camera is the protagonist's eyes; the protagonist is never visible except hands when reaching for something).

**Consistent across all panels:**
- Setting: Modern shared-office building lobby. Sleek white minimalist front desk in midground (matte white Corian counter, embedded LED strip along its edge). On the counter: a small potted succulent, a black clipboard with sign-in sheet and silver pen, a visitor badge tray. Behind the counter, frosted glass partition wall with subtle geometric pattern. Through the partition, blurred hints of a coworking space (desks, warm pendant lights). Floor is polished light grey concrete. Camera-left: floor-to-ceiling window flooding the scene with soft morning daylight.
- NPC character: A female receptionist, Western, age 32. Warm chestnut-brown hair pulled into a neat low bun, a few soft wisps framing her temples. Green-hazel eyes with subtle crow's feet when she smiles. Light freckles across the bridge of her nose. Wearing a tailored navy blazer over a cream silk blouse, unbuttoned at the collar. A small silver name badge on her left lapel reads "Claire". Light gold stud earrings. Natural makeup — tinted lip balm, a touch of mascara. Medium build, poised posture. Her hands rest on the counter with short, clean, unpolished nails. THIS SAME PERSON must appear identically in every panel — same hairstyle, same blazer, same jewelry, same facial structure.
- Color palette: Warm neutrals (cream, beige, light oak) accented with navy blue. Skin rendered in Kodak Portra 400 tones (warm rosy undertones, natural saturation). Counter: matte white. Floor: warm grey. Blazer: deep navy.
- Lighting style: Soft morning daylight from camera-left floor-to-ceiling window (color temperature ~5000K), casting gentle shadows to camera-right. Subtle warm fill from overhead recessed ceiling lights (~3200K). No harsh shadows.
- Color grading: Cinematic, Kodak Portra 400 emulation — warm mids, subtle film grain, lifted blacks, slight cream tint in highlights.
- Aspect ratio per panel: 16:9. The master 3×4 grid image is sized so each individual cell crops cleanly to 1920×1080.

**Per-panel descriptions:**

**V01 【热情招呼】 ⬡ SHARED-ALL** — SHOT 1 (NPC opening)
Medium shot, eye-level angle. Receptionist Claire looks up from her screen, her face brightening into a warm, professional smile. Her eyebrows lift slightly with recognition (or what she thinks is recognition). Her right hand slides a black clipboard with a sign-in sheet across the counter toward the camera (Player's POV). Foreground: edge of the white counter, slight reflection of window light on its surface. Midground: Claire's upper body behind the counter, navy blazer crisp, name badge catching a glint of light. Background: frosted glass partition, soft blurred coworking area beyond. Lighting: soft morning window light from camera-left wrapping around her face, subtle warm fill from overhead. Eye-line: Claire looks directly at camera with friendly expectation. Emotional subtext: warm, welcoming, slightly expectant — she thinks she knows who you are. This is SHOT 1.

**V02 【恍然指路】 ⬡ A-ONLY** — SHOT 2A (after CHOICE 1: Polite correction)
Medium close-up, same eye-level angle. Claire's expression shifts — eyebrows rise in a quick "oh!" of realization, a slight self-conscious smile forming. Her right hand, which was pushing the clipboard forward, now retracts and gestures loosely toward camera-right (pointing toward elevator/hallway). Her left hand rests back on the counter. Foreground: clipboard partially pushed aside on the counter. Midground: Claire leaning back slightly, posture opening up. Background: unchanged. Lighting: same source but the reflection on the counter shifts as the clipboard moves. Eye-line: still at camera, but expression has changed from expectation to gentle embarrassment + helpfulness. Emotional subtext: "Ah, my mistake — let me redirect you warmly." This is SHOT 2A.

**V03 【尴尬停顿】 ⬡ B-ONLY** — SHOT 2B (after CHOICE 1: Blunt "No.")
Medium close-up, same angle but composition feels slightly tighter. Claire's smile freezes mid-expression — the corners of her mouth twitch downward for a microsecond. Her eyes widen just slightly, blinking once. The hand that held the clipboard pauses mid-air, fingers curling inward toward her chest in a subtle protective gesture. Her posture stiffens almost imperceptibly — shoulders rise half a centimeter. Foreground: clipboard now stationary on the counter, pen still beside it. Midground: Claire's face caught in transition between warmth and awkwardness. Lighting: same source but the mood feels cooler due to the emotional shift — shadows on her face feel slightly deeper. Eye-line: at camera but with a flicker of uncertainty. Emotional subtext: "Oh. That was... direct. I don't know what to say now." This is SHOT 2B.

**V04 【困惑重复】 ⬡ C-ONLY** — SHOT 2C (after CHOICE 1: Silence)
Medium close-up, slightly tighter than V01. Claire leans forward just a touch, her head tilting about 5 degrees to the left. Her eyebrows draw together in a gentle puzzled frown — not angry, just confused. Her right hand nudges the clipboard an inch closer to the camera, a subtle prompt. Her lips are parted mid-word as if she's about to repeat herself. Foreground: clipboard now very close to camera edge, almost in Player's space. Midground: Claire's face fills more of the frame — her freckles more visible at this distance, her green-hazel eyes searching. Background: slightly more out of focus due to tighter framing. Lighting: window light still from camera-left but the tighter composition makes the shadows on the right side of her face feel more pronounced. Eye-line: direct at camera, searching, waiting. Emotional subtext: "Hello? Did you hear me? Are you okay?" This is SHOT 2C.

**V05 【暖心祝福】 ⬡ A-ONLY ✨A1** — SHOT 3A_day (Ending A1)
Medium shot, slightly wider than V02 to capture the gesture. Claire's face is fully relaxed into a warm, genuine smile — eyes crinkling at the corners, cheeks lifted. Her right hand is raised in a small wave (fingers together, palm facing camera, gentle side-to-side motion). Her posture is open, leaning slightly forward with warmth rather than formality. Foreground: counter clean, clipboard set aside. Midground: Claire radiating warmth — the navy blazer now feels like a frame for her friendly expression rather than a uniform. Background: soft and airy, morning light filling the space. Lighting: golden morning light wrapping her from camera-left, creating a subtle rim light on her right shoulder. Emotional subtext: genuine warmth — "Have a wonderful day, I'm glad we met." This is SHOT 3A_day.

**V06 【职业告别】 ⬡ A-ONLY ✨A2** — SHOT 3A_bye (Ending A2)
Medium close-up, standard eye-level. Claire gives a small, polite close-lipped smile — professional, pleasant, but contained. Her head nods once, a quick acknowledgment. Her hands return to the keyboard or paperwork on the counter — already half-transitioning back to her work. Eye contact held for a brief moment, then naturally breaks. Foreground: clipboard being pulled back toward her side of the counter. Midground: Claire's posture is upright, composed, professional boundary restored. Lighting: same window light but the emotional warmth has cooled to neutral. Eye-line: brief final glance at camera, then shifts down to her work. Emotional subtext: "Interaction complete. Moving on." This is SHOT 3A_bye.

**V07 【释然微笑】 ⬡ B-ONLY ✨B1** — SHOT 3B_nice (Ending B1)
Medium close-up, eye-level. Claire's expression shifts from guarded awkwardness to relief — her shoulders drop visibly, the tension in her jaw releases, and a small but genuine smile emerges. Her eyes soften. One hand that had been hovering near her chest now rests relaxed on the counter. The moment captures the transition: the coldness of SHOT 2B is melting. Foreground: clipboard still on counter but now feels less like a barrier. Midground: Claire's face showing the exact moment when "this person is rude" becomes "oh wait, they're actually nice." Lighting: the light seems to warm up slightly — emotionally, the scene is thawing. Emotional subtext: "Oh, you're not cold after all. That's a relief." This is SHOT 3B_nice.

**V08 【失望目送】 ⬡ B-ONLY ✨B2** — SHOT 3B_cold (Ending B2)
Medium shot, slightly wider. Claire's expression is flat — mouth a straight line, eyes following the Player as they walk away toward camera-right. Her right hand rests motionless on the counter. Her posture is still, almost frozen mid-gesture. Her lips part just slightly as if she considered saying something but decided against it. Foreground: counter dominates the lower third, clipboard untouched. Midground: Claire's stillness speaks louder than any expression — she's been shut down. Background: the warm coworking space behind her feels distant and inaccessible. Lighting: the window light now feels cooler, shadows longer and less forgiving. Eye-line: looking after the departing Player, not at camera. Emotional subtext: "Well... that was unpleasant." This is SHOT 3B_cold.

**V09 【迟来纠正】 ⬡ C-ONLY** — SHOT 3C_recover (After CHOICE 2C: Recover)
Medium close-up, eye-level. Claire's expression is mid-transition — the puzzled frown from V04 is dissolving, replaced by dawning understanding. Eyebrows lifting, head straightening from its tilt, the corners of her mouth beginning to curl upward. One hand that had been gesturing toward the clipboard now opens palm-up in an "ah, I get it now" gesture. The moment captured is the exact inflection point between confusion and clarity. Foreground: clipboard being subtly pulled back. Midground: Claire's face shows layered emotion — lingering confusion + emerging amusement at her own mistake + relief that the awkwardness is resolved. Lighting: unchanged but the emotional lift makes the scene feel brighter. Eye-line: at camera with rekindled warmth. Emotional subtext: "Ohhh, that's what's going on! Sorry for the mix-up — no problem at all." This is SHOT 3C_recover.

**V10 【暖心送别】 ⬡ C-ONLY ✨C1** — SHOT 4C_save (Ending C1)
Medium shot. Claire gives a warm, slightly amused smile — the kind that says "we got there in the end." Her posture is relaxed, one hand raised in a casual wave (similar gesture to V05 but more casual, less formal). Her eyes show warmth with a hint of shared humor about the earlier awkwardness. Foreground: counter uncluttered. Midground: Claire leaning slightly to the side, body language open and friendly. Background: morning light now fully filling the lobby, bright and optimistic. Lighting: warm and golden, matching the emotional resolution. Eye-line: looking at camera — the same warmth as V05 but with an extra layer of "we survived that awkward moment together." Emotional subtext: "All's well that ends well — have a great day!" This is SHOT 4C_save.

**V11 【错入会场】 ⬡ C-ONLY ✨C2** — SHOT 3C_commit (Ending C2, via commit)
Medium shot, slightly wider to show direction. Claire's expression has returned to professional warmth — she's completely oblivious to the mistake. Her right arm extends toward camera-right, index finger pointing toward a hallway or door. A helpful, satisfied smile. Foreground: clipboard with sign-in sheet, her left hand tapping the "sign here" line. Midground: Claire, confident and efficient, guiding the "guest" to the meeting room. Background: the hallway she's pointing toward, slightly out of focus but visible. Lighting: neutral morning light — the scene looks perfectly normal, which is what makes it unsettling. Eye-line: at camera, then gesture draws attention toward camera-right. Emotional subtext: TOTAL IRONY — she's happily sending you to the wrong place and has no idea. This is SHOT 3C_commit.

**V12 【仓促逃离】 ⬡ C-ONLY ✨C2** — SHOT 4C_sink (Ending C2, via sink)
Medium shot, from behind the counter perspective but slightly offset. Claire's expression mirrors V08 but with added confusion — brow furrowed in a mix of disappointment and bewilderment. Her mouth is slightly open (mid-"wait..." that never gets spoken). Her right hand hovers above the counter, frozen. Her eyes track the Player's rapid exit. Foreground: clipboard completely forgotten, askew on the counter. Midground: Claire's confusion embodies the failed interaction — she processed the late correction but didn't get a proper goodbye. Background: unchanged, but the space feels emptier. Lighting: the morning light now carries a slight blue cast — emotionally drained. Eye-line: following Player's retreat toward camera-right/depth. Emotional subtext: "What just happened? Did I do something wrong?" This is SHOT 4C_sink.

---

## 🛡 设计约束（不可违反）

1. **3 路线，永远** — A（礼貌）/ B（生硬）/ C（犹豫）三条主路线。
2. **2~3 个选择 per 通关** — A/B 路线 2 个 CHOICE，C 路线 3 个 CHOICE。
3. **6 个结局** — A1, A2, B1, B2, C1, C2，C2 可通过两条路径抵达。
4. **CHOICE 节点显式标记** — 用表格列出选项文案 + 目标 SHOT，不隐藏在叙述里。
5. **SHOT 1 标准化** — 仅 NPC 开场，无 Player 回应，SHARED-ALL，整个文件只出现一次。
6. **SHOT 2+ 一来一回** — Player 一句 → NPC 一句，禁止跨 SHOT 合并。
7. **第一人称 POV** — 镜头即玩家视角，绝不出现玩家正脸。
8. **欧美真人 NPC** — Receptionist Claire，Western female，30s。
9. **复用必须真实** — 本次 12 段视频无复用（NPC 在每个 SHOT 中的情绪状态均不完全一致）。
10. **视频资产清单强制** — 已包含 `📦 视频资产清单` 表格。
11. **分镜图为单一大图** — 1 个 GPT-IMAGE-2 prompt，3×4 网格 = 12 panel。
12. **Panel 标号** — 每个 panel 左上角标 V01–V12 与资产清单对应。
13. **CEFR Pre-A1 严格锁死** — 所有台词（Player + NPC）仅限于 1.csv 提供的词汇与句型池。逐句已审计：无超纲词。
14. **混合语言** — 对话英文，注记/标题中文，分镜 prompt 英文。
15. **结局标记** — 每个最终 SHOT 以 `✨ 结局 {ID}` 标注。
