from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import user, message
import socket

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname) 

# Create
@app.route('/users/register', methods=['POST'])
def register_user():
    if user.User.save(request.form):
        return redirect(f'/users/profile/{session["user_id"]}')
    return render_template('index.html', info = request.form)

# Read
@app.route('/')
def index():
    return render_template('index.html', info = request.form)
    
@app.route('/users/profile/<int:id>')
def show_profile(id):
    if session['user_id'] != id:
        return redirect(f'/users/profile/{session["user_id"]}')
    this_user = user.User.get_user_by_id(id)
    other_users = user.User.get_all_other_users(id)
    received_count=len(message.Message.get_all_received_by_id(id))
    sent_count=len(message.Message.get_all_sent_by_id(id))
    received_messages = message.Message.get_all_messages_to_user_by_id(id)
    return render_template('profile.html', user = this_user, other_users = other_users, received_count=received_count, sent_count=sent_count, received_messages = received_messages)

@app.route('/danger/<int:id>')
def show_danger(id):
    return render_template('danger.html', message = message.Message.get_message_by_id(id), ip = IPAddr)

# Update

# Delete

# Login
@app.route('/users/login', methods=['POST'])
def login():
    if user.User.login(request.form):
        return redirect(f'/users/profile/{session["user_id"]}')
    return render_template('index.html',info = request.form)

# Logout
@app.route('/users/logout')
def logout():
    session.clear()
    return redirect('/')