#!/bin/bash

# 传记人物照片批量下载脚本
# 使用方法: bash download_portraits.sh

BIO_DIR="/Users/pengwenfan/project/pwf/ai/myClaw/Biography"

echo "开始下载传记人物照片..."
echo "================================"

# 下载函数
download_portrait() {
    local name="$1"
    local url="$2"
    local dir="$BIO_DIR/$name/images"
    local ext="${url##*.}"
    local output="$dir/portrait"

    mkdir -p "$dir"

    if [ -f "$dir/portrait.jpg" ] || [ -f "$dir/portrait.png" ]; then
        echo "⏭️  跳过 $name (已存在)"
        return 0
    fi

    echo "📥 下载 $name..."

    # 使用curl下载
    curl -L --retry 3 --retry-delay 2 \
         -o "${output}.${ext}" \
         -A "Mozilla/5.0" \
         "$url" 2>/dev/null

    if [ -f "${output}.${ext}" ] && [ -s "${output}.${ext}" ]; then
        # 转换为jpg
        if [ "$ext" != "jpg" ]; then
            mv "${output}.${ext}" "${output}.jpg"
        fi
        echo "✅ 完成 $name"
    else
        echo "❌ 失败 $name"
        rm -f "${output}.${ext}"
        return 1
    fi
}

# 逐个下载 - 避免关联数组语法问题
echo "📥 下载 Elon Musk..."
[ -d "$BIO_DIR/Elon Musk/images" ] && curl -L -o "$BIO_DIR/Elon Musk/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/0/06/Elon_Musk,_2018_(cropped).jpg" 2>/dev/null && echo "✅ Elon Musk 完成"

echo "📥 下载 Tim Cook..."
[ -d "$BIO_DIR/Tim Cook/images" ] && curl -L -o "$BIO_DIR/Tim Cook/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Tim_Cook_(2017,_cropped).jpg/440px-Tim_Cook_(2017,_cropped).jpg" 2>/dev/null && echo "✅ Tim Cook 完成"

echo "📥 下载 Satya Nadella..."
[ -d "$BIO_DIR/Satya Nadella/images" ] && curl -L -o "$BIO_DIR/Satya Nadella/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Satya_Nadella.jpg/440px-Satya_Nadella.jpg" 2>/dev/null && echo "✅ Satya Nadella 完成"

echo "📥 下载 Sundar Pichai..."
[ -d "$BIO_DIR/Sundar Pichai/images" ] && curl -L -o "$BIO_DIR/Sundar Pichai/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Sundar_Pichai.jpg/440px-Sundar_Pichai.jpg" 2>/dev/null && echo "✅ Sundar Pichai 完成"

echo "📥 下载 Mark Zuckerberg..."
[ -d "$BIO_DIR/Mark Zuckerberg/images" ] && curl -L -o "$BIO_DIR/Mark Zuckerberg/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Mark_Zuckerberg_F8_2019_Keynote_%28cropped%29.jpg/440px-Mark_Zuckerberg_F8_2019_Keynote_%28cropped%29.jpg" 2>/dev/null && echo "✅ Mark Zuckerberg 完成"

echo "📥 下载 Jeff Bezos..."
[ -d "$BIO_DIR/Jeff Bezos/images" ] && curl -L -o "$BIO_DIR/Jeff Bezos/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Jeff_Bezos_at_Economic_Times_India_Tomorrow_Summit_2014.jpg/440px-Jeff_Bezos_at_Economic_Times_India_Tomorrow_Summit_2014.jpg" 2>/dev/null && echo "✅ Jeff Bezos 完成"

echo "📥 下载 Jensen Huang..."
[ -d "$BIO_DIR/Jensen Huang/images" ] && curl -L -o "$BIO_DIR/Jensen Huang/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Jensen_Huang_%28cropped%29.jpg/440px-Jensen_Huang_%28cropped%29.jpg" 2>/dev/null && echo "✅ Jensen Huang 完成"

