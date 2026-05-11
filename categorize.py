import csv
import re

def categorize(row):
    name = row.get('name', '')
    desc = row.get('description', '')
    cid = row.get('category_id', '')
    book_label = row.get('book_label', '')
    
    # 教材同步：中小学教材 + 大学教材
    textbook_patterns = [
        '人教版高中英语', '外研社高中英语', '牛津高中英语', '北师大版高中英语',
        '人教版初中英语', '仁爱版初中英语', '外研社初中英语', '沪教版牛津英语',
        '译林版牛津英语', '鲁教版五四学制', '冀教版三年级起点', '牛津上海版',
        '人教版小学英语', '人教版三年级起点', '人教版一年级起点',
        '北师大版小学英语', '北师大版三年级起点', '北师大版一年级起点',
        '北京版小学英语', '北京版一年级起点',
        '外研版小学英语', '外研版三年级起点',
        '译林版小学英语', '译林版三年级起点', '译林版牛津小学英语',
        '沪教版小学英语', '沪教版三年级起点',
        '广州版小学英语', '广州版三年级起点',
        '湘少版小学英语', '湘少版三年级起点',
        '闽教版小学英语', '闽教版三年级起点',
        '科普版小学英语', '科普版三年级起点',
        '广东版小学英语', '广东版三年级起点',
        '陕西版小学英语', '陕西版三年级起点',
        '冀教版小学英语', '冀教版三年级起点',
        '教科版EEC小学英语', '教科版EEC三年级起点',
        '全新版大学英语', '新视野大学英语', '新标准大学英语',
        '大学英语精读', '新世纪大学英语', '新编大学英语',
        '高级英语', '新世纪英语专业综合教程',
        '2003人教版PEP', '2004人教版PEP', '2007人教版初中',
    ]
    for p in textbook_patterns:
        if p in name:
            return '教材同步'
    
    # 人教版高中/外研社高中/牛津高中/北师大版高中 → 教材同步
    if cid == '3':
        if any(kw in name for kw in ['必修', '选修', '模块']):
            return '教材同步'
        # 剩下的高中类是备战高考
        return '备战高考'
    
    # 大学教材 category_id=4
    if cid == '4':
        return '教材同步'
    
    # 四六级
    if cid in ['5', '6', '7', '8']:
        return '四六级'
    
    # 考研 + 考博
    if cid in ['10', '11']:
        return '考研'
    
    # 出国留学
    if cid in ['14', '15', '16', '17', '18', '19', '20']:
        return '出国留学'
    
    # 职场提升
    if cid in ['21', '22']:
        return '职场提升'
    
    # 综合提升
    if cid in ['12', '23', '24']:
        return '综合提升'
    
    # category_id=9 (PETS/全国等级考试/AB级/大学生英语竞赛)
    if cid == '9':
        if '大学生英语竞赛' in name:
            return '综合提升'
        return '职场提升'
    
    # category_id=13 (自考/专升本/成人/同等学力/剑桥/Side by Side/Academic Voc List/英语单词笔记)
    if cid == '13':
        if '剑桥国际英语教程' in name or '朗文国际英语教程' in name or 'Side by Side' in name:
            return '综合提升'
        if 'Academic Voc List' in name or '英语单词笔记' in name:
            return '综合提升'
        return '职场提升'
    
    # category_id=25 (旧版废弃)
    if cid == '25':
        if '小学' in name or 'PEP' in name or '初中' in name:
            return '教材同步'
        if '四级' in name or '六级' in name or '四六级' in name:
            return '四六级'
        if '考研' in name:
            return '考研'
        if '雅思' in name or 'GRE' in name or '托福' in name or 'TOEFL' in name:
            return '出国留学'
        if '高中' in name:
            # Check if it's a textbook or prep book
            if any(kw in name for kw in ['必修', '选修', '模块']):
                return '教材同步'
            return '备战高考'
        return '综合提升'
    
    # Fallback based on name keywords
    if any(kw in name for kw in ['高考', '高中英语词汇', '高中英语巧记', '高中词汇', '高中短语']):
        return '备战高考'
    if any(kw in name for kw in ['四级', '六级', '四六级', '专四', '专八', 'CET']):
        return '四六级'
    if any(kw in name for kw in ['考研', '硕士研究生', '考博', '硕士博士']):
        return '考研'
    if any(kw in name for kw in ['托福', 'TOEFL', '雅思', 'IELTS', 'GRE', 'GMAT', 'SAT', 'ACT', '托业', 'TOEIC']):
        return '出国留学'
    if any(kw in name for kw in ['MBA', 'BEC', '成人', '专升本', '自考', '同等学力', 'PETS', '全国等级', 'AB级']):
        return '职场提升'
    if any(kw in name for kw in ['小学', '初中', '高中', '七年级', '八年级', '九年级']):
        return '教材同步'
    
    return '综合提升'

# Read CSV
with open('/Users/yr/ACE/执行结果590.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

# Add category column
new_fieldnames = fieldnames + ['category']

with open('/Users/yr/ACE/执行结果590_categorized.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=new_fieldnames)
    writer.writeheader()
    for row in rows:
        row['category'] = categorize(row)
        writer.writerow(row)

# Print summary
from collections import Counter
cats = Counter(row['category'] for row in rows)
for cat, count in cats.most_common():
    print(f"{cat}: {count}")
print(f"\nTotal: {len(rows)}")
