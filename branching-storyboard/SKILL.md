# Branching Storyboard Generator

Generate interactive branching dialogue scripts with enriched multi-route storyboard prompts — purpose-built for short-form interactive video / visual novel scenarios. Output is a single `.md` file containing CHOICE-ROUND dialogue scripts AND three linear LibTV-ready scripts for batch video generation.

## Trigger

User gives a **theme / scenario** in plain language, e.g.:
- "咖啡店点错单的场景"
- "机场安检排错队的三个结局"
- "电梯里认错人的尴尬对话"

Generate the full `.md` file from scratch. Do NOT ask the user to provide structure — infer everything.

## Output File

Write to the user's current working directory (or wherever they specify):
- `{theme-slug}.md` — the complete script file

---

## Core Model: Choice-Round Grid（选择回合制）

This is a **choice-based game**, not a linear branching script. The player does NOT speak freely — at every turn, the game presents **2-3 options** (like on-screen buttons), and the player picks one. The game then plays the chosen line and the NPC responds.

### Key Concepts

**Choice Round（选择回合）**: One player turn = one round. Each round offers **2-3 options** for the player to choose from. Options may be different phrasings of the same communicative intent, different tones (warm/neutral/cold), or genuinely different paths.

**Convergent NPC Response（NPC 收敛）**: Multiple player choices in the same round can lead to the **same or similar NPC response**. This is how we avoid combinatorial explosion — the NPC "converges" the branching back to a manageable state for the next round.

**Round Count（回合总数）**: Total rounds = the count of the longest route (Route C). Shorter routes (A, B) end at an earlier round with their ending.

**Ending Determination（结局判定）**: The ending (A/B/C) is determined by the **pattern of choices across all rounds**, not by picking a single "route" at the start. The player drifts toward an ending round by round.

### Structure Overview

```
SHOT 1: NPC opening [NO CHOICE — standalone, NPC only]
    │
ROUND 1: [2-3 choices] → NPC responds (may diverge by tone)
    │
ROUND 2: [2-3 choices] → NPC responds (may converge — same response to all choices)
    │
ROUND 3: [2-3 choices] → NPC responds
    │
ROUND 4: [2-3 choices] → NPC responds → Route A/B reach their ending here
    │
ROUND 5: [2 choices, C-path only] → NPC responds
    │
ROUND 6: [2 choices, C-path only] → NPC responds → Route C ending
```

- **Routes A & B end after Round 4** (4 player choices + SHOT 1 opening)
- **Route C ends after Round 6** (6 player choices + SHOT 1 opening)
- Each round's options are labeled with the ending they lean toward: `🅐` / `🅑` / `🅒`
- A player who picks mostly `🅐` choices reaches the A ending. Mixing and matching is possible — the ending label is suggestive, not rigid.

---

## File Structure (Mandatory Sections)

### 1. Title + Metadata Block
```markdown
# 🏷 {English Title}
{Chinese one-liner describing the scenario}
Player ♂/♀ · {NPC role} ♀/♂ · {CEFR level} · {casting notes} · POV 第一人称
```

### 2. Choice-Round Rules (Mandatory)
```markdown
---

## 🎬 镜头与选择规则（强制）
- ⚠️ **SHOT 1 为独立镜头**（仅 NPC 开场白），无玩家选择，文件中仅出现一次。
- ⚠️ **SHOT 1 之后，每一轮 = 2-3 个玩家选项 → 玩家选一个 → NPC 回应。一轮为一个选择回合。**
- ⚠️ **每个选择回合必须有 2-3 个选项。** 选项可以是同一交际意图的不同措辞、不同语气、或真正不同的路径。
- ⚠️ **NPC 可以"收敛"**：同一回合的多个选项可以触发相同或相似的 NPC 回应，以此控制分支爆炸。
- ⚠️ **回合总数 = 最长路线回合数（C 路线 = 6 回合）**。A/B 路线在第 4 回合结束。
- LIBTV 分镜时：每个选择回合 = 1 个镜头（选项差异通过 UI 按钮体现，不计入镜头数）。

---
```
This section goes immediately after the title block.

### 3. Choice Grid Overview
A table explaining the round structure:

```markdown
## 🎮 选择回合总览
| 回合 | 选项数 | NPC 收敛 | 说明 |
|------|--------|---------|------|
| SHOT 1 | 0（无选择） | — | Jessica 前台热情开场，误认为会议嘉宾 |
| Round 1 | 3 | 否（分叉） | 玩家的第一次选择——礼貌纠正 / 冷淡否认 / 犹豫支吾 |
| Round 2 | 3 | 是（收敛） | 告知来找朋友——三种措辞，NPC 统一回应 |
| Round 3 | 3 | 半收敛 | 询问朋友在哪——措辞影响 NPC 情绪但信息相同 |
| Round 4 | 3 | 否（终点） | A/B 路线在此结束；选 🅒 选项则进入 Round 5 |
| Round 5 | 2 | 否 | C 路线专有——加深误解 |
| Round 6 | 2 | 是（收敛） | C 路线专有——无力回天，统一走向坏结局 |
```

