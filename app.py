from flask import Flask, request, jsonify, send_file, render_template
import yt_dlp
import subprocess
import os
import uuid
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# 获取环境变量端口，默认 5000
port = int(os.environ.get('PORT', 5000))

TEMP_DIR = Path("temp_downloads")
TEMP_DIR.mkdir(exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_video():
    data = request.json
    url = data.get('url', '').strip()
    
    if not url:
        return jsonify({'error': 'Please provide a valid URL | 请提供有效的 URL'}), 400
    
    session_id = str(uuid.uuid4())
    video_path = TEMP_DIR / f"{session_id}.mp4"
    
    try:
        # 使用 yt-dlp 下载视频
        ydl_opts = {
            'format': 'best[ext=mp4]/best',
            'outtmpl': str(video_path),
            'quiet': False,
            'no_warnings': False,
            'socket_timeout': 30,
            'retries': 10,
            'fragment_retries': 10,
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            },
            'proxy': os.getenv('PROXY_URL', ''),
        }
        
        print(f"正在处理 URL: {url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            if not info:
                return jsonify({'error': 'Unable to parse the link | 无法解析该链接'}), 400
        
        if not video_path.exists():
            return jsonify({'error': 'Video download failed | 视频下载失败'}), 500
        
        print(f"视频下载成功: {video_path}")
        
        return jsonify({
            'success': True,
            'download_url': f'/download/{session_id}'
        })
    
    except yt_dlp.utils.DownloadError as e:
        error_msg = str(e)
        print(f"yt-dlp 错误: {error_msg}")
        if 'Connection' in error_msg or '10054' in error_msg:
            return jsonify({'error': 'Network connection failed, please check proxy settings | 网络连接失败,请检查代理设置'}), 400
        return jsonify({'error': f'Download error | 下载错误: {error_msg}'}), 400
    except Exception as e:
        print(f"未知错误: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': f'Processing failed | 处理失败: {str(e)}'}), 500

@app.route('/download/<session_id>')
def download_video(session_id):
    video_path = TEMP_DIR / f"{session_id}.mp4"
    
    if not video_path.exists():
        return "File not found or expired | 文件不存在或已过期", 404
    
    return send_file(
        video_path,
        mimetype='video/mp4',
        as_attachment=True,
        download_name='twitter_video.mp4'
    )

@app.route('/cleanup', methods=['POST'])
def cleanup():
    """清理超过1小时的临时文件"""
    import time
    current_time = time.time()
    for file in TEMP_DIR.glob('*'):
        if current_time - file.stat().st_mtime > 3600:
            file.unlink()
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
