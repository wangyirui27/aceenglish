const fs = require('fs');

function gen(id, title, scene, tags, npcOpening, data) {
  const d = (t, v, e) => {
    if (v === undefined) return '';
    return `${t}="${v.replace(/"/g,'&quot;')}"`;
  };
  const color = {'a':'#4ade80','bs':'#fbbf24','bh':'#f87171'};
  const emoji = {'a':'✅','bs':'💸','bh':'🚫'};
  
  let rounds = {};
  for (let [k,v] of Object.entries(data)) {
    let [g,idx] = k.match(/^r(\d+)(.*)/).slice(1);
    if (!rounds[g]) rounds[g] = {a:[],bs:[],bh:[]};
    let type = v.type || k.substring(0,k.match(/[ab]/) ? k.length-1 : 1);
    if (k.includes('bs')) type = 'bs';
    else if (k.includes('bh')) type = 'bh';
    else if (idx && idx.includes('a')) type = 'a';
    rounds[g][type] = rounds[g][type] || [];
    rounds[g][type].push({id:k, ...v});
  }
  
  let r1 = '';
  let r2 = '';
  let npcEls = '';
  let dataJS = '';

  for (let [g,types] of Object.entries(rounds)) {
    let gid = 'g-r'+g;
    for (let [type, nodes] of Object.entries(types)) {
      if (!nodes.length) continue;
      let subgroup = g === '1' ? 'g-r1' : (type === 'a' ? gid+'a' : type === 'bs' ? gid+'bs' : gid+'bh');
      let cls = type === 'a' ? ' a' : type === 'bs' ? ' bs' : ' bh';
      let disp = (type === 'a' && g === '2') || g === '1' ? '' : ' style="display:none"';
      let npcId = 'npc-'+subgroup;
      
      let nds = '';
      nodes.forEach(n => {
        let dc = n.end ? ` data-end="${n.end}"` : '';
        let dt = n.to ? ` data-to="g-r${n.to}"` : '';
        nds += `<div class="node${cls}" data-n="${n.id}" data-g="${subgroup}" data-t="${type}"${dc}${dt} onclick="pick(this)">`;
        nds += `<div class="n-badge">${n.label||''}</div>`;
        nds += `<div class="dialogue"><div class="d-player">"${(n.player||'').replace(/"/g,'&quot;')}"</div>`;
        if (n.npc) nds += `<div class="d-npc"><span class="who">${n.npcWho||'NPC'}:</span>"${n.npc.replace(/"/g,'&quot;')}"</div>`;
        if (n.note) nds += `<div class="d-npc"><span style="color:${color[type]||'#888'}">${n.note}</span></div>`;
        nds += `</div></div>`;
        dataJS += `'${n.id}':{npc:'${(n.npc||'').replace(/'/g,"\\'")}'`;
        if (n.endText) dataJS += `,end:'${n.endText.replace(/'/g,"\\'")}'`;
        dataJS += `},`;
      });
      
      if (g === '1') {
        r1 += nds;
      } else {
        r2 += `<div class="round-group" id="${subgroup}"${disp}>`;
        let label = type === 'a' ? 'A' : type === 'bs' ? 'B软' : 'B硬';
        r2 += `<div class="round-header"><div class="r-num">Round ${g} · ${label} 路线</div>`;
        r2 += `<div class="r-npc" id="${npcId}"><div class="npc-tag">${npcOpening.who}</div><span class="txt"></span></div>`;
        r2 += `<div class="r-title">${nodes[0].roundTitle||''}</div></div>`;
        r2 += `<div class="options-row">${nds}</div></div>`;
        if(npcEls) npcEls+=','; npcEls+="'"+npcId+"'";
      }
    }
  }
  
  dataJS = dataJS.replace(/,$/,'');
  
  let html = `<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>🏷 ${title} — ${id}</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#0f0f14;color:#ddd;min-height:100vh}header{background:#1a1a24;border-bottom:1px solid #2a2a3a;padding:12px 24px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:100}header h1{font-size:18px;color:#fff}header button{padding:6px 16px;border-radius:8px;border:1px solid #333;background:transparent;color:#aaa;cursor:pointer;font-size:12px}header button:hover{border-color:#555;color:#fff}main{max-width:720px;margin:0 auto;padding:24px 16px 80px}.mission{background:#0f0f1f;border:1px solid #2a2a3e;border-radius:14px;padding:18px 24px;margin-bottom:24px}.mission .label{font-size:10px;color:#888;letter-spacing:1px;margin-bottom:8px}.mission .desc{font-size:13px;color:#bbb;line-height:1.7;margin-bottom:12px}.mission .tags{display:flex;gap:10px;font-size:11px;flex-wrap:wrap}.mission .scene{font-size:13px;color:#ccc;margin-top:14px;padding-top:12px;border-top:1px solid #1f1f2e}.mission .scene .speaker{color:#a78bfa;font-weight:600}.round-group{margin-bottom:24px;opacity:.12;pointer-events:none;transition:opacity .4s}.round-group.active{opacity:1;pointer-events:auto}.round-group.played{opacity:.45}.round-header{text-align:center;margin-bottom:16px}.round-header .r-num{font-size:10px;color:#444;letter-spacing:1px;margin-bottom:4px}.round-header .r-npc{background:#14141c;border:1px solid #1f1f2e;border-left:3px solid #fbbf24;border-radius:8px;padding:10px 18px;font-size:14px;color:#ddd;display:inline-block;min-width:240px;margin-bottom:8px;opacity:0;transition:opacity .3s;text-align:center}.round-header .r-npc.on{opacity:1}.round-header .r-npc .npc-tag{font-size:9px;color:#fbbf24;margin-bottom:3px}.round-header .r-title{font-size:14px;color:#888}.options-row{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}.node{background:#14141c;border:1px solid #1f1f2e;border-radius:14px;padding:14px 16px;min-width:200px;max-width:250px;display:flex;flex-direction:column;gap:6px;transition:all .25s;cursor:default;opacity:.4;pointer-events:none}.node.on{opacity:1;pointer-events:auto;border-color:#3a3a4a}.node.on:hover{border-color:#666;transform:translateY(-2px);box-shadow:0 6px 20px rgba(0,0,0,.5)}.node.pick{opacity:1;pointer-events:none;border-width:2px}.node.off{opacity:.04;pointer-events:none}.node .n-badge{font-size:9px;letter-spacing:.8px}.node.a{border-left:4px solid #4ade80}.node.a .n-badge{color:#4ade80}.node.bs{border-left:4px solid #fbbf24}.node.bs .n-badge{color:#fbbf24}.node.bh{border-left:4px solid #f87171}.node.bh .n-badge{color:#f87171}.node.pick.a{border-color:#4ade80;background:#0a1a10}.node.pick.bs{border-color:#fbbf24;background:#1a1a10}.node.pick.bh{border-color:#f87171;background:#1a0a0a}.node .dialogue{display:flex;flex-direction:column;gap:3px}.node .d-player{font-size:13px;color:#ccc;line-height:1.4;padding-left:8px;border-left:2px solid #a78bfa}.node .d-npc{font-size:12px;color:#999;line-height:1.4;padding-left:8px;border-left:2px solid #fbbf24}.node .d-npc .who{font-size:9px;color:#fbbf24;margin-right:4px}.end-badge{display:none;text-align:center;padding:18px 24px;margin-top:20px;border-radius:12px;font-size:15px;font-weight:600}.end-badge.show{display:block}.end-badge.a{background:#0f2a1a;border:1px solid #2a4a2a;color:#4ade80}.end-badge.bs{background:#2a2a0f;border:1px solid #4a4a2a;color:#fbbf24}.end-badge.bh{background:#2a0f0f;border:1px solid #4a2a2a;color:#f87171}#path-bar{position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:#1a1a28;border:1px solid #333;border-radius:14px;padding:10px 18px;display:none;align-items:center;gap:8px;z-index:200;font-size:12px;color:#ccc;box-shadow:0 8px 32px rgba(0,0,0,.6)}#path-bar.show{display:flex}#path-bar .trace{display:flex;gap:3px;align-items:center}#path-bar .step{width:22px;height:22px;border-radius:5px;font-size:9px;display:flex;align-items:center;justify-content:center;font-weight:700;color:#000}#path-bar .step.a{background:#4ade80}#path-bar .step.bs{background:#fbbf24}#path-bar .step.bh{background:#f87171}#path-bar .arr{color:#444;font-size:9px}
</style></head><body>
<header><h1>🏷 ${title}</h1><button onclick="reset()">🔄 重来</button></header>
<main>
<div class="mission"><div class="label">🎯 核心任务</div><div class="desc">${scene.desc}<br><span style="color:#fff;font-weight:500;">${scene.goal}</span></div><div class="tags">${Object.entries(tags).map(([k,v])=>'<span style="color:'+color[k]+'">'+emoji[k]+' '+k.toUpperCase()+' · '+v+'</span>').join(' ')}</div><div class="scene"><span class="speaker">${npcOpening.who}:</span> "${npcOpening.line}"</div></div>
<div class="round-group active" id="g-r1"><div class="round-header"><div class="r-num">Round 1</div><div class="r-title">${data.r1a.roundTitle||''}</div></div><div class="options-row">${r1}</div></div>
${r2}
<div class="end-badge" id="end"></div></main>
<div id="path-bar"><span>🎯 路径：</span><div class="trace" id="trace"></div><button onclick="reset()" style="background:transparent;border:1px solid #333;color:#888;padding:3px 10px;border-radius:6px;font-size:11px;cursor:pointer;">重来</button></div>
<script>
const D={${dataJS}};
let P=[],done=false;
function reset(){P=[];done=false;['g-r1','g-r2a','g-r2bs','g-r2bh'].forEach(id=>{let e=document.getElementById(id);if(e){e.classList.remove('active','played');e.style.display=id==='g-r1'?'':'none';}});document.getElementById('g-r1').classList.add('active');document.querySelectorAll('.node').forEach(n=>{n.classList.remove('pick','off','on')});document.querySelectorAll('#g-r1 .node').forEach(n=>n.classList.add('on'));[${npcEls}].forEach(id=>{let e=document.getElementById(id);if(e){e.classList.remove('on');e.querySelector('.txt').textContent='';}});document.getElementById('end').className='end-badge';document.getElementById('end').textContent='';document.getElementById('path-bar').classList.remove('show');}
function pick(el){if(done||!el.classList.contains('on'))return;let nid=el.dataset.n,gid=el.dataset.g,rt=el.dataset.t,ed=el.dataset.end,to=el.dataset.to;document.querySelectorAll('[data-g="'+gid+'"]').forEach(n=>{n===el?(n.classList.remove('on'),n.classList.add('pick')):(n.classList.remove('on'),n.classList.add('off'));});let rg=document.getElementById(gid);if(rg){rg.classList.remove('active');rg.classList.add('played');}P.push({g:gid,n:nid,t:rt});let npc=D[nid];if(to&&npc&&npc.npc){let ne=document.getElementById('npc-'+to);if(ne){ne.querySelector('.txt').textContent='\"'+npc.npc+'\"';ne.classList.add('on');}}if(ed){finish(ed,npc);return;}if(to){let ng=document.getElementById(to);if(ng){ng.style.display='';ng.classList.add('active');ng.querySelectorAll('.node').forEach(n=>n.classList.add('on'));ng.scrollIntoView({behavior:'smooth',block:'center'});}}
function finish(t,npc){done=true;document.querySelectorAll('.node.on').forEach(n=>n.classList.remove('on'));let eb=document.getElementById('end');eb.className='end-badge show '+t;eb.textContent=npc&&npc.end||'';document.getElementById('path-bar').classList.add('show');let tr=document.getElementById('trace'),h='';P.forEach((s,i)=>{if(i>0)h+='<span class="arr">\u2192</span>';h+='<span class="step '+s.t+'">'+s.t.toUpperCase()+'</span>';});h+='<span class="arr">\u2192</span><span style="font-size:12px">'+(t==='a'?'\u2705':t==='bs'?'\uD83D\uDCB8':'\uD83D\uDEAB')+'</span>';tr.innerHTML=h;eb.scrollIntoView({behavior:'smooth',block:'center'});}
reset();
</script></body></html>`;
  return html;
}

