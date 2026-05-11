#!/bin/bash
# 头号听力 · 一键同步到 GitHub（双向智能版）
# 双击 → 先拉远程 → 再推本地 → 两边保持一致

cd "$(dirname "$0")" || { echo "❌ 找不到目录"; read -p "按回车退出..."; exit 1; }

echo "📂 $(pwd)"
echo "━━━━━━━━━━━━━━━━━━━━"

# ── 第一步：拉取远程更新 ──
echo "⬇️  检查远程更新..."
git fetch origin main 2>&1

LOCAL=$(git rev-parse HEAD 2>/dev/null)
REMOTE=$(git rev-parse origin/main 2>/dev/null)

if [ "$LOCAL" != "$REMOTE" ]; then
    echo "🔔 远程有更新，正在拉取..."
    git pull origin main --rebase 2>&1
    echo "✅ 远程更新已合并"
else
    echo "✅ 远程没有新内容"
fi

echo ""

# ── 第二步：检查本地改动 ──
if git diff --quiet && git diff --cached --quiet && [ -z "$(git ls-files --others --exclude-standard)" ]; then
    echo "✅ 本地没有改动，无需推送"
    sleep 2
    osascript -e 'tell application "Terminal" to close front window' 2>/dev/null
    exit 0
fi

echo "📝 本地待推送的文件:"
git status --short
echo ""

# ── 第三步：提交并推送 ──
COMMIT_MSG="sync: $(date '+%m/%d %H:%M')"
git add -A
git commit -m "$COMMIT_MSG" 2>&1

echo "🚀 推送到 GitHub..."
git push origin main 2>&1

echo ""
echo "━━━━━━━━━━━━━━━━━━━━"
echo "✅ 同步完成"
sleep 2
osascript -e 'tell application "Terminal" to close front window' 2>/dev/null
