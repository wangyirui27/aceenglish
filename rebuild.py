import csv

rate = {'入门':50, '初级':40, '中级':30, '中高级':20, '高级':15}

def categorize(row):
    name = row.get('name', '')
    cid = row.get('category_id', '')
    textbook_patterns = [
        '人教版高中英语','外研社高中英语','牛津高中英语','北师大版高中英语',
        '人教版初中英语','仁爱版初中英语','外研社初中英语','沪教版牛津英语',
        '译林版牛津英语','鲁教版五四学制','冀教版三年级起点','牛津上海版',
        '人教版小学英语','人教版三年级起点','人教版一年级起点',
        '北师大版小学英语','北师大版三年级起点','北师大版一年级起点',
        '北京版小学英语','北京版一年级起点',
        '外研版小学英语','外研版三年级起点',
        '译林版小学英语','译林版三年级起点','译林版牛津小学英语',
        '沪教版小学英语','沪教版三年级起点',
        '广州版小学英语','广州版三年级起点',
        '湘少版小学英语','湘少版三年级起点',
        '闽教版小学英语','闽教版三年级起点',
        '科普版小学英语','科普版三年级起点',
        '广东版小学英语','广东版三年级起点',
        '陕西版小学英语','陕西版三年级起点',
        '冀教版小学英语','冀教版三年级起点',
        '教科版EEC小学英语','教科版EEC三年级起点',
        '全新版大学英语','新视野大学英语','新标准大学英语',
        '大学英语精读','新世纪大学英语','新编大学英语',
        '高级英语','新世纪英语专业综合教程',
        '2003人教版PEP','2004人教版PEP','2007人教版初中',
    ]
    for p in textbook_patterns:
        if p in name:
            return '教材同步'
    if cid == '3':
        if any(kw in name for kw in ['必修','选修','模块']):
            return '教材同步'
        return '备战高考'
    if cid == '4': return '教材同步'
    if cid in ['5','6','7','8']: return '四六级'
    if cid in ['10','11']: return '考研'
    if cid in ['14','15','16','17','18','19','20']: return '出国留学'
    if cid in ['21','22']: return '职场提升'
    if cid in ['12','23','24']: return '综合提升'
    if cid == '9':
        return '综合提升' if '大学生英语竞赛' in name else '职场提升'
    if cid == '13':
        if any(kw in name for kw in ['剑桥国际英语教程','朗文国际英语教程','Side by Side','Academic Voc List','英语单词笔记']):
            return '综合提升'
        return '职场提升'
    if cid == '25':
        if '小学' in name or 'PEP' in name or '初中' in name:
            return '教材同步'
        if '四级' in name or '六级' in name or '四六级' in name:
            return '四六级'
        if '考研' in name: return '考研'
        if '雅思' in name or 'GRE' in name or '托福' in name or 'TOEFL' in name:
            return '出国留学'
        if '高中' in name:
            return '教材同步' if any(kw in name for kw in ['必修','选修','模块']) else '备战高考'
        return '综合提升'
    if any(kw in name for kw in ['四级','六级','四六级','专四','专八']): return '四六级'
    if any(kw in name for kw in ['考研','硕士研究生','考博']): return '考研'
    if any(kw in name for kw in ['托福','TOEFL','雅思','IELTS','GRE','GMAT','SAT','ACT','托业','TOEIC']): return '出国留学'
    return '综合提升'

