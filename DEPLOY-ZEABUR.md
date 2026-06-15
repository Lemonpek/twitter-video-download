# Zeabur 部署指南

## 准备工作

### 1. Zeabur 账号
- 访问 [Zeabur](https://zeabur.com) 并注册账号
- 完成邮箱验证

### 2. 项目准备
确保以下文件已创建：
1. `Dockerfile` - ✅ 已创建
2. `zeabur.json` - ✅ 已创建
3. `.dockerignore` - ✅ 已创建
4. `app.py` - ✅ 已修改为云部署版本

## 部署步骤

### 方法一：通过 GitHub 部署（推荐）

1. **将项目推送到 GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit for Zeabur deployment"
   git branch -M main
   git remote add origin https://github.com/你的用户名/twitter-video-download.git
   git push -u origin main
   ```

2. **Zeabur 控制台操作**
   - 登录 Zeabur 控制台
   - 点击 "New Project"
   - 选择 "GitHub" 作为代码源
   - 授权访问你的 GitHub 账号
   - 选择 `twitter-video-download` 仓库
   - Zeabur 会自动检测 Dockerfile 并开始构建

3. **配置环境变量**
   - 在项目设置中找到 "Environment Variables"
   - 添加代理配置（如需要）：
     - `PROXY_URL`: `http://your-proxy-server:port`
   - 可选环境变量：
     - `PORT`: 8080（默认已配置）

### 方法二：通过 Docker 镜像部署

1. **本地构建 Docker 镜像**
   ```bash
   docker build -t twitter-video-download .
   ```

2. **推送到 Docker Hub**
   ```bash
   docker tag twitter-video-download 你的用户名/twitter-video-download
   docker push 你的用户名/twitter-video-download
   ```

3. **Zeabur 控制台操作**
   - 登录 Zeabur 控制台
   - 点击 "New Project"
   - 选择 "Docker" 作为部署方式
   - 输入镜像名称：`你的用户名/twitter-video-download`
   - 配置环境变量（同上）

## 环境变量配置

### 必需的环境变量
- 无（应用可以无代理运行）

### 可选的环境变量
1. **PROXY_URL** - 代理服务器地址
   - 示例：`http://127.0.0.1:7890`（Clash）
   - 示例：`socks5://127.0.0.1:1080`（Shadowsocks）

2. **PORT** - 应用端口（默认：8080）
   - Zeabur 会自动设置此变量，无需手动配置

## 注意事项

### 存储限制
- Zeabur 使用临时文件存储
- `temp_downloads/` 目录会自动清理
- 确保视频处理完成后及时下载

### 网络限制
- 中国大陆用户可能需要配置代理
- 代理配置在 `.env` 文件或环境变量中设置
- Zeabur 服务器位于海外，访问 Twitter 可能无需代理

### 性能限制
- Zeabur 免费版有资源限制
- 长时间的视频处理可能需要更多时间
- 建议下载的视频不超过 5 分钟

## 故障排除

### 部署失败
1. **检查 Dockerfile 语法**
   ```bash
   docker build --no-cache -t test .
   ```

2. **检查环境变量**
   - 确保没有空格和特殊字符
   - 使用正确的 URL 格式

3. **查看日志**
   - Zeabur 控制台 → 项目 → Logs
   - 查看详细的错误信息

### 应用无法运行
1. **检查端口配置**
   - 确保应用监听 `0.0.0.0:8080`
   - 检查 Zeabur 的网络配置

2. **检查依赖**
   - `requirements.txt` 中的包版本兼容性
   - Python 版本兼容性（已配置为 3.11）

## 域名配置（可选）

1. **自定义域名**
   - Zeabur 控制台 → 项目 → Domains
   - 添加你的自定义域名
   - 按照指示配置 DNS

2. **SSL 证书**
   - Zeabur 自动提供免费的 SSL 证书
   - 无需额外配置

## 监控和维护

1. **访问日志**
   - Zeabur 控制台提供访问日志
   - 可以查看请求和错误信息

2. **资源监控**
   - 监控 CPU、内存使用情况
   - 免费版有使用限制，注意不要超限

3. **自动重启**
   - Zeabur 会自动重启异常的应用
   - 提供健康检查配置（已在 zeabur.json 中配置）

## 技术支持
- Zeabur 官方文档：https://docs.zeabur.com
- GitHub Issues：项目问题报告
- 社区支持：Zeabur Discord 社区