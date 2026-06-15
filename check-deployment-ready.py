#!/usr/bin/env python3
"""
GitHub 部署检查脚本
检查项目是否已准备好部署到 Zeabur
"""

import os
import sys
from pathlib import Path

def check_file_exists(filepath, description):
    """检查文件是否存在"""
    exists = os.path.exists(filepath)
    status = "✅" if exists else "❌"
    print(f"{status} {description}: {filepath}")
    return exists

def check_file_content(filepath, required_keywords, description):
    """检查文件内容是否包含必要的关键词"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        missing_keywords = []
        for keyword in required_keywords:
            if keyword not in content:
                missing_keywords.append(keyword)
        
        if missing_keywords:
            print(f"⚠️  {description}: 缺少关键词 {missing_keywords}")
            return False
        else:
            print(f"✅ {description}: 内容检查通过")
            return True
    except Exception as e:
        print(f"❌ {description}: 无法读取文件 - {e}")
        return False

def check_directory_structure():
    """检查目录结构"""
    print("📁 检查目录结构...")
    
    required_files = [
        (".gitignore", "Git 忽略文件"),
        ("Dockerfile", "Docker 配置文件"),
        ("zeabur.json", "Zeabur 配置文件"),
        ("app.py", "主应用文件"),
        ("requirements.txt", "Python 依赖文件"),
        ("README.md", "项目说明文档"),
        ("DEPLOY-ZEABUR.md", "部署指南"),
        ("DEPLOY-GITHUB-STEPS.md", "GitHub 部署步骤"),
    ]
    
    checks_passed = 0
    for filename, description in required_files:
        if check_file_exists(filename, description):
            checks_passed += 1
    
    return checks_passed

def check_app_py():
    """检查 app.py 的云部署配置"""
    print("\n🔧 检查应用配置...")
    
    required_keywords = [
        "0.0.0.0",
        "os.environ.get('PORT'",
        "load_dotenv()",
        "Flask(__name__)"
    ]
    
    return check_file_content("app.py", required_keywords, "app.py 云部署配置")

def check_dockerfile():
    """检查 Dockerfile"""
    print("\n🐳 检查 Dockerfile...")
    
    required_keywords = [
        "FROM python",
        "WORKDIR /app",
        "COPY requirements.txt",
        "RUN pip install",
        "EXPOSE",
        "CMD [\"python\", \"app.py\"]"
    ]
    
    return check_file_content("Dockerfile", required_keywords, "Dockerfile 配置")

def check_requirements_txt():
    """检查 requirements.txt"""
    print("\n📦 检查依赖文件...")
    
    required_packages = ["Flask", "yt-dlp", "python-dotenv"]
    
    try:
        with open("requirements.txt", 'r') as f:
            content = f.read()
        
        missing_packages = []
        for package in required_packages:
            if package.lower() not in content.lower():
                missing_packages.append(package)
        
        if missing_packages:
            print(f"⚠️  requirements.txt: 缺少包 {missing_packages}")
            return False
        else:
            print(f"✅ requirements.txt: 依赖检查通过")
            return True
    except Exception as e:
        print(f"❌ requirements.txt: 无法读取文件 - {e}")
        return False

def check_zeabur_config():
    """检查 Zeabur 配置"""
    print("\n☁️ 检查 Zeabur 配置...")
    
    if not check_file_exists("zeabur.json", "zeabur.json 配置文件"):
        return False
    
    required_keywords = [
        "Dockerfile",
        "PORT",
        "healthCheck",
        "volumes"
    ]
    
    return check_file_content("zeabur.json", required_keywords, "zeabur.json 配置")

def main():
    """主函数"""
    print("=" * 60)
    print("GitHub + Zeabur 部署就绪检查")
    print("=" * 60)
    
    # 切换到项目目录
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    print(f"检查目录: {os.getcwd()}")
    
    print("\n" + "=" * 60)
    
    # 执行各项检查
    total_checks = 7
    passed_checks = 0
    
    # 1. 检查目录结构
    dir_checks = check_directory_structure()
    if dir_checks == 8:  # 所有8个文件都存在
        passed_checks += 1
    
    # 2. 检查应用配置
    if check_app_py():
        passed_checks += 1
    
    # 3. 检查 Dockerfile
    if check_dockerfile():
        passed_checks += 1
    
    # 4. 检查依赖
    if check_requirements_txt():
        passed_checks += 1
    
    # 5. 检查 Zeabur 配置
    if check_zeabur_config():
        passed_checks += 1
    
    # 6. 检查临时目录是否存在
    if check_file_exists("temp_downloads", "临时下载目录"):
        passed_checks += 1
    else:
        print("ℹ️  临时目录不存在，将在运行时自动创建")
    
    # 7. 检查模板目录
    if check_file_exists("templates/index.html", "前端模板文件"):
        passed_checks += 1
    
    print("\n" + "=" * 60)
    
    # 总结
    print(f"\n📊 检查总结:")
    print(f"   总检查项: {total_checks}")
    print(f"   通过项: {passed_checks}")
    
    if passed_checks >= total_checks - 1:  # 允许1项失败
        print(f"\n🎉 恭喜！项目已准备好部署到 Zeabur！")
        print(f"\n下一步:")
        print(f"1. 运行: git init")
        print(f"2. 运行: git add .")
        print(f"3. 运行: git commit -m \"Initial commit\"")
        print(f"4. 在 GitHub 创建新仓库")
        print(f"5. 运行: git remote add origin https://github.com/YOUR_USERNAME/twitter-video-download.git")
        print(f"6. 运行: git push -u origin main")
        print(f"7. 登录 Zeabur 并连接 GitHub 仓库")
    else:
        print(f"\n⚠️  需要修复一些问题才能部署")
        print(f"请查看上面的错误信息并进行修复")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()