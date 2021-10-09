from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db
from .models import User
# from flask_socketio import SocketIO

# socketio = SocketIO('main', cors_allowed_origins='*')
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/', methods=['POST'])
def my_form_post():
    user_id = request.form['search']
    print(user_id)
    user = User.query.filter_by(name=user_id).first()
    print(user)
    if user == None:
        return render_template('index.html', user_name = "Invalid username")
    else:
        return render_template('index.html', user_name = "User found: " + user.name)

@main.route('/profile')
def profile():
    
    return render_template('profile.html', name = current_user.name, email = current_user.email)

# @main.route('/chat')
# def sessions():
#     return render_template('chat.html')

# def messageReceived(methods=['GET', 'POST']):
#     print('message was received!!!')

# @socketio.on('my event')
# def handle_my_custom_event(json, methods=['GET', 'POST']):
#     print('received my event: ' + str(json))
#     socketio.emit('my response', json, callback=messageReceived)
