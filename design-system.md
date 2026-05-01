# 🎨 Design System Specification v2.0
# 主色调：#FF600F

---

## 0. 设计哲学 Design Philosophy

ACE 的视觉性格：**沉浸式暗黑 + 橙色活力**。

核心原则：让用户感觉自己在刷短视频，不是在上课。设计像 TikTok/抖音一样让人上瘾，不像 Duolingo 一样卡通。

- **沉浸感优先** — 纯黑底色 + 大面积留暗，让内容（视频、字幕）成为绝对主角
- **橙色是信号灯，不是油漆** — 橙色只在关键时刻出现（CTA、价格、进度完成、紧迫感），不大面积铺色
- **呼吸感** — 信息密集区域之间必须有留白缓冲，避免视觉疲劳
- **触手可及** — 所有关键操作（购买、收藏、跟读）都在拇指热区内，单手可达
- **暗中发光** — 利用 glow/shadow 让关键元素在暗背景上"浮起来"，引导视线

### DO / DON'T

| ✅ DO | ❌ DON'T |
|-------|---------|
| 用橙色 glow 让 CTA 按钮"浮起" | 用大面积橙色背景抢视觉焦点 |
| 用 `--bg-1` / `--bg-2` 层级制造卡片深度 | 用边框线分割内容（用阴影和间距代替）|
| 动效快速、干脆（200-300ms） | 动效缓慢、花哨（超过 500ms 的过渡）|
| 文字用 `--text-2` 做正文，`--text-1` 做标题 | 全部文字都用白色，没有层次 |
| Badge 只用语义色（绿=完成、蓝=进行中、橙=热门）| Badge 随意用色，没有统一语义 |
| 价格用 Display 字级 + 橙色，制造冲击 | 价格和正文用同样字号，淹没在信息里 |
| 底部 CTA 带 backdrop-filter 毛玻璃 | 底部 CTA 用纯色块遮挡内容 |
| 图标统一 line style，stroke-width 1.5 | 混用 line / solid / emoji 风格 |

---

## 1. 色彩系统

### 主色及衍生

