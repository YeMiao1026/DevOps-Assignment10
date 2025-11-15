from flask import Flask, request
import os # 一個未被使用的 import (用於 Linter 演示)

app = Flask(__name__)

# 一個潛在的安全漏洞 (用於 SAST 演示)
@app.route('/user_page')
def user_page():
    username = request.args.get('username')
    # 不安全：直接在頁面上顯示用戶輸入
    return f"<h1>歡迎, {username}!</h1>"

if __name__ == '__main__':
    # 嚴重安全問題：在生產中啟用 Debug 模式 (用於 SAST 演示)
    app.run(debug=True, host='0.0.0.0')