echo "📥 下载 Tim Sweeney..."
[ -d "$BIO_DIR/Tim Sweeney/images" ] && curl -L -o "$BIO_DIR/Tim Sweeney/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Tim_Sweeney_at_GDC_2016_%28cropped%29.jpg/440px-Tim_Sweeney_at_GDC_2016_%28cropped%29.jpg" 2>/dev/null && echo "✅ Tim Sweeney 完成"

echo "📥 下载 Jack Dorsey..."
[ -d "$BIO_DIR/Jack Dorsey/images" ] && curl -L -o "$BIO_DIR/Jack Dorsey/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Jack_Dorsey.jpg/440px-Jack_Dorsey.jpg" 2>/dev/null && echo "✅ Jack Dorsey 完成"

echo "📥 下载 Sam Altman..."
[ -d "$BIO_DIR/Sam Altman/images" ] && curl -L -o "$BIO_DIR/Sam Altman/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Sam_Altman_TechCrunch_SF_2019_%28cropped%29.jpg/440px-Sam_Altman_TechCrunch_SF_2019_%28cropped%29.jpg" 2>/dev/null && echo "✅ Sam Altman 完成"

echo "📥 下载 乔布斯..."
[ -d "$BIO_DIR/乔布斯/images" ] && curl -L -o "$BIO_DIR/乔布斯/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Steve_Jobs_Headshot_2010-CROP_%28cropped_2%29.jpg/440px-Steve_Jobs_Headshot_2010-CROP_%28cropped_2%29.jpg" 2>/dev/null && echo "✅ 乔布斯 完成"

# 国内人物
echo "📥 下载 马化腾..."
[ -d "$BIO_DIR/马化腾/images" ] && curl -L -o "$BIO_DIR/马化腾/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/d/d6/%E9%A9%AC%E5%8C%96%E8%85%BE_Pony_Ma_2019.jpg" 2>/dev/null && echo "✅ 马化腾 完成"

echo "📥 下载 张一鸣..."
[ -d "$BIO_DIR/张一鸣/images" ] && curl -L -o "$BIO_DIR/张一鸣/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Zhang_Yiming.jpg/440px-Zhang_Yiming.jpg" 2>/dev/null && echo "✅ 张一鸣 完成"

echo "📥 下载 刘强东..."
[ -d "$BIO_DIR/刘强东/images" ] && curl -L -o "$BIO_DIR/刘强东/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Liu_Qiangdong_WEF_2011.jpg/440px-Liu_Qiangdong_WEF_2011.jpg" 2>/dev/null && echo "✅ 刘强东 完成"

echo "📥 下载 马云..."
[ -d "$BIO_DIR/马云/images" ] && curl -L -o "$BIO_DIR/马云/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Jack_Ma_2015.jpg/440px-Jack_Ma_2015.jpg" 2>/dev/null && echo "✅ 马云 完成"

echo "📥 下载 李彦宏..."
[ -d "$BIO_DIR/李彦宏/images" ] && curl -L -o "$BIO_DIR/李彦宏/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Li_Yanhong.jpg/440px-Li_Yanhong.jpg" 2>/dev/null && echo "✅ 李彦宏 完成"

echo "📥 下载 雷军..."
[ -d "$BIO_DIR/雷军/images" ] && curl -L -o "$BIO_DIR/雷军/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Lei_June_2023.jpg/440px-Lei_June_2023.jpg" 2>/dev/null && echo "✅ 雷军 完成"

echo "📥 下载 周鸿祎..."
[ -d "$BIO_DIR/周鸿祎/images" ] && curl -L -o "$BIO_DIR/周鸿祎/images/portrait.png" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/b/bf/Zhou_Hongyi-20240307.png" 2>/dev/null && echo "✅ 周鸿祎 完成"

