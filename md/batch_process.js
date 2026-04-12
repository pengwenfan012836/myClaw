#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

// 使用绝对路径
const baseDir = '/Users/pengwenfan/project/claw/myClaw/Biography';

// emoji 映射
const emojiMap = {
  '诞生': '👶', '出生': '👶', '降生': '👶', '仙桃诞生': '👶',
  '求学': '🎓', '上学': '🎓', '毕业': '🎓', '读书': '🎓', '学生': '🎓',
  '创业': '🚀', '辞职': '🚀', '加入': '🚀', '入职': '🚀',
  '上市': '💰', '融资': '💰', '收购': '💰', '投资': '💰',
  '获奖': '🏆', '荣誉': '🏆', '当选': '🏆',
  '演讲': '🎤', '访谈': '🎤', '对话': '🎤', '对话': '🎤',
  '回忆': '💭', '反思': '💭',
  '觉醒': '⚡', '转折': '⚡', '突破': '⚡',
  '首富': '👑', '巅峰': '👑', '辉煌': '👑',
  '危机': '🌊', '风波': '🌊', '争议': '🌊', '打架': '🌊',
  '和解': '🤝', '合作': '🤝', '握手': '🤝',
  '转型': '🔄', '改革': '🔄', '变革': '🔄',
  '学霸': '🧠', '天才': '🧠', '神童': '🧠',
  '朋友': '🌟', '导师': '🌟', '贵人': '🌟',
  '午餐': '🍽️', '巴菲特': '🍽️',
  '教育': '📝',
  '成长': '🌱', '童年': '🌱', '少年': '🌱',
  '老师': '👨‍🏫', '老师回忆': '👨‍🏫',
  '同学': '👥', '室友': '👥',
  '同事': '💼', '员工': '💼', '员工回忆': '💼',
  '家人': '❤️', '父母': '❤️', '妻子': '❤️', '配偶': '❤️', '太太': '❤️', '亲友': '❤️',
  '媒体': '📰', '记者': '📰', '评价': '📰',
  '传记': '📖',
  '出柜': '🏳️‍🌈', '隐私': '🏳️‍🌈',
  '乔布斯': '🍎', '后乔布斯': '🍎',
  '光磁': '💿', '中关村': '💿',
  '农村': '🏡', '宿迁': '🏡',
  '安全': '🛡️', '杀毒': '🛡️',
  '3Q': '⚔️', '大战': '⚔️',
  '分校': '📍',
};

function getEmoji(title) {
  for (const [key, emoji] of Object.entries(emojiMap)) {
    if (title.includes(key)) {
      return emoji;
    }
  }
  return '📌';
}

function processFile(filePath) {
  let content = fs.readFileSync(filePath, 'utf-8');
  let lines = content.split('\n');
  
  // 第一步：删除末尾的整理来源说明
  const skipPatterns = [
    /^整理日期/,
    /^以下内容整理自/,
    /^本页面整理自/,
  ];
  
  // 从后往前找到第一个需要保留的行
  let lastKeepLine = lines.length - 1;
  for (let i = lines.length - 1; i >= 0; i--) {
    const trimmed = lines[i].trim();
    const isSkipLine = skipPatterns.some(p => p.test(trimmed));
    if (!isSkipLine && trimmed !== '') {
      lastKeepLine = i;
      break;
    }
  }
  
  // 保留到 lastKeepLine
  lines = lines.slice(0, lastKeepLine + 1);
  
  // 第二步：将 ## 改成 #### 并添加 emoji
  const newLines = [];
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const trimmed = line.trim();
    
    // 跳过开头的空行和来源说明行
    if (trimmed === '' || trimmed.startsWith('*以下内容') || trimmed.startsWith('*本页面')) {
      newLines.push(line);
      continue;
    }
    
    // 处理 ## 标题
    if (trimmed.startsWith('## ')) {
      const title = trimmed.substring(3);
      const emoji = getEmoji(title);
      newLines.push(`#### ${emoji} ${title}`);
    } else {
      newLines.push(line);
    }
  }
  
  // 写回文件
  fs.writeFileSync(filePath, newLines.join('\n'), 'utf-8');
}

// 遍历所有演讲与访谈目录
function processAll() {
  const interviewDirs = [];

  // 获取所有人物目录
  const entries = fs.readdirSync(baseDir);
  for (const entry of entries) {
    // 跳过非目录
    const entryPath = path.join(baseDir, entry);
    if (!fs.statSync(entryPath).isDirectory()) continue;
    
    const interviewPath = path.join(entryPath, '演讲与访谈');
    if (fs.existsSync(interviewPath)) {
      interviewDirs.push(interviewPath);
    }
  }

  let count = 0;
  for (const dir of interviewDirs) {
    const files = fs.readdirSync(dir).filter(f => f.endsWith('.md'));
    for (const file of files) {
      const filePath = path.join(dir, file);
      processFile(filePath);
      count++;
    }
  }

  console.log(`处理完成！共处理 ${count} 个文件`);
}

processAll();
