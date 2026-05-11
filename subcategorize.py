import csv
import re

def subcategorize(row):
    name = row.get('name', '')
    cat = row.get('category', '')
    cid = row.get('category_id', '')
    desc = row.get('description', '')
    
    # ============================================================
    # 备战高考
    # ============================================================
    if cat == '备战高考':
        # 联想巧记图解
        if any(kw in name for kw in ['一笑而过', '白金版', '图解速记', '巧记', '快速记忆']):
            return '联想巧记图解'
        # 高频分频速记
        if any(kw in name for kw in ['分频', '高频', '核心高频', '优先顺序', '真题词汇']):
            return '高频分频速记'
        # 周计划综合练
        if any(kw in name for kw in ['周计划', '综合', '抗遗忘', '随身记', '速记速诀']):
            return '周计划综合练'
        # 考纲同步词汇（默认）
        return '考纲同步词汇'
    
    # ============================================================
    # 四六级
    # ============================================================
    if cat == '四六级':
        if '专四' in name or '专4' in name or '专业4级' in name or '专业四级' in name:
            return '专四词汇'
        if '专八' in name or '专8' in name or '专业8级' in name or '专业八级' in name:
            return '专八词汇'
        if '四级' in name or '4级' in name or 'CET-4' in name or 'CET4' in name:
            if '六级' not in name and '6级' not in name:
                return '四级词汇'
        if '六级' in name or '6级' in name or 'CET-6' in name or 'CET6' in name:
            if '四级' not in name and '4级' not in name:
                return '六级词汇'
        if '四六级' in name or '四、六级' in name:
            return '四六级通用'
        if '词组' in name:
            return '四六级通用'
        return '四六级通用'
    
    # ============================================================
    # 考研
    # ============================================================
    if cat == '考研':
        if '词组' in name or '专项' in name:
            return '词组与专项'
        if any(kw in name for kw in ['便携版', '便携本', '十天搞定', '7天', '8天', '随身']):
            return '便携冲刺版'
        if any(kw in name for kw in ['一笑而过', '速记指南', '巧记速记', '词根', '联想', '强词有理', '词汇速记']):
            return '联想巧记速记'
        if any(kw in name for kw in ['分频', '高频', '闪过', '真题', '词频', '分级词汇', '阅读真题']):
            return '分频真题词汇'
        if any(kw in name for kw in ['英语二', '英二', '英语（二）', '(二)']):
            return '英语二专项'
        if '考博' in name or '博士' in name:
            return '考博词汇'
        # default
        return '大纲核心词汇'
    
    # ============================================================
    # 出国留学
    # ============================================================
    if cat == '出国留学':
        if any(kw in name for kw in ['托福', 'TOEFL', 'TOEFLIBT', '新托福']):
            return '托福/TOEFL'
        if any(kw in name for kw in ['雅思', 'IELTS']):
            return '雅思/IELTS'
        if 'GRE' in name:
            return 'GRE'
        if 'GMAT' in name:
            return 'GMAT'
        if 'SAT' in name:
            return 'SAT'
        if 'ACT' in name:
            return 'ACT'
        if any(kw in name for kw in ['托业', 'TOEIC']):
            return '托业/TOEIC'
        return '其他留学考试'
    
    # ============================================================
    # 职场提升
    # ============================================================
    if cat == '职场提升':
        if 'BEC' in name or '商务英语' in name:
            return 'BEC商务英语'
        if any(kw in name for kw in ['全国等级', 'PETS', 'AB级', '应用能力']):
            return 'PETS等级考试'
        if any(kw in name for kw in ['MBA']):
            return 'MBA/管理类'
        if any(kw in name for kw in ['成人', '专升本', '自考', '同等学力', '英语（一）自学', '英语（二）自学']):
            return '成人学历考试'
        # 英语词组全书 is a general reference
        if '英语词组全书' in name:
            return '成人学历考试'  # it was categorized under 职场提升 based on cid=13
        return '成人学历考试'
    
    # ============================================================
    # 教材同步
    # ============================================================
    if cat == '教材同步':
        if any(kw in name for kw in ['小学', '一年级', '二年级', '三年级', '四年级', '五年级', '六年级']):
            # Check if it's primary school
            if any(kw in name for kw in ['PEP', '人教版', '外研版', '译林版', '北师大版', '北京版', '沪教版', 
                                           '广州版', '冀教版', '湘少版', '闽教版', '科普版', '广东版', 
                                           '陕西版', '教科版', '牛津小学']):
                if not any(kw in name for kw in ['初中', '高中', '七年级', '八年级', '九年级']):
                    return '小学教材'
        if any(kw in name for kw in ['初中', '七年级', '八年级', '九年级', '中考']):
            return '初中教材'
        if any(kw in name for kw in ['高中', '必修', '选修', '模块']):
            if not any(kw in name for kw in ['初中']):
                return '高中教材'
        if any(kw in name for kw in ['大学英语', '新视野', '新标准大学', '新世纪大学', '新编大学', 
                                       '高级英语', '新世纪英语专业', '全新版大学']):
            return '大学教材'
        # Fallback: check category_id
        if cid == '1':
            return '小学教材'
        if cid == '2':
            return '初中教材'
        if cid == '3':
            return '高中教材'
        if cid == '4':
            return '大学教材'
        # For 2003/2004/2007 PEP editions
        if 'PEP' in name:
            if '六年级' in name or '五年级' in name or '四年级' in name or '三年级' in name:
                return '小学教材'
        if '2007人教版初中' in name:
            return '初中教材'
        return '大学教材'
    
    # ============================================================
    # 综合提升
    # ============================================================
    if cat == '综合提升':
        if '新概念英语' in name:
            return '新概念英语系列'
        if any(kw in name for kw in ['Oxford 3000', '朗文3000', 'COCA', '美国当代语料库']):
            return '词频词典/语料库'
        if any(kw in name for kw in ['词汇进阶', '突破英文词汇', '突破英文基础']):
            return '词汇进阶系列'
        if any(kw in name for kw in ['剑桥国际英语', 'Side by Side', '朗文国际英语', '口语达人']):
            return '交际口语教程'
        if any(kw in name for kw in ['终极英语', '终极单词', '英语学霸', '英语母语', '畅读英文']):
            return '分级主题词汇'
        if any(kw in name for kw in ['热词', '英语单词笔记', 'Academic Voc List', '英语词汇的奥秘']):
            return '工具书/其他'
        if '新英语多功能词典' in name:
            return '工具书/其他'
        if '大学生英语竞赛' in name:
            return '工具书/其他'
        if any(kw in name for kw in ['中考', '初中英语词汇', '初中考点', '上海市初中']):
            return '工具书/其他'  # will be reclassified below
        return '工具书/其他'
    
    return '综合提升'


