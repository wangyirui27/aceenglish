# AI微表情精准控制指南

## 核心认知

微表情是AI最容易露馅的地方。控制不好的根本原因：你在描述"感觉"而不是"过程"。

## 三个方法

### 方法一：控制情绪强度（不写=默认最大值）

**问题**：直接写情绪结果 → AI默认最大值 → 微表情变成大表情

**解决**：先限制情绪幅度，AI才会走微表情路径

| 情绪 | ❌ 直接写 | ✅ 控制强度 |
|------|----------|-----------|
| 开心 | happy | slight smile, subtle joy, hint of amusement |
| 悲伤 | sad | eyes slightly downcast, faint melancholy |
| 愤怒 | angry | jaw slightly tightened, controlled irritation |
| 惊讶 | surprised | eyebrows slightly raised, brief widen of eyes |
| 害羞 | shy | barely noticeable blush, glance downward |

**关键词参考**：`subtle`, `slight`, `faint`, `barely noticeable`, `restrained`, `understated`, `mild`

### 方法二：给微表情一个发生原因（动作驱动情绪）

**问题**：只写表情 → 像摆拍 → 假

**解决**：加上伴随的身体变化/半身动作，让AI构建完整姿态

| 情绪 | ❌ 只写表情 | ✅ 加动作驱动 |
|------|-----------|-------------|
| 害羞 | shy expression | glances away while tucking hair behind ear |
| 紧张 | nervous look | fingers tapping on table, swallowing subtly |
| 心虚 | guilty face | avoids eye contact, rubs the back of neck |
| 思考 | thinking | chin resting on hand, eyes drifting to the side |
| 压抑 | suppressed anger | grips cup tightly, jaw clenching slightly |

**关键词参考**：`while doing...`, `as she/he...`, `accompanied by...`, `subtle body language`

### 方法三：给情绪加时间顺序（过程而非结果）

**问题**：只写最终状态（他笑了）→ 截图脸 → 静态

**解决**：描述变化过程，让AI生成"正在发生的画面"

| 情绪 | ❌ 写结果 | ✅ 写过程 |
|------|---------|---------|
| 笑 | she smiles | her lips slowly curl into a smile |
| 紧张 | he is nervous | his smile fades as he notices the danger |
| 哭 | she cries | her eyes well up, lips tremble before tears fall |
| 愤怒 | he gets angry | his expression shifts from calm to cold fury |
| 惊喜 | she is surprised | her eyes widen gradually, mouth opens in disbelief |

**关键词参考**：`slowly`, `gradually`, `shifts from...to...`, `transition`, `before`, `as realization hits`

## 组合应用示例

> A young woman sitting by the window. Her fingers pause on the book she's reading. She glances up slowly, eyes distant, lips parting slightly as if about to say something — then she looks away, a faint melancholy settling across her face.

拆解：
- 强度控制：`faint melancholy`（不是大悲）
- 动作驱动：`fingers pause`, `glances up`, `looks away`
- 时间顺序：先停顿→抬头→嘴唇微张→看向别处→情绪浮现

## 关联知识
- 参见：`AI微表情演技控制指南.md`
- 参见：`AI视频活人感制作秘诀.md`
- 参见：`AI反向提示词法_皮肤真实感指南.md`
