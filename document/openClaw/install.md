# openClaw 安装指南

## 系统要求

- **操作系统**: macOS (Darwin)
- **包管理器**: Homebrew
- **其他**: 建议已安装 Homebrew（未安装请参考下方安装步骤）

## 安装 Homebrew（如已安装可跳过）

如果你还没有安装 Homebrew，请在终端中执行以下命令：

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

安装完成后，将 Homebrew 路径添加到你的 shell 配置文件中：

**对于 zsh（macOS 默认）：**
```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
source ~/.zshrc
```

**对于 bash：**
```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.bash_profile
source ~/.bash_profile
```

## 安装 openClaw

### 方法一：通过 Homebrew 安装（推荐）

```bash
brew install openclaw
```

### 方法二：通过 GitHub 安装

如果你有 Homebrew 的 GitHub API Token，可以选择手动安装：

```bash
# 克隆仓库
git clone https://github.com/your-repo/openclaw.git

# 进入目录
cd openclaw

# 安装依赖
brew install ./Formula/openclaw.rb
```

## 验证安装

安装完成后，验证 openClaw 是否安装成功：

```bash
openclaw --version
```

如果显示版本号，说明安装成功。

## 卸载 openClaw

如需卸载 openClaw，执行：

```bash
brew uninstall openclaw
```

## 常见问题

### Q: 提示 "Command not found"

请确保 Homebrew 的 bin 目录在你的 PATH 中：

```bash
echo $PATH
```

如果没有包含 `/opt/homebrew/bin` 或 `/usr/local/bin`，请重新执行 Homebrew 初始化命令。

### Q: 安装失败，提示权限错误

尝试使用 sudo 权限安装：

```bash
sudo brew install openclaw
```

### Q: 需要更新 openClaw

```bash
brew upgrade openclaw
```

## 联系方式

如有问题或建议，请提交 Issue 或联系维护者。
