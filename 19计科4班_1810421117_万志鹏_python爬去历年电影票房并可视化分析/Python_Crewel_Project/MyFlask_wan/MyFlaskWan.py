from flask import Flask, render_template,request
app = Flask(__name__)

@app.route("/")
def index():
    #发送字符串
    # s = "wanzhipeng"
    # lst = ['a', 'b', 'c']
    # return render_template("index.html", jay = s, lst = lst)
    return  render_template("Login.html")
@app.route("/login", methods = ['POST'])
def login():
    username = request.form.get("username")
    pwd = request.form.get("pwd")
    if username == "wan" and pwd == "123456":
        return "登陆成功"
    else:
        MSG = "登陆失败"
        return render_template("Login.html", msg = MSG)

if (__name__) == "__main__":
    app.run()