def subcategorize(row):
    name = row.get('name', '')
    cat = row['category']
    cid = row.get('category_id', '')
    if cat == '备战高考':
        if any(kw in name for kw in ['一笑而过','白金版','图解速记','巧记','快速记忆']): return '趣味巧记'
        if any(kw in name for kw in ['分频','高频','核心高频','优先顺序','真题词汇']): return '高频速记'
        if any(kw in name for kw in ['周计划','综合','抗遗忘','随身记','速记速诀']): return '综合训练'
        return '考纲词汇'
    if cat == '四六级':
        if '四六级' in name or '四、六级' in name: return '四六通用'
        if '词组' in name and ('四级' in name or '六级' in name): return '四六通用'
        if any(kw in name for kw in ['专四','专4','专业4级','专业四级']): return '专四词汇'
        if any(kw in name for kw in ['专八','专8','专业8级','专业八级']): return '专八词汇'
        if '四级' in name or '4级' in name: return '四级词汇'
        if '六级' in name or '6级' in name: return '六级词汇'
        return '四六通用'
    if cat == '考研':
        if any(kw in name for kw in ['词组','高分写作','命题人预测']): return '词组专项'
        if any(kw in name for kw in ['便携版','便携本','十天搞定','7天','8天']): return '便携冲刺'
        if any(kw in name for kw in ['一笑而过','速记指南','巧记速记','词根','强词有理','词汇速记']): return '巧记速记'
        if any(kw in name for kw in ['分频','高频','闪过','真题','词频','分级词汇','阅读真题']): return '真题词汇'
        if any(kw in name for kw in ['英语二','英二','英语（二）','(二)']): return '英二专项'
        if '考博' in name or '博士' in name: return '考博词汇'
        return '大纲词汇'
    if cat == '出国留学':
        if any(kw in name for kw in ['托福','TOEFL','TOEFLIBT','新托福']): return '托福'
        if any(kw in name for kw in ['雅思','IELTS']): return '雅思'
        if 'GRE' in name: return 'GRE'
        if 'GMAT' in name: return 'GMAT'
        if 'SAT' in name: return 'SAT'
        if 'ACT' in name: return 'ACT'
        if any(kw in name for kw in ['托业','TOEIC']): return '托业'
        return '其他'
    if cat == '职场提升':
        if 'BEC' in name or '商务英语' in name: return '商务英语'
        if any(kw in name for kw in ['全国等级','PETS','AB级','应用能力']): return '等级考试'
        if 'MBA' in name: return '管理类'
        return '成人学历'
    if cat == '教材同步':
        pk = ['人教版小学','译林版小学','译林版牛津小学','牛津小学英语',
              '北师大版小学','北京版小学','外研版小学','沪教版小学',
              '广州版小学','湘少版小学','闽教版小学','科普版小学',
              '广东版小学','陕西版小学','冀教版小学','教科版EEC小学',
              'PEP小学','小学英语升学夺冠','三年级起点三年级','三年级起点四年级',
              '三年级起点五年级','三年级起点六年级','一年级起点一年级',
              '一年级起点二年级','一年级起点三年级','一年级起点四年级',
              '一年级起点五年级','一年级起点六年级']
        if any(kw in name for kw in pk) or cid == '1': return '小学教材'
        mk = ['人教版初中','仁爱版初中','外研社初中','中考','初中英语词汇','初中考点',
              '上海市初中','译林版牛津英语七年级','译林版牛津英语八年级','译林版牛津英语九年级',
              '鲁教版五四学制','牛津上海版','冀教版三年级起点七年级','冀教版三年级起点八年级',
              '冀教版三年级起点九年级','2007人教版初中']
        if any(kw in name for kw in mk) or cid == '2': return '初中教材'
        hk = ['人教版高中','外研社高中','牛津高中','北师大版高中']
        if any(kw in name for kw in hk) or cid == '3': return '高中教材'
        return '大学教材'
    if cat == '综合提升':
        if '新概念英语' in name: return '新概念'
        if any(kw in name for kw in ['Oxford 3000','朗文3000','COCA','美国当代语料库']): return '词频语料'
        if any(kw in name for kw in ['词汇进阶','突破英文词汇','突破英文基础']): return '词汇进阶'
        if any(kw in name for kw in ['剑桥国际英语','Side by Side','朗文国际英语','口语达人']): return '交际口语'
        if any(kw in name for kw in ['终极英语','终极单词','英语学霸','英语母语','畅读英文']): return '分级词汇'
        return '工具书'
    return '综合提升'

