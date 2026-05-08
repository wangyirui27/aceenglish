
# Branching Storyboard Generator v2.0

生成「视频复用型伪游戏」的分支剧本 + 多宫格分镜图提示词。
输出单一 `.md` 文件，包含完整的 SHOT 脚本、显式选择节点、视频资产清单，以及可直接喂给 GPT-IMAGE-2 的多宫格分镜图 prompt。

---

## 🎯 核心理念：生产管线倒推设计

### 端到端流程
```
1. 本 SKILL 输出  → 分支剧本 .md（含选择树、SHOT 脚本、分镜 prompt）
2. GPT-IMAGE-2    → 生成 1~3 张多宫格分镜大图
3. 人工裁剪宫格    → N 张独立起始帧
4. 图生视频模型    → N 段 3~5 秒对话视频
5. 前端播放器      → 玩家选择 → 播放对应视频 → 串联成伪游戏
```

### 核心等式（贯穿整个 SKILL）
**1 SHOT = 1 视频片段 = 1 宫格 panel = 1 张起始帧**

所以：
- SHOT 数量 = 需要生产的视频数量 = 分镜图总宫格数
- 多条路线**共享同一个 SHOT** → **共用同一段视频** → **省钱**
- 分镜图的宫格数严格等于"独立视频数"，不存在冗余 panel

---

## 🎮 玩家体验目标

**每次通关玩家做 2~3 个选择，触达不同结局。**

- **CHOICE 1**（强制 3 选项）：决定主路线 A / B / C
- **CHOICE 2**（强制 2 选项）：在每条主路线内部决定子结局
- **CHOICE 3**（仅 Route C，2 选项）：错误路径上的"挽救机会"

| 路线 | 选择数 | SHOT 数（玩家体验） | 子结局数 |
|------|--------|-------------------|---------|
| A | 2 | 3（SHOT 1 + 2A + 3A） | 2 |
| B | 2 | 3（SHOT 1 + 2B + 3B） | 2 |
| C | 3 | 4（SHOT 1 + 2C + 3C + 4C） | 2（挽救成功 / 沉沦坏结局）|

**总结局数 = 6**（A1, A2, B1, B2, C1, C2）。

---

## 💰 视频复用策略（核心成本控制）

### 复用判定原则
> **如果在某个 SHOT 时刻，两条路径的 NPC 情绪状态、物理动作、台词完全一致，则共用同一段视频。**

注意：是 NPC 的状态决定能否复用，不是 Player 的选择。Player 的不同选择可以汇入同一个 NPC 反应。

### 强制复用点
- **SHOT 1**：所有路线共用，1 段视频，标记 `⬡ SHARED-ALL`
- **结局收敛**：当 Route C 的"挽救成功"分支与 Route A 的某个子结局在情绪上一致时，**强制复用同一段视频**，标记 `⬡ SHARED-AC`

### 禁止伪复用
- **不要**为了省钱让两个明显不同的情绪状态共用视频（例如愤怒 NPC 和微笑 NPC 不可共用）
- **不要**让 Player 选择不同但 NPC 反应被强制写成完全一样（这会让玩家感到选择无意义）

---

## 📥 触发

用户给出场景主题，例如：
- "咖啡店点错单的场景"
- "机场安检排错队"
- "酒店前台拿错房卡"

不要反问结构。直接生成完整 `.md` 文件。

## 📤 输出文件

写入 `{theme-slug}.md` 至用户当前目录。

---

## 📐 文件结构（强制章节，按顺序）

### § 1. 标题元数据块

```markdown
# 🏷 {English Title}
{中文一句话场景描述}
Player ♂/♀ · {NPC role} ♀/♂ · {casting notes} · POV 第一人称
**结构：3 路线 · 6 结局 · {N} 段视频 · {M} 宫格分镜**
```

### § 2. 选择规则（强制）

```markdown
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
```

### § 3. 选择树可视化（Choice Map）

```markdown
## 🗺 Choice Map

​```
                    SHOT 1 (NPC 开场, SHARED-ALL)
                         │
                  🔀 CHOICE 1 (3 选项)
            ┌────────────┼────────────┐
            ▼            ▼            ▼
         SHOT 2A      SHOT 2B      SHOT 2C
            │            │            │
       🔀 CHOICE 2A  🔀 CHOICE 2B  🔀 CHOICE 2C
         (2 选项)     (2 选项)     (recover / commit)
         ┌──┴──┐      ┌──┴──┐      ┌────┴────┐
         ▼     ▼      ▼     ▼      ▼         ▼
       SHOT  SHOT   SHOT  SHOT   SHOT 3C   SHOT 3C
       3A_w  3A_c   3B_a  3B_c   _recover  _commit
       ✨A1  ✨A2   ✨B1  ✨B2     │          │
                                🔀 CHOICE 3   ✨ C2
                                 (2 选项)   (坏结局)
                                  ┌──┴──┐
                                  ▼     ▼
                                SHOT  SHOT
                                4C_   4C_
                                save  half
                                ✨C1   (复用?)