echo "📥 下载 王兴..."
[ -d "$BIO_DIR/王兴/images" ] && curl -L -o "$BIO_DIR/王兴/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Wang_Xing_2023.jpg/440px-Wang_Xing_2023.jpg" 2>/dev/null && echo "✅ 王兴 完成"

echo "📥 下载 黄铮..."
[ -d "$BIO_DIR/黄铮/images" ] && curl -L -o "$BIO_DIR/黄铮/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Colin_Huang.jpg/440px-Colin_Huang.jpg" 2>/dev/null && echo "✅ 黄铮 完成"

echo "📥 下载 王传福..."
[ -d "$BIO_DIR/王传福/images" ] && curl -L -o "$BIO_DIR/王传福/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Wang_Chuanfu.jpg/440px-Wang_Chuanfu.jpg" 2>/dev/null && echo "✅ 王传福 完成"

echo "📥 下载 任正非..."
[ -d "$BIO_DIR/任正非/images" ] && curl -L -o "$BIO_DIR/任正非/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Ren_Zhengfei_2023.jpg/440px-Ren_Zhengfei_2023.jpg" 2>/dev/null && echo "✅ 任正非 完成"

echo "📥 下载 董明珠..."
[ -d "$BIO_DIR/董明珠/images" ] && curl -L -o "$BIO_DIR/董明珠/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/e/e2/Dong_Mingzhu.JPG" 2>/dev/null && echo "✅ 董明珠 完成"

echo "📥 下载 何享健..."
[ -d "$BIO_DIR/何享健/images" ] && curl -L -o "$BIO_DIR/何享健/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/He_Xiangjian.jpg/440px-He_Xiangjian.jpg" 2>/dev/null && echo "✅ 何享健 完成"

echo "📥 下载 王健林..."
[ -d "$BIO_DIR/王健林/images" ] && curl -L -o "$BIO_DIR/王健林/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Wang_Jianlin_2023.jpg/440px-Wang_Jianlin_2023.jpg" 2>/dev/null && echo "✅ 王健林 完成"

echo "📥 下载 许家印..."
[ -d "$BIO_DIR/许家印/images" ] && curl -L -o "$BIO_DIR/许家印/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Hui_Ka_Yan_2023.jpg/440px-Hui_Ka_Yan_2023.jpg" 2>/dev/null && echo "✅ 许家印 完成"

echo "📥 下载 王卫..."
[ -d "$BIO_DIR/王卫/images" ] && curl -L -o "$BIO_DIR/王卫/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Wang_Wei_2019.jpg/440px-Wang_Wei_2019.jpg" 2>/dev/null && echo "✅ 王卫 完成"

echo "📥 下载 丁磊..."
[ -d "$BIO_DIR/丁磊/images" ] && curl -L -o "$BIO_DIR/丁磊/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Ding_Lei.jpg/440px-Ding_Lei.jpg" 2>/dev/null && echo "✅ 丁磊 完成"

echo "📥 下载 李书福..."
[ -d "$BIO_DIR/李书福/images" ] && curl -L -o "$BIO_DIR/李书福/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Li_Shufu.jpg/440px-Li_Shufu.jpg" 2>/dev/null && echo "✅ 李书福 完成"

echo "📥 下载 曹德旺..."
[ -d "$BIO_DIR/曹德旺/images" ] && curl -L -o "$BIO_DIR/曹德旺/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Cao_Dewang.jpg/440px-Cao_Dewang.jpg" 2>/dev/null && echo "✅ 曹德旺 完成"

echo "📥 下载 钟睒睒..."
[ -d "$BIO_DIR/钟睒睒/images" ] && curl -L -o "$BIO_DIR/钟睒睒/images/portrait.jpg" -A "Mozilla/5.0" "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Zhong_Shanshan.jpg/440px-Zhong_Shanshan.jpg" 2>/dev/null && echo "✅ 钟睒睒 完成"

echo "================================"
echo "下载完成！"
