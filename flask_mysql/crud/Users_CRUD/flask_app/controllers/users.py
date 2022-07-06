from flask_app import app
from flask import render_template,redirect,request
from flask_app.models import user

#CREATE
@app.route('/users/create', methods=['POST'])
def create_user():
    user.User.save(request.form)
    return redirect('/')
    
#READ
@app.route('/')
def dashboard():
    return render_template('users.html', users= user.User.get_all())

@app.route('/add_user')
def add_user():
    return render_template('new_user.html')

@app.route('/users/<int:id>')
def show_user(id):
    data = {
        "id": id
    }
    return render_template('show_user.html', user = user.User.get_one(data))

@app.route('/users/<int:id>/edit')
def show_edit_form(id):
    data = {
        "id": id
    }
    return render_template('edit_user.html', user = user.User.get_one(data))

@app.route('/users/<int:id>/delete')
def show_delete_form(id):
    data = {
        "id": id
    }
    return render_template('delete_user.html', user = user.User.get_one(data))

#UPDATE
@app.route('/users/<int:id>/update', methods=['POST'])
def update_user(id):
    user.User.update(request.form)
    return redirect('/')

#DELETE
@app.route('/users/<int:id>/destroy', methods=['POST'])
def delete_user(id):
    user.User.delete(request.form)
    return redirect('/')