# 写入人物传记到 FlowUs

## 说明
将 myClaw/Biography 目录下的人物传记写入 FlowUs 多维表格，与黄铮、马云同一个父页面。遵循现有的代码结构，按人物分目录存放脚本，使用正确的 Markdown 解析避免文字重复。

## 工作流程
1. 获取人物信息：
   - 中文名（如：马云）
   - 英文 ID（如：jackma）

2. 确认源文件结构：
   - `/Users/pengwenfan/project/claw/myClaw/Biography/{中文名}/{中文名}传记.md`
   - `/Users/pengwenfan/project/claw/myClaw/Biography/{中文名}/演讲与访谈/*.md`

3. 创建目录：
   - `/Users/pengwenfan/project/ai/biography/FlowUs/scripts/{英文ID}/`

4. 从模板复制四个脚本到目录：
   - 模板位置：`/Users/pengwenfan/project/ai/biography/FlowUs/scripts/templates/`
   - `write-person-template.js` → `write-{英文ID}.js`
   - `add-person-to-database-template.js` → `add-{英文ID}-to-database.js`
   - `recreate-person-database-template.js` → `recreate-{英文ID}-database.js`
   - `update-person-database-template.js` → `update-{英文ID}-database.js`

5. 替换模板中的占位符：
   - `PERSON_NAME` → 中文名
   - `PERSON_ID` → 英文ID
   - `INTERVIEW_FILES_LIST` → 列出演讲与访谈目录下所有 .md 文件

6. 在 `generateTitle` 函数中添加特殊标题规则，为文章生成带 emoji 的美观标题（参考马云/黄铮的方式）

7. 运行写入脚本：
   ```bash
   cd /Users/pengwenfan/project/ai/biography/FlowUs
   node scripts/{英文ID}/write-{英文ID}.js
   ```

8. 获取输出的主页 ID 后，更新另外三个脚本中的占位符

9. 运行添加到数据库：
   ```bash
   node scripts/{英文ID}/add-{英文ID}-to-database.js
   ```

## 已有的配置
- 根数据库页面 ID：`91748b10-c47f-4a6d-bd6b-31e4832e2fdd`（固定不变）
- FlowUs Token 在 `/Users/pengwenfan/project/ai/biography/FlowUs/.env` 已配置
- 使用 `/Users/pengwenfan/project/ai/biography/FlowUs/src/markdown-to-blocks.js` 解析 Markdown（避免文字重复）

## 要求
- 严格按人物分目录存放脚本，不允许平铺
- 所有路径要绝对路径，确保能正确找到文件
- 检查所有演讲访谈文件都已列入列表
- 使用正确的 Markdown 解析模块，避免文字重复问题
