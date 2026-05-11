import json, os

def gen_html(file_id, title, scene_desc, scene_goal, npc_name, npc_opening, tags, routes):
    """
    routes = {
      "r1": [
        {"id":"r1a","label":"...","player":"...","npc":"...","type":"a","to":"r2a"},
        {"id":"r1bs","label":"...","player":"...","npc":"...","type":"bs","to":"r2bs"},
        {"id":"r1bh","label":"...","player":"...","npc":"...","type":"bh","to":"r2bh"},
      ],
      "r2a": [
        {"id":"r2a1","label":"...","player":"...","npc":"...","type":"a","end_text":"..."},
        {"id":"r2a2","label":"...","player":"...","npc":"...","type":"a","end_text":"..."},
      ],
      "r2bs": [...],
      "r2bh": [...],
    }
    """
    
    # Build D object for JS
    d_obj = {}
    for rnd in ["r1", "r2a", "r2bs", "r2bh"]:
        if rnd not in routes:
            continue
        for opt in routes[rnd]:
            entry = {"npc": opt["npc"]}
            if "end_text" in opt:
                entry["end"] = opt["end_text"]
            d_obj[opt["id"]] = entry
    
    d_json = json.dumps(d_obj, ensure_ascii=False)
    
    # Build R1 nodes
    r1_html = ""
    for opt in routes["r1"]:
        cls = opt["type"]
        r1_html += f'''
<div class="node {cls}" data-n="{opt["id"]}" data-g="r1" data-t="{cls}" data-to="{opt.get("to","")}" onclick="pick(this)">
  <div class="n-badge">{opt["label"]}</div>
  <div class="dialogue">
    <div class="d-player">"{opt["player"]}"</div>
    <div class="d-npc"><span class="who">{npc_name}:</span>"{opt["npc"]}"</div>
  </div>
</div>'''
    
    # Build R2 groups
    r2_html = ""
    r2_ids = []
    for rnd_key in ["r2a", "r2bs", "r2bh"]:
        if rnd_key not in routes:
            continue
        r2_ids.append(rnd_key)
        rnd_data = routes[rnd_key]
        # Get the type and title
        rnd_type = rnd_data[0]["type"] if rnd_data else "a"
        rnd_label = {"a":"A 路线","bs":"B软 路线","bh":"B硬 路线"}[rnd_type]
        rnd_num = "2"
        rnd_title = rnd_data[0].get("round_title", "") if rnd_data else ""
        
        nodes_html = ""
        for opt in rnd_data:
            cls = opt["type"]
            end_attr = ' data-end="a"' if "end_text" in opt and opt["type"] == "a" else \
                        ' data-end="bs"' if "end_text" in opt and opt["type"] == "bs" else \
                        ' data-end="bh"' if "end_text" in opt and opt["type"] == "bh" else ""
            nodes_html += f'''
<div class="node {cls}" data-n="{opt["id"]}" data-g="{rnd_key}" data-t="{cls}"{end_attr} onclick="pick(this)">
  <div class="n-badge">{opt["label"]}</div>
  <div class="dialogue">
    <div class="d-player">"{opt["player"]}"</div>
    <div class="d-npc"><span class="who">{npc_name}:</span>"{opt["npc"]}"</div>
  </div>
</div>'''
        
        r2_html += f'''
<div class="round-group" id="{rnd_key}" style="display:none">
  <div class="round-header">
    <div class="r-num">Round 2 · {rnd_label}</div>
    <div class="r-npc" id="npc-{rnd_key}"><div class="npc-tag">{npc_name}</div><span class="txt"></span></div>
    <div class="r-title">{rnd_title}</div>
  </div>
  <div class="options-row">{nodes_html}</div>
</div>'''
    
    r2_ids_js = ",".join([f"'{x}'" for x in r2_ids])
    
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>🏷 {title}</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#0f0f14;color:#ddd;min-height:100vh}}
header{{background:#1a1a24;border-bottom:1px solid #2a2a3a;padding:12px 24px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:100}}
header h1{{font-size:18px;color:#fff}}
header button{{padding:6px 16px;border-radius:8px;border:1px solid #333;background:transparent;color:#aaa;cursor:pointer;font-size:12px}}
header button:hover{{border-color:#555;color:#fff}}
main{{max-width:720px;margin:0 auto;padding:24px 16px 80px}}
.mission{{background:#0f0f1f;border:1px solid #2a2a3e;border-radius:14px;padding:18px 24px;margin-bottom:24px}}
.mission .label{{font-size:10px;color:#888;letter-spacing:1px;margin-bottom:8px}}
.mission .desc{{font-size:13px;color:#bbb;line-height:1.7;margin-bottom:12px}}
.mission .tags{{display:flex;gap:10px;font-size:11px;flex-wrap:wrap}}
.mission .scene{{font-size:13px;color:#ccc;margin-top:14px;padding-top:12px;border-top:1px solid #1f1f2e}}
.mission .scene .speaker{{color:#a78bfa;font-weight:600}}
.round-group{{margin-bottom:24px;opacity:.12;pointer-events:none;transition:opacity .4s}}
.round-group.active{{opacity:1;pointer-events:auto}}
.round-group.played{{opacity:.45}}
.round-header{{text-align:center;margin-bottom:16px}}
.round-header .r-num{{font-size:10px;color:#444;letter-spacing:1px;margin-bottom:4px}}
.round-header .r-npc{{background:#14141c;border:1px solid #1f1f2e;border-left:3px solid #fbbf24;border-radius:8px;padding:10px 18px;font-size:14px;color:#ddd;display:inline-block;min-width:240px;margin-bottom:8px;opacity:0;transition:opacity .3s;text-align:center}}
.round-header .r-npc.on{{opacity:1}}
.round-header .r-npc .npc-tag{{font-size:9px;color:#fbbf24;margin-bottom:3px}}
.round-header .r-title{{font-size:14px;color:#888}}
.options-row{{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}}
.node{{background:#14141c;border:1px solid #1f1f2e;border-radius:14px;padding:14px 16px;min-width:200px;max-width:250px;display:flex;flex-direction:column;gap:6px;transition:all .25s;cursor:default;opacity:.4;pointer-events:none}}
.node.on{{opacity:1;pointer-events:auto;border-color:#3a3a4a}}
.node.on:hover{{border-color:#666;transform:translateY(-2px);box-shadow:0 6px 20px rgba(0,0,0,.5)}}
.node.pick{{opacity:1;pointer-events:none;border-width:2px}}
.node.off{{opacity:.04;pointer-events:none}}
.node .n-badge{{font-size:9px;letter-spacing:.8px}}
.node.a{{border-left:4px solid #4ade80}}.node.a .n-badge{{color:#4ade80}}
.node.bs{{border-left:4px solid #fbbf24}}.node.bs .n-badge{{color:#fbbf24}}
.node.bh{{border-left:4px solid #f87171}}.node.bh .n-badge{{color:#f87171}}
.node.pick.a{{border-color:#4ade80;background:#0a1a10}}
.node.pick.bs{{border-color:#fbbf24;background:#1a1a10}}
.node.pick.bh{{border-color:#f87171;background:#1a0a0a}}
.node .dialogue{{display:flex;flex-direction:column;gap:3px}}
.node .d-player{{font-size:13px;color:#ccc;line-height:1.4;padding-left:8px;border-left:2px solid #a78bfa}}
.node .d-npc{{font-size:12px;color:#999;line-height:1.4;padding-left:8px;border-left:2px solid #fbbf24}}
.node .d-npc .who{{font-size:9px;color:#fbbf24;margin-right:4px}}
.end-badge{{display:none;text-align:center;padding:18px 24px;margin-top:20px;border-radius:12px;font-size:15px;font-weight:600}}
.end-badge.show{{display:block}}
.end-badge.a{{background:#0f2a1a;border:1px solid #2a4a2a;color:#4ade80}}
.end-badge.bs{{background:#2a2a0f;border:1px solid #4a4a2a;color:#fbbf24}}
.end-badge.bh{{background:#2a0f0f;border:1px solid #4a2a2a;color:#f87171}}
#path-bar{{position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:#1a1a28;border:1px solid #333;border-radius:14px;padding:10px 18px;display:none;align-items:center;gap:8px;z-index:200;font-size:12px;color:#ccc;box-shadow:0 8px 32px rgba(0,0,0,.6)}}
#path-bar.show{{display:flex}}
#path-bar .trace{{display:flex;gap:3px;align-items:center}}
#path-bar .step{{width:22px;height:22px;border-radius:5px;font-size:9px;display:flex;align-items:center;justify-content:center;font-weight:700;color:#000}}
#path-bar .step.a{{background:#4ade80}}.path-bar .step.bs{{background:#fbbf24}}.path-bar .step.bh{{background:#f87171}}
#path-bar .arr{{color:#444;font-size:9px}}
</style>
</head>
<body>
<header>
  <h1>🏷 {title}</h1>
  <button onclick="reset()">🔄 重来</button>
</header>
<main>
  <div class="mission">
    <div class="label">🎯 核心任务</div>
    <div class="desc">{scene_desc}<br><span style="color:#fff;font-weight:500;">{scene_goal}</span></div>
    <div class="tags">
      <span style="color:#4ade80;">✅ A · {tags["a"]}</span>
      <span style="color:#fbbf24;">💸 B软 · {tags["bs"]}</span>
      <span style="color:#f87171;">🚫 B硬 · {tags["bh"]}</span>
    </div>
    <div class="scene"><span class="speaker">{npc_name}:</span> "{npc_opening}"</div>
  </div>

  <div class="round-group active" id="r1">
    <div class="round-header">
      <div class="r-num">Round 1</div>
      <div class="r-title">{routes["r1"][0].get("round_title","")}</div>
    </div>
    <div class="options-row">{r1_html}</div>
  </div>

  {r2_html}

  <div class="end-badge" id="end"></div>
</main>

<div id="path-bar">
  <span>🎯 路径：</span>
  <div class="trace" id="trace"></div>
  <button onclick="reset()" style="background:transparent;border:1px solid #333;color:#888;padding:3px 10px;border-radius:6px;font-size:11px;cursor:pointer;">重来</button>
</div>

<script>
const D = {d_json};
let P = [];
let done = false;

function reset() {{
  P = [];
  done = false;
  ["r1", {r2_ids_js}].forEach(function(id) {{
    var e = document.getElementById(id);
    if (e) {{
      e.classList.remove("active", "played");
      e.style.display = id === "r1" ? "" : "none";
    }}
  }});
  document.getElementById("r1").classList.add("active");
  document.querySelectorAll(".node").forEach(function(n) {{
    n.classList.remove("pick", "off", "on");
  }});
  document.querySelectorAll("#r1 .node").forEach(function(n) {{
    n.classList.add("on");
  }});
  [{r2_ids_js}].forEach(function(id) {{
    var e = document.getElementById("npc-" + id);
    if (e) {{
      e.classList.remove("on");
      e.querySelector(".txt").textContent = "";
    }}
  }});
  var eb = document.getElementById("end");
  eb.className = "end-badge";
  eb.textContent = "";
  document.getElementById("path-bar").classList.remove("show");
}}

function pick(el) {{
  if (done || !el.classList.contains("on")) return;
  var nid = el.dataset.n;
  var gid = el.dataset.g;
  var rt = el.dataset.t;
  var ed = el.dataset.end;
  var to = el.dataset.to;

  document.querySelectorAll("[data-g=\\"" + gid + "\\"]").forEach(function(n) {{
    if (n === el) {{
      n.classList.remove("on");
      n.classList.add("pick");
    }} else {{
      n.classList.remove("on");
      n.classList.add("off");
    }}
  }});

  var rg = document.getElementById(gid);
  if (rg) {{
    rg.classList.remove("active");
    rg.classList.add("played");
  }}

  P.push({{g: gid, n: nid, t: rt}});
  var npc = D[nid];

  if (to && npc && npc.npc) {{
    var ne = document.getElementById("npc-" + to);
    if (ne) {{
      ne.querySelector(".txt").textContent = npc.npc;
      ne.classList.add("on");
    }}
  }}

  if (ed) {{
    finish(ed, npc);
    return;
  }}

  if (to) {{
    var ng = document.getElementById(to);
    if (ng) {{
      ng.style.display = "";
      ng.classList.add("active");
      ng.querySelectorAll(".node").forEach(function(n) {{
        n.classList.add("on");
      }});
      ng.scrollIntoView({{behavior: "smooth", block: "center"}});
    }}
  }}
}}

function finish(t, npc) {{
  done = true;
  document.querySelectorAll(".node.on").forEach(function(n) {{
    n.classList.remove("on");
  }});
  var eb = document.getElementById("end");
  eb.className = "end-badge show " + t;
  eb.textContent = npc ? (npc.end || "") : "";
  document.getElementById("path-bar").classList.add("show");
  var tr = document.getElementById("trace");
  var h = "";
  P.forEach(function(s, i) {{
    if (i > 0) h += '<span class="arr">→</span>';
    h += '<span class="step ' + s.t + '">' + s.t.toUpperCase() + '</span>';
  }});
  var emoji = t === "a" ? "✅" : t === "bs" ? "💸" : "🚫";
  h += '<span class="arr">→</span><span style="font-size:12px">' + emoji + '</span>';
  tr.innerHTML = h;
  eb.scrollIntoView({{behavior: "smooth", block: "center"}});
}}

reset();
</script>
</body>
</html>'''

# ── S1E01 ──
s01 = gen_html("S1E01", "Wrong Badge", "前台 Jessica 误把你当成来开会的嘉宾。<br>", "让她明白你是来找朋友 Sarah 的。",
  "Jessica", "Good morning! Here for the morning meeting?",
  {"a":"赢了", "bs":"进了错会", "bh":"被请走"},
  {"r1": [
    {"id":"r1a","label":"🅐 · 说清楚 → 赢","player":"Not here for the meeting. I am here to see my friend Sarah.","npc":"Oh! Not for the meeting. Let me call Sarah.","type":"a","to":"r2a","round_title":"Jessica 把你当成了参会嘉宾"},
    {"id":"r1bs","label":"🅑 · 随口 OK → B软","player":"OK.","npc":"Great! The meeting is in room 3.","type":"bs","to":"r2bs"},
    {"id":"r1bh","label":"🅒 · 敷衍 → B硬","player":"Hi.","npc":"…Hi. Are you here for the meeting?","type":"bh","to":"r2bh"},
  ], "r2a": [
    {"id":"r2a1","label":"🅐 · 感谢 → 最好","player":"Yes. Thank you!","npc":"Sarah will be right here. Next time I will know — you are Sarah's friend, not the meeting.","type":"a","end_text":"✅ 代价 $0。Jessica 记住你了。下次你进来，她是你的熟人。","round_title":"Jessica 在帮你联系 Sarah"},
    {"id":"r2a2","label":"🅐 · 不谢 → 一般","player":"…OK. Thanks.","npc":"…OK. Sarah will be here soon.","type":"a","end_text":"😐 代价 $0。Sarah 下来了。Jessica 对你没印象。"},
  ], "r2bs": [
    {"id":"r2bs1","label":"🅑 · 试着纠正","player":"Wait. Not the meeting. My friend Sarah.","npc":"…OK. But the meeting is in room 3. You can go in.","type":"bs","end_text":"💸 她没有叫 Sarah。你还是进了会议室。代价：一个下午 + Jessica 的信任。","round_title":"你已经被带向会议室了"},
    {"id":"r2bs2","label":"🅑 · 不纠正","player":"…OK. Room 3.","npc":"Yes. Room 3. Enjoy the meeting.","type":"bs","end_text":"💸 你走进了不属于你的会议室。Sarah 在大厅等你。代价：一个下午。"},
  ], "r2bh": [
    {"id":"r2bh1","label":"🅒 · 试着解释","player":"I am here for my friend.","npc":"OK. But you did not say that. Next time, tell me.","type":"bh","end_text":"🚫 Sarah 被叫下来了。但 Jessica 不会忘记——代价：她的信任。","round_title":"Jessica 在等你解释"},
    {"id":"r2bh2","label":"🅒 · 不解释","player":"…Bye.","npc":"…Bye.","type":"bh","end_text":"🚫 Jessica 签了你的名字，旁边多了一个 ✗。代价：这座楼里的信誉。"},
  ]})

# ── S1E02 ──
s02 = gen_html("S1E02", "Wrong Drink", "你点了一杯拿铁。Mike 端来卡布奇诺。<br>", "让他给你换上拿铁。",
  "Mike", "Here you go! One cappuccino.",
  {"a":"赢了", "bs":"喝了错的", "bh":"被跳过"},
  {"r1": [
    {"id":"r1a","label":"🅐 · 说清楚 → 赢","player":"Not a cappuccino. One latte, please.","npc":"Oh! Sorry. One latte — coming up.","type":"a","to":"r2a","round_title":"Mike 端来卡布奇诺"},
    {"id":"r1bs","label":"🅑 · 没说清 → B软","player":"Wrong.","npc":"Wrong? OK… Flat white?","type":"bs","to":"r2bs"},
    {"id":"r1bh","label":"🅒 · 只给否定 → B硬","player":"No. Not right.","npc":"OK. You know what? Next customer, please.","type":"bh","to":"r2bh"},
  ], "r2a": [
    {"id":"r2a1","label":"🅐 · 感谢 → 最好","player":"That is right. Thanks!","npc":"Sorry about that. I will remember — latte. See you tomorrow!","type":"a","end_text":"✅ 代价 $0。Mike 记住你了。明天他会说 Latte, right?","round_title":"Mike 换回来了"},
    {"id":"r2a2","label":"🅐 · 不谢 → 一般","player":"…OK. Thanks.","npc":"OK. Good. …Is it OK?","type":"a","end_text":"😐 代价 $0。拿铁对了。Mike 没记住你。"},
  ], "r2bs": [
    {"id":"r2bs1","label":"🅑 · 试着纠正","player":"Not flat white. Latte, please.","npc":"Oh! Latte! OK. Sorry.","type":"bs","end_text":"💸 拿铁到了。但 Mike 记住你了——那个说了 Wrong 又不告诉我哪错了的人。","round_title":"Mike 正在做 flat white"},
    {"id":"r2bs2","label":"🅑 · 放弃纠正","player":"…OK. Thanks.","npc":"Good. Flat white for you. Enjoy!","type":"bs","end_text":"💸 你喝了一杯 flat white。代价：一杯你不想要的咖啡。"},
  ], "r2bh": [
    {"id":"r2bh1","label":"🅒 · 再开口","player":"Excuse me. One latte, please.","npc":"…One latte. OK.","type":"bh","end_text":"🚫 你拿到了拿铁。Mike 不会再跟你笑了。代价：他的笑容。","round_title":"Mike 已经跳过了你"},
    {"id":"r2bh2","label":"🅒 · 放弃","player":"…OK. Cappuccino.","npc":"Good.","type":"bh","end_text":"🚫 你拿走了卡布奇诺。Mike 已经不看你。代价：一杯不想要的咖啡 + 他的印象。"},
  ]})

# ── S1E03 ──
s03 = gen_html("S1E03", "Dropped Papers", "你在电梯口撞掉了一位男士的文件。<br>", "道歉 + 帮忙捡，让他接受你的道歉。",
  "Tom", "Oh! My papers!",
  {"a":"赢了", "bs":"只动嘴", "bh":"说错话"},
  {"r1": [
    {"id":"r1a","label":"🅐 · 道歉+帮忙 → 赢","player":"I am so sorry! Let me help you.","npc":"Oh… Thank you.","type":"a","to":"r2a","round_title":"你撞掉了别人的文件"},
    {"id":"r1bs","label":"🅑 · 只道歉不动手 → B软","player":"Sorry.","npc":"…OK.","type":"bs","to":"r2bs"},
    {"id":"r1bh","label":"🅒 · 说错话 → B硬","player":"It is OK.","npc":"It is OK? …Excuse me.","type":"bh","to":"r2bh"},
  ], "r2a": [
    {"id":"r2a1","label":"🅐 · 递去+再道歉 → 最好","player":"Here you go. Sorry about that.","npc":"Thank you. No problem. Have a good day!","type":"a","end_text":"✅ 代价 $0。Tom 说了 No problem.","round_title":"文件捡起来了——最后一句话"},
    {"id":"r2a2","label":"🅐 · 递去不道歉 → 一般","player":"Here you go.","npc":"Thanks.","type":"a","end_text":"😐 代价 $0。文件递了，但 Tom 没说 No problem。"},
  ], "r2bs": [
    {"id":"r2bs1","label":"🅑 · 再道一次歉","player":"…Sorry about that.","npc":"…OK. Bye.","type":"bs","end_text":"💸 Tom 听到了。但他没说 No problem——你的道歉晚了。代价：他的好感。","round_title":"Tom 捡完了文件站起来"},
    {"id":"r2bs2","label":"🅑 · 不说了","player":"…Bye.","npc":"Bye.","type":"bs","end_text":"💸 Tom 走进电梯。你对他来说不重要了。代价：一个印象。"},
  ], "r2bh": [
    {"id":"r2bh1","label":"🅒 · 追上去道歉","player":"Sorry!","npc":"…OK.","type":"bh","end_text":"🚫 电梯门关了。你道歉了 但 Tom 没原谅。代价：一句没分量的 Sorry。","round_title":"Tom 已经进了电梯"},
    {"id":"r2bh2","label":"🅒 · 放弃","player":"…OK.","npc":"…Excuse me.","type":"bh","end_text":"🚫 门关了。Tom 没有看你第二眼。代价：一段没机会修复的关系。"},
  ]})

# ── S1E04 ──
s04 = gen_html("S1E04", "Wine Bill", "账单上多了一瓶 $45 的红酒——你没点。<br>", "让 Lisa 划掉那 $45。",
  "Lisa", "Here you go. $65 total.",
  {"a":"赢了", "bs":"付了 $45", "bh":"被赶走"},
  {"r1": [
    {"id":"r1a","label":"🅐 · 说清楚 → 赢","player":"Excuse me. I did not order this wine. $45 here.","npc":"Oh! Let me check. One moment.","type":"a","to":"r2a","round_title":"账单上多了 $45 红酒"},
    {"id":"r1bs","label":"🅑 · 没说 → B软","player":"…OK. Here you go.","npc":"Thank you. (swipes — $65 gone)","type":"bs","to":"r2bs"},
    {"id":"r1bh","label":"🅒 · 质问 → B硬","player":"This is wrong! $45? No!","npc":"I am sorry. Let me get my manager.","type":"bh","to":"r2bh"},
  ], "r2a": [
    {"id":"r2a1","label":"🅐 · 感谢 → 最好","player":"Thank you. This is right now.","npc":"Sorry about that. It was table 3. Have a good evening!","type":"a","end_text":"✅ 代价 $0。你付了 $20。Lisa 笑着说晚安。","round_title":"Lisa 回来了"},
    {"id":"r2a2","label":"🅐 · 不谢 → 一般","player":"OK. That is right.","npc":"OK. Good. Thank you.","type":"a","end_text":"😐 代价 $0。账单对了。但 Lisa 没记住你。"},
  ], "r2bs": [
    {"id":"r2bs1","label":"🅑 · 终于开口","player":"Wait. This $45. I did not order this.","npc":"Oh. …OK. Let me check.","type":"bs","end_text":"💸 Lisa 划掉了 $45。但退款要 3 天。代价：$45 + 3 天等待 + 她心里的问号。","round_title":"Lisa 把卡和账单还给你"},
    {"id":"r2bs2","label":"🅑 · 算了","player":"…OK. Thank you.","npc":"Thank you. Good night!","type":"bs","end_text":"💸 代价：$45——你一天工资。Lisa 不知道。明天她也不知道。"},
  ], "r2bh": [
    {"id":"r2bh1","label":"🅒 · 试着解释","player":"I am sorry. I did not order this wine.","npc":"OK. Pay the bill. Then you can go.","type":"bh","end_text":"🚫 你付了 $65。经理没听你的——他听了 Lisa 的。代价：$45 + 被请走 + 信誉。","round_title":"经理来了"},
    {"id":"r2bh2","label":"🅒 · 继续争执","player":"This is wrong! I am not paying!","npc":"OK. Pay now. Or I call someone.","type":"bh","end_text":"🚫 你付了 $65。下次你走进这家餐厅——经理会记得。代价：$45 + 被请走 + 黑名单。"},
  ]})

# Write all files
base = "/Users/yr/ACE"
for fname, content in [
    ("S1E01-wrong-badge.html", s01),
    ("S1E02-wrong-drink.html", s02),
    ("S1E03-dropped-papers.html", s03),
    ("S1E04-wine-bill.html", s04),
]:
    path = os.path.join(base, fname)
    with open(path, "w") as f:
        f.write(content)
    print(f"{fname}: {len(content)} bytes written")

print("All done!")