​```
```

### § 4. 视频资产清单（生产排期表）

```markdown
## 📦 视频资产清单

| 视频 ID | 复用范围 | 对应 SHOT | 描述 |
|---------|---------|-----------|------|
| V01 | SHARED-ALL | SHOT 1 | NPC 开场白 |
| V02 | A-ONLY | SHOT 2A | Player 礼貌纠正 |
| V03 | B-ONLY | SHOT 2B | Player 生硬否认 |
| V04 | C-ONLY | SHOT 2C | Player 犹豫沉默 |
| V05 | A-ONLY | SHOT 3A_warm | 温暖收尾 ✨ |
| V06 | A-ONLY | SHOT 3A_cool | 客气但疏离 ✨ |
| V07 | B-ONLY | SHOT 3B_apology | 缓和道歉 ✨ |
| V08 | B-ONLY | SHOT 3B_cold | 冷淡结束 ✨ |
| V09 | C-ONLY | SHOT 3C_recover | 转折挽救节拍 |
| V10 | C-ONLY | SHOT 3C_commit | 走向错误的关键帧 ✨ |
| V11 | SHARED-AC | SHOT 4C_save | 与 A 某结局复用？还是独立 |
| ... | | | |

**总计：N 段独立视频 / 6 个结局**
```

### § 5. SHOT 1（共享开场，独立模块）

```markdown
---

## 🎬 SHOT 1 · 共享开场 ⬡ SHARED-ALL

**{NPC}:** {Opening line}
*（{中文动作/情绪注记}）*

---
```

### § 6. CHOICE 1（强制 3 选项）

```markdown
## 🔀 CHOICE 1 · 主路线分岔

| 选项 | 玩家说 / 做 | 跳转 |
|------|------------|------|
| A | "{Polite line}" | → SHOT 2A |
| B | "{Blunt line}" | → SHOT 2B |
| C | *（{Hesitation action}）* | → SHOT 2C |
```

### § 7. Route A · 礼貌路径（2 选择 · 3 SHOT · 2 子结局）

```markdown
---

## 路线 A · {route name} → ✨ 温暖结局
{风格注记：欧美真人 POV，色调/氛围}

### SHOT 2A ⬡ A-ONLY
**Player:** {选项 A 的 dialogue}
**{NPC}:** {Response}
*（{中文情绪注记}）*

### 🔀 CHOICE 2A · 子结局分岔
| 选项 | 玩家说 | 跳转 |
|------|--------|------|
| A1 | "{Warm line}" | → SHOT 3A_warm ✨ |
| A2 | "{Polite-distance line}" | → SHOT 3A_cool ✨ |

### SHOT 3A_warm ⬡ A-ONLY ✨ 结局 A1
**Player:** {Warm closing}
**{NPC}:** {Warm response}
*（{中文情绪注记}）*

✨ **结局 A1**：{一句话总结}

### SHOT 3A_cool ⬡ A-ONLY ✨ 结局 A2
**Player:** {Polite-distant closing}
**{NPC}:** {Brief professional response}
*（{中文情绪注记}）*

✨ **结局 A2**：{一句话总结}
```

### § 8. Route B · 冷漠路径（结构同 A）

完全平行 A 的结构，2 个子结局：B1 缓和道歉、B2 冷淡结束。

### § 9. Route C · 犹豫路径（3 选择 · 4 SHOT · 2 子结局 · 含挽救机制）

