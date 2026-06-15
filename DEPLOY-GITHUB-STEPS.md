# GitHub 部署到 Zeabur 详细步骤

## 第1步：准备 GitHub 仓库

### 1.1 初始化 Git 仓库（本地）
```bash
# 进入项目目录
cd twitter-video-download

# 初始化 Git
git init

# 查看当前状态
git status
```

### 1.2 创建 .gitignore（已存在，确认内容）
确保 `.gitignore` 包含：
- `temp_downloads/` - 临时文件
- `__pycache__/` - Python 缓存
- `.env` - 本地环境变量（不要提交）
- `*.pyc` - Python 编译文件
- `.DS_Store` - Mac 系统文件
- `*.mp4` - 下载的视频文件
- `*.gif` - GIF 文件

### 1.3 创建初始提交
```bash
# 添加所有文件（排除 .gitignore 中的文件）
git add .

# 查看要提交的文件
git status

# 创建初始提交
git commit -m "Initial commit: Twitter video downloader with Zeabur deployment support"
```

## 第2步：创建 GitHub 仓库

### 2.1 登录 GitHub
- 访问 https://github.com
- 登录你的账号（如果没有，请注册）

### 2.2 创建新仓库
1. 点击右上角的 "+" 图标 → "New repository"
2. 填写仓库信息：
   - **Repository name**: twitter-video-download
   - **Description**: Twitter/X video downloader web app with Zeabur deployment
   - **Public**（推荐，免费）
   - **Initialize this repository with:**
     - ✅ 不要勾选 "Add a README file"（我们已有）
     - ✅ 不要勾选 "Add .gitignore"（我们已有）
     - ✅ 不要勾选 "Choose a license"
3. 点击 "Create repository"

### 2.3 获取远程仓库地址
创建成功后，你会看到类似这样的命令提示：
```bash
git remote add origin https://github.com/你的用户名/twitter-video-download.git
git branch -M main
git push -u origin main
```

## 第3步：连接到 GitHub

### 3.1 设置远程仓库（回到本地终端）
```bash
# 添加远程仓库（替换 YOUR_USERNAME 为你的 GitHub 用户名）
git remote add origin https://github.com/YOUR_USERNAME/twitter-video-download.git

# 验证远程仓库
git remote -v
# 应该显示：
# origin  https://github.com/YOUR_USERNAME/twitter-video-download.git (fetch)
# origin  https://github.com/YOUR_USERNAME/twitter-video-download.git (push)
```

### 3.2 推送到 GitHub
```bash
# 设置主分支
git branch -M main

# 推送到 GitHub
git push -u origin main
```

**如果遇到认证问题**：
```bash
# 使用 GitHub CLI（如果已安装）
gh auth login

# 或者使用个人访问令牌
# 1. 在 GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
# 2. 生成新令牌，选择 repo 权限
# 3. 使用令牌替代密码：
git push https://YOUR_TOKEN@github.com/YOUR_USERNAME/twitter-video-download.git main
```

## 第4步：Zeabur 部署

### 4.1 登录 Zeabur
- 访问 https://zeabur.com
- 点击 "Sign in"，使用 GitHub 账号登录
- 授权 Zeabur 访问你的 GitHub 账号

### 4.2 创建新项目
1. 在 Zeabur 控制台，点击 "New Project"
2. 输入项目名称：twitter-video-download
3. 点击 "Create Project"

### 4.3 连接 GitHub 仓库
1. 在项目页面，点击 "Connect Repository"
2. 选择 GitHub 作为代码源
3. 会显示你的 GitHub 仓库列表
4. 选择 `twitter-video-download`
5. 点击 "Connect"

### 4.4 自动构建和部署
连接后，Zeabur 会自动：
1. 检测到 `Dockerfile` 和 `zeabur.json`
2. 开始构建 Docker 镜像
3. 部署应用到云服务器

**构建过程大约需要 3-5 分钟**

## 第5步：配置环境变量（可选）

### 5.1 如果需要代理访问 Twitter
在 Zeabur 项目页面：

1. 点击 "Environment Variables"
2. 添加新变量：
   - **Key**: `PROXY_URL`
   - **Value**: 你的代理地址，例如：
     - Clash: `http://127.0.0.1:7890`
     - V2Ray: `http://127.0.0.1:10809`
     - Shadowsocks: `socks5://127.0.0.1:1080`
     - 公司代理: `http://proxy.company.com:8080`
3. 点击 "Save"

### 5.2 代理配置说明
- **中国大陆用户**：可能需要配置代理才能访问 Twitter
- **海外用户**：通常不需要代理
- **测试**：如果不确定，可以先不配置，测试是否需要

## 第6步：访问应用

### 6.1 获取应用 URL
部署成功后，在 Zeabur 项目页面：

1. 点击 "Domains"
2. 你会看到一个自动生成的域名，例如：
   - `twitter-video-download-123456.zeabur.app`

### 6.2 访问应用
- 打开浏览器，访问你的 Zeabur 域名
- 应用应该正常显示界面
- 测试视频下载功能

## 第7步：更新应用

### 7.1 本地修改后推送到 GitHub
```bash
# 修改代码后
git add .
git commit -m "Update: 描述修改内容"
git push origin main
```

### 7.2 Zeabur 自动更新
- Zeabur 会自动检测 GitHub 仓库的更新
- 自动重新构建和部署
- 更新过程大约 2-3 分钟

## 常见问题解决

### 问题1：构建失败
**检查：**
1. Dockerfile 语法是否正确
2. requirements.txt 格式是否正确
3. 查看 Zeabur 的构建日志

**重新构建：**
1. 在 Zeabur 项目页面，点击 "Redeploy"
2. 或者等待 GitHub push 触发重新构建

### 问题2：应用启动失败
**检查：**
1. 应用日志：Zeabur → Logs
2. 确认端口设置正确（app.py 监听 0.0.0.0:8080）
3. 环境变量格式是否正确

### 问题3：视频下载失败
**可能原因：**
1. Twitter API 限制（需要等待重试）
2. 网络连接问题（检查代理配置）
3. 视频链接无效

### 问题4：GitHub 推送失败
**解决方法：**
```bash
# 强制推送（小心使用）
git push -f origin main

# 或者先拉取更新
git pull origin main --rebase
git push origin main
```

## 最佳实践

### 1. 版本控制
- 每次修改前创建新分支
- 使用有意义的提交信息
- 定期推送更新

### 2. 环境管理
- 使用 `.env.example` 作为配置模板
- 不要在代码中硬编码敏感信息
- Zeabur 的环境变量会自动加密

### 3. 监控和日志
- 定期查看 Zeabur 的应用日志
- 监控应用性能和错误
- 设置错误告警（Zeabur 专业版功能）

### 4. 备份
- GitHub 会自动备份代码
- 定期导出环境变量配置
- 备份重要的 Dockerfile 和配置文件

## 技术支持

### 官方文档
- Zeabur 文档：https://docs.zeabur.com
- GitHub Actions：https://docs.github.com/en/actions
- Flask 文档：https://flask.palletsprojects.com/

### 社区支持
- Zeabur Discord：https://zeabur.com/discord
- GitHub Issues：项目页面 Issues 标签
- Stack Overflow：相关技术标签

### 联系我们
- 项目问题：GitHub Issues
- 部署问题：Zeabur 支持
- 功能建议：GitHub Discussions（如开启）