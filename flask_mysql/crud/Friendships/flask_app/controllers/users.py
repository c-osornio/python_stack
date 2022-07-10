from flask_app import app
from flask import render_template,redirect,request 
from flask_app.models import user, friendship

@app.route('/')
def index():
    return redirect('/friendships')

@app.route('/friendships')
def homepage():
    return render_template('friendships.html', friendships = user.User.get_all_users_friendships(), users = user.User.get_all())

@app.route('/users/create', methods=['POST'])
def create_user():
    user.User.save(request.form)
    return redirect('/')

@app.route("/friendship/create",methods = ['POST'])
def create_friendship():
    data = {
        'user_id' : request.form['user_id'],
        'friend_id' : request.form['friend_id']
    }
    if data['friend_id'] == data['user_id']:
        return redirect('/friendships')
    elif friendship.Friendship.check_if_already_friends(data) == True:
        return redirect('/friendships')
    friendship.Friendship.save(data)
    return redirect('/')