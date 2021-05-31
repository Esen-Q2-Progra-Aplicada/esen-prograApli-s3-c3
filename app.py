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
        return f"posted rows: {rows}"


if __name__ == "__main__":
    app.run(debug=True)