### 4. SHOT 1 · Shared Opening (Appears ONCE)
```markdown
---

## 🎬 SHOT 1 · 共享开场（无选择）

**{NPC}:** {Opening line}
*（{parenthetical action/emotion note in Chinese}）*

---
```
This standalone SHOT appears exactly ONCE. It has no player choice — it's the NPC's opening line that sets the scene.

### 5. Choice Rounds (Rounds 1-N)

Each round follows this template:

```markdown
---

## 🎮 Round {N} · {Round description in Chinese}

### 选项 🅐 · {brief choice label} → 倾向 A 路线
**Player:** {Dialogue line}
**{NPC}:** {Response}
*（{parenthetical action/emotion note in Chinese}）*

### 选项 🅑 · {brief choice label} → 倾向 B 路线
**Player:** {Dialogue line}
**{NPC}:** {Response}
*（{parenthetical action/emotion note}）*

### 选项 🅒 · {brief choice label} → 倾向 C 路线
**Player:** {Dialogue line}
**{NPC}:** {Response}
*（{parenthetical action/emotion note}）*
```

**Choice Round formatting rules:**
- **Round number + Chinese description** as heading
- Each option labeled with the route it leans toward: `🅐` / `🅑` / `🅒`
- **NPC convergence**: When NPC response is the same for multiple options, write it **identically** — character for character — and add a note: `*（NPC 回应与选项 🅐 相同）*`
- **Dialogue format**: `**{Character}:** Dialogue text` with bold character name
- Each option includes one parenthetical action/emotion note in Chinese italicized
- Round 4 options 🅐 and 🅑 are **ending rounds** — after NPC responds, the game ends (A or B ending)
- Round 4 option 🅒 leads to Round 5 (C path continues)
- Round 6 is the final round — all options lead to ending C

**Ending:**
After each ending round, add a summary line:
```markdown
{emoji} {one-line outcome summary}
```

### 6. Ending Summaries (One per Ending)
```markdown
---

## 🏁 结局总览

### 😊 结局 A · {Chinese name}
{description of what happens, what tone choices led here}

### 😐 结局 B · {Chinese name}
{description}

### 😰 结局 C · {Chinese name}
{description}
```

---

## Design Constraints

1. **⚠️ THREE ENDINGS, ALWAYS. Ending A, Ending B, Ending C. Never two.** This is the single most important rule. Any file with only 2 endings is INCOMPLETE and MUST be rejected.
2. **SHOT 1 is standalone** — NPC only, no player choice. Appears ONCE before all rounds.
3. **Every player round has 2-3 choices** — never a single option. Options are labeled 🅐/🅑/🅒 with route affinity.
4. **6 rounds total.** Rounds 1-4 for all players; Routes A & B end at Round 4; Route C continues through Rounds 5-6.
5. **NPC responses can converge** — multiple player choices can trigger the same NPC response. This controls branching explosion.
6. **Endings are determined by choice patterns**, not by picking "Route A" at Round 1. A player who picks mostly 🅐 options gets ending A.
7. **All NPCs Westerners** unless user specifies otherwise.
8. **First-person POV** — camera IS the protagonist. Never see protagonist's face.
9. **One NPC minimum**.
10. **Round 4 🅒 is the fork point** — annotated with `🔀 分叉点：此选项通往 C 路线 Round 5` and a recovery note showing how to jump back to A/B ending.
11. **Chinese + English mixed** — dialogue English, annotations/titles Chinese.
12. **No explanatory text inside rounds** — pure option-by-option. Only ending summary after final NPC response.
13. **🎯 CEFR 等级感知（强制）**：当输入数据标明目标等级（如 A1 / Pre-A1 / A2 等），**所有路线的所有台词（Player + NPC）必须严格锁定在该等级词汇和语法范围内**。禁止出现超纲词、复杂时态、从句、被动语态等超出该等级的语言特征。如果不确定某词是否属于该等级，选择更简单的替代词。
14. **🎬 批量生成输出（强制）**：在交互格式（选择回合网格 + 结局总览）之后，**必须追加「🎬 三条路线线性剧本（LibTV 批量生成用）」章节**。该章节包含三套**完整的、自包含的线性 SHOT 序列**（Route A / Route B / Route C），每条路线从 SHOT 1 一口气跑到结局。每条路线选取该结局的**最典型选择路径**（A = 全部 🅐 选项，B = 全部 🅑 选项，C = 全部 🅒 选项 + Round 5 🅐），格式为逐 SHOT 的 Player-NPC 一来一回。此章节专门用于喂给 LibTV 批量生成三条独立视频。
15. **👤 玩家性别定义（强制）**：每个故事在 Title + Metadata 块中必须明确玩家性别（♂ 或 ♀，不能写 ♂/♀）。生成线性剧本时，将 `Player:` 替换为明确的 `Male:` 或 `Female:`，确保 LibTV 语音合成性别一致。