# ============================================================
# Read and process
# ============================================================
with open('/Users/yr/ACE/执行结果590_categorized.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

# Fix misclassifications before sub-categorizing
for row in rows:
    name = row.get('name', '')
    cid = row.get('category_id', '')
    
    # These disabled middle school items should be 教材同步
    if name in ['5·3中考英语核心词汇', '初中英语词汇乱序版', 
                 '上海市初中英语教学基本要求', '初中考点精练英语词汇（中考）']:
        row['category'] = '教材同步'
    
    # 英语词组全书 should be 综合提升 (general reference, not career)
    if name == '英语词组全书（上）':
        row['category'] = '综合提升'
    
    # 英语词汇的奥秘（六级版）should stay 四六级
    if name == '英语词汇的奥秘（六级版）':
        row['category'] = '四六级'
    
    # 英语四、六级考试词汇必备 should stay 四六级 
    # (already correct since cid=6)

# Now add sub_category
new_fieldnames = fieldnames + ['sub_category']

with open('/Users/yr/ACE/执行结果590_final.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=new_fieldnames)
    writer.writeheader()
    for row in rows:
        row['sub_category'] = subcategorize(row)
        writer.writerow(row)

# Print summary
from collections import Counter, defaultdict

cat_sub = defaultdict(Counter)
for row in rows:
    cat_sub[row['category']][row['sub_category']] += 1

for cat in ['备战高考','四六级','考研','出国留学','职场提升','教材同步','综合提升']:
    subs = cat_sub[cat]
    total = sum(subs.values())
    print(f'\n=== {cat} ({total}本) ===')
    for sub, count in subs.most_common():
        print(f'  {sub}: {count}')

print(f'\n总计: {sum(sum(v.values()) for v in cat_sub.values())}')
