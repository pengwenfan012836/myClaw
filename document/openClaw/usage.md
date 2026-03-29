# openClaw 使用指南

## 简介

openClaw 是一款功能强大的命令行工具，旨在帮助用户更高效地完成日常开发和运维任务。

## 快速开始

### 基本用法

```bash
openclaw [command] [options]
```

### 查看帮助

```bash
# 查看全局帮助
openclaw --help

# 查看特定命令的帮助
openclaw [command] --help
```

## 命令参考

### 常用命令

| 命令 | 说明 | 示例 |
|------|------|------|
| `openclaw init` | 初始化新项目 | `openclaw init myproject` |
| `openclaw start` | 启动服务 | `openclaw start` |
| `openclaw stop` | 停止服务 | `openclaw stop` |
| `openclaw status` | 查看状态 | `openclaw status` |
| `openclaw config` | 配置管理 | `openclaw config set key value` |

### 初始化项目

```bash
# 创建新项目
openclaw init project-name

# 指定模板
openclaw init project-name --template basic

# 指定目录
openclaw init --path ./my-project
```

### 服务管理

```bash
# 启动服务
openclaw start

# 后台运行
openclaw start --daemon

# 停止服务
openclaw stop

# 重启服务
openclaw restart

# 查看服务状态
openclaw status
```

### 配置管理

```bash
# 查看所有配置
openclaw config list

# 设置配置项
openclaw config set api-key your-api-key

# 获取配置项
openclaw config get api-key

# 删除配置项
openclaw config delete api-key
```

## 配置文件

openClaw 使用 YAML 格式的配置文件，默认位置为：

- macOS: `~/.openclaw/config.yaml`
- Linux: `~/.openclaw/config.yaml`
- Windows: `%USERPROFILE%\.openclaw\config.yaml`

### 配置示例

```yaml
# 基本配置
app:
  name: my-app
  port: 8080
  host: localhost

# 高级配置
logging:
  level: info
  output: ./logs

# 自定义配置
custom:
  theme: dark
  language: zh-CN
```

## 环境变量

openClaw 支持通过环境变量进行配置：

| 环境变量 | 说明 | 默认值 |
|----------|------|--------|
| `OPENCLAW_HOME` | 配置目录 | `~/.openclaw` |
| `OPENCLAW_PORT` | 端口号 | `8080` |
| `OPENCLAW_LOG_LEVEL` | 日志级别 | `info` |

## 日志

openClaw 的日志文件位于：

- macOS/Linux: `~/.openclaw/logs/`
- Windows: `%USERPROFILE%\.openclaw\logs\`

日志文件按日期命名：`openclaw-YYYY-MM-DD.log`

### 日志级别

- `debug`: 调试信息（最详细）
- `info`: 一般信息
- `warn`: 警告信息
- `error`: 错误信息

## 插件系统

openClaw 支持插件扩展功能。

### 安装插件

```bash
openclaw plugin install plugin-name
```

### 常用插件

| 插件名称 | 功能描述 |
|----------|----------|
| `openclaw-plugin-git` | Git 集成 |
| `openclaw-plugin-docker` | Docker 支持 |
| `openclaw-plugin-db` | 数据库管理 |

### 管理插件

```bash
# 查看已安装插件
openclaw plugin list

# 更新插件
openclaw plugin update plugin-name

# 卸载插件
openclaw plugin uninstall plugin-name
```

## 高级用法

### 批量操作

```bash
# 批量执行命令
openclaw batch commands.txt

# 并行执行
openclaw batch commands.txt --parallel
```

### 脚本集成

openClaw 可以与其他脚本语言集成使用：

**Shell 脚本：**
```bash
#!/bin/bash
openclaw start
openclaw status
```

**Python 脚本：**
```python
import subprocess
result = subprocess.run(['openclaw', 'status'], capture_output=True)
print(result.stdout)
```

## 故障排除

### 常见问题

**1. 服务启动失败**
```bash
# 检查端口占用
lsof -i :8080

# 查看详细日志
openclaw start --debug
```

**2. 配置不生效**
```bash
# 检查配置文件路径
openclaw config --show-path

# 重置配置
openclaw config reset
```

**3. 权限问题**
```bash
# 检查权限
ls -la ~/.openclaw

# 修复权限
chmod -R 755 ~/.openclaw
```

### 调试模式

开启调试模式获取更多信息：

```bash
openclaw --debug [command]
```

## 最佳实践

1. **定期更新**: 保持 openClaw 为最新版本
   ```bash
   brew upgrade openclaw
   ```

2. **备份配置**: 定期备份配置文件

3. **查看日志**: 遇到问题时先查看日志文件

4. **使用 Tab 自动补全**: 启用 shell 自动补全提高效率
   ```bash
   openclaw completion --shell zsh
   ```

## 获取帮助

- 在线文档: [https://docs.openclaw.dev](https://docs.openclaw.dev)
- 问题反馈: [https://github.com/your-repo/openclaw/issues](https://github.com/your-repo/openclaw/issues)
- 社区讨论: [https://discord.gg/openclaw](https://discord.gg/openclaw)

## 版本信息

查看当前版本：

```bash
openclaw --version
```

更新到最新版本：

```bash
brew upgrade openclaw
```
