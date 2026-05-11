import csv, re

def generate_tags(row):
    name = row.get('name', '')
    cat = row.get('category', '')
    sub = row.get('sub_category', '')
    cid = row.get('category_id', '')
    desc = row.get('description', '')
    
    tags = []
    level = None
    
    # === LEVEL ===
    if any(kw in name for kw in ['小学', '一年级', '二年级', '三年级起点三', '三年级起点四',
                                   '一年级起点一', '一年级起点二', '入门级', '入门级A', '入门级B']):
        level = '入门'
    elif any(kw in name for kw in ['初中', '七年级', '八年级', '九年级', '中考',
                                     '三年级起点五', '三年级起点六',
                                     '一年级起点三', '一年级起点四',
                                     '新概念英语第一册', '新概念英语第二册',
                                     '新概念英语青少版1', '新概念英语青少版2',
                                     '突破英文基础', '词汇进阶 BASIC']):
        level = '初级'
    elif any(kw in name for kw in ['高中', '高考', '必修', '选修', '模块',
                                     '四级', '4级', 'CET-4', 'CET4', '专四', '专4',
                                     '新概念英语第三册',
                                     '新概念英语青少版3', '新概念英语青少版4',
                                     '词汇进阶 6000', '突破英文词汇5000',
                                     'PETS', '全国等级', 'AB级']):
        level = '中级'
    elif any(kw in name for kw in ['六级', '6级', 'CET-6', 'CET6', '专八', '专8',
                                     '考研', '硕士研究生', '考博', '硕士博士',
                                     '新概念英语第四册',
                                     '新概念英语青少版5',
                                     '词汇进阶 12000', '突破英文词汇10000',
                                     'BEC', 'MBA', '成人', '专升本', '自考', '同等学力',
                                     '大学英语', '全新版大学', '新视野', '新标准大学',
                                     '新世纪大学', '新编大学', '高级英语',
                                     '朗文国际英语', '剑桥国际英语']):
        level = '中高级'
    elif any(kw in name for kw in ['托福', 'TOEFL', '雅思', 'IELTS', 'GRE', 'GMAT',
                                     'SAT', 'ACT', '托业', 'TOEIC',
                                     '词汇进阶 23000', '突破英文词汇22000',
                                     '英语母语', '美国当代语料库 15000', '美国当代语料库 20200']):
        level = '高级'
    
    # Fill in missing levels based on sub-category
    if level is None:
        if sub in ['小学教材']: level = '入门'
        elif sub in ['初中教材']: level = '初级'
        elif sub in ['高中教材', '考纲词汇', '趣味巧记', '综合训练', '高频速记',
                      '四级词汇', '专四词汇', '等级考试']: level = '中级'
        elif sub in ['大学教材', '六级词汇', '专八词汇', '四六通用',
                      '大纲词汇', '真题词汇', '巧记速记', '便携冲刺', '词组专项', '英二专项',
                      '成人学历', '商务英语', '管理类', '新概念', '交际口语',
                      '词频语料', '分级词汇']: level = '中高级'
        elif sub in ['托福', '雅思', 'GRE', 'GMAT', 'SAT', 'ACT', '托业', '词汇进阶']: level = '高级'
        else: level = '中级'
    
    tags.append(level)
    
    # === TARGET EXAM / PURPOSE ===
    if cat == '备战高考':
        tags.append('高考')
    elif cat == '四六级':
        if sub == '四级词汇': tags.append('四级')
        elif sub == '六级词汇': tags.append('六级')
        elif sub == '专四词汇': tags.append('专四')
        elif sub == '专八词汇': tags.append('专八')
        elif sub == '四六通用': tags.append('四六级')
    elif cat == '考研':
        if sub == '英二专项': tags.append('英语二')
        else: tags.append('考研')
    elif cat == '出国留学':
        if sub == '托福': tags.append('托福')
        elif sub == '雅思': tags.append('雅思')
        elif sub == 'GRE': tags.append('GRE')
        elif sub == 'GMAT': tags.append('GMAT')
        elif sub == 'SAT': tags.append('SAT')
        elif sub == 'ACT': tags.append('ACT')
        elif sub == '托业': tags.append('托业')
    elif cat == '职场提升':
        if sub == '商务英语': tags.append('BEC')
        elif sub == '等级考试': tags.append('PETS')
        elif sub == '管理类': tags.append('MBA')
        elif sub == '成人学历': 
            if '专升本' in name: tags.append('专升本')
            elif '自考' in name: tags.append('自考')
            elif '同等学力' in name: tags.append('同等学力')
            else: tags.append('成人本')
    elif cat == '教材同步':
        if sub == '小学教材': tags.append('小学')
        elif sub == '初中教材': tags.append('初中')
        elif sub == '高中教材': tags.append('高中')
        elif sub == '大学教材': tags.append('大学')
    elif cat == '综合提升':
        if sub in ['新概念']: tags.append('通用')
        elif sub in ['交际口语']: tags.append('口语')
        elif sub in ['词频语料']: tags.append('词频')
        else: tags.append('通用')
    
    # === CONTENT TYPE ===
    if cat == '备战高考':
        if sub == '考纲词汇': tags.append('考纲')
        elif sub == '高频速记': tags.append('词频')
        elif sub == '趣味巧记': tags.append('巧记')
        elif sub == '综合训练': tags.append('综合')
        if '乱序' in name: tags.append('乱序')
        if '便携' in name: tags.append('便携')
        if '图解' in name: tags.append('图解')
    elif cat == '四六级':
        if '词组' in name: tags.append('词组')
        elif sub == '四六通用': tags.append('词组')
        else: tags.append('核心')
        if '乱序' in name: tags.append('乱序')
        if '便携' in name: tags.append('便携')
        if '词根' in name or '联想' in name: tags.append('词根')
        if '周计划' in name: tags.append('周计划')
        if '新大纲' in name: tags.append('新大纲')
    elif cat == '考研':
        if sub == '大纲词汇': tags.append('考纲')
        elif sub == '真题词汇': tags.append('真题')
        elif sub == '巧记速记': tags.append('巧记')
        elif sub == '便携冲刺': tags.append('便携')
        elif sub == '词组专项': tags.append('词组')
        elif sub == '英二专项': tags.append('核心')
        if '词根' in name: tags.append('词根')
        if '乱序' in name: tags.append('乱序')
        if '一笑而过' in name: tags.append('巧记')
    elif cat == '出国留学':
        tags.append('核心')
        if '词组' in name or '短语' in name: tags.append('词组')
        if '乱序' in name: tags.append('乱序')
        if '便携' in name: tags.append('便携')
        if '词以类记' in name: tags.append('分类')
        if '7天' in name or '21天' in name or '45天' in name or '570个单词' in name:
            tags.append('速成')
        if '听力' in name: tags.append('听力')
        if '写作' in name: tags.append('写作')
        if '阅读' in name: tags.append('阅读')
        if '口语' in name: tags.append('口语')
        if '词伙' in name: tags.append('词伙')
        if '807' in name: tags.append('高频')
        if '胜经' in name or '加强版' in name: tags.append('进阶')
        if '核心词汇考法' in name: tags.append('考法')
    elif cat == '职场提升':
        if sub == '商务英语': tags.append('商务')
        elif sub == '等级考试': tags.append('考纲')
        elif sub == '成人学历': tags.append('考纲')
        if '乱序' in name: tags.append('乱序')
        if '便携' in name: tags.append('便携')
    elif cat == '教材同步':
        tags.append('教材')
        if '人教版' in name: tags.append('人教版')
        elif '外研社' in name or '外研版' in name: tags.append('外研版')
        elif '译林版' in name or '译林' in name: tags.append('译林版')
        elif '北师大版' in name: tags.append('北师大')
        elif '北京版' in name: tags.append('北京版')
        elif '沪教版' in name: tags.append('沪教版')
        elif '广州版' in name: tags.append('广州版')
        elif '冀教版' in name: tags.append('冀教版')
        elif '湘少版' in name: tags.append('湘少版')
        elif '闽教版' in name: tags.append('闽教版')
        elif '科普版' in name: tags.append('科普版')
        elif '广东版' in name: tags.append('广东版')
        elif '陕西版' in name: tags.append('陕西版')
        elif '教科版' in name: tags.append('教科版')
        elif '仁爱版' in name: tags.append('仁爱版')
        elif '鲁教版' in name: tags.append('鲁教版')
        elif '牛津上海版' in name: tags.append('牛津上海')
        elif '牛津高中' in name: tags.append('牛津版')
        elif 'PEP' in name: tags.append('PEP')
        if '一年级起点' in name: tags.append('一起点')
        elif '三年级起点' in name: tags.append('三起点')
        if '必修' in name: tags.append('必修')
        elif '选修' in name: tags.append('选修')
        if '上册' in name or '七年级上' in name or '八年级上' in name or '九年级上' in name or '高一上' in name:
            tags.append('上学期')
        elif '下册' in name or '七年级下' in name or '八年级下' in name or '九年级下' in name or '高一下' in name:
            tags.append('下学期')
    elif cat == '综合提升':
        if sub == '新概念':
            if '青少版' in name: tags.append('青少版')
            else: tags.append('经典版')
            if '第一册' in name or '1A' in name or '1B' in name or '入门' in name:
                tags.append('基础')
            elif '第二册' in name or '2A' in name or '2B' in name:
                tags.append('进阶')
            elif '第三册' in name: tags.append('提高')
            elif '第四册' in name: tags.append('流利')
        elif sub == '交际口语':
            if '剑桥' in name: tags.append('剑桥')
            elif '朗文' in name or 'Side by Side' in name: tags.append('朗文')
            if '入门' in name: tags.append('入门')
            elif '第1册' in name: tags.append('初级')
            elif '第2册' in name: tags.append('中级')
            elif '第3册' in name: tags.append('高级')
        elif sub == '词汇进阶':
            if 'BASIC' in name: tags.append('基础')
            elif '6000' in name: tags.append('进阶')
            elif '12000' in name: tags.append('高级')
            elif '23000' in name: tags.append('精通')
            elif '突破英文基础' in name: tags.append('入门篇')
            elif '突破英文词汇5000' in name: tags.append('初级篇')
            elif '突破英文词汇10000' in name: tags.append('中级篇')
            elif '突破英文词汇22000' in name: tags.append('高级篇')
        elif sub == '词频语料':
            if 'Oxford 3000' in name: tags.append('牛津')
            elif '朗文3000' in name: tags.append('朗文')
            elif 'COCA' in name or '美国当代' in name: tags.append('COCA')
        elif sub == '分级词汇':
            tags.append('分级')
        elif sub == '工具书':
            if '词典' in name: tags.append('词典')
            if '热词' in name: tags.append('时政')
            if '竞赛' in name: tags.append('竞赛')
            if '单词笔记' in name: tags.append('笔记')
        if '词组' in name: tags.append('词组')
        if '口语' in name: tags.append('口语')
    
    # === Deduplicate and limit ===
    seen = set()
    result = []
    for t in tags:
        if t not in seen:
            seen.add(t)
            result.append(t)
    
    # Keep it 2-4 tags
    return ','.join(result[:4])

# Read, tag, write
with open('/Users/yr/ACE/执行结果590_final.csv') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

for row in rows:
    row['tags'] = generate_tags(row)

new_fieldnames = fieldnames + ['tags']
with open('/Users/yr/ACE/执行结果590_final.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=new_fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# Sample output
print("=== 各分类标签示例 ===\n")
from collections import defaultdict
samples = defaultdict(list)
for row in rows:
    cat = row['category']
    if len(samples[cat]) < 5:
        samples[cat].append((row['name'], row['tags']))

for cat in ['备战高考','四六级','考研','出国留学','职场提升','教材同步','综合提升']:
    print(f'【{cat}】')
    for name, tags in samples[cat]:
        print(f'  {name}')
        print(f'    → {tags}')
    print()

# Stats
print('=== 标签统计 ===')
all_tags = []
for row in rows:
    all_tags.extend(row['tags'].split(','))
from collections import Counter
for tag, count in Counter(all_tags).most_common(30):
    print(f'  {tag}: {count}')
