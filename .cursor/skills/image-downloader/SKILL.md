---
name: image-downloader
description: 从网页批量提取并下载图片。适用于复杂页面、人物照片、书籍封面等场景。自动生成 URL 列表并支持批量下载。
---

# 网页图片批量下载工具

从网页提取图片 URL 并批量下载到本地，支持复杂页面的图片抓取。

---

## 工作流程

```
1. 用户提供目标网页 URL
2. 分析页面结构，提取图片 URL
3. 展示可用图片列表
4. 用户选择要下载的图片
5. 批量下载到指定目录
```

---

## 图片来源识别

### 常见图片源

| 类型 | 来源 | URL 格式 |
|------|------|----------|
| 🖼️ Wikipedia | Wikimedia Commons | `upload.wikimedia.org/wikipedia/...` |
| 📚 豆瓣书籍 | 豆瓣 | `img1.doubanio.com/view/subject/...` |
| 👤 人物照片 | 百度百科/维基 | 词条配图 |
| 📰 新闻配图 | 新华社/Reuters | CDN 链接 |

### Wikimedia Commons 特点

- **免费商用**：采用 CC BY-SA 等开放协议
- **高质量**：多为原始尺寸或高清缩略图
- **稳定可靠**：CDN 加速，链接持久

---

## URL 提取方法

### 方法一：Playwright MCP（推荐）

在目标页面执行 JavaScript：

```javascript
// 获取页面所有图片 URL
const images = Array.from(document.querySelectorAll('img')).map(img => ({
  src: img.src,
  dataSrc: img.dataset.src || img.getAttribute('data-src'),
  alt: img.alt
})).filter(img => img.src || img.dataSrc);

// 去重并输出
const uniqueImages = [...new Set(images.map(i => i.src || i.dataSrc))];
console.log(JSON.stringify(uniqueImages, null, 2));
```

### 方法二：WebFetch 分析页面

对于静态页面，提取 `<img>` 标签的 `src` 属性：

```markdown
1. 使用 WebFetch 获取页面 HTML
2. 搜索 `src="https://..."` 模式
3. 过滤出图片 URL（.jpg, .png, .gif 等）
4. 转换为绝对 URL
```

### 方法三：搜索直接获取

```
搜索关键词：site:commons.wikimedia.org 人物名
搜索关键词：书名 豆瓣 封面图片 URL
```

---

## 下载工具使用

### 位置

```
ai/tools/download-images.py
```

### 基本用法

```bash
# 从 URL 文件下载
python3 ai/tools/download-images.py urls.txt

# 直接传入 URL（逗号分隔）
python3 ai/tools/download-images.py "url1,url2,url3"

# 下载到指定目录
SAVE_DIR="Biography/雷军/images"
python3 ai/tools/download-images.py urls.txt

### 下载到指定目录

```python
from ai.tools.download_images import download_from_urls

urls = ["图片链接1", "图片链接2"]
save_dir = "Biography/雷军/images"
download_from_urls(urls, save_dir)
```

---

## 输出格式

### URL 列表文件

```markdown
# [人物/书籍名] 图片 URL 列表

## 图片列表

| 序号 | 名称 | URL |
|------|------|-----|
| 1 | portrait.jpg | https://... |
| 2 | cover.jpg | https://... |

## 纯 URL 列表（用于脚本）

https://...
https://...
```

### 下载结果报告

```
📥 开始下载 7 张图片...

✅ [1/7] 雷军.jpg (156.2KB)
✅ [2/7] 雷军_2024.jpg (234.5KB)
❌ [3/7] 连接失败
✅ [4/7] 发布会.jpg (189.3KB)
...

📊 完成：成功 6/7
```

---

## 人物传记图片规范

### 照片要求

- **格式**：JPG 或 PNG
- **命名**：`portrait.jpg`（主照片）
- **位置**：`Biography/[人名]/images/`
- **尺寸**：建议 400px 以上宽度

### Wikimedia 雷军照片

| 文件名 | URL | 说明 |
|--------|-----|------|
| 雷军.jpg | `upload.wikimedia.org/.../5/53/雷军_Lei_Jun.jpg` | 标准照 |
| 雷军_2024.jpg | `upload.wikimedia.org/.../fc/雷军_2024-09-13.jpg` | 近照 |

### Wikimedia 图片 URL 格式

```
# 中文 Wikipedia
https://upload.wikimedia.org/wikipedia/zh/[hash1]/[hash2]/[文件名]

# 英文 Wikipedia  
https://upload.wikimedia.org/wikipedia/commons/[hash1]/[hash2]/[文件名]

# 缩略图（推荐）
https://upload.wikimedia.org/wikipedia/zh/thumb/[hash1]/[hash2]/[文件名]/400px-[文件名]
```

---

## 常见问题

### Q: 遇到网络超时怎么办？

A: Wikimedia 等国外站点可能超时，可尝试：
- 使用代理或 VPN
- 分批下载
- 换用国内镜像站

### Q: 如何获取书籍封面？

A: 豆瓣封面 URL 格式：
```
https://img1.doubanio.com/view/subject/l/public/s[编号].jpg
```

### Q: 图片链接失效怎么办？

A: 搜索同类资源替换：
- 百度图片
- Google 图片
- 其他百科站点

---

## 注意事项

- 优先选择 Wikimedia Commons（免费商用）
- 下载前验证 URL 可访问性
- 保存原始 URL 便于后续追溯
- 记录图片来源和授权信息
