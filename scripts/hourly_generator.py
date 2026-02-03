#!/usr/bin/env python3
"""
《西游后记》每小时自动更新脚本
生成新章节 + 绘本插图
"""

import os
import sys
import json
from datetime import datetime

# 章节大纲 - 已规划的前10回
CHAPTERS = {
    1: {
        "title": "雷音寺佛祖论劫 花果山悟空思凡",
        "summary": "如来佛祖预言三界大劫，观音菩萨前往花果山传旨，悟空慨然应允，一个筋斗云往福陵山找八戒。",
        "scenes": [
            "雷音寺佛祖论劫",
            "观音菩萨领旨",
            "花果山水帘洞",
            "悟空与观音对话",
            "悟空决定出发"
        ]
    },
    2: {
        "title": "福陵山悟空戏八戒 高老庄师徒诉旧情",
        "summary": "悟空来到福陵山云栈洞，戏弄还在睡懒觉的八戒。五百年不见，二人叙旧，八戒虽有犹豫，但最终答应重走西游路。",
        "scenes": [
            "福陵山云栈洞",
            "八戒正在酣睡",
            "悟空变虫戏八戒",
            "师兄弟叙旧",
            "八戒答应同行"
        ]
    },
    3: {
        "title": "流沙河沙僧悟道 取经路有缘人现",
        "summary": "三人来到流沙河，沙僧正在诵经。三兄弟重逢，沙僧二话不说答应同行。途中救下一村庄，有缘人"明心"出现。",
        "scenes": [
            "流沙河岸边",
            "沙僧诵经悟道",
            "师兄弟三人重逢",
            "妖怪袭击村庄",
            "有缘人明心出现"
        ]
    },
    4: {
        "title": "长安城唐僧讲经 大唐国御弟西行",
        "summary": "师徒来到长安，拜见师父唐僧。唐僧虽已成佛，但为三界众生，决定再次西行。唐太宗设宴饯行，封唐僧为御弟。",
        "scenes": [
            "长安大雁塔",
            "唐僧正在讲经",
            "师徒四人拜见",
            "唐僧决定西行",
            "唐太宗设宴饯行"
        ]
    },
    5: {
        "title": "两界山初遇妖魔 五行山重忆往事",
        "summary": "师徒行至两界山，遇到新妖怪"混沌魔王"。悟空与之大战，师徒齐心降妖。路过五行山，悟空重忆当年。",
        "scenes": [
            "两界山险峻",
            "混沌魔王出现",
            "悟空大战魔王",
            "师徒齐心降妖",
            "五行山前回忆"
        ]
    },
    6: {
        "title": "鹰愁涧白龙再现 新取经路险象生",
        "summary": "行至鹰愁涧，白龙马早已修成正果，这次是它的后辈"玉龙太子"前来相助。师徒六人正式集结。",
        "scenes": [
            "鹰愁涧深潭",
            "白龙已成正果",
            "玉龙太子现身",
            "新白龙马加入",
            "师徒六人集结"
        ]
    },
    7: {
        "title": "观音院金池转世 黑风山熊罴重修",
        "summary": "路过观音院，发现金池长老转世为善良僧人。黑风山黑熊精也已修成正果，这次是新妖怪"暗影大王"。",
        "scenes": [
            "观音院旧址",
            "金池长老转世",
            "善良僧人出现",
            "黑风山新妖怪",
            "暗影大王现身"
        ]
    },
    8: {
        "title": "高老庄再访八戒家 云栈洞重聚师徒情",
        "summary": "路过福陵山，八戒想回家看看。发现云栈洞已被新妖怪占据。师徒合力降妖，八戒感慨万千。",
        "scenes": [
            "福陵山旧路",
            "八戒想家",
            "云栈洞被占",
            "新妖怪出现",
            "师徒合力降妖"
        ]
    },
    9: {
        "title": "黄风岭虎先锋再现 灵吉菩萨新传妙法",
        "summary": "黄风岭上，虎先锋的后人"狂风魔王"兴风作浪。灵吉菩萨前来相助，传授新的降魔法门。",
        "scenes": [
            "黄风岭狂风",
            "狂风魔王出现",
            "虎先锋后人",
            "灵吉菩萨来助",
            "新传降魔法门"
        ]
    },
    10: {
        "title": "流沙河重聚三兄弟 取经路初见大乘经",
        "summary": "返回流沙河，三兄弟重聚。河中出现异象，"大乘真经"的第一页显现。新的取经路正式开启！",
        "scenes": [
            "流沙河重逢",
            "三兄弟重聚",
            "河中出现异象",
            "大乘经显现",
            "新取经路开启"
        ]
    }
}

