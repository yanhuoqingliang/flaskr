from flask import Flask, render_template, request, redirect, url_for, Response
from flask_sockets import Sockets
import subprocess

app = Flask(__name__)
sockets = Sockets(app)

# 模拟用户数据
users = {
    "user1": "password1",
    "user2": "password2"
}


# 登录页面
# @app.route("/", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]
#         if username in users and users[username] == password:
#             return redirect(url_for("welcome", username=username))
#         else:
#             return "登录失败，用户名或密码错误"
#     return render_template("login.html")
#
#
# # 欢迎页面
# @app.route("/welcome/<username>")
# def welcome(username):
#     return render_template("menu.html", username=username)


# @sockets.route('/screen')
# def screen_socket(ws):
#     print('Started scrcpy')
#     cmd = ['D:\\scrcpy-win64-v1.24\\scrcpy']
#     process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
#     while True:
#         output = process.stdout.read(1024)
#         ws.send(output)
#
#
# @app.route('/')
# def index():
#     print('haha+++')
#     return render_template('index.html')


# 定义 WebSocket 路由
@sockets.route('/echo')
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        if message:
            ws.send("Echo: " + message)


# 定义普通 HTTP 路由
@app.route('/')
def index():
    return render_template('index2.html')


if __name__ == '__main__':
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler

    server = pywsgi.WSGIServer(('127.0.0.1', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()