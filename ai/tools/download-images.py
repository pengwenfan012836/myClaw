#!/usr/bin/env python3
"""
从网页批量提取并下载图片
使用方式：
1. 用 Playwright MCP 打开目标页面
2. 执行 JS 提取图片 URL
3. 将 URL 列表保存到 urls.txt
4. 运行: python download-images.py
"""

import requests
import os
import time
from urllib.parse import urlparse, urljoin
from pathlib import Path

# 配置
SAVE_DIR = "./downloaded-images"
CONCURRENCY = 5  # 并发数

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
    "Referer": "https://www.google.com"
}


def get_extension(url):
    """从 URL 获取文件扩展名"""
    parsed = urlparse(url)
    path = parsed.path
    ext = os.path.splitext(path)[1]
    if not ext or len(ext) > 5:
        return '.jpg'
    return ext


def download_single(url, save_dir, index):
    """下载单张图片"""
    try:
        if url.startswith('data:') or url.startswith('blob:'):
            return False, f"跳过 base64/blob: {url[:50]}..."

        ext = get_extension(url)
        filename = f"img_{index:04d}{ext}"
        filepath = os.path.join(save_dir, filename)

        if os.path.exists(filepath):
            return True, f"已存在: {filename}"

        response = requests.get(url, headers=headers, timeout=15, allow_redirects=True)
        
        if response.status_code == 200:
            content_type = response.headers.get('Content-Type', '')
            if 'image' not in content_type and not ext:
                return False, f"非图片类型: {content_type}"
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            size = len(response.content) / 1024
            return True, f"✅ {filename} ({size:.1f}KB)"
        else:
            return False, f"HTTP {response.status_code}"
            
    except requests.exceptions.Timeout:
        return False, "超时"
    except requests.exceptions.ConnectionError:
        return False, "连接失败"
    except Exception as e:
        return False, str(e)[:50]


def download_from_file(filepath, save_dir):
    """从文件读取 URL 列表并下载"""
    os.makedirs(save_dir, exist_ok=True)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    if not urls:
        print("❌ 未找到 URL，请检查文件内容")
        return
    
    print(f"📥 开始下载 {len(urls)} 张图片...\n")
    
    success = 0
    failed = []
    
    for i, url in enumerate(urls, 1):
        ok, msg = download_single(url, save_dir, i)
        status = "✅" if ok else "❌"
        print(f"{status} [{i}/{len(urls)}] {msg}")
        
        if ok:
            success += 1
        else:
            failed.append((url, msg))
        
        if i % 10 == 0:
            time.sleep(1)
    
    print(f"\n📊 完成：成功 {success}/{len(urls)}")
    
    if failed:
        print(f"\n❌ 失败列表 ({len(failed)} 个)：")
        for url, err in failed[:10]:
            print(f"  - {err}: {url[:80]}")
        if len(failed) > 10:
            print(f"  ... 还有 {len(failed) - 10} 个")


def download_from_urls(urls, save_dir):
    """直接从 URL 列表下载"""
    os.makedirs(save_dir, exist_ok=True)
    
    print(f"📥 开始下载 {len(urls)} 张图片...\n")
    
    success = 0
    for i, url in enumerate(urls, 1):
        ok, msg = download_single(url, save_dir, i)
        print(f"{'✅' if ok else '❌'} [{i}/{len(urls)}] {msg}")
        if ok:
            success += 1
    
    print(f"\n📊 完成：成功 {success}/{len(urls)}")


def extract_from_html(html_content, base_url=""):
    """从 HTML 内容提取图片 URL"""
    import re
    
    urls = []
    
    # 提取 <img src>
    urls.extend(re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html_content, re.IGNORECASE))
    
    # 提取 <img data-src
    urls.extend(re.findall(r'<img[^>]+data-src=["\']([^"\']+)["\']', html_content, re.IGNORECASE))
    
    # 提取 srcset
    srcsets = re.findall(r'srcset=["\']([^"\']+)["\']', html_content, re.IGNORECASE)
    for srcset in srcsets:
        for part in srcset.split(','):
            url = part.strip().split()[0]
            if url:
                urls.append(url)
    
    # 转绝对 URL
    absolute_urls = []
    for url in urls:
        if url.startswith('//'):
            url = 'https:' + url
        elif url.startswith('/'):
            parsed = urlparse(base_url)
            url = f"{parsed.scheme}://{parsed.netloc}{url}"
        absolute_urls.append(url)
    
    return list(set(absolute_urls))


if __name__ == "__main__":
    print("""
╔═══════════════════════════════════════════╗
║      网页图片批量下载工具                 ║
╠═══════════════════════════════════════════╣
║  方式1: 从文件读取                        ║
║    python download-images.py urls.txt     ║
║                                            ║
║  方式2: 直接传入 URL（用逗号分隔）         ║
║    python download-images.py "url1,url2"  ║
╚═══════════════════════════════════════════╝
    """)
    
    import sys
    
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if os.path.isfile(arg):
            download_from_file(arg, SAVE_DIR)
        else:
            urls = [u.strip() for u in arg.split(',') if u.strip()]
            download_from_urls(urls, SAVE_DIR)
    else:
        print("用法: python download-images.py <urls.txt 或 url1,url2>")
