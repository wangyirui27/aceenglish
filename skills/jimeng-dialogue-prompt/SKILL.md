---
name: jimeng-dialogue-prompt
description: Generate a ready-to-paste 15-second Jimeng (即梦) text-to-video prompt for a two-person English-dialogue short drama. Use this whenever the user gives an English sentence and asks for a 15-second two-person dialogue storyboard / video prompt / 双人对话分镜 for Jimeng, Seedance, or similar Chinese text-to-video tools. Produces one single English prompt block that contains the scene, both characters, 4 shots with timecodes, 4 lines of dialogue baked in, environment details, and a negative prompt — all tuned for Jimeng's review policy and the user's preference for real-person photographic style.
allowed-tools:
  - Bash
  - Read
---

# Jimeng 15-Second Two-Person Dialogue Prompt Generator

This skill encodes the full workflow developed for Ace English's 即梦文生视频 pipeline. When the user gives you an English target sentence (often an English-learning high-frequency phrase) and asks for a **15-second two-person dialogue** video prompt, follow this skill exactly.

---

## When to Use

Trigger on any of these signals:
- User provides an English sentence + asks for "15秒双人对话 / 双人对话分镜 / 文生视频提示词 / 丢给即梦"
- User mentions 即梦 / Seedance / Jimeng and wants a dialogue scene
- User is working on 短剧 / 英语学习短剧 / Ace English content