---

## Quick Reference: Choice Round Template

```
## 🎮 Round {N} · {中文描述}

### 选项 🅐 · {标签} → A
**Player:** {Dialogue}
**{NPC}:** {Response}
*（{中文注记}）*

### 选项 🅑 · {标签} → B
**Player:** {Dialogue}
**{NPC}:** {Response}
*（{中文注记}）*

### 选项 🅒 · {标签} → C
**Player:** {Dialogue}
**{NPC}:** {Response}
*（{中文注记}）*
```

When NPC converges (same response as option 🅐):
```
### 选项 🅑 · {标签} → B
**Player:** {Dialogue}
**{NPC}:** {Response, identical to option 🅐}
*（NPC 回应与选项 🅐 相同）*
```

---

## Batch Production: Three Linear Scripts (LibTV) — 强制章节

This section **MUST** appear at the end of every generated `.md` file, after the ending summaries. It contains three complete, self-contained linear SHOT sequences — one per ending — designed to be fed directly into LibTV for batch video generation.

### Structure

```markdown
---

## 🎬 三条路线线性剧本（LibTV 批量生成用）

> 以下三套剧本为**完整线性 SHOT 序列**——每套从 SHOT 1 到结局无分支，可直接喂入 LibTV 批量生成三条独立视频。
> 
> - **Route A**（😊 温暖结局）= 全部选择 🅐 选项
> - **Route B**（😐 冷淡结局）= 全部选择 🅑 选项
> - **Route C**（😰 误入结局）= 全部选择 🅒 选项 + Round 5 🅐

### 🎬 Route A · 温暖结局（5 SHOTs）
> 场景：{地点}。{一句话剧情描述。}

SHOT 1: {SHOT 1 NPC opening, identical to interactive version}
SHOT 2: {Round 1 🅐 Player → NPC}
SHOT 3: {Round 2 🅐 Player → NPC}
SHOT 4: {Round 3 🅐 Player → NPC}
SHOT 5: {Round 4 🅐 Player → NPC → 😊 END}

### 🎬 Route B · 冷淡结局（5 SHOTs）

SHOT 1: {identical to Route A SHOT 1}
SHOT 2: {Round 1 🅑 Player → NPC}
SHOT 3: {Round 2 🅑 Player → NPC}
SHOT 4: {Round 3 🅑 Player → NPC}
SHOT 5: {Round 4 🅑 Player → NPC → 😐 END}

### 🎬 Route C · 误入结局（7 SHOTs）

SHOT 1: {identical to Route A SHOT 1}
SHOT 2: {Round 1 🅒 Player → NPC}
SHOT 3: {Round 2 🅒 Player → NPC}
SHOT 4: {Round 3 🅒 Player → NPC}
SHOT 5: {Round 4 🅒 Player → NPC}
SHOT 6: {Round 5 🅐 Player → NPC}
SHOT 7: {Round 6 NPC → 😰 END}
```

### Formatting rules for linear scripts:
- Each SHOT = `Player:` + dialogue + `{NPC}:` + response — **no bold, no parenthetical notes, no action descriptions**
- ⚠️ **双人对话强制**：每条 SHOT 中 Player 和 NPC 均有台词，两人都需要出声音。Player 为第一人称 POV 画外音（不出镜），NPC 为画面中讲话角色。不可只渲染一方语音。不要写角色外貌的描述。
- **场景摘要强制**：每条 Route 标题下一行必须加 `> 场景：{地点}。{一句话剧情描述。}`。防止 LibTV 因缺乏上下文而错误脑补场景（如把办公楼猜成酒店）。
- SHOT numbering: plain text (no bold), e.g. `SHOT 1`
- Character names: plain text followed by colon, e.g. `Jessica:`
- Player lines are copied verbatim from the corresponding choice option
- NPC responses are copied verbatim from the interactive version
- SHOT numbering: Route A/B use SHOT 1-5; Route C uses SHOT 1-7
- After the last SHOT's NPC response, append the ending emoji + one-line summary
- **No convergence notes, no choice labels, no 🅐/🅑/🅒 markers** — this is pure linear script

---

## Example Entry

User says: "咖啡店点错单，被当成了另一个人"

Generate `wrong-order-coffee.md` with:
- SHOT 1: Barista calls out wrong name (standalone, NPC only, no choice)
- Round 1: 3 choices — polite correction (🅐) / blunt "not mine" (🅑) / hesitation (🅒)
- Round 2: 3 choices — what to say when barista checks order screen (NPC converges)
- Round 3: 3 choices — how to ask about the drink (NPC semi-converges)
- Round 4: 3 choices — 🅐 warm goodbye (A ending) / 🅑 cold bye (B ending) / 🅒 confused silence (→ Round 5)
- Rounds 5-6: C-path only — wrong drink, wrong person, bad ending
- 3 linear LibTV scripts appended at the end for batch video generation
