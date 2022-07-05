from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import user

#CREATE
@app.route('/users/create', methods=['POST'])
def create_user():
    user.User.create_user(request.form)
    return redirect('/')
    
#READ
@app.route('/')
def root():
    all_users = user.User.get_all_users()
    return render_template('users.html', users=all_users)

@app.route('/add_user')
def add_user():
    return render_template('new_user.html')