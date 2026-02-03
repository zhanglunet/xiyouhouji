#!/usr/bin/env python3
"""
《西游后记》绘本生成器
为每回生成精美插图
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import requests
import json

def get_font(size=40):
    """获取中文字体"""
    font_paths = [
        "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except:
                pass
    return ImageFont.load_default()

def create_scene_card(scene_title, chapter_num, scene_num, output_dir="picture_books"):
    """创建场景卡片"""
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 创建画布 (1080x1920，适合手机阅读)
    width, height = 1080, 1920
    img = Image.new('RGB', (width, height), color=(20, 20, 40))
    draw = ImageDraw.Draw(img)
    
    # 添加渐变背景
    for y in range(height):
        r = int(20 + (y / height) * 40)
        g = int(20 + (y / height) * 30)
        b = int(40 + (y / height) * 60)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # 添加装饰边框
    border_width = 20
    draw.rectangle(
        [(border_width, border_width), (width-border_width, height-border_width)],
        outline=(200, 180, 100), width=3
    )
    
    # 添加标题
    title_font = get_font(60)
    title = f"第{chapter_num}回"
    bbox = draw.textbbox((0, 0), title, font=title_font)
    title_w = bbox[2] - bbox[0]
    draw.text(((width - title_w) // 2, 100), title, font=title_font, fill=(255, 215, 0))
    
    # 添加场景标题
    scene_font = get_font(50)
    bbox = draw.textbbox((0, 0), scene_title, font=scene_font)
    scene_w = bbox[2] - bbox[0]
    draw.text(((width - scene_w) // 2, 200), scene_title, font=scene_font, fill=(255, 255, 255))
    
    # 添加占位符（这里可以放AI生成的图片）
    placeholder_y = 350
    placeholder_height = 1000
    
    # 绘制图片占位区域
    draw.rectangle(
        [(80, placeholder_y), (width-80, placeholder_y + placeholder_height)],
        fill=(40, 40, 60), outline=(150, 150, 150), width=2
    )
    
    # 添加占位符文字
    placeholder_font = get_font(40)
    placeholder_text = "[ 绘本插图区域 ]"
    bbox = draw.textbbox((0, 0), placeholder_text, font=placeholder_font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    text_x = (width - text_w) // 2
    text_y = placeholder_y + (placeholder_height - text_h) // 2
    draw.text((text_x, text_y), placeholder_text, font=placeholder_font, fill=(150, 150, 150))
    
    # 添加描述文字
    desc_font = get_font(30)
    desc_text = f"第{scene_num}场景 - 待AI生成精美插图"
    bbox = draw.textbbox((0, 0), desc_text, font=desc_font)
    desc_w = bbox[2] - bbox[0]
    draw.text(((width - desc_w) // 2, placeholder_y + placeholder_height + 30), desc_text, font=desc_font, fill=(180, 180, 180))
    
    # 添加页脚
    footer_font = get_font(24)
    footer_text = f"《西游后记》第{chapter_num}回 · 场景{scene_num} · {scene_title}"
    bbox = draw.textbbox((0, 0), footer_text, font=footer_font)
    footer_w = bbox[2] - bbox[0]
    draw.text(((width - footer_w) // 2, height - 60), footer_text, font=footer_font, fill=(150, 150, 150))
    
    # 保存图片
    output_file = os.path.join(output_dir, f"chapter{chapter_num:02d}_scene{scene_num:02d}.png")
    img.save(output_file, "PNG", quality=95)
    print(f"  ✅ 绘本卡片已生成: {output_file}")
    
    return output_file

def create_chapter_picture_book(chapter_num, output_dir="picture_books"):
    """为一回创建完整绘本"""
    if chapter_num not in CHAPTERS:
        print(f"❌ 第{chapter_num}回尚未定义")
        return []
    
    chapter = CHAPTERS[chapter_num]
    scenes = chapter["scenes"]
    
    print(f"\n🎨 正在为第{chapter_num}回《{chapter['title']}》生成绘本...")
    print(f"   共{len(scenes)}个场景")
    
    generated_files = []
    
    for i, scene_title in enumerate(scenes, 1):
        try:
            file_path = create_scene_card(scene_title, chapter_num, i, output_dir)
            generated_files.append(file_path)
        except Exception as e:
            print(f"  ❌ 场景{i}生成失败: {e}")
    
    print(f"\n✅ 第{chapter_num}回绘本生成完成！")
    print(f"   共生成{len(generated_files)}张绘本卡片")
    
    return generated_files

def main():
    """主函数"""
    print("=" * 70)
    print("📚 《西游后记》绘本生成器")
    print("=" * 70)
    print()
    
    # 获取命令行参数
    if len(sys.argv) > 1:
        try:
            chapter_num = int(sys.argv[1])
        except ValueError:
            print("❌ 参数错误：请提供章节数字")
            return
    else:
        # 默认生成所有已定义的章节
        chapter_num = None
    
    output_dir = "picture_books"
    os.makedirs(output_dir, exist_ok=True)
    
    if chapter_num:
        # 生成指定章节
        create_chapter_picture_book(chapter_num, output_dir)
    else:
        # 生成所有已定义的章节
        for num in sorted(CHAPTERS.keys()):
            create_chapter_picture_book(num, output_dir)
            print()
    
    print("=" * 70)
    print("🎉 绘本生成完成！")
    print("=" * 70)
    print()
    print(f"📁 输出目录: {output_dir}/")
    print()

if __name__ == "__main__":
    main()
