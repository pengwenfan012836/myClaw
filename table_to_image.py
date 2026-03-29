#!/usr/bin/env python3
"""使用Pillow绘制表格并保存为PNG"""

from PIL import Image, ImageDraw, ImageFont
import textwrap

def draw_table():
    # 表格数据
    headers = ["人群", "原因"]
    rows = [
        ["讨好型人格", "总在意别人眼光、害怕被讨厌？书中告诉你如何摆脱认可欲求，找回自己"],
        ["容易内耗的人", "总在纠结'别人怎么看我'？课题分离让你轻松做自己"],
        ["想改变但总失败", "觉得'我就是这样改不了'？目的论帮你打破借口，勇敢改变"],
        ["心理学爱好者", "阿德勒心理学入门必读，对话体形式轻松易懂"],
        ["迷茫的年轻人", "不知道人生意义？书中说'意义由你自己决定'"],
    ]

    # 字体设置
    font_size = 15
    try:
        font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", font_size)
        header_font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", font_size + 2)
    except:
        font = ImageFont.load_default()
        header_font = font

    # 尺寸设置
    padding = 20
    line_height = 42
    header_height = 40
    col1_width = 130
    col2_width = 520
    table_width = col1_width + col2_width + padding * 3
    table_height = header_height + line_height * len(rows) + padding * 2

    # 创建图片
    img = Image.new('RGB', (table_width, table_height), 'white')
    draw = ImageDraw.Draw(img)

    # 绘制表头
    draw.rectangle([padding, padding, table_width - padding, padding + header_height], fill='#4a90d9')
    draw.text((padding + 10, padding + 8), headers[0], font=header_font, fill='white')
    draw.text((padding + col1_width + 20, padding + 8), headers[1], font=header_font, fill='white')

    # 绘制数据行
    y = padding + header_height
    for i, row in enumerate(rows):
        bg_color = '#f8f9fa' if i % 2 == 0 else 'white'
        draw.rectangle([padding, y, table_width - padding, y + line_height], fill=bg_color)
        
        # 第一列
        draw.text((padding + 10, y + 10), row[0], font=font, fill='#333')
        
        # 第二列 - 自动换行
        wrapped = textwrap.wrap(row[1], width=32)
        text_y = y + 8
        for line_text in wrapped:
            draw.text((padding + col1_width + 20, text_y), line_text, font=font, fill='#333')
            text_y += 20
        
        # 画横线
        draw.line([(padding, y + line_height), (table_width - padding, y + line_height)], fill='#ddd', width=1)
        
        y += line_height

    # 画外边框
    draw.rectangle([padding, padding, table_width - padding, table_height - padding], outline='#999', width=2)

    # 画竖线
    x1 = padding + col1_width + 10
    draw.line([(x1, padding), (x1, table_height - padding)], fill='#999', width=2)

    output_path = "book/被讨厌的勇气/推荐人群表.png"
    img.save(output_path)
    print(f"表格图片已保存: {output_path}")

if __name__ == '__main__':
    draw_table()
