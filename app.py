from flask import Flask, render_template, request
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
        # logic.insertUser()
        return "posted"


if __name__ == "__main__":
    app.run(debug=True)
