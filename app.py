from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET"])
def register():
    if request.method == "GET":
        return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
