from flask import Flask
from flask import render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')


@app.route("/")
def index():
    return render_template('login.html')

@app.route("/signup/")
def signup():
    return render_template('signup.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/chat")
def chat():
    return render_template('chat.html')

@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg)
	send(msg, broadcast=True)


if __name__ == "__main__":
    app.run()
    #socketio.run(app)