from flask import Flask, render_template



app = Flask (__name__)


@app.route('/')
def index():
    return render_template("main.html")

@app.route('/admin')
def admin():
    return render_template("adminaccount.html")

@app.route('/signin')
def signing():
    return render_template("signin.html")


@app.route('/singup')
def signup():
    return render_template("signup.html")



if __name__ == '__main__':
    app.run("0.0.0.0", port=5500, debug=False)