```markdown
---

## 路线 C · 犹豫之路 → ⚠️ 危险路径
{风格注记}

### SHOT 2C ⬡ C-ONLY
**Player:** *（{犹豫/沉默动作}）* "{Mumbled line}"
**{NPC}:** {Misinterpretation response}
*（{中文情绪注记}）*

### 🔀 CHOICE 2C · 关键岔路
| 选项 | 玩家说 / 做 | 跳转 |
|------|------------|------|
| Recover | "{Late correction}" | → SHOT 3C_recover |
| Commit | *（{Nod / silent acceptance}）* | → SHOT 3C_commit |

### SHOT 3C_recover ⬡ C-ONLY · 🔀 挽救节拍
**Player:** {Apologetic correction}
**{NPC}:** {Slightly puzzled but accommodating response}
*（{中文情绪注记}）*

### 🔀 CHOICE 3 · 挽救后的态度
| 选项 | 玩家说 | 跳转 |
|------|--------|------|
| C1 | "{Sincere apology}" | → SHOT 4C_save ✨ |
| C2-half | "{Brief excuse}" | → SHOT 4C_half |

### SHOT 4C_save ⬡ C-ONLY ✨ 结局 C1
**Player:** {Sincere closing}
**{NPC}:** {Forgiving warm response}
*（{中文情绪注记}）*

✨ **结局 C1（挽救成功）**：{一句话总结}

### SHOT 3C_commit ⬡ C-ONLY ✨ 结局 C2
**Player:** *（{Nodding}）* "...Yeah."
**{NPC}:** {Final response leading to wrong outcome}
*（{中文情绪注记 — 灾难感}）*

✨ **结局 C2（沉沦）**：{一句话总结，例如"拿着别人的拿铁离开了咖啡店"}
```

---

## 🎨 § 10. 多宫格分镜图 Prompt（核心输出）

### 设计逻辑

GPT-IMAGE-2 一次生成 **1 张多宫格大图**，所有独立 SHOT 的起始帧放在一张图里以便保持人物 / 风格一致性。
人工裁剪后每个 panel 喂给图生视频模型。

### 网格布局规则

- 总 panel 数 = 视频资产清单中的独立视频数（典型 9~12 张）
- 推荐网格：
  - 9 panel → 3×3
  - 10 panel → 2×5
  - 12 panel → 3×4
- **每个 panel 必须有清晰的边框分隔和左上角小标号**（V01, V02...），方便裁剪和对应资产清单

### 输出模板

```markdown
## 🎨 Storyboard Master Prompt

**Image Generation Prompt for GPT-IMAGE-2:**

A {N}-panel comic storyboard arranged in a {rows}×{cols} grid, each panel separated by thin black borders, labeled in the top-left corner with V01–V{N}. First-person POV throughout (camera is the protagonist's eyes; the protagonist is never visible except hands/arms when relevant).

**Consistent across all panels:**
- Setting: {detailed environment — coffee shop / hotel lobby / etc., with consistent props}
- NPC character: {detailed appearance — age, ethnicity (Western), hair, eye color, clothing, badge/uniform, build}. This SAME PERSON must appear identically in every panel.
- Color palette: {warm/cool palette description}
- Lighting style: {key light source — window light, ceiling fluorescent, etc.}
- Color grading: cinematic, {film stock style — Kodak Portra 400 / Fuji Eterna / etc.}
- Aspect ratio per panel: 16:9 (the master image is sized so each cell crops cleanly to 16:9)

**Per-panel descriptions:**

**V01 【中文情绪标题】 ⬡ SHARED-ALL** — SHOT 1 (NPC opening)
{Shot type, e.g. Medium close-up}, {angle}. {NPC} {action — looks up from counter, holds out item, etc.}, {facial expression — warm smile / neutral / questioning}. {Foreground: counter edge with prop X}. {Midground: NPC}. {Background: blurred shop interior}. {Lighting: soft window light from camera-left, warm color temperature ~3200K}. {Eye-line: NPC looks directly at camera (POV)}. {Emotional subtext: friendly anticipation}. This is SHOT 1.

**V02 【中文情绪标题】 ⬡ A-ONLY** — SHOT 2A (after CHOICE 1: Polite)
{Shot type}, {angle}. {NPC reaction at the moment Player has just spoken — eyebrow lifts, smile shifts, holds prop differently}. {Foreground / midground / background}. {Lighting same source, but maybe slightly warmer to match positive emotion}. {Eye-line}. {Emotional subtext: surprised but pleased}. This is SHOT 2A.

**V03 【中文情绪标题】 ⬡ B-ONLY** — SHOT 2B (after CHOICE 1: Blunt)
{Shot type}, {angle}. {NPC reaction — slight frown, stiffening, polite-but-cooling smile}. {...}. {Lighting subtly cooler to match emotional drop}. {Emotional subtext: professional withdrawal}. This is SHOT 2B.

**V04 【中文情绪标题】 ⬡ C-ONLY** — SHOT 2C (after CHOICE 1: Hesitation)
{Shot type}, {angle}. {NPC's expression — confused, leaning forward, prop offered tentatively}. {...}. {Lighting unchanged but composition tighter to feel claustrophobic}. {Emotional subtext: ambiguous expectation}. This is SHOT 2C.

{... continue for V05 through V{N} ...}

**V{N-1} 【沉沦终结】 ⬡ C-ONLY** — SHOT 3C_commit (Ending C2)
{Wide shot or detail shot — e.g. NPC turning away as Player walks off with wrong item}. {Lighting cools dramatically — long shadows, blue cast}. {Emotional subtext: irrevocable error}. This is SHOT 3C_commit.

**V{N} 【挽救圆满】 ⬡ C-ONLY** — SHOT 4C_save (Ending C1)
{Mirror to V{X — corresponding A1 ending} for visual rhyme — same warm key light, NPC smiling kindly}. {Emotional subtext: relief, redemption}. This is SHOT 4C_save.

---
```