| Token | 色值 | 用途 |
|-------|------|------|
| --accent | #FF600F | 主色调·按钮/价格/核心强调 |
| --accent-hover | #E85500 | hover状态 |
| --accent-light | #FF7A33 | 渐变终点/次要强调 |
| --accent-dark | #CC4D0C | pressed状态 |
| --accent-glow | rgba(255, 96, 15, 0.3) | 发光阴影 |
| --accent-subtle | rgba(255, 96, 15, 0.1) | 背景微透 |
| --accent-gradient | linear-gradient(135deg, #FF600F, #FF7A33) | 按钮渐变 |
| --accent-gradient-h | linear-gradient(90deg, #FF600F, #FFB800) | 进度条渐变 |

### 背景层级

| Token | 色值 | 用途 |
|-------|------|------|
| --bg-0 | #000000 | 页面底色 |
| --bg-1 | #111111 | 卡片背景 |
| --bg-2 | #1A1A1A | 嵌套卡片/输入框 |
| --bg-3 | #222222 | hover/分隔线 |
| --bg-accent | #2A1508 | 强调色背景（深底衬托橙色文字）|

### 辅助色

| Token | 色值 | 用途 |
|-------|------|------|
| --secondary | #FFB800 | 星标、金色装饰 |
| --success | #00C853 | 已完成/已上线 |
| --info | #448AFF | 信息标签（开发中）|
| --warning | #FF600F | 复用主色（紧迫感）|
| --error | #FF3B30 | 错误状态 |

### 文字色

| Token | 色值 | 用途 |
|-------|------|------|
| --text-1 | #FFFFFF | 标题/核心信息 |
| --text-2 | #AAAAAA | 正文/描述 |
| --text-3 | #666666 | 弱化/禁用 |
| --text-accent | #FF600F | 价格/强调文字 |

---

## 2. CSS变量声明（直接复制使用）

```css
:root {
  /* 主色 */
  --accent: #FF600F;
  --accent-hover: #E85500;
  --accent-light: #FF7A33;
  --accent-dark: #CC4D0C;
  --accent-glow: rgba(255, 96, 15, 0.3);
  --accent-subtle: rgba(255, 96, 15, 0.1);
  --accent-gradient: linear-gradient(135deg, #FF600F, #FF7A33);
  --accent-gradient-h: linear-gradient(90deg, #FF600F, #FFB800);

  /* 背景 */
  --bg-0: #000000;
  --bg-1: #111111;
  --bg-2: #1A1A1A;
  --bg-3: #222222;
  --bg-accent: #2A1508;

  /* 辅助色 */
  --secondary: #FFB800;
  --success: #00C853;
  --info: #448AFF;

  /* 文字 */
  --text-1: #FFFFFF;
  --text-2: #AAAAAA;
  --text-3: #666666;
  --text-accent: #FF600F;

  /* 间距 */
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 32px;
  --space-2xl: 48px;

  /* 圆角 */
  --radius-sm: 6px;
  --radius-md: 12px;
  --radius-lg: 16px;
  --radius-xl: 20px;
  --radius-full: 999px;
}
```

---

## 3. 字体系统

```css
font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display",
             "Helvetica Neue", "PingFang SC", Arial, sans-serif;
```

| 层级 | 字号 | 字重 | 行高 | 用途 |
|------|------|------|------|------|
| Display | 36px | 800 | 1.2 | 价格数字 |
| H1 | 28px | 700 | 1.3 | 页面主标题 |
| H2 | 20px | 700 | 1.4 | 区块标题 |
| H3 | 16px | 600 | 1.5 | 卡片标题 |
| Body | 14px | 400 | 1.6 | 正文 |
| Caption | 12px | 400 | 1.5 | 辅助文字 |
| Overline | 11px | 600 | 1.4 | 标签/badge文字 |

---

## 4. 间距使用策略

间距不只是数值，是节奏。

| 场景 | 间距 | 说明 |
|------|------|------|
| 元素内部微调 | `--space-xs` 4px | Badge 文字内边距、图标与文字间距 |
| 紧凑排列 | `--space-sm` 8px | 功能列表项内部、按钮内文字与图标间距 |
| 标准间距 | `--space-md` 16px | 卡片内边距、段落间距、列表项间距 |
| 区块分隔 | `--space-lg` 24px | 卡片之间、section 内部子区块间距 |
| 章节呼吸 | `--space-xl` 32px | section 与 section 之间的间距 |
| 大段留白 | `--space-2xl` 48px | Hero 区域上下、价格区块前后、页脚上方 |

**规则：**
- Hero 区域下方用 `--space-2xl`，给用户"进入"的感觉
- 信息密集区（功能列表、FAQ）内部用 `--space-md`，紧凑但不拥挤
- 相邻的两个"不同类型"的内容块之间至少 `--space-xl`
- 底部 CTA 上方留 `--space-2xl`，避免最后一条内容被遮挡

---

## 5. 核心组件

### 5.1 主按钮 CTA

**意图：** 页面中唯一的行动号召。用于触发购买/订阅。只在底部固定栏和 Hero 区域出现，每个页面最多 2 个。

```css
.btn-primary {
  background: var(--accent-gradient);
  color: #FFFFFF;
  font-weight: 700;
  font-size: 16px;
  padding: 14px 32px;
  border-radius: var(--radius-md);
  border: none;
  width: 100%;
  box-shadow: 0 4px 20px var(--accent-glow);
  cursor: pointer;
  transition: all 0.2s ease;
}
.btn-primary:hover {
  box-shadow: 0 6px 30px rgba(255, 96, 15, 0.45);
  transform: translateY(-1px);
}
.btn-primary:active {
  transform: translateY(0);
  box-shadow: 0 2px 10px var(--accent-glow);
}
```

### 5.2 卡片

**意图：** 内容容器。普通卡片承载信息，高亮卡片承载推荐/限时内容。用阴影和层级区分，不用边框线。

```css
.card {
  background: var(--bg-1);
  border: 1px solid var(--bg-3);
  border-radius: var(--radius-lg);
  padding: 20px;
  transition: border-color 0.2s ease;
}
.card-highlight {
  border: 1px solid var(--accent);
  box-shadow: 0 0 20px var(--accent-subtle);
}
```

### 5.3 标签 Badge

**意图：** 状态指示器。只用语义色，不装饰性使用。Badge 是"信息标签"，不是"好看的色块"。

| Badge | 语义 | 色值 | 场景 |
|-------|------|------|------|
| `.badge-live` | 已上线/已完成 | success 绿 | 功能状态 |
| `.badge-building` | 开发中 | info 蓝 | 功能状态 |
| `.badge-hot` | 热门/限时 | accent 橙 | 紧迫感/推荐 |
| `.badge-new` | 新功能 | secondary 金 | 新上线标记 |

```css
.badge-live {
  background: rgba(0, 200, 83, 0.12);
  color: var(--success);
  padding: 4px 10px;
  border-radius: var(--radius-sm);
  font-size: 11px;
  font-weight: 600;
}
.badge-building {
  background: rgba(68, 138, 255, 0.12);
  color: var(--info);
}
.badge-hot {
  background: var(--bg-accent);
  color: var(--accent);
}
.badge-new {
  background: rgba(255, 184, 0, 0.12);
  color: var(--secondary);
}
```

### 5.4 进度条

**意图：** 制造紧迫感和完成感。用于"剩余名额"、"学习进度"、"解锁进度"。

```css
.progress-track {
  background: var(--bg-3);
  border-radius: var(--radius-full);
  height: 6px;
  overflow: hidden;
}
.progress-fill {
  background: var(--accent-gradient-h);
  border-radius: var(--radius-full);
  height: 100%;
  transition: width 0.6s ease;
}
```

### 5.5 价格组合

**意图：** 价格是页面最强的视觉锚点。大号橙色数字 + 划线原价 = 立刻感知优惠力度。

```css
.price-hero {
  font-size: 36px;
  font-weight: 800;
  color: var(--accent);
}
.price-symbol {
  font-size: 20px;
  font-weight: 700;
  color: var(--accent);
}
.price-unit {
  font-size: 14px;
  color: var(--text-2);
  margin-left: 4px;
}
.price-original {
  text-decoration: line-through;
  color: var(--text-3);
  font-size: 16px;
}
```

### 5.6 底部固定栏

**意图：** 永远可见的行动入口。毛玻璃半透明，不完全遮挡内容，但足够让用户随时能找到"下一步"。

```css
.bottom-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(0, 0, 0, 0.95);
  backdrop-filter: blur(10px);
  border-top: 1px solid var(--bg-3);
  padding: 12px 16px;
  padding-bottom: calc(12px + env(safe-area-inset-bottom));
  z-index: 100;
}
```

### 5.7 功能列表项

**意图：** 展示产品功能/卖点。图标方块 + 标题 + 描述，一行一个，扫描式阅读。

```css
.feature-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px;
  background: var(--bg-2);
  border-radius: var(--radius-md);
  transition: background 0.15s ease;
}
.feature-item:active {
  background: var(--bg-3);
}
.feature-icon {
  width: 40px;
  height: 40px;
  border-radius: var(--radius-sm);
  background: var(--bg-accent);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
```

---

## 6. 布局规范

```css
.page {
  max-width: 402px;
  margin: 0 auto;
  padding: 20px 16px 100px;
  background: var(--bg-0);
  min-height: 100vh;
  color: var(--text-1);
}

.section {
  margin-bottom: var(--space-xl);
}

.section-title {
  font-size: 20px;
  font-weight: 700;
  margin-bottom: var(--space-md);
  display: flex;
  align-items: center;
  gap: 8px;
}
```

---

## 7. 动效规范 Motion Guidelines

ACE 是短视频产品，动效必须**快、准、有反馈感**。像刷抖音一样流畅，不要像 PPT 一样机械。

### 7.1 时长规则

| 类型 | 时长 | 缓动 | 场景 |
|------|------|------|------|
| 微交互 | 150ms | ease-out | 按钮点击、开关切换 |
| 状态变化 | 200ms | ease | hover、focus、颜色变化 |
| 元素进出 | 300ms | ease-in-out | 卡片出现/消失、弹窗 |
| 布局变化 | 350ms | ease-in-out | 展开/折叠、高度变化 |
| 页面转场 | 400ms | cubic-bezier(0.4, 0, 0.2, 1) | 页面切换 |
| 进度动画 | 600ms | ease-out | 进度条填充、数字滚动 |

### 7.2 标准动效

```css
/* 按钮点击反馈 */
@keyframes tap-pulse {
  0% { transform: scale(1); }
  50% { transform: scale(0.97); }
  100% { transform: scale(1); }
}

/* 卡片进入（从下方滑入） */
@keyframes slide-up {
  from { opacity: 0; transform: translateY(16px); }
  to { opacity: 1; transform: translateY(0); }
}

/* 数字滚动（价格/统计） */
@keyframes count-up {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}

/* 微光扫描（高亮卡片装饰） */
@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

/* 脉冲发光（CTA 按钮吸引注意） */
@keyframes pulse-glow {
  0%, 100% { box-shadow: 0 4px 20px var(--accent-glow); }
  50% { box-shadow: 0 4px 30px rgba(255, 96, 15, 0.5); }
}
```

### 7.3 动效原则

- **入场用 slide-up**，不用 fade（fade 太慢太柔）
- **按钮用 scale 反馈**，不用颜色变化（scale 更有"按下去"的物理感）
- **进度条必须有动画**，静态进度条没有紧迫感
- **数字变化用 count-up**，不要瞬间跳变
- **禁止 bounce / elastic 效果**，太卡通，不符合沉浸感

---

## 8. 页面叙事结构

1. **🎯 Hero** — 身份标签 + 主标题 + 价格锚点
2. **📊 社会证明** — 数据统计（已购人数/总限额/∞收益）
3. **⏰ 紧迫感** — 剩余名额进度条 / 倒计时
4. **⚡ 核心功能** — 分卡片展示，每个带状态Badge和进度
5. **🗺️ 路线图** — 时间线或阶段展示
6. **💰 价格对比** — 现在 vs 涨价后 / 免费 vs 付费表格
7. **🛡️ 信任保障** — 3列图标（安全支付/无理由退/永久锁价）
8. **❓ FAQ** — 可展开的常见问题
9. **🔥 底部CTA** — fixed按钮 + 价格提示

---

## 9. 图标规范（重要）

- **统一使用线性 SVG 图标（line / outline 风格）**
- **禁止使用 emoji 作为 UI 图标**（emoji 仅可在用户生成内容、文案中出现）
- 标准规格：
  - `stroke-width: 1.5` 或 `2`
  - `stroke-linecap: round`
  - `stroke-linejoin: round`
  - `fill: none`
  - `stroke: currentColor`（继承文字颜色，方便主题切换）
- 标准尺寸：
  - 小图标 16×16
  - 默认 20×20
  - 大图标 24×24
  - 装饰性大图标 28-32×28-32
- 推荐使用 Lucide / Feather Icons / Tabler Icons 风格
- 容器图标（带圆角背景方块）：
  ```css
  .icon-box {
    width: 36px;
    height: 36px;
    border-radius: var(--radius-sm);
    background: var(--bg-accent);
    color: var(--accent);
    display: flex;
    align-items: center;
    justify-content: center;
  }
  ```

### 标准线性图标 SVG 示例

```html
<!-- 书签 / 收藏 -->
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/>
</svg>

<!-- 目标 -->
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="12" cy="12" r="10"/>
  <circle cx="12" cy="12" r="6"/>
  <circle cx="12" cy="12" r="2"/>
</svg>

<!-- 文档 / 笔记 -->
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
  <polyline points="14 2 14 8 20 8"/>
  <line x1="9" y1="13" x2="15" y2="13"/>
  <line x1="9" y1="17" x2="13" y2="17"/>
</svg>
```

---

## 10. 输出规范

- 完整单文件HTML（内联CSS + 内联少量JS交互）
- 所有颜色使用CSS变量
- 移动端优先，402px居中
- 使用语义化标签
- **图标统一使用线性 SVG，禁用 emoji**
- 底部CTA固定浮动
- 中文环境优化（PingFang SC）
- **所有交互元素必须有 :active / :focus 状态**
- **页面加载时卡片用 slide-up 动画依次入场**

---

## 11. AI Agent 生成规则

当 AI 代理基于本规范生成页面时，必须遵守以下硬性规则：

### 结构规则
1. 单文件 HTML，所有 CSS 内联在 `<style>` 标签中
2. 所有颜色值使用 CSS 变量引用（`var(--accent)` 而非 `#FF600F`）
3. 页面宽度锁定 `max-width: 402px`，居中显示
4. 底部 CTA 必须 `position: fixed`，必须有 `env(safe-area-inset-bottom)` 适配

### 视觉规则
5. 页面底色必须是 `#000000`，不接受深灰替代
6. 正文文字必须用 `--text-2`（#AAAAAA），不接受全白文字
7. 橙色只用于 CTA、价格、进度完成、紧迫感元素，不大面积铺色
8. 图标必须是线性 SVG，禁止 emoji 作为 UI 元素
9. 卡片之间用阴影和间距分隔，不用粗边框

### 动效规则
10. 按钮必须有 `:active` 状态（scale 0.97）
11. 卡片入场用 `slide-up` 动画，延迟依次递增
12. 进度条必须有 `transition: width` 动画
13. 所有 transition 时长不超过 400ms

### 内容规则
14. 价格数字必须用 Display 字级（36px/800）+ 橙色
15. 原价必须有 `text-decoration: line-through`
16. Badge 必须使用语义色（绿=完成、蓝=进行中、橙=热门、金=新增）
17. FAQ 使用 `<details>` / `<summary>` 语义标签

---

## 12. Prompt模板

```
请基于 design-system.md 规范，生成以下页面：

**页面类型**：[会员订阅页/落地页/功能介绍/活动页]
**产品名称**：xxx
**核心信息**：
- 价格：¥xxx/年
- 卖点：1. xxx 2. xxx 3. xxx
- 紧迫感：[剩余xx名额 / 限时xx天]
- 数据：[已有xx人加入]

**必须遵守**：
- 暗黑沉浸风格，橙色仅用于 CTA 和价格
- 卡片用 slide-up 动画依次入场
- 底部 CTA 固定悬浮 + 毛玻璃背景
- 图标用线性 SVG，禁用 emoji
- 文字层次：标题白、正文灰（#AAA）、弱化灰（#666）

生成完整单文件HTML。
```
