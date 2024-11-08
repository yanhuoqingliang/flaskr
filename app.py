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


#登录页面
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            return redirect(url_for("welcome", username=username))
        else:
            return "登录失败，用户名或密码错误"
    return render_template("login.html")


# 欢迎页面
@app.route("/welcome/<username>")
def welcome(username):
    return render_template("menu.html", username=username)


if __name__ == '__main__':
    app.run(debug=True)