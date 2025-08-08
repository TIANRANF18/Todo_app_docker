from flask import Flask, render_template, request, redirect, url_for
import requests
import os
import time
import threading
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# 后端API地址
backend_url = os.getenv('BACKEND_URL', 'http://backend:5000')

def get_todos():
    """安全获取待办事项"""
    try:
        response = requests.get(f"{backend_url}/todos", timeout=3)
        return response.json() if response.status_code == 200 else []
    except:
        return []

@app.route('/')
def index():
    return render_template('index.html', todos=get_todos())

@app.route('/add', methods=['POST'])
def add_todo():
    """添加新待办项 (PRG模式)"""
    title = request.form.get('title', '').strip()
    if not title:
        return redirect(url_for('index'))
    
    try:
        requests.post(
            f"{backend_url}/todos",
            json={'title': title, 'completed': False},
            timeout=3
        )
    except:
        pass  # 简单忽略错误
    
    return redirect(url_for('index'))  # 关键修改：使用重定向

@app.route('/update/<int:todo_id>', methods=['POST'])
def update_todo(todo_id):
    """更新待办项"""
    action = request.form.get('action')
    
    try:
        if action == 'toggle':
            # 获取当前状态
            todo = requests.get(f"{backend_url}/todos/{todo_id}").json()
            requests.put(
                f"{backend_url}/todos/{todo_id}",
                json={'completed': not todo['completed']}
            )
        elif action == 'edit':
            new_title = request.form.get('title', '').strip()
            if new_title:
                requests.put(
                    f"{backend_url}/todos/{todo_id}",
                    json={'title': new_title}
                )
        elif action == 'delete':
            requests.delete(f"{backend_url}/todos/{todo_id}")
    except:
        pass
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    # 保活线程
    t = threading.Thread(
        target=lambda: app.run(host='0.0.0.0', port=8000, threaded=True),
        daemon=True
    )
    t.start()
    while True: time.sleep(3600)
