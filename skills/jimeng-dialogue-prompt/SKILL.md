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

## Required Prompt Structure

Output a single fenced code block containing, in this exact order:

1. **AI-creation disclaimer** (first line):
   `This is an AI-generated [genre] short film using AI-created original characters for creative storytelling, not based on real persons.`

2. **Global specs paragraph** — include all of these phrases:
   - `15-second realistic cinematic [tone] drama`
   - `9:16 vertical format`
   - `ARRI Alexa look with subtle 35mm film grain`
   - Specific lighting (color temp / time of day / physical light source)
   - `shallow depth of field, PBR materials`
   - `realistic skin with [detail] and fine pore detail`
   - `photographic realism, NOT stylized CG, NOT anime, NOT cartoon`

3. **Characters section** — 2 characters, each with:
   - Ethnicity + age + body type
   - Skin tone with specific adjective
   - Eye color + shape
   - Hair (length / texture / style / any accessory)
   - Distinctive features (nose stud / earrings / tattoo / glasses / etc.)
   - Full outfit (top / bottom / accessories / bag / shoes as relevant)
   - Presence descriptor (e.g. "relaxed artistic presence")

4. **Four shots** labelled `Shot 1 【0-3s】` through `Shot 4 【11-15s】`. Each shot contains:
   - Framing (medium close-up / over-the-shoulder / wide / etc.)
   - Camera angle + movement (eye level / low angle / push-in / static / handheld)
   - Physical action described as **muscle/movement language, not emotion words** (e.g. "eyebrows pull together" not "she looks confused")
   - Exactly one line of dialogue formatted: `[Character] says [tone adverb] in English: "..."`

5. **Environment details paragraph** — specific, physically-motivated details (not decorative): props, background blur, dust motes, ambient sound description. End with: `No subtitles on screen, no background music, only natural dialogue in English, [specific ambient sounds].`

6. **Negative prompt line** — must include all of these baseline blockers:
   ```
   NO subtitles, NO text overlay, NO music, NO cartoon, NO anime, NO plastic skin, NO over-smoothed faces, NO weapons, NO blood, NO violence, NO logos, NO brand names, NO horror imagery, NO non-English dialogue, NO [local language] spoken words, NO foreign language in dialogue.
   ```

---

## Jimeng Review-Safe Checklist (MUST pass before output)

Before finalizing, scan the draft for these review-triggering words/concepts and rewrite:

| ❌ Don't write | ✅ Write instead |
|---|---|
| blood / bleeding / wound | dust smudges / sweat / flushed cheeks |
| weapon / gun / knife / sword | (remove entirely) |
| dead body / corpse / soldier | (remove entirely) |
| mercenary / assassin / hitman | explorer / traveler / technician |
| exosuit / tactical harness / military | technical jacket / utility belt |
| haunted / cursed / ghost / demon | (drop the genre — user rejected horror/mystery) |
| enemy / pursuers / ambush | natural threat (sandstorm / sealed path / weather) |
| race/ethnicity words in negative prompt | only technical blockers in negative |

Also: no alcohol, no cigarettes if avoidable (if user loved a smoking detail earlier, keep it but flag it; default to no smoking), no religious specifics in close-up, no brand names, no real celebrity likenesses.

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

## Output Template Skeleton

Fill this template, then output. Do NOT show the template itself to the user, only the filled result.

```
This is an AI-generated {GENRE} short film using AI-created original characters for creative storytelling, not based on real persons.

15-second realistic cinematic {TONE} drama, {SCENE_ONE_LINER}, {LOCATION_DETAIL}, 9:16 vertical format, ARRI Alexa look with subtle 35mm film grain, {LIGHTING_PHYSICAL_DESCRIPTION}, {COLOR_PALETTE}, shallow depth of field, PBR materials, realistic skin with {SKIN_DETAIL} and fine pore detail, photographic realism, NOT stylized CG, NOT anime, NOT cartoon.

Characters:
{LEAD_NAME} — {ETHNICITY} {ROLE} in {AGE_RANGE}, {BODY_TYPE}, {SKIN_TONE}, {EYES}, {HAIR}, {DISTINCTIVE_FEATURES}, wearing {OUTFIT}, {PROPS_CARRIED}, {PRESENCE}.
{PARTNER_NAME} — {ETHNICITY} {ROLE} in {AGE_RANGE}, {BODY_TYPE}, {SKIN_TONE}, {EYES}, {HAIR}, {DISTINCTIVE_FEATURES}, wearing {OUTFIT}, {PROPS_CARRIED}, {PRESENCE}.

Shot 1 【0-3s】{FRAMING}, {ANGLE}, {CAMERA_MOVEMENT}. {PHYSICAL_ACTION_IN_MUSCLE_LANGUAGE}. {SPEAKER} says {TONE} in English: "{LINE_1}"

Shot 2 【3-7s】{FRAMING}, {ANGLE}, {CAMERA_MOVEMENT}. {PHYSICAL_ACTION_IN_MUSCLE_LANGUAGE}. {SPEAKER} says {TONE} in English: "{LINE_2}"

Shot 3 【7-11s】{FRAMING}, {ANGLE}, {CAMERA_MOVEMENT}. {PHYSICAL_ACTION_IN_MUSCLE_LANGUAGE}. {SPEAKER} says {TONE} in English: "{LINE_3}"

Shot 4 【11-15s】{FRAMING}, {ANGLE}, {CAMERA_MOVEMENT}. {PHYSICAL_ACTION_IN_MUSCLE_LANGUAGE}. {SPEAKER} says {TONE} in English: "{LINE_4}"

Environment details: {5_TO_8_SPECIFIC_PROPS_AND_BACKGROUND_ELEMENTS}, {AMBIENT_PARTICLES_OR_WEATHER}. Subtle handheld micro-movement on camera. No subtitles on screen, no background music, only natural dialogue in English, {AMBIENT_SOUNDS}.

Negative prompt: NO subtitles, NO text overlay, NO music, NO cartoon, NO anime, NO plastic skin, NO over-smoothed faces, NO weapons, NO blood, NO violence, NO logos, NO brand names, NO horror imagery, NO non-English dialogue, NO {LOCAL_LANGUAGE} spoken words, NO foreign language in dialogue.
```

---

## Reply Format

After the prompt code block, add a short section (in 中文, matching the user's language):

1. **🌟 这版的新意** — a small table explaining what makes this version different from prior ones (new location, new lead appearance, new arc)
2. **✅ 过审清单** — 3-5 bullets confirming review-safe choices
3. **下一站？** — invite the user to give another sentence or pick a next location

Keep it tight. The user is iterating fast — don't bloat the response.

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