// ── S1E01 ──
const s01 = gen('S1E01', 'Wrong Badge', {
  desc: '前台 Jessica 误把你当成来开会的嘉宾。<br>',
  goal: '让她明白你是来找朋友 Sarah 的。'
}, {a:'赢了', bs:'进了错会', bh:'被请走'}, {who:'Jessica', line:'Good morning! Here for the morning meeting?'}, {

r1a:{player:'Not here for the meeting. I am here to see my friend Sarah.', npc:'Oh! Not for the meeting. Let me call Sarah.', npcWho:'Jessica', roundTitle:'Jessica 把你当成了参会嘉宾', label:'🅐 · 说清楚 → 赢', type:'a', to:'r2a'},
r1bs:{player:'OK.', npc:'Great! The meeting is in room 3.', npcWho:'Jessica', label:'🅑 · 随口 OK → B软', type:'bs', to:'r2bs'},
r1bh:{player:'Hi.', npc:'…Hi. Are you here for the meeting?', npcWho:'Jessica', label:'🅒 · 敷衍 → B硬', type:'bh', to:'r2bh'},

r2a1:{player:'Yes. Thank you!', npc:'Sarah will be right here. Next time I will know — you are Sarah\'s friend, not the meeting.', npcWho:'Jessica', end:'a', endText:'✅ 代价 $0。Jessica 记住你了。', roundTitle:'Jessica 在帮你联系 Sarah', label:'🅐 · 感谢 → 最好', type:'a'},
r2a2:{player:'…OK. Thanks.', npc:'…OK. Sarah will be here soon.', npcWho:'Jessica', end:'a', endText:'😐 代价 $0。Sarah 下来了。Jessica 对你没印象。', label:'🅐 · 不谢 → 一般', type:'a'},

r2bs1:{player:'Wait. Not the meeting. My friend Sarah.', npc:'…OK. But the meeting is in room 3. You can go in.', npcWho:'Jessica', end:'bs', endText:'💸 她没有叫 Sarah。你还是进了会议室。代价：一个下午 + Jessica 的信任。', roundTitle:'你已经被带向会议室了', label:'🅑 · 试着纠正', type:'bs'},
r2bs2:{player:'…OK. Room 3.', npc:'Yes. Room 3. Enjoy the meeting.', npcWho:'Jessica', end:'bs', endText:'💸 你走进了不属于你的会议室。Sarah 在大厅等你。代价：一个下午。', label:'🅑 · 不纠正', type:'bs'},

r2bh1:{player:'I am here for my friend.', npc:'OK. But you did not say that. Next time, tell me.', npcWho:'Jessica', end:'bh', endText:'🚫 Sarah 被叫下来了。但 Jessica 不会忘记——代价：她的信任。', roundTitle:'Jessica 在等你解释', label:'🅒 · 试着解释', type:'bh'},
r2bh2:{player:'…Bye.', npc:'…Bye.', npcWho:'Jessica', end:'bh', endText:'🚫 Jessica 签了你的名字，旁边多了一个 ✗。代价：这座楼里的信誉。', label:'🅒 · 不解释', type:'bh'}

});
fs.writeFileSync('/Users/yr/ACE/S1E01-wrong-badge.html', s01);
console.log('S1E01 written', s01.length, 'bytes');

