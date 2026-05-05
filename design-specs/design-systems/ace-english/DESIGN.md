# 头号听力 (Ace English)

> Category: Education & Language
> Immersive dark video-first English learning app. Pure black canvas, orange (#FF600F) as the only signal color, TikTok-style swipe UX.

## 1. Visual Theme & Atmosphere

Ace English 的视觉性格：沉浸式暗黑 + 橙色活力。让用户感觉自己在刷短视频，不是在上课。像 TikTok/抖音一样让人上瘾，不像 Duolingo 一样卡通。

核心原则：
- 沉浸感优先 — 纯黑底色 `#000000` + 大面积留暗，让视频和字幕成为绝对主角
- 橙色是信号灯 — 只在关键时刻出现（CTA、价格、进度完成、紧迫感），不大面积铺色
- 呼吸感 — 信息密集区域之间必须有留白缓冲
- 触手可及 — 所有关键操作（购买、收藏、跟读）都在拇指热区内
- 暗中发光 — 利用 glow/shadow 让关键元素在暗背景上浮起来
- 动效快而干脆 — 150-400ms，按钮用 scale 反馈，卡片用 slide-up 入场

## 2. Color Palette & Roles

### Primary
- **Ace Orange** (`#FF600F`): 主色调，仅用于 CTA 按钮、价格数字、进度完成标记、紧迫感提示
- **Ace Orange Hover** (`#E85500`): hover 状态
- **Ace Orange Light** (`#FF7A33`): 渐变终点、次要强调
- **Ace Orange Glow** (`rgba(255, 96, 15, 0.3)`): 发光阴影，让 CTA 按钮"浮起"
- **Ace Orange Subtle** (`rgba(255, 96, 15, 0.1)`): 背景微透，用于 badge 和弱强调

### Background Hierarchy
- **Page Base** (`#000000`): 页面底色 — 必须纯黑，不接受深灰替代
- **Card** (`#111111`): 一级卡片背景
- **Nested** (`#1A1A1A`): 嵌套卡片、输入框
- **Hover/Divider** (`#222222`): hover 态、分隔线
- **Accent Background** (`#2A1508`): 强调色背景，深底衬托橙色文字

### Text
- **Title** (`#FFFFFF`): 标题和核心信息
- **Body** (`#AAAAAA`): 正文和描述 — 不全部用白色
- **Dim** (`#666666`): 弱化和禁用文字
- **Accent Text** (`#FF600F`): 价格和强调文字

### Semantic
- **Gold/Star** (`#FFB800`): 星标、金色装饰、新功能标记
- **Success Green** (`#00C853`): 已完成、已上线、答对反馈
- **Info Blue** (`#448AFF`): 信息标签、开发中状态
- **Error Red** (`#FF3B30`): 错误状态

## 3. Typography

```css
font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display",
             "Helvetica Neue", "PingFang SC", Arial, sans-serif;
```

| Scale | Size | Weight | Line Height | Usage |
|-------|------|--------|-------------|-------|
| Display | 36px | 800 | 1.2 | 价格数字、结算分数 |
| H1 | 28px | 700 | 1.3 | 页面主标题 |
| H2 | 20px | 700 | 1.4 | 区块标题 |
| H3 | 16px | 600 | 1.5 | 卡片标题 |
| Body | 14px | 400 | 1.6 | 正文 |
| Caption | 12px | 400 | 1.5 | 辅助文字 |
| Overline | 11px | 600 | 1.4 | 标签和 badge 文字 |

Special: Gold coin numbers use system font (`font-family: 'SF Pro Display', sans-serif`) at weight 700-800.

## 4. Spacing Rhythm

4px grid system, with named tokens:

| Token | Value | Usage |
|-------|-------|-------|
| xs | 4px | Badge padding, icon-text gap |
| sm | 8px | Compact list items, btn internal gap |
| md | 16px | Card padding, paragraph spacing |
| lg | 24px | Section sub-blocks, card gaps |
| xl | 32px | Section-to-section breathing room |
| 2xl | 48px | Hero area, price blocks, footer |

Rules:
- Hero 区域下方用 2xl，给用户"进入"的感觉
- 信息密集区内部用 md，紧凑但不拥挤
- 相邻不同类型的块之间至少 xl
- 底部 CTA 上方留 2xl

## 5. Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| sm | 6px | Badge, small labels |
| md | 12px | Buttons, form elements, option cards |
| lg | 16px | Main cards, modal containers |
| xl | 20px | Large containers |
| full | 999px | Pills, combo counters, status badges |

## 6. Core Components

### Primary CTA Button
- Background: `linear-gradient(135deg, #FF600F, #FF7A33)`
- Color: white, weight 700, 16px
- Padding: 14px 32px, border-radius 12px
- Box-shadow: `0 4px 20px rgba(255, 96, 15, 0.3)`
- Hover: shadow expands + translateY(-1px)
- Active: scale(0.97)
- Max 2 per page — bottom fixed bar and hero area

### Cards
- Background: #111111, border: 0.5px solid #222222
- Border-radius: 16px, padding: 20px
- Separated by shadow and spacing, never thick borders
- Highlight variant: border-color #FF600F + `0 0 20px rgba(255,96,15,0.1)`

### Badges
Only semantic colors — green (completed), blue (in-progress), orange (hot/urgency), gold (new):
- Background: rgba(color, 0.12), border-radius: 6px
- Padding: 4px 10px, font: 11px weight 600

### Progress Bar
- Track: #222222, height 6px, border-radius full
- Fill: `linear-gradient(90deg, #FF600F, #FFB800)`, animated width transition 600ms

### Bottom Fixed Bar
- Position: fixed, bottom: 0
- Background: `rgba(0, 0, 0, 0.95)`, backdrop-filter: blur(10px)
- Border-top: 0.5px solid #222222
- Padding-bottom: calc(12px + env(safe-area-inset-bottom))

### Tab Bar (Bottom Navigation)
- 5 tabs: 收藏夹 / 刷剧 / 排位赛 / 学习 / 我的
- Active: accent color, inactive: #666666
- Background: rgba(0,0,0,0.95) with backdrop-filter blur
- Icons: linear SVG, stroke-width 1.5, 22px

## 7. Icon System

- Unified line/outline style SVG icons
- stroke-width: 1.5 or 2
- stroke-linecap: round, stroke-linejoin: round
- fill: none, stroke: currentColor
- Standard sizes: 16px (small), 20px (default), 24px (large)
- Icon box wrapper: 36px × 36px, border-radius 6px, background #2A1508, accent color
- NO emoji as UI icons — emoji only allowed in user-generated content

## 8. Motion & Animation

| Type | Duration | Easing | Usage |
|------|----------|--------|-------|
| Micro-interaction | 150ms | ease-out | Button clicks, toggle switches |
| State change | 200ms | ease | Hover, focus, color changes |
| Element enter/exit | 300ms | ease-in-out | Card appearance, modals |
| Layout change | 350ms | ease-in-out | Expand/collapse |
| Page transition | 400ms | cubic-bezier(0.4,0,0.2,1) | Page swaps |
| Progress animation | 600ms | ease-out | Progress bars, number counters |

Standard animations:
- `slide-up`: opacity 0→1, translateY(12px)→0, 300ms ease — for card entrance
- `count-up`: opacity 0→1, translateY(8px)→0 — for price/score numbers
- `tap-pulse`: scale(1)→scale(0.97)→scale(1) — for button feedback
- `pulse-glow`: box-shadow 0 4px 20px ↔ 0 4px 30px — for CTA attention
- `timer-beat`: alternating box-shadow pulse — for countdown urgency
- `coin-pop`: scale bounce + translate up — for gold coin reward toast

Rules:
- 入场用 slide-up，不用 fade（fade 太慢太柔）
- 按钮用 scale 反馈，不用颜色变化
- 进度条必须有动画，静态没有紧迫感
- 数字变化用 count-up，不要瞬间跳变
- 禁止 bounce/elastic 效果 — 太卡通，不符合沉浸感

## 9. Layout & Page Structure

- Mobile-first, max-width: 402px, centered
- Page background: #000000 (mandatory, never deep gray)
- Bottom CTA must be position: fixed with safe-area-inset
- Phone device frame: 44px border-radius, notch + home indicator
- Status bar: iOS-style time + signal + battery
- Content tags: horizontal scroll pills, selected = white on #222222
- Arena tag: #2A1508 background, orange text
