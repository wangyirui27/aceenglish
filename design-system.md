# 🎨 Design System Specification v1.1
# 主色调：#FF600F

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

## 4. 核心组件

### 4.1 主按钮 CTA
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
```

### 4.2 卡片
```css
.card {
  background: var(--bg-1);
  border: 1px solid var(--bg-3);
  border-radius: var(--radius-lg);
  padding: 20px;
}
.card-highlight {
  border: 1px solid var(--accent);
  box-shadow: 0 0 20px var(--accent-subtle);
}
```

### 4.3 标签 Badge
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
```

### 4.4 进度条
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

### 4.5 价格组合
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

### 4.6 底部固定栏
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

### 4.7 功能列表项
```css
.feature-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px;
  background: var(--bg-2);
  border-radius: var(--radius-md);
}
.feature-icon {
  width: 40px;
  height: 40px;
  border-radius: var(--radius-sm);
  background: var(--bg-accent);
  display: flex;
  align-items: center;
  justify-content: center;
}
```

---

## 5. 布局规范

```css
.page {
  max-width: 390px;
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

## 6. 页面叙事结构

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

## 7. 图标规范（重要）

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

## 8. 输出规范

- 完整单文件HTML（内联CSS + 内联少量JS交互）
- 所有颜色使用CSS变量
- 移动端优先，390px居中
- 使用语义化标签
- **图标统一使用线性 SVG，禁用 emoji**
- 底部CTA固定浮动
- 中文环境优化（PingFang SC）

---

## 9. Prompt模板

```
请基于 design-system.md 规范，生成以下页面：

**页面类型**：[会员订阅页/落地页/功能介绍/活动页]
**产品名称**：xxx
**核心信息**：
- 价格：¥xxx/年
- 卖点：1. xxx 2. xxx 3. xxx
- 紧迫感：[剩余xx名额 / 限时xx天]
- 数据：[已有xx人加入]

生成完整单文件HTML。
```