### 复用 panel 的处理
**复用视频对应的 panel 在大图中只画一次。**
- 复用清单中标记 `⬡ SHARED-AC` 的 SHOT，分镜图里不重复绘制。
- 在该 panel 描述中写明：`Reused as the ending for both Route A1 and Route C1 — must convey emotion compatible with both contexts.`

---

## 🛡 设计约束（不可违反）

1. **3 路线，永远** — A / B / C 三条主路线，不允许 2 条或 4 条。
2. **2~3 个选择 per 通关** — A/B 路线 2 个 CHOICE，C 路线 3 个 CHOICE。
3. **6 个结局** — A1, A2, B1, B2, C1, C2，每个结局有专属（或复用的）SHOT 视频。
4. **CHOICE 节点显式标记** — 用表格列出选项文案 + 目标 SHOT，不要把选择隐藏在叙述里。
5. **SHOT 1 标准化** — 仅 NPC 开场，无 Player 回应，SHARED-ALL，整个文件只出现一次。
6. **SHOT 2+ 一来一回** — Player 一句 → NPC 一句，禁止跨 SHOT 合并。
7. **第一人称 POV** — 镜头即玩家视角，绝不出现玩家正脸。
8. **欧美真人** NPC（除非用户特别说明）。
9. **复用必须真实** — NPC 情绪/动作完全一致才能复用视频。禁止"为省钱强行共用情绪不符的镜头"。
10. **视频资产清单强制** — 文件必须包含 `📦 视频资产清单` 表格，列出每段视频的 ID + 复用范围 + 对应 SHOT。
11. **分镜图为单一大图** — 输出 1 个 GPT-IMAGE-2 prompt，包含所有独立 panel；panel 数 = 资产清单视频数。
12. **Panel 标号** — 每个 panel 左上角标 V01, V02... 与资产清单对应。
13. **CEFR 等级感知（强制）** — 当输入数据标明目标等级（如 A1 / Pre-A1 / A2 等），所有路线的所有台词（Player + NPC）必须严格锁定在该等级词汇和语法范围内，禁止超纲。
14. **混合语言** — 对话英文，注记/标题中文，分镜 prompt 英文。
15. **结局标记** — 每个最终 SHOT 必须以 `✨ 结局 {ID}` 标注。

---

## 📋 Quick Reference

### SHOT 模板
```
### SHOT {ID} ⬡ {MARKER}
**Player:** {dialogue}
**{NPC}:** {response}
*（{中文情绪注记}）*
```

### CHOICE 模板
```
### 🔀 CHOICE {N} · {名称}
| 选项 | 玩家说 / 做 | 跳转 |
|------|------------|------|
| {ID} | "{line}" | → SHOT {next} |
```

### Panel 模板
```
**V{NN} 【{中文标题}】 ⬡ {MARKER}** — SHOT {ID}
{Shot type}, {angle}. {Composition}. {Foreground/midground/background}. 
{Lighting}. {NPC expression and micro-expressions}. {Eye-line}. 
{Emotional subtext}. {Reuse note if applicable}. This is SHOT {ID}.
```

---

## 🎬 示例触发

**输入**："咖啡店点错单，被当成了另一个人"

**输出文件名**：`wrong-order-coffee.md`

**预期结构**：
- SHOT 1：Barista 喊错名字递上拿铁（V01, SHARED-ALL）
- CHOICE 1：礼貌纠正 / 生硬否认 / 犹豫沉默
- Route A：礼貌纠正后 CHOICE 2 选热情道谢或得体收下 → A1 / A2
- Route B：生硬否认后 CHOICE 2 选缓和或冷淡走人 → B1 / B2
- Route C：犹豫后 CHOICE 2 选迟到挽救或硬接错单
  - 挽救分支再 CHOICE 3 → C1 圆满收尾 / C2 半挽救
  - 硬接分支 → C2-bad 拿着错单走出咖啡店
- 资产清单约 10~12 段视频
- 1 张 3×4 分镜大图 prompt 喂给 GPT-IMAGE-2
```

