# 快速开始：GitHub + Zeabur 部署

## 部署摘要（5分钟完成）

### 第1步：准备本地项目（1分钟）
```bash
git init
git add .
git commit -m "Initial commit"
```

### 第2步：创建 GitHub 仓库（1分钟）
1. 访问 https://github.com
2. 点击 "+" → "New repository"
3. 名称: `twitter-video-download`
4. 点击 "Create repository"

### 第3步：连接到 GitHub（1分钟）
```bash
git remote add origin https://github.com/YOUR_USERNAME/twitter-video-download.git
git branch -M main
git push -u origin main
```

### 第4步：Zeabur 部署（2分钟）
1. 访问 https://zeabur.com
2. 用 GitHub 登录
3. 点击 "New Project"
4. 连接 GitHub 仓库 `twitter-video-download`
5. 等待自动部署完成

### 第5步：访问应用（立即）
- 从 Zeabur 控制台获取域名
- 访问你的应用

## 一键部署命令

如果你熟悉命令行，可以按顺序运行以下命令：

```bash
# 步骤1: Git 初始化
git init
git add .
git commit -m "Initial commit: Twitter video downloader"

# 步骤2: 连接 GitHub（替换 YOUR_USERNAME）
git remote add origin https://github.com/YOUR_USERNAME/twitter-video-download.git
git branch -M main
git push -u origin main
```

然后去 Zeabur 网页界面完成剩下的步骤。

## 验证工具

在部署前，你可以使用以下工具验证项目：

### 1. 检查部署就绪
```bash
python check-deployment-ready.py
```

### 2. 测试本地构建（可选）
```bash
# Windows
test-local-build.bat

# Linux/Mac
chmod +x test-local-build.sh
./test-local-build.sh
```

### 3. 本地运行测试
```bash
python app.py
```
访问 http://localhost:5000 测试本地功能

## 常见快捷方式

### 已经创建了 GitHub 仓库？
```bash
# 只需要推送代码
git push origin main
```

### 已经连接了 Zeabur？
- Zeabur 会自动检测 GitHub 更新
- 推送代码后会自动重新部署

### 需要重新部署？
```bash
# 修改代码后
git add .
git commit -m "Update"
git push origin main
```

## 问题快速解决

### 部署失败？
1. 检查 `check-deployment-ready.py` 输出
2. 查看 Zeabur 构建日志
3. 运行本地测试：`test-local-build.bat`

### 应用不工作？
1. 检查 Zeabur 应用日志
2. 验证环境变量
3. 测试代理配置（如果需要）

### GitHub 推送失败？
```bash
# 强制推送（小心使用）
git push -f origin main

# 或者先同步
git pull origin main
git push origin main
```

## 技术支持

- 详细部署指南：查看 `DEPLOY-GITHUB-STEPS.md`
- Zeabur 配置：查看 `zeabur.json`
- 容器配置：查看 `Dockerfile`

## 下一步

成功部署后：
1. 测试视频下载功能
2. 配置自定义域名（可选）
3. 监控应用性能
4. 考虑备份策略