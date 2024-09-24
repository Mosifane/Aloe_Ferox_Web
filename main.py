from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("Home.html")


@app.route('/main')
def main():
    return render_template("Main.html")


@app.route('/login')
def login():
    return render_template("Login.html")


@app.route('/settings')
def settings():
    return render_template('Settings.html')


@app.route('/sign_up')
def sign_up():
    return render_template('SignUp.html')


if __name__ == "__main__":
    app.run(debug=True)