#!/bin/bash
cd "$(dirname "$0")"

# 生成首页合集
cat > index.html << 'HEADER'
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ace English - 页面合集</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { font-family: -apple-system, "Helvetica Neue", sans-serif; background: #f5f5f7; color: #1d1d1f; padding: 40px 20px; }
  .container { max-width: 640px; margin: 0 auto; }
  h1 { font-size: 28px; font-weight: 700; margin-bottom: 8px; }
  .subtitle { color: #86868b; font-size: 14px; margin-bottom: 32px; }
  .card { display: block; background: #fff; border-radius: 14px; padding: 18px 20px; margin-bottom: 12px; text-decoration: none; color: inherit; box-shadow: 0 1px 3px rgba(0,0,0,0.06); transition: transform 0.15s, box-shadow 0.15s; }
  .card:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
  .card-name { font-size: 16px; font-weight: 600; margin-bottom: 4px; }
  .card-desc { font-size: 13px; color: #86868b; }
  .empty { text-align: center; padding: 60px 0; color: #86868b; }
</style>
</head>
<body>
<div class="container">
  <h1>Ace English</h1>
  <p class="subtitle">页面合集</p>
HEADER

# 扫描所有 HTML 文件（排除 index.html），按修改时间倒序
BASE_URL="https://wangyirui27.github.io/aceenglish"
found=0
while IFS= read -r f; do
  [ "$f" = "index.html" ] && continue
  [ -z "$f" ] && continue
  title="${f%.html}"
  encoded=$(FILENAME="$f" python3 -c "import urllib.parse, os; print(urllib.parse.quote(os.environ['FILENAME']))" 2>/dev/null || echo "$f")
  cat >> index.html << CARD
  <a class="card" href="${BASE_URL}/${encoded}">
    <div class="card-name">$title</div>
    <div class="card-desc">点击查看 →</div>
  </a>
CARD
  found=1
done < <(ls -t *.html 2>/dev/null)

# 如果没有其他 HTML 文件
if [ "$found" = "0" ]; then
  echo '  <div class="empty">还没有页面</div>' >> index.html
fi

cat >> index.html << 'FOOTER'
</div>
</body>
</html>
FOOTER

# 同步到 git
git add -A
git commit -m "同步页面合集 $(date '+%Y-%m-%d %H:%M')" 2>/dev/null
git push 2>/dev/null

echo "✅ 搞定！合集地址：https://wangyirui27.github.io/aceenglish/"
