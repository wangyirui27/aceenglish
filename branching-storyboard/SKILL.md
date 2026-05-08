# Branching Storyboard Generator

Generate interactive branching dialogue scripts with enriched multi-route storyboard prompts — purpose-built for short-form interactive video / visual novel scenarios. Output is a single `.md` file containing SHOT-based dialogue scripts AND 6-panel comic storyboard prompts.

## Trigger

User gives a **theme / scenario** in plain language, e.g.:
- "咖啡店点错单的场景"
- "机场安检排错队的三个结局"
- "电梯里认错人的尴尬对话"

Generate the full `.md` file from scratch. Do NOT ask the user to provide structure — infer everything.

## Output File

Write to the user's current working directory (or wherever they specify):
- `{theme-slug}.md` — the complete script + storyboard file

---

## File Structure (Mandatory Sections)

### 1. Title + Metadata Block
```markdown
# 🏷 {English Title}
{Chinese one-liner describing the scenario}
Player ♂/♀ · {NPC role} ♀/♂ · {casting notes} · POV 第一人称
```

### 2. Shot Rule (Mandatory)
```markdown
---

## 🎬 镜头规则（强制）
- ⚠️ **SHOT 1 为独立镜头**（仅 NPC 开场白），三条路线共用，文件中仅出现一次。
- ⚠️ **SHOT 2 起，每个 SHOT = Player 先说 → NPC 回应，一来一回为一个镜头。禁止跨 SHOT 合并。**
- LIBTV 分镜时：SHOT 数量 = 独立镜头数量，逐 SHOT 输出，不允许压缩或跳号。

---
```
This section goes immediately after the title block.

### 3. Dialogue Structure Overview
A brief paragraph explaining:
- SHOT 1 is standalone and shared by all routes
- SHOT 2+ branch into A/B/C
- Which SHOTs are structurally shared between A and B
- Where crossover/fork points exist (Route C)
- How a player can slip between routes

### 4. Shared SHOT Nodes Table
```markdown
| SHOT | 共享范围 | 内容 |
|------|---------|------|
| SHOT 1 | ALL | NPC 开场（独立镜头，无 Player 回应） |
| SHOT {N} | A·B | {brief description} |
| SHOT {M} | A·B | {brief description} |
```
SHOT 1 is always SHARED-ALL and standalone. A and B share 2 additional SHOTs (typically tablet-check and room-directions).

### 5. SHOT 1 · Shared Opening (Appears ONCE before routes)
```markdown
---

## 🎬 SHOT 1 · 共享开场 ⬡ SHARED-ALL

**{NPC}:** {Opening line}
*（{parenthetical action/emotion note in Chinese}）*

---
```
This standalone SHOT appears exactly ONCE in the file. Routes B and C do NOT repeat it. Route A starts from SHOT 2A, B from SHOT 2B, C from SHOT 2C.

### 6. Three Routes (A, B, C)

Each route follows this template:

```markdown
## 路线 {A/B/C} · {route name in Chinese} → {emoji outcome}
{style notes: 欧美真人出镜，全程第一人称 POV 视角，色调/氛围}

### SHOT 2 ⬡ {ROUTE}-ONLY
**Player:** {Dialogue line}
**{NPC}:** {Response}
*（{parenthetical action/emotion note in Chinese}）*

### SHOT 3 ⬡ {SHARED marker or ROUTE-ONLY}
**Player:** {Dialogue line}
**{NPC}:** {Response}
*（{parenthetical action/emotion note}）*
```

**SHOT formatting rules:**
- **SHOT 1**: NPC only, standalone, shared. Player does NOT respond.
- **SHOT 2+**: Player speaks first, then NPC responds. One back-and-forth per SHOT.
- Player may speak one or multiple sentences in one turn. NPC may speak multiple sentences in response. But only ONE turn each per SHOT.
- Shared SHOTs get `⬡ SHARED-AB` marker.
- Route-only SHOTs get `⬡ {ROUTE}-ONLY`.
- Fork points get `🔀 分叉点` annotation with a note about how to cross over.
- Each SHOT has one parenthetical action/emotion note in Chinese italicized, placed after the appropriate character line.
- Dialogue format: `**{Character}:** Dialogue text` with bold character name.
- SHOT 7 (Route C only) may be Player-only or NPC-only (silent final beat).

**Route design principles:**
- Route A: The "good" path — polite, warm outcome. Target 5 SHOTs (SHOT 1 + 4 back-and-forth).
- Route B: The "cold" path — same structural goal, different emotional register. Target 5 SHOTs (SHOT 1 + 4 back-and-forth).
- Route C: The "wrong" path — hesitation leads to bad outcome. Target 7 SHOTs (SHOT 1 + 6 back-and-forth).
- A and B share SHOT 3 and SHOT 4 (structural beats: tablet check, room directions).
- C shares only SHOT 1, then diverges completely.
- C SHOT 4 is the 🔀 fork point where player could recover.

**Ending:**
After the last SHOT, add a summary line:
```markdown
{emoji} {one-line outcome summary}
```

---

### 7. Storyboard Prompts (One per Route)

Each route gets a `### 🎨 Route {A/B/C} Storyboard Prompt` section. **Storyboard is 6 panels per route** — a separate visualization from the SHOT-based dialogue. Map key SHOT beats to 6 panels.