Do **not** use this skill for:
- Single-character monologues
- Non-dialogue videos
- Image generation (that's a different flow)

---

## Core Principles (non-negotiable)

1. **Real-person photographic style only** — never anime, never stylized CG.
2. **Exactly 4 shots, exactly 4 dialogue lines** (2 rounds of dialogue). Timecodes: `0-3s`, `3-7s`, `7-11s`, `11-15s`.
3. **All dialogue in English only.** Explicitly write "says ... in English" for each line. Add `NO non-English dialogue` / `NO [local language] spoken words` to negative prompt.
4. **Every female lead must be visually distinct from any previous session's lead.** Rotate across: ethnicity (Asian / Black / Latina / Middle Eastern / mixed European / etc.), body type (slim / athletic / curvy), hair (straight / curly / braided / locs / undercut / bangs), style signifiers (glasses / nose stud / henna / hoops / tattoos). Pick something you haven't used recently. This rule exists because the user called out repeated-face on earlier outputs.
5. **Genre default = real-world travel / slice-of-life / warm human encounter.** Do NOT default to sci-fi, horror, mystery, thriller unless the user explicitly asks for that genre. This was a hard user preference correction.
6. **One single prompt block, English, pasteable as-is into Jimeng.** Never split into multiple prompts — Jimeng supports 15s one-shot generation.
7. **i+1 level mixing (comprehensible input) — RELATIVE, not absolute.** First, **assess the actual CEFR level of the current scene/lesson yourself** (look at sentence length, grammar, vocabulary frequency, visual complexity). Then seed **1-2 words from exactly one level above** your assessed level. Do NOT apply a fixed "A2 + B1" rule regardless of actual lesson difficulty — that would overshoot easy lessons and undershoot hard ones. The seeded word must be **inferrable from visual context**.

   Examples:
   - If the scene is A0+ (very basic "This is X / What's this"), seed 1 A1 word like "actually" or "over there"
   - If the scene is A1 (basic spatial / possession), seed 1-2 A1+/A2 words like "grab", "spare", "hang on"
   - If the scene is A2 (complex noun phrases, multi-clue tasks), seed 1-2 B1 words like "figure out", "in a rush", "make it work"

---

## i+1 Vocabulary Layering (how to pick the seeded words)

Goal: make dialogue feel **real** (not textbook-flat) while staying listenable.

**Good seeds** (natural, frequent, context-clear):
- Discourse fillers: `actually, probably, anyway, well, by the way`
- Informal verbs: `grab, hang on, figure out, check on, look after`
- Emphasis words: `totally, seriously, honestly, definitely`
- Soft qualifiers: `a bit, kind of, sort of, pretty + adj`
- Common idioms tied to action on screen: `in a rush, no worries, my bad, hold on`

**Bad seeds** (avoid):
- Academic / formal words (`nevertheless, furthermore, consequently`)
- Low-frequency vocabulary (`ambiguous, meticulous, rudimentary`)
- Multi-word phrasal verbs with non-obvious meaning (`put up with, come across as`)
- Anything the picture can't explain

**Placement rule**: put the seeded word in the character's line that has the **strongest matching visual cue**. If the line is "I'll grab a spare charger", the camera should show them actually grabbing a charger — the visual IS the definition.

**Counter per 15s script**: max 2 seeded B1 words total across all 4 lines. Never stack 2 new words in the same sentence.

---

## Dramatic Density Rule (CRITICAL — prevents boring A0/A1 scenes)

**The problem**: When dialogue is intentionally simple (A0-A2 for English-learning listening content), the scene feels flat and childish if the visual storytelling doesn't compensate. Simple lines × bland visuals = textbook energy, not short-drama energy.

**The principle**: Dialogue dictates what characters *say*, not what's *happening*. Even with 4 short A0 lines, a 15-second scene must feel like a slice of a real adult life with real stakes, real relationships, and real atmosphere.

**The rule**: Every 15s script must enrich **at least TWO** of these four non-dialogue dimensions:

1. **Situational weight (情境)** — give the character a small predicament. Are they running late? Just got bad news? Their hands are full? Something spilled? The simple line "Where's my phone?" hits completely differently when the character is juggling three things in the rain vs sitting calmly at a clean desk.

2. **Relational tension (关系)** — two people in the scene have a micro-dynamic beyond "friendly coworkers." Maybe one has a crush. Maybe they're in a quiet disagreement. Maybe one is a mentor who's proud of the other. Convey this through glances, body angle, micro-pauses, physical distance — NOT through extra dialogue.

3. **Environmental storytelling (环境)** — time of day, weather, light quality, ambient activity in the background, sound layers. Rain-just-stopped morning ≠ exhausted late-afternoon ≠ bright lunchtime. Pick one with specific atmosphere, not generic "office daytime."

4. **Unspoken narrative hooks (钩子)** — small visual details the dialogue does NOT mention but the audience notices: a half-eaten breakfast, a jacket draped over the chair back, a notification buzzing on screen, a specific photo frame, a trembling hand, an eye-line that lingers half a second too long. These create micro-story seeds without stealing focus from the learning target.

**What to avoid**:
- ❌ Characters standing in clean empty rooms delivering lines like props.
- ❌ "Generic friendly smile" on both faces the whole time.
- ❌ Backgrounds that are visually busy but narratively empty (just decoration).
- ❌ Anything that competes with the target dialogue for attention (e.g. a TV playing in the background, loud argument elsewhere).

**The test**: After writing the 4 shot descriptions, ask yourself: "If I muted this video entirely, would I still feel like something is happening to these people?" If the answer is no, add situational weight or relational tension until the answer is yes.

**Example — same line, two treatments**:

| Line | Flat version | Dense version |
|---|---|---|
| "Where's my phone?" | Alex at a tidy desk, calmly asks Maya. She points. He picks it up. | Alex just hung up a tense video call, rubs his temple, pats his pocket. He starts flipping through scattered papers with slightly shaking hands. Maya arrives carrying two coffees, reads his stress in one glance, gently says "It's next to the laptop." Camera catches the phone screen still lit with "Mom: call me back". He stares for two seconds before picking it up. |

Both have the same 4-5 words of target dialogue. One is forgettable. The other makes the viewer care.

---

## Spatial Asymmetry Rule (the single biggest quality multiplier)

**Default human intuition for "two-person dialogue" = two people sitting across a table at equal height.** This is the most boring choice possible and must be actively avoided unless the scene specifically requires it (e.g. restaurant, interview).

Instead, stage the two characters with **asymmetrical spatial relationships** that create automatic visual interest:

| Asymmetry type | Example | Why it works |
|---|---|---|
| **Upper / Lower** | One on balcony, one on street. One on stairs, one at the bottom. One standing, one sitting on the floor. | Creates natural high-angle + low-angle shots; forces looking-up / looking-down body language; amplifies "help-giver / help-seeker" dynamics |
| **Inside / Outside** | One inside a shop, the other at the doorway. One in a car, the other at the window. | Creates doorway/window framing; adds a physical boundary that dialogue crosses |
| **Near / Far (depth)** | One in foreground, the other deep in background walking closer. | Forces push-in / pull-back camera moves; creates "arrival" moments |
| **Stationary / Moving** | One sitting, the other walking past or approaching. | Creates narrative direction; the moving character carries the scene forward |
| **Doing / Waiting** | One actively doing something (cooking, folding laundry, fixing a bike), the other asking a question. | The active character's props become additional visual storytelling tools |

**The test**: draw a stick-figure diagram of your two characters in the scene. If the diagram is two circles at the same height facing each other, you've defaulted. Redesign.

**The landmark reference**: the Cinque Terre Vernazza scene (landlady on balcony, backpacker on cobbled street below, Italian grandma holding a bed sheet while answering) — this was the team's favorite output and it's almost entirely because of the up/down + stationary/arriving + doing/asking asymmetries stacked together.

---

## Hook Typology (what kind of ending your 15s should have)

The final line of a 15s short must leave **emotional residue**. Pick the right hook type for the tone of the scene:

| Hook type | When to use | Example | Feeling left with viewer |
|---|---|---|---|
| **Invitation hook** 🫂 | Warm / slice-of-life / travel / everyday kindness | "Come back tonight — I make pasta!" / "Want to grab coffee later?" | "I wish someone treated me like that" |
| **Anticipation hook** ✨ | Discovery / arrival / first-time scenes | "I heard it's magical at sunset." / "Wait till you see what's upstairs." | "I want to see what happens next" |
| **Realization hook** 💡 | Learning / help / small epiphany | "Ohh, so it's not about actual beans?" / "Oh, I was looking in the wrong place." | "A tiny joy of understanding" |
| **Warmth-shift hook** 🌅 | When the scene has emotional arc (guarded → open) | "...Come inside. Let me see it." / "Alright — I'll help you." | "Two strangers just became human to each other" |
| **Suspense hook** ❓ | ONLY for mystery / thriller tone | "...What do you mean?" | "I need episode 2 right now" — but user rejected this genre, so avoid |

**Default for Ace English content = Invitation / Anticipation / Realization.** Never default to Suspense — user explicitly rejected horror/mystery genres.

**Anti-pattern**: ending a 15s scene on a flat "Thanks, bye." or "Okay, see you." — that's not a hook, that's a period. The hook should slightly crack the scene open so the viewer wants to keep the world alive in their head.

---

## How to Read User Prompts (meta-insight on constraint quality)

The team's favorite output so far came from the user prompt: *"再来一个：I'll be staying at this hotel. 加入一个前提，背景必须是出国旅行"*. Why this produced a great scene:

1. **"再来一个" = implicit "don't repeat"** — forces you to differ from every prior scene on every axis (lead appearance, location, relationship, emotional arc). Don't take shortcuts; actively rotate.
2. **The target line was dramatically *flat*** — "I'll be staying at this hotel" has zero built-in tension. This is a gift: it forces the *scene* to carry all narrative weight, which produces richer visuals than a dramatic line would. Simple lines → richer pictures.
3. **"Must be abroad" = half-tight, half-loose constraint** — specific enough to rule out domestic settings, loose enough to leave country/culture/vibe fully open. This is the ideal constraint shape for creativity.

**Takeaway when user gives you a line + constraint**:
- Treat the line's flatness as a green light to invent rich circumstances around it, not as a limitation.
- When the constraint is "half-tight half-loose", use that freedom to find **specific + non-cliché** locations (Vernazza, Marrakech — not Paris / Tokyo / NYC).
- When the user says "再来一个" / "another one" / "next", enforce the **non-repetition rule hard**: new ethnicity, new age, new profession, new emotional arc, new spatial staging, new hook type.

---

## Prompt Language: Chinese for prompt body, English for dialogue lines

**The entire Jimeng prompt is written in Chinese** (scene description, character description, shot descriptions, environment details, negative prompt) — because:
1. Jimeng is a Chinese model, Chinese prompts are understood more accurately
2. Chinese tokens are ~30-40% more efficient than English tokens for the same meaning
3. Saves token budget for richer visual detail

**Exception: dialogue lines stay in English** — because the target learning language is English. Each dialogue line is explicitly formatted as: `[角色]用英语说道："..."`

---

## Required Prompt Structure

Output a single fenced code block containing, in this exact order:

1. **AI声明**（第一行）：
   `这是一个AI生成的[类型]短片，使用AI原创角色进行创意叙事，不基于真实人物。`

2. **全局规格段落** — 必须包含以下关键词：
   - `15秒写实电影感[情绪]短剧`
   - `9:16竖屏`
   - `ARRI Alexa质感，35mm胶片颗粒感`
   - 具体光源描写（色温 / 时间段 / 物理光源）
   - `浅景深，PBR材质`
   - `真实皮肤质感，[细节描写]，毛孔清晰可见`
   - `摄影写实风格，非CG，非动漫，非卡通`

3. **角色段落** — 2个角色，每个包含：
   - 民族 + 年龄 + 体型
   - 肤色（具体形容词）
   - 眼睛颜色+形状
   - 头发（长度/质感/发型/配饰）
   - 特征（鼻钉/耳环/纹身/眼镜等）
   - 完整穿搭（上衣/下装/配饰/包/鞋）
   - 气质描写（如"沉稳的导师感"）

4. **四个镜头**，标注为 `镜头一【0-3s】` 到 `镜头四【11-15s】`。每个镜头包含：
   - 景别（中近景/过肩/全景等）
   - 机位角度+运动（平视/低角度/推进/固定/手持）
   - **用肌肉/动作语言描写**角色物理动作（如"眉心微皱"而不是"她看起来困惑"）
   - 恰好一句台词，格式：`[角色]用英语说道："..."`

5. **环境细节段落** — 具体的、有物理依据的细节（不是装饰性堆砌）：道具、背景虚化、光线粒子、环境音描写。结尾：`画面无字幕，无背景音乐，仅有英语自然对话和[具体环境音]。`

6. **负面提示词** — 必须包含以下全部基础阻断词：
   ```
   无字幕、无文字覆盖、无音乐、无卡通风格、无动漫、无塑料皮肤、无过度磨皮、无武器、无血腥、无暴力、无品牌标志、无商标、无恐怖画面、无非英语对话、无[当地语言]口语、无外语对话。
   ```

---

## Jimeng Review-Safe Checklist (MUST pass before output)

Before finalizing, scan the draft for these review-triggering words/concepts and rewrite:

| ❌ 不要写 | ✅ 改成 |
|---|---|
| 血/流血/伤口 | 汗水/灰尘/脸颊泛红 |
| 武器/枪/刀/剑 | （直接删除） |
| 尸体/死者/士兵 | （直接删除） |
| 雇佣兵/杀手/刺客 | 探险家/旅行者/技师 |
| 外骨骼/战术装备/军用 | 技术外套/工具腰带 |
| 闹鬼/诅咒/鬼魂/恶魔 | （换题材——用户拒绝恐怖/悬疑） |
| 敌人/追兵/伏击 | 自然威胁（暴风雪/封路/天气） |
| negative prompt里的种族/民族词 | 只用技术类阻断词 |

另外：尽量不出现酒精、烟（如果用户特别喜欢某个抽烟细节可以保留但需标注；默认不抽烟）、特写不要有宗教具体符号、不要品牌名、不要真实名人肖像。

---

## Proper Nouns Rule

Local-language proper nouns (hotel names, landmarks, neighborhoods) **are allowed** inside English dialogue because they read as names, not foreign speech. Examples that passed: `Casa Marina`, `Jemaa el-Fnaa`, `Shibuya`. Use them — they boost place realism.

But do NOT include full foreign phrases like `Buongiorno!`, `Sì sì`, `Merci beaucoup`. User explicitly asked for English-only dialogue.

---

## Character Rotation Memory

Keep a running mental list across the conversation of every female lead already used. Each new request must introduce a lead who differs on **at least 2 of these axes** from every prior lead in this session:
- Ethnicity
- Hair (color / texture / length / style)
- Body type
- Age bracket
- Signature accessory (glasses / piercing / tattoo / hat)
- Clothing palette

If the user says "再来一个" / "continue" / "next one", assume it's a new scene in the same session and rotate.

---

## Emotional Arc Template (pick one per scene)

Every 15-second dialogue must have a clear 4-beat arc. Pick one:
- **Confusion → relief → gratitude → warmth** (classic learning/help)
- **Initial disconnect → breakthrough → realization → shared laugh**
- **Tired/lost → kindness offered → guard drops → hope lifts**
- **Curiosity → information → new curiosity → anticipation**
- **Guarded → melted by warmth → vulnerability → invitation**

Avoid flat "just friendly chat" — there must be a small emotional turn.

---

## Spatial Language Tricks (avoid visual monotony)

Don't default to "two people sitting across a table." Rotate staging:
- Up/down (balcony vs street, stairs, hill)
- Past/toward each other (walking toward, one leaving)
- Over a shared object (map, phone screen, photo, suitcase)
- One seated / one standing
- Through a window / doorway / vehicle

---

## Output Template Skeleton (Chinese prompt body, English dialogue lines)

Fill this template, then output. Do NOT show the template itself to the user, only the filled result.

```
这是一个AI生成的{类型}短片，使用AI原创角色进行创意叙事，不基于真实人物。

15秒写实电影感{情绪}短剧，{场景一句话描术}，{地点细节}，9:16竖屏，ARRI Alexa质感，35mm胶片颗粒感，{光源物理描写}，{色板}，浅景深，PBR材质，真实皮肤质感，{皮肤细节}，毛孔清晰可见，摄影写实风格，非CG，非动漫，非卡通。

角色：
{角色名}——{民族}{身份}，{年龄段}，{体型}，{肤色}，{眼睛}，{头发}，{特征}，穿着{穿搭}，{手持道具}，{气质}。
{角色名}——{民族}{身份}，{年龄段}，{体型}，{肤色}，{眼睛}，{头发}，{特征}，穿着{穿搭}，{手持道具}，{气质}。

镜头一【0-3s】{景别}，{机位}，{运镜}。{肌肉动作描写}。{角色}用英语说道："{台词1}"

镜头二【3-7s】{景别}，{机位}，{运镜}。{肌肉动作描写}。{角色}用英语说道："{台词2}"

镜头三【7-11s】{景别}，{机位}，{运镜}。{肌肉动作描写}。{角色}用英语说道："{台词3}"

镜头四【11-15s】{景别}，{机位}，{运镜}。{肌肉动作描写}。{角色}用英语说道："{台词4}"

环境细节：{5-8个具体道具和背景元素}，{光线粒子或天气}。手持微晃镜头。画面无字幕，无背景音乐，仅有英语自然对话，{环境音}。

负面提示词：无字幕、无文字覆盖、无音乐、无卡通风格、无动漫、无塑料皮肤、无过度磨皮、无武器、无血腥、无暴力、无品牌标志、无商标、无恐怖画面、无非英语对话、无{当地语言}口语、无外语对话。
```

---

## Reply Format

After the prompt code block, add a short section (in 中文, matching the user's language):

1. **🌟 这版的新意** — a small table explaining what makes this version different from prior ones (new location, new lead appearance, new arc)
2. **✅ 过审清单** — 3-5 bullets confirming review-safe choices
3. **下一站？** — invite the user to give another sentence or pick a next location

Keep it tight. The user is iterating fast — don't bloat the response.

---

## Dialogue Naturalness (CRITICAL — all lines must sound like real speech, not textbook)

This skill is used for English-learning content. The temptation is to write "correct" English that reads like a textbook example. **Resist this.** Every line of dialogue must sound like something a real person would actually say in the scene.

**Checklist — apply to EVERY line before output:**

| Textbook English ❌ | Real Spoken English ✅ | Why |
|---|---|---|
| "This is Maya. She is your partner today." | "This is Kai — he'll help you today." | Contractions, natural phrasing |
| "It is a trumpet." | "A trumpet." | Drop obvious subjects when context is clear |
| "Nice to meet you. How are you?" | "Hey!" / "Oh — hi!" | Real people use minimal greetings |
| "Where are my keys? I cannot find them." | "My keys? ...Where are my keys?" | Repetition, fragments, trailing off |
| "Please take the blue cup." | "The blue one." / "Can you grab the blue cup?" | Polite but not robotic |
| "Is this your phone? It was on the seat." | "This yours? — was on the back seat." | Dropping subjects, combining sentences |
| "I am new here. This is my first day." | "New girl? Over here." | Context makes full sentences unnecessary |

**Core principles:**
1. **Use contractions always** — he's, she's, it's, don't, can't, won't, I'm, that's
2. **Drop subjects when context is clear** — "A trumpet." not "It is a trumpet." / "My keys?" not "Where are my keys?"
3. **Use fragments** — "Over here." / "By the door." / "The blue one."
4. **Allow hesitation in dialogue** — "This is… yours?" (the pause IS the realism)
5. **Use casual openers** — "Hey" / "Oh" / "So" / "Well" / "Right"
6. **Don't over-explain in dialogue** — if the visual shows it, the character doesn't need to say it
7. **Keep it SHORT** — real spoken sentences in casual settings are 2-7 words, rarely more

**The test**: read each line out loud. If it sounds like something you'd say to a friend, it's good. If it sounds like a line from an English textbook, rewrite it.

**Important**: contractions and fragments do NOT raise the CEFR level. "A trumpet." is still A0. "This is Kai — he'll help you today." is still A0-A1. Naturalness ≠ difficulty.

---

## Scene Selection for Learning Content (how to pick a scene that carries simple dialogue)

When designing a scene for English-learning content, the scene must carry ALL the narrative weight because the dialogue is intentionally simple (A0-A2). This means the scene choice is the single most important design decision.

**The principle**: Simple dialogue × flat scene = boring. Simple dialogue × rich scene = powerful.

**What makes a scene "rich":**
- The character has a **micro-predicament** (lost, confused, embarrassed, late, overwhelmed, new)
- The scene has a **built-in emotional arc** (tension → resolution, or curiosity → discovery)
- The space has **natural asymmetry** (different heights, through a window, across a counter)
- The scene has a **built-in hook** (an invitation, a discovery, a small kindness that lingers)

**What makes a scene "flat":**
- Characters just exchanging information with no stakes
- "Meet and greet" with no emotional texture
- Two people at the same height in a neutral space
- Ending on "Thanks, bye." with no residue

**Examples:**

| Scene type | Flat version | Rich version |
|---|---|---|
| Introducing people | Three people stand in a clean office, shake hands | A nervous newcomer holds a lumpy clay bowl in a dusty pottery workshop, the master potter calls her over from his wheel |
| Finding objects | Someone calmly asks "Where's my phone?" at a tidy desk | A person just hung up a tense call, is juggling three things in the rain, pats their pocket in panic |
| Giving directions | "The elevator is over there." in a generic lobby | An elderly woman with a suitcase squints at signs in a foreign airport, a volunteer points gently toward the far gate |

**The "mute test" for scene selection**: Before designing the scene, imagine it as a silent video. Would you still feel like something is happening to these people? If yes, the scene is rich enough. If no, add predicament, relationship texture, or environmental stakes.

**Never choose a scene where the ONLY thing happening is the dialogue.** The dialogue should feel like a small moment inside a bigger world that's already in motion.

---

## Difficulty vs. Dramatic Density (they are independent dimensions)

**A common mistake**: assuming that simple dialogue (A0) requires simple visuals. This is WRONG.

- **Dialogue difficulty** = what words and grammar the characters use (controlled by CEFR level)
- **Visual richness** = how much is happening in the scene (controlled by scene design)

These two dimensions are completely independent. You can have:
- Simple dialogue + rich visuals = ✅ (the Cinque Terre scene — A0 dialogue, five-star visuals)
- Simple dialogue + flat visuals = ❌ (textbook energy)
- Complex dialogue + flat visuals = 😐 (academic lecture feel)
- Complex dialogue + rich visuals = ✅ (but not relevant for A0-A2 learning content)

**The takeaway**: When the user constrains dialogue difficulty (e.g., "this is A0 level"), do NOT constrain visual richness. In fact, **the simpler the dialogue, the MORE you should invest in visual richness** — because the scene has to carry all the engagement on its own.

---

## Standard Workflow for Level-Based Scene Design

When the user gives you a **level (A0/A1/A2/B1…)** and **target vocabulary/sentences** for a lesson, follow this exact workflow:

### Step 1: Assess the actual CEFR level
- Read the target vocabulary/sentences
- Assess the real level based on: sentence length, grammar complexity, vocabulary frequency, typical learner profile
- If the user says "A2" but the sentences are all 2-3 word fragments, the real level might be A1 — trust your assessment, not the label

### Step 2: Calculate the seed word level
- **Seed level = assessed level + exactly 1**
- A0 → seed A1
- A0+ → seed A1
- A1 → seed A1+
- A2 → seed A2+
- A2- → seed A2
- A2 → seed B1
- **Never skip levels.** If assessed level is A0+, the seed MUST be A1 — not A2, not A1+

### Step 3: Choose a scene with dramatic weight
- Use the Scene Selection criteria above
- The scene must have: a predicament + an emotional arc + spatial asymmetry
- **Do NOT default to the most obvious scene** for the target language. "What's this?" doesn't have to be in a classroom — try a backstage jazz room, a flea market, a pottery workshop

### Step 4: Write 4 lines of dialogue (15 seconds)
- Must cover 1-3 of the target vocabulary/sentences from the user's lesson
- Seed exactly 1-2 words from the seed level
- Apply Dialogue Naturalness checklist to every line
- **Target words should be the ones the user explicitly asked to teach** — don't invent new targets

### Step 5: Design the 4 shots
- Apply Spatial Asymmetry Rule (stick-figure test)
- Apply Dramatic Density Rule (at least 2 of 4 dimensions: predicament / relationship / environment / hook)
- Apply Hook Typology (invitation / anticipation / realization for Ace content)
- Every shot must use muscle/movement language, never emotion words

### Step 6: Write the full Jimeng prompt
- Follow Required Prompt Structure exactly
- Pass Jimeng Review-Safe Checklist
- Character Rotation: new names + new ethnicity + new look vs. every prior scene in this session

### Step 7: Verify
- [ ] All dialogue is English only
- [ ] All dialogue sounds like real speech (Dialogue Naturalness)
- [ ] Seed word(s) are exactly 1 level above assessed level
- [ ] Seed word has matching visual cue in the shot
- [ ] At least 2 of 4 Dramatic Density dimensions enriched
- [ ] Spatial Asymmetry applied (stick-figure ≠ two circles at same height)
- [ ] Hook type selected and last line delivers it
- [ ] No Jimeng review triggers
- [ ] Characters visually distinct from all prior scenes in session
- [ ] Target vocabulary from user's lesson is present in dialogue

### Input format (what user will give you)

The user will typically provide something like:

```
关卡：2-5 拿蓝色那个
难度：A1
语言焦点：Which one? / The red one. / The blue cup. / Not that one. / Yes, that one.
```

Or simply:
```
学这句话：Where are my keys?
```

Or:
```
词汇：wallet, keys, charger
短语：Is this your ___? / It's mine.
级别：A1
```

In all cases: extract the target language, assess the real level, pick a scene, and go.

---

## Failure Modes to Avoid

- ❌ Writing the dialogue in Chinese and then the rest in English. Dialogue must be English.
- ❌ Mixing foreign phrases into dialogue lines (Buongiorno, Sì, Merci).
- ❌ Repeating the same "cute Asian girl with glasses" lead across sessions.
- ❌ Defaulting to sci-fi / cyberpunk / mystery / horror — user rejected these.
- ❌ Including `blood / weapon / dead / ghost / violence` anywhere in the prompt.
- ❌ Writing emotion words ("she feels sad") instead of muscle language ("her brow furrows, lower lip tightens").
- ❌ Forgetting the AI-creation disclaimer on line 1.
- ❌ Forgetting to add `in English` after each `says`.
- ❌ Negative prompt missing the non-English dialogue blocker.

---

## Reference — prior Ace English scenes that passed review

- 📍 Cinque Terre (Italy) — suitcase + balcony landlady, "I'll be staying at this hotel"
- 📍 Marrakech (Morocco) — Petit Taxi + fez driver, "To the city center, please"

Don't reuse these locations in the same session. Fresh destination each time (Kyoto / Chiang Mai / Reykjavik / Cape Town / Buenos Aires / Lisbon / Hanoi / Istanbul / Cusco / Oaxaca / Dublin / Prague are all good untapped options).