// ── S1E02 ──
const s02 = gen('S1E02', 'Wrong Drink', {
  desc: '你点了一杯拿铁。Mike 端来卡布奇诺。<br>',
  goal: '让他给你换上拿铁。'
}, {a:'赢了', bs:'喝了错的', bh:'被跳过'}, {who:'Mike', line:'Here you go! One cappuccino.'}, {

r1a:{player:'Not a cappuccino. One latte, please.', npc:'Oh! Sorry. One latte — coming up.', npcWho:'Mike', roundTitle:'Mike 端来卡布奇诺', label:'🅐 · 说清楚 → 赢', type:'a', to:'r2a'},
r1bs:{player:'Wrong.', npc:'Wrong? OK… Flat white?', npcWho:'Mike', label:'🅑 · 没说清 → B软', type:'bs', to:'r2bs'},
r1bh:{player:'No. Not right.', npc:'OK. You know what? Next customer, please.', npcWho:'Mike', label:'🅒 · 只给否定 → B硬', type:'bh', to:'r2bh'},

r2a1:{player:'That\'s right. Thanks!', npc:'Sorry about that. I will remember — latte. See you tomorrow!', npcWho:'Mike', end:'a', endText:'✅ 代价 $0。Mike 记住你了。', roundTitle:'Mike 换回来了', label:'🅐 · 感谢 → 最好', type:'a'},
r2a2:{player:'…OK. Thanks.', npc:'OK. Good. …Is it OK?', npcWho:'Mike', end:'a', endText:'😐 代价 $0。拿铁对了。Mike 没记住你。', label:'🅐 · 不谢 → 一般', type:'a'},

r2bs1:{player:'Not flat white. Latte, please.', npc:'Oh! Latte! OK. Sorry.', npcWho:'Mike', end:'bs', endText:'💸 拿铁到了。但 Mike 记住你了——那个说了 Wrong 又不告诉我哪错了的人。', roundTitle:'Mike 正在做 flat white', label:'🅑 · 试着纠正', type:'bs'},
r2bs2:{player:'…OK. Thanks.', npc:'Good. Flat white for you. Enjoy!', npcWho:'Mike', end:'bs', endText:'💸 你喝了一杯 flat white。代价：一杯你不想要的咖啡。', label:'🅑 · 放弃纠正', type:'bs'},

r2bh1:{player:'Excuse me. One latte, please.', npc:'…One latte. OK.', npcWho:'Mike', end:'bh', endText:'🚫 你拿到了拿铁。Mike 不会再跟你笑了。代价：他的笑容。', roundTitle:'Mike 已经跳过了你', label:'🅒 · 再开口', type:'bh'},
r2bh2:{player:'…OK. Cappuccino.', npc:'Good.', npcWho:'Mike', end:'bh', endText:'🚫 你拿走了卡布奇诺。Mike 已经不看你。代价：一杯不想要的咖啡 + 他的印象。', label:'🅒 · 放弃', type:'bh'}

});
fs.writeFileSync('/Users/yr/ACE/S1E02-wrong-drink.html', s02);
console.log('S1E02 written', s02.length, 'bytes');