```markdown
### 🎨 Route {A/B/C} Storyboard Prompt
Comic storyboard. 6 panels. First-person POV (camera is protagonist's eyes). {Character description: age, hair, clothing, etc.}. {Environment description}. {Color palette description}. {Lighting description}. {Color grading / film style}. Aspect ratio 16:9.
```

**Then 6 panels. Each panel MUST include:**

1. **`Panel N 【Chinese Emotion Title】`** — a 2-4 character Chinese title capturing the emotional beat
2. **⬡ Shared marker** — `SHARED-ALL`, `SHARED-AB`, or `{ROUTE}-ONLY`
3. **Shot type** — Close-up / Medium shot / Wide shot / Over-the-shoulder / Low angle / High angle / Overhead
4. **Composition** — what's in frame, foreground/background relationship
5. **Character performance** — facial expression, body language, hand gestures, eye contact
6. **Lighting specifics** — source, direction, color temperature, shadows, highlights
7. **Emotional subtext** — what the image should make the viewer feel
8. **Cross-reference to parallel panels** in other routes when applicable
9. **SHOT mapping** — which dialogue SHOT this panel covers (e.g. "This is SHOT 1")

**Panel → SHOT mapping:**
- Panel 1 always = SHOT 1 (standalone opening, SHARED-ALL)
- Panels 2-6 = SHOTs 2-5 (Route A/B) or SHOTs 2-7 (Route C, with one SHOT condensed)

**Panel description template:**
```
Panel {N} 【{中文标题}】⬡ {SHARED marker} — {Shot type}, {angle}. {Composition and action}. {Foreground/midground/background}. {Lighting}. {Character expression}. {Emotional subtext}. {Cross-ref if shared}. This is SHOT {N} dialogue beat.
```

**Dimension checklist per panel:**
- Shot type + angle
- Foreground / midground / background elements
- Character expression (micro-expressions: eyebrows, lips, eyes, posture)
- Hand gestures (if POV includes protagonist's hands)
- Props in focus (badge, tablet, book, etc.)
- Light source + quality + direction
- Color temperature (warm vs cool)
- Depth of field notes
- Eye-line / eye contact
- Panel 6: ending card overlay

**Cross-route visual design:**
- Panel 1 (SHARED-ALL) describes identical composition but may have route-specific lighting hints
- Panels marked SHARED-AB explicitly reference their counterpart in the other route
- Route C Panel 1 must be identical to Route A Panel 1 for false-start irony

---

## Design Constraints

1. **⚠️ THREE ROUTES, ALWAYS. Route A, Route B, Route C. Never two. This is the single most important rule. Any file with only 2 routes is INCOMPLETE and MUST be rejected.**
2. **SHOT 1 is standalone** — NPC only, no Player response. Appears ONCE before all routes. Never repeated in B or C.
3. **SHOT 2+ is Player-first** — Player speaks, then NPC responds. One back-and-forth per SHOT.
4. **Route A: 5 SHOTs** (1 standalone + 4 back-and-forth). Good outcome — correct response, warm tone.
5. **Route B: 5 SHOTs** (1 standalone + 4 back-and-forth). Cold/neutral outcome — same structural goal but emotional failure (abrupt, mishear, cold treatment).
6. **Route C: 7 SHOTs** (1 standalone + 6 back-and-forth). Wrong outcome — hesitation/mumbling leads to completely wrong result. Heavier path.
7. **Storyboard: 6 panels per route, always** — independent of SHOT count.
8. **All NPCs Westerners** unless user specifies otherwise.
9. **First-person POV** — camera IS the protagonist. Never see protagonist's face.
10. **One NPC minimum**.
11. **Shared SHOTs mandatory** — SHOT 1 is SHARED-ALL. SHOT 3 and SHOT 4 are SHARED-AB (A and B share structural middle beats).
12. **Fork points mandatory** — Route C SHOT 4 annotated with `🔀 分叉点`.
13. **Storyboard prompts are for image generation** — dense, vivid visual descriptions.
14. **Panel descriptions are visual only** — no dialogue text in panels (except prop text).
15. **Chinese + English mixed** — dialogue English, annotations/titles Chinese, storyboard English.
16. **No explanatory text between SHOTs** — pure SHOT-by-SHOT. Only ending summary after final SHOT.

---

## Quick Reference: SHOT Template

```
### SHOT 1 · 共享开场 ⬡ SHARED-ALL
**{NPC}:** {Dialogue}
*（{中文动作/情绪注记}）*

### SHOT {N} ⬡ {MARKER}
**Player:** {Dialogue}
**{NPC}:** {Response}
*（{中文动作/情绪注记}）*
```

## Quick Reference: Panel Template

```
Panel {N} 【{中文情绪标题}】⬡ {MARKER} — {Shot type}, {angle}. {Composition and action}. {Lighting details}. {Expression and micro-expressions}. {Emotional subtext}. {Cross-ref if shared panel}. This is SHOT {N} dialogue beat.
```

---

## Example Entry

User says: "咖啡店点错单，被当成了另一个人"

Generate `wrong-order-coffee.md` with:
- SHOT 1: Barista calls wrong name (standalone, shared)
- Route A: Politely correct → warm exchange, right drink (SHOTs 2-5)
- Route B: Blunt "that's not mine" → cold treatment, right drink (SHOTs 2-5)
- Route C: Hesitate, take wrong drink → walk away with someone else's latte (SHOTs 2-7)
- Shared A·B: SHOT 3 (barista checks order screen), SHOT 4 (barista hands drink)
- Fork: Route C SHOT 4 where barista asks "wait, aren't you {name}?"
