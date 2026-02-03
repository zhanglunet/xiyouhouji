#!/usr/bin/env python3
"""
自动生成《西游后记》章节脚本
每天生成一回新章节
"""

import os
import sys
from datetime import datetime

# 章节模板
CHAPTER_TEMPLATE = """# 第{chapter_num}回 {chapter_title}

{content}

---

**【本回完】**

---

*下回预告：*

第{next_chapter_num}回《{next_chapter_title}》

（待续...）
"""

# 章节大纲
CHAPTERS = {
    1: ("雷音寺佛祖论劫 花果山悟空思凡", """
五百年前，唐僧师徒西天取经功成。五百年后，三界再遭大劫。

雷音寺内，如来佛祖告知观音菩萨，唯有重走西游路，寻得"大乘真经"，方可化解此劫。观音领旨，前往花果山传旨。

孙悟空虽已成佛，但为三界众生，慨然应允。他一个筋斗云，望福陵山而去，要找二师弟猪八戒。
"""),
    2: ("福陵山悟空戏八戒 高老庄师徒诉旧情", """
福陵山云栈洞，猪八戒正在酣睡。悟空潜入洞中，变作小虫戏弄八戒。

八戒惊醒，见是师兄，又惊又喜。五百年不见，八戒还是那个贪吃懒做的呆子，但也多了几分稳重。

二人叙旧，谈起师父和沙师弟，不胜唏嘘。悟空说明来意，八戒虽有犹豫，但念及三界众生，也答应同行。

二人决定先去流沙河找沙悟净。
"""),
    3: ("流沙河沙僧悟道 取经路有缘人现", """
流沙河波涛汹涌，沙悟净正在岸边诵经。五百年清修，他已悟得大道，心境通明。

悟空、八戒驾云而至，三兄弟重逢，喜极而泣。沙僧听闻三界大劫，二话不说，愿随师兄们重走西游路。

三人决定前往长安，拜访师父唐三藏。

途中，他们路过一处村庄，忽闻呼救声。只见一群妖怪正在袭击村民。悟空大喝一声，挥棒上前...

与此同时，观音菩萨在云端看着这一切，微微一笑。那"有缘人"，似乎就要出现了。
"""),
    4: ("长安城唐僧讲经 大唐国御弟西行", """
长安大雁塔，唐三藏正在讲经说法。五百年过去，他依然慈悲为怀，普度众生。

悟空、八戒、沙僧来到长安，拜见师父。唐僧见到三个徒弟，老泪纵横。听闻三界大劫，唐僧毅然决定，要与徒弟们一同西行。

唐太宗得知此事，设宴饯行，封唐僧为"御弟"，赐号"西行取经大使"。

师徒四人，再加上观音菩萨指定的"有缘人"——一位名叫"明心"的年轻僧人，正式踏上了新的西游之路。

他们的第一站，是前往西域的火焰山...
"""),
}

def get_chapter_filename(chapter_num):
    """生成章节文件名"""
    return f"chapters/chapter{chapter_num:02d}.md"

def generate_chapter(chapter_num):
    """生成指定章节"""
    if chapter_num not in CHAPTERS:
        print(f"错误：第{chapter_num}回尚未定义")
        return False
    
    chapter_title, content = CHAPTERS[chapter_num]
    next_chapter_num = chapter_num + 1
    next_chapter_title = CHAPTERS.get(next_chapter_num, ("待续", ""))[0]
    
    # 生成章节内容
    chapter_content = CHAPTER_TEMPLATE.format(
        chapter_num=chapter_num,
        chapter_title=chapter_title,
        content=content.strip(),
        next_chapter_num=next_chapter_num,
        next_chapter_title=next_chapter_title
    )
    
    # 保存文件
    filename = get_chapter_filename(chapter_num)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(chapter_content)
    
    print(f"✅ 第{chapter_num}回《{chapter_title}》已生成")
    print(f"   文件：{filename}")
    return True

def update_readme(chapter_num):
    """更新README中的章节列表"""
    readme_file = 'README.md'
    
    if not os.path.exists(readme_file):
        print(f"警告：{readme_file} 不存在")
        return
    
    with open(readme_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 添加新章节到目录
    chapter_title = CHAPTERS.get(chapter_num, ("", ""))[0]
    if chapter_title:
        new_entry = f"- [第{chapter_num}回 {chapter_title}](chapters/chapter{chapter_num:02d}.md)\n"
        
        # 在章节目录后添加
        if '## 章节目录' in content:
            lines = content.split('\n')
            new_lines = []
            in_chapter_section = False
            for line in lines:
                new_lines.append(line)
                if '## 章节目录' in line:
                    in_chapter_section = True
                elif in_chapter_section and line.startswith('## '):
                    # 在下一个章节前插入新章节
                    new_lines.insert(-1, new_entry.rstrip())
                    in_chapter_section = False
            content = '\n'.join(new_lines)
        
        with open(readme_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ README.md 已更新")

def main():
    """主函数"""
    print("=" * 60)
    print("📚 《西游后记》自动更新脚本")
    print("=" * 60)
    print()
    
    # 获取今天应该更新的章节
    # 从2026年2月3日开始，每天更新一回
    start_date = datetime(2026, 2, 3)
    today = datetime.now()
    days_diff = (today - start_date).days
    
    if days_diff < 0:
        print(f"⏳ 还没到开始日期（2026年2月3日）")
        return
    
    chapter_num = days_diff + 1
    
    print(f"📅 今天是：{today.strftime('%Y年%m月%d日')}")
    print(f"📖 今天应该更新：第{chapter_num}回")
    print()
    
    # 检查章节是否已定义
    if chapter_num not in CHAPTERS:
        print(f"⏳ 第{chapter_num}回尚未定义，跳过更新")
        return
    
    # 生成章节
    if generate_chapter(chapter_num):
        # 更新README
        update_readme(chapter_num)
        
        print()
        print("=" * 60)
        print("✅ 更新完成！")
        print("=" * 60)
        print()
        print(f"📁 新章节文件：chapters/chapter{chapter_num:02d}.md")
        print("📝 请使用 git add、git commit、git push 推送到GitHub")
    else:
        print("❌ 更新失败")

if __name__ == "__main__":
    main()
