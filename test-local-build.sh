#!/bin/bash
# 本地 Docker 构建测试脚本

echo "🔨 测试本地 Docker 构建..."
echo "=========================="

# 1. 检查 Docker 是否安装
echo "1. 检查 Docker 是否安装..."
if ! command -v docker &> /dev/null; then
    echo "❌ Docker 未安装，请先安装 Docker"
    echo "   下载地址: https://www.docker.com/products/docker-desktop/"
    exit 1
else
    echo "✅ Docker 已安装"
    docker --version
fi

echo ""

# 2. 检查 Docker 是否运行
echo "2. 检查 Docker 是否运行..."
if ! docker info &> /dev/null; then
    echo "❌ Docker 守护进程未运行"
    echo "   请启动 Docker Desktop"
    exit 1
else
    echo "✅ Docker 正在运行"
fi

echo ""

# 3. 构建 Docker 镜像
echo "3. 构建 Docker 镜像..."
docker build -t twitter-video-download-test .

if [ $? -eq 0 ]; then
    echo "✅ Docker 镜像构建成功"
else
    echo "❌ Docker 镜像构建失败"
    echo "   请检查 Dockerfile 语法错误"
    exit 1
fi

echo ""

# 4. 列出镜像
echo "4. 检查构建的镜像..."
docker images | grep twitter-video-download-test

echo ""

# 5. 运行测试容器
echo "5. 运行测试容器..."
echo "   运行: docker run -d -p 8080:8080 --name twitter-test twitter-video-download-test"
echo "   然后访问: http://localhost:8080"

read -p "是否要运行测试容器？(y/n): " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "正在启动测试容器..."
    
    # 停止并删除可能存在的旧容器
    docker stop twitter-test 2>/dev/null
    docker rm twitter-test 2>/dev/null
    
    # 运行新容器
    docker run -d -p 8080:8080 --name twitter-test twitter-video-download-test
    
    if [ $? -eq 0 ]; then
        echo "✅ 测试容器启动成功"
        echo ""
        echo "📋 容器信息:"
        echo "   名称: twitter-test"
        echo "   端口: 8080"
        echo "   访问: http://localhost:8080"
        echo ""
        echo "🔍 查看日志: docker logs twitter-test"
        echo "⏹️  停止容器: docker stop twitter-test"
        echo "🗑️  删除容器: docker rm twitter-test"
        echo "📁 进入容器: docker exec -it twitter-test bash"
        echo ""
        echo "🧪 测试完成后，运行:"
        echo "   docker stop twitter-test"
        echo "   docker rm twitter-test"
    else
        echo "❌ 测试容器启动失败"
        echo "   查看错误: docker logs twitter-test"
    fi
fi

echo ""
echo "✅ 本地构建测试完成"
echo "=========================="
echo ""
echo "下一步："
echo "1. 推送代码到 GitHub"
echo "2. 在 Zeabur 连接 GitHub 仓库"
echo "3. 自动部署到云端"