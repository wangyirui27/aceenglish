#!/bin/bash
# 头号听力 · 一键同步到 GitHub
# 双击本文件即可提交并推送到 https://github.com/wangyirui27/aceenglish.git

cd "$(dirname "$0")" || { echo "❌ 进不去目录"; read -p "按回车退出..."; exit 1; }

echo "📂 $(pwd)"
echo ""

# 检查是否有改动
if git diff --quiet && git diff --cached --quiet && [ -z "$(git ls-files --others --exclude-standard)" ]; then
    echo "✅ 没有需要同步的改动"
    sleep 2
    exit 0
fi

# 显示改动
echo "📝 待同步的文件:"
git status --short
echo ""

# 提交
COMMIT_MSG="sync: $(date '+%m/%d %H:%M')"
git add -A
git commit -m "$COMMIT_MSG" 2>/dev/null && echo "✅ 已提交: $COMMIT_MSG" || echo "⚠️ 提交可能有冲突，继续推送..."

# 推送
echo ""
echo "🚀 推送到 GitHub..."
git push origin main 2>&1

echo ""
echo "✅ 同步完成"
sleep 2