// ── S1E03 ──
const s03 = gen('S1E03', 'Dropped Papers', {
  desc: '你在电梯口撞掉了一位男士的文件。<br>',
  goal: '道歉 + 帮忙捡，让他接受你的道歉。'
}, {a:'赢了', bs:'只动嘴', bh:'说错话'}, {who:'Tom', line:'Oh! My papers!'}, {

r1a:{player:'I am so sorry! Let me help you.', npc:'Oh… Thank you.', npcWho:'Tom', roundTitle:'你撞掉了别人的文件', label:'🅐 · 道歉+帮忙 → 赢', type:'a', to:'r2a'},
r1bs:{player:'Sorry.', npc:'…OK.', npcWho:'Tom', label:'🅑 · 只道歉不动手 → B软', type:'bs', to:'r2bs'},
r1bh:{player:'It\'s OK.', npc:'It\'s OK? …Excuse me.', npcWho:'Tom', label:'🅒 · 说错话 → B硬', type:'bh', to:'r2bh'},

r2a1:{player:'Here you go. Sorry about that.', npc:'Thank you. No problem. Have a good day!', npcWho:'Tom', end:'a', endText:'✅ 代价 $0。Tom 说了 No problem.', roundTitle:'文件捡起来了——最后一句话', label:'🅐 · 递去+再道歉 → 最好', type:'a'},
r2a2:{player:'Here you go.', npc:'Thanks.', npcWho:'Tom', end:'a', endText:'😐 代价 $0。文件递了，但 Tom 没说 No problem。', label:'🅐 · 递去不道歉 → 一般', type:'a'},

r2bs1:{player:'…Sorry about that.', npc:'…OK. Bye.', npcWho:'Tom', end:'bs', endText:'💸 Tom 听到了。但他没说 No problem——你的道歉晚了。代价：他的好感。', roundTitle:'Tom 捡完了文件站起来', label:'🅑 · 再道一次歉', type:'bs'},
r2bs2:{player:'…Bye.', npc:'Bye.', npcWho:'Tom', end:'bs', endText:'💸 Tom 走进电梯。你对他来说不重要了。代价：一个印象。', label:'🅑 · 不说了', type:'bs'},

r2bh1:{player:'Sorry!', npc:'…OK.', npcWho:'Tom', end:'bh', endText:'🚫 电梯门关了。你道歉了 但 Tom 没原谅。代价：一句没分量的 Sorry。', roundTitle:'Tom 已经进了电梯', label:'🅒 · 追上去道歉', type:'bh'},
r2bh2:{player:'…OK.', npc:'…Excuse me.', npcWho:'Tom', end:'bh', endText:'🚫 门关了。Tom 没有看你第二眼。代价：一段没机会修复的关系。', label:'🅒 · 放弃', type:'bh'}

});
fs.writeFileSync('/Users/yr/ACE/S1E03-dropped-papers.html', s03);
console.log('S1E03 written', s03.length, 'bytes');

