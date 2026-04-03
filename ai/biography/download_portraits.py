#!/usr/bin/env python3
"""下载传记人物照片"""

import os
import time
import urllib.request

BIO_DIR = "/Users/pengwenfan/project/pwf/ai/myClaw/Biography"

# 人物和URL映射
people = [
    # 国外
    ("Elon Musk", "https://upload.wikimedia.org/wikipedia/commons/0/06/Elon_Musk,_2018_(cropped).jpg"),
    ("Tim Cook", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Tim_Cook_(2017,_cropped).jpg/440px-Tim_Cook_(2017,_cropped).jpg"),
    ("Satya Nadella", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Satya_Nadella.jpg/440px-Satya_Nadella.jpg"),
    ("Sundar Pichai", "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Sundar_Pichai.jpg/440px-Sundar_Pichai.jpg"),
    ("Mark Zuckerberg", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Mark_Zuckerberg_F8_2019_Keynote_%28cropped%29.jpg/440px-Mark_Zuckerberg_F8_2019_Keynote_%28cropped%29.jpg"),
    ("Jeff Bezos", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Jeff_Bezos_at_Economic_Times_India_Tomorrow_Summit_2014.jpg/440px-Jeff_Bezos_at_Economic_Times_India_Tomorrow_Summit_2014.jpg"),
    ("Jensen Huang", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Jensen_Huang_%28cropped%29.jpg/440px-Jensen_Huang_%28cropped%29.jpg"),
    ("Tim Sweeney", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Tim_Sweeney_at_GDC_2016_%28cropped%29.jpg/440px-Tim_Sweeney_at_GDC_2016_%28cropped%29.jpg"),
    ("Jack Dorsey", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Jack_Dorsey.jpg/440px-Jack_Dorsey.jpg"),
    ("Sam Altman", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Sam_Altman_TechCrunch_SF_2019_%28cropped%29.jpg/440px-Sam_Altman_TechCrunch_SF_2019_%28cropped%29.jpg"),
    ("乔布斯", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Steve_Jobs_Headshot_2010-CROP_%28cropped_2%29.jpg/440px-Steve_Jobs_Headshot_2010-CROP_%28cropped_2%29.jpg"),
    # 国内
    ("马化腾", "https://upload.wikimedia.org/wikipedia/commons/d/d6/%E9%A9%AC%E5%8C%96%E8%85%BE_Pony_Ma_2019.jpg"),
    ("张一鸣", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Zhang_Yiming.jpg/440px-Zhang_Yiming.jpg"),
    ("刘强东", "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Liu_Qiangdong_WEF_2011.jpg/440px-Liu_Qiangdong_WEF_2011.jpg"),
    ("马云", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Jack_Ma_2015.jpg/440px-Jack_Ma_2015.jpg"),
    ("李彦宏", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Li_Yanhong.jpg/440px-Li_Yanhong.jpg"),
    ("雷军", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Lei_June_2023.jpg/440px-Lei_June_2023.jpg"),
    ("周鸿祎", "https://upload.wikimedia.org/wikipedia/commons/b/bf/Zhou_Hongyi-20240307.png"),
    ("王兴", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Wang_Xing_2023.jpg/440px-Wang_Xing_2023.jpg"),
    ("黄铮", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Colin_Huang.jpg/440px-Colin_Huang.jpg"),
    ("王传福", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Wang_Chuanfu.jpg/440px-Wang_Chuanfu.jpg"),
    ("任正非", "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Ren_Zhengfei_2023.jpg/440px-Ren_Zhengfei_2023.jpg"),
    ("董明珠", "https://upload.wikimedia.org/wikipedia/commons/e/e2/Dong_Mingzhu.JPG"),
    ("何享健", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/He_Xiangjian.jpg/440px-He_Xiangjian.jpg"),
    ("王健林", "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Wang_Jianlin_2023.jpg/440px-Wang_Jianlin_2023.jpg"),
    ("许家印", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Hui_Ka_Yan_2023.jpg/440px-Hui_Ka_Yan_2023.jpg"),
    ("王卫", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Wang_Wei_2019.jpg/440px-Wang_Wei_2019.jpg"),
    ("丁磊", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Ding_Lei.jpg/440px-Ding_Lei.jpg"),
    ("李书福", "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Li_Shufu.jpg/440px-Li_Shufu.jpg"),
    ("曹德旺", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Cao_Dewang.jpg/440px-Cao_Dewang.jpg"),
    ("钟睒睒", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Zhong_Shanshan.jpg/440px-Zhong_Shanshan.jpg"),
]

def download_image(name, url):
    """下载单张图片"""
    dir_path = os.path.join(BIO_DIR, name, "images")
    os.makedirs(dir_path, exist_ok=True)

    # 检查是否已存在
    jpg_path = os.path.join(dir_path, "portrait.jpg")
    png_path = os.path.join(dir_path, "portrait.png")

    if os.path.exists(jpg_path) and os.path.getsize(jpg_path) > 1000:
        print(f"⏭️  跳过 {name} (已存在)")
        return True
    if os.path.exists(png_path) and os.path.getsize(png_path) > 1000:
        print(f"⏭️  跳过 {name} (已存在)")
        return True

    print(f"📥 下载 {name}...")

    # 确定扩展名
    ext = "png" if url.endswith(".png") else "jpg"
    output_path = os.path.join(dir_path, f"portrait.{ext}")

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        req = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(req, timeout=30) as response:
            data = response.read()

        with open(output_path, 'wb') as f:
            f.write(data)

        if os.path.getsize(output_path) > 1000:
            print(f"✅ 完成 {name} ({len(data)} bytes)")
            return True
        else:
            print(f"❌ 失败 {name} (文件太小)")
            os.remove(output_path)
            return False

    except Exception as e:
        print(f"❌ 失败 {name}: {str(e)}")
        return False

def main():
    print("开始下载传记人物照片...")
    print("=" * 40)

    success_count = 0
    fail_count = 0
    failed_list = []

    for name, url in people:
        # 检查目录是否存在
        person_dir = os.path.join(BIO_DIR, name)
        if not os.path.isdir(person_dir):
            print(f"⏭️  跳过 {name} (目录不存在)")
            continue

        if download_image(name, url):
            success_count += 1
        else:
            fail_count += 1
            failed_list.append(name)

        time.sleep(0.5)  # 避免请求过快

    print("=" * 40)
    print(f"下载完成！成功: {success_count}, 失败: {fail_count}")

    if failed_list:
        print(f"失败的人物: {', '.join(failed_list)}")

if __name__ == "__main__":
    main()