from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import user, recipe

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
    if 'user_id' not in session:
        return redirect('/')
    return render_template('profile.html', user = user.User.get_user_by_id(id), recipes = recipe.Recipe.get_all_recipes())

# Update
# Destroy

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