def generate_tags(row):
    name = row.get('name', '')
    cat = row['category']
    sub = row['sub_category']
    tags = []
    if any(kw in name for kw in ['小学','入门级A','入门级B']): tags.append('入门')
    elif any(kw in name for kw in ['初中','七年级','八年级','九年级','中考',
        '新概念英语第一册','新概念英语第二册','新概念英语青少版1','新概念英语青少版2',
        '突破英文基础','词汇进阶 BASIC']): tags.append('初级')
    elif any(kw in name for kw in ['高中','高考','必修','选修','模块',
        '四级','4级','专四','专4','新概念英语第三册','新概念英语青少版3','新概念英语青少版4',
        '词汇进阶 6000','突破英文词汇5000','PETS','全国等级','AB级']): tags.append('中级')
    elif any(kw in name for kw in ['六级','6级','专八','专8','考研','硕士研究生','考博',
        '新概念英语第四册','新概念英语青少版5','词汇进阶 12000','突破英文词汇10000',
        'BEC','MBA','成人','专升本','自考','同等学力','大学英语','全新版大学',
        '新视野','新标准大学','新世纪大学','新编大学','高级英语']): tags.append('中高级')
    elif any(kw in name for kw in ['托福','TOEFL','雅思','IELTS','GRE','GMAT','SAT','ACT','托业','TOEIC',
        '词汇进阶 23000','突破英文词汇22000','英语母语']): tags.append('高级')
    else: tags.append('中级')

    if cat == '备战高考': tags.append('高考')
    elif cat == '四六级':
        if sub == '四级词汇': tags.append('四级')
        elif sub == '六级词汇': tags.append('六级')
        elif sub == '专四词汇': tags.append('专四')
        elif sub == '专八词汇': tags.append('专八')
        elif sub == '四六通用': tags.append('四六级')
    elif cat == '考研':
        if sub == '英二专项':
            tags.extend(['考研','英语二'])
        else:
            tags.append('考研')
    elif cat == '出国留学': tags.append(sub.upper())
    elif cat == '职场提升':
        if sub == '商务英语': tags.append('BEC')
        elif sub == '等级考试': tags.append('PETS')
        elif sub == '管理类': tags.append('MBA')
        else: tags.append('成人')
    elif cat == '教材同步':
        if sub == '小学教材': tags.append('小学')
        elif sub == '初中教材': tags.append('初中')
        elif sub == '高中教材': tags.append('高中')
        else: tags.append('大学')
    elif cat == '综合提升': tags.append('通用')

    if '词组' in name: tags.append('词组')
    elif '口语' in name: tags.append('口语')
    elif '听力' in name: tags.append('听力')
    elif '写作' in name: tags.append('写作')

    seen = set()
    out = []
    for t in tags:
        if t not in seen:
            seen.add(t)
            out.append(t)
    return ','.join(out[:4])

def calc_days(row):
    tags = row['tags'].split(',')
    level = next((t for t in tags if t in rate), '中级')
    return round(int(row['item_count']) / rate[level])

# MAIN
with open('/Users/yr/ACE/执行结果590.csv') as f:
    rows = list(csv.DictReader(f))

for row in rows:
    row['category'] = categorize(row)
    # fix misclassified
    name = row['name']
    if name in ['5·3中考英语核心词汇','初中英语词汇乱序版','上海市初中英语教学基本要求','初中考点精练英语词汇（中考）']:
        row['category'] = '教材同步'
    if name == '英语词组全书（上）':
        row['category'] = '综合提升'
    row['sub_category'] = subcategorize(row)
    row['tags'] = generate_tags(row)
    row['est_days'] = str(calc_days(row))

fieldnames = list(rows[0].keys())
with open('/Users/yr/ACE/执行结果590_final.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# Print samples
samples = [
    '人教版三年级起点三年级上','人教版初中英语七年级上册',
    '四级词汇正序版','六级英语新大纲词汇表',
    '考研词汇正序版','GRE词汇精选（NEW）',
    '新概念英语第一册（新版）','雅思词汇加强版',
]
print('词书                            词条    天数')
print('-'*55)
for row in rows:
    if row['name'] in samples:
        print('%-28s %5s词  %3s天' % (row['name'], row['item_count'], row['est_days']))

from collections import Counter
all_tags = Counter()
for row in rows:
    for t in row['tags'].split(','):
        all_tags[t] += 1
print('\n总计: %d本' % len(rows))
