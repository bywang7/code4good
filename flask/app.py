from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! test"

@app.route("/route/")
def route():
    return "This worked"


if __name__ == "__main__":
    app.run()