def generate_chapter_content(chapter_num):
    """生成章节内容"""
    if chapter_num not in CHAPTERS:
        return None
    
    chapter = CHAPTERS[chapter_num]
    title = chapter["title"]
    summary = chapter["summary"]
    scenes = chapter["scenes"]
    
    # 生成正文
    content = f"""## {title}

**本回概要：** {summary}

---

"""
    
    # 添加每个场景的详细描述
    for i, scene in enumerate(scenes, 1):
        content += f"""### 场景{i}：{scene}

【详细描写待AI生成】

"""
    
    content += f"""---

**本回结束，敬请期待下一回：**

第{chapter_num + 1}回《{CHAPTERS.get(chapter_num + 1, {}).get('title', '待续')}》
"""
    
    return {
        "num": chapter_num,
        "title": title,
        "content": content,
        "scenes": scenes
    }

def save_chapter(chapter_data):
    """保存章节到文件"""
    filename = f"chapters/chapter{chapter_data['num']:02d}.md"
    
    full_content = f"""# 第{chapter_data['num']}回 {chapter_data['title']}

{chapter_data['content']}

---

**【本回完】**

---

*更新时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    print(f"✅ 章节已保存: {filename}")
    return filename

def update_readme(chapter_num, chapter_title):
    """更新README.md"""
    readme_file = 'README.md'
    
    with open(readme_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 添加新章节到目录
    new_entry = f"- [第{chapter_num}回 {chapter_title}](chapters/chapter{chapter_num:02d}.md)\n"
    
    # 找到章节目录部分并插入
    if '## 章节目录' in content:
        lines = content.split('\n')
        new_lines = []
        in_chapter_section = False
        inserted = False
        
        for line in lines:
            new_lines.append(line)
            if '## 章节目录' in line:
                in_chapter_section = True
            elif in_chapter_section and line.startswith('- [第'):
                # 检查是否已经插入过这个章节
                if f'第{chapter_num}回' in line:
                    inserted = True
            elif in_chapter_section and line.startswith('## ') and not inserted:
                # 在下一个章节前插入
                new_lines.insert(-1, new_entry.rstrip())
                inserted = True
                in_chapter_section = False
        
        if not inserted and in_chapter_section:
            new_lines.append(new_entry.rstrip())
        
        content = '\n'.join(new_lines)
        
        with open(readme_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ README.md 已更新")

def main():
    """主函数"""
    print("=" * 60)
    print("📚 《西游后记》章节生成器")
    print("=" * 60)
    print()
    
    # 确定要生成的章节
    # 从2026年2月3日开始，每小时更新一回
    start_date = datetime(2026, 2, 3, 0, 0, 0)
    now = datetime.now()
    hours_diff = int((now - start_date).total_seconds() / 3600)
    
    if hours_diff < 0:
        chapter_num = 1  # 从第一回开始
    else:
        chapter_num = min(hours_diff + 1, 100)  # 最多100回
    
    # 检查是否已经生成过
    chapter_file = f"chapters/chapter{chapter_num:02d}.md"
    if os.path.exists(chapter_file):
        print(f"⏳ 第{chapter_num}回已存在，跳过生成")
        print(f"   文件：{chapter_file}")
        return
    
    print(f"📅 当前时间：{now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📖 生成第{chapter_num}回")
    print()
    
    # 生成章节
    chapter_data = generate_chapter_content(chapter_num)
    if chapter_data:
        # 保存章节
        save_chapter(chapter_data)
        
        # 更新README
        update_readme(chapter_num, chapter_data['title'])
        
        print()
        print("=" * 60)
        print("✅ 章节生成完成！")
        print("=" * 60)
        print()
        print(f"📁 新章节：{chapter_file}")
        print(f"📖 标题：第{chapter_num}回 {chapter_data['title']}")
        print(f"🎨 场景数：{len(chapter_data['scenes'])}")
    else:
        print("❌ 章节生成失败")

if __name__ == "__main__":
    main()
