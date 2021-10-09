from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('login.html')

@app.route("/signup/")
def signup():
    return render_template('signup.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')

if __name__ == "__main__":
    app.run()