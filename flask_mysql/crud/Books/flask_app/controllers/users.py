from flask_app import app
from flask import render_template,redirect,request
from flask_app.models import user, book

#CREATE
@app.route('/authors/create', methods=['POST'])
def create_author():
    user.User.save(request.form)
    return redirect('/')

#READ
@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def show_authors():
    return render_template('show_authors.html', users = user.User.get_all())

@app.route('/authors/<int:id>')
def show_author(id):
    data = {
        "id": id
    }
    return render_template('show_author.html', user = user.User.get_by_id(data), unfavorited = book.Book.unfavorited(data))

@app.route('/join/books',methods=['POST'])
def join_book():
    data = {
        'user_id': request.form['user_id'],
        'book_id': request.form['book_id']
    }
    book.Book.favorite(data)
    return redirect(f"/authors/{request.form['user_id']}")