// ── S1E04 ──
const s04 = gen('S1E04', 'Wine Bill', {
  desc: '账单上多了一瓶 $45 的红酒——你没点。<br>',
  goal: '让 Lisa 划掉那 $45。'
}, {a:'赢了', bs:'付了 $45', bh:'被赶走'}, {who:'Lisa', line:'Here you go. $65 total.'}, {

r1a:{player:'Excuse me. I did not order this wine. $45 here.', npc:'Oh! Let me check. One moment.', npcWho:'Lisa', roundTitle:'账单上多了 $45 红酒', label:'🅐 · 说清楚 → 赢', type:'a', to:'r2a'},
r1bs:{player:'…OK. Here you go.', npc:'Thank you. (swipes — $65 gone)', npcWho:'Lisa', label:'🅑 · 没说 → B软', type:'bs', to:'r2bs'},
r1bh:{player:'This is wrong! $45? No!', npc:'I am sorry. Let me get my manager.', npcWho:'Lisa', label:'🅒 · 质问 → B硬', type:'bh', to:'r2bh'},

r2a1:{player:'Thank you. This is right now.', npc:'Sorry about that. It was table 3. Have a good evening!', npcWho:'Lisa', end:'a', endText:'✅ 代价 $0。你付了 $20。Lisa 笑着说晚安。', roundTitle:'Lisa 回来了', label:'🅐 · 感谢 → 最好', type:'a'},
r2a2:{player:'OK. That\'s right.', npc:'OK. Good. Thank you.', npcWho:'Lisa', end:'a', endText:'😐 代价 $0。账单对了。但 Lisa 没记住你。', label:'🅐 · 不谢 → 一般', type:'a'},

r2bs1:{player:'Wait. This $45. I did not order this.', npc:'Oh. …OK. Let me check.', npcWho:'Lisa', end:'bs', endText:'💸 Lisa 划掉了 $45。但退款要 3 天。代价：$45 + 3 天等待 + 她心里的问号。', roundTitle:'Lisa 把卡和账单还给你', label:'🅑 · 终于开口', type:'bs'},
r2bs2:{player:'…OK. Thank you.', npc:'Thank you. Good night!', npcWho:'Lisa', end:'bs', endText:'💸 代价：$45——你一天工资。Lisa 不知道。明天她也不知道。', label:'🅑 · 算了', type:'bs'},

r2bh1:{player:'I am sorry. I did not order this wine.', npc:'OK. Pay the bill. Then you can go.', npcWho:'Manager', end:'bh', endText:'🚫 你付了 $65。经理没听你的——他听了 Lisa 的。代价：$45 + 被请走 + 信誉。', roundTitle:'经理来了', label:'🅒 · 试着解释', type:'bh'},
r2bh2:{player:'This is wrong! I am not paying!', npc:'OK. Pay now. Or I call someone.', npcWho:'Manager', end:'bh', endText:'🚫 你付了 $65。下次你走进这家餐厅——经理会记得。代价：$45 + 被请走 + 黑名单。', label:'🅒 · 继续争执', type:'bh'}

});
fs.writeFileSync('/Users/yr/ACE/S1E04-wine-bill.html', s04);
console.log('S1E04 written', s04.length, 'bytes');

console.log('All done!');
