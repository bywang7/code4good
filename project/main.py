from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
# from flask_socketio import SocketIO

# socketio = SocketIO('main', cors_allowed_origins='*')
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

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
