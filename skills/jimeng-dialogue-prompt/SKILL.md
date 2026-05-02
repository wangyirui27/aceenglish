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
