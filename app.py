from flask import Flask, render_template, request, redirect
from logic.user_logic import UserLogic
import bcrypt

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        logic = UserLogic()
        userName = request.form["username"]
        userEmail = request.form["useremail"]
        passwd = request.form["passwd"]
        confpasswd = request.form["confpasswd"]
        if passwd == confpasswd:
            salt = bcrypt.gensalt(rounds=14)
            strSalt = salt.decode("utf-8")
            encPasswd = passwd.encode("utf-8")
            hashPasswd = bcrypt.hashpw(encPasswd, salt)
            strPasswd = hashPasswd.decode("utf-8")
            rows = logic.insertUser(userName, userEmail, strPasswd, strSalt)
            return redirect("login")
        else:
            return redirect("register")
        return f"posted register rows: {rows}"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        logic = UserLogic()
        userEmail = request.form["useremail"]
        passwd = request.form["passwd"]
        userDict = logic.getUserByEmail(userEmail)
        salt = userDict["salt"].encode("utf-8")
        hashPasswd = bcrypt.hashpw(passwd.encode("utf-8"), salt)
        dbPasswd = userDict["password"].encode("utf-8")
        if hashPasswd == dbPasswd:
            print("they are a match!")
        else:
            print("they are not matched")
        return "posted login"


if __name__ == "__main__":
    app.run(debug=True)
