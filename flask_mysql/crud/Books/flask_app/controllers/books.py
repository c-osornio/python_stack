from flask_app import app
from flask import render_template,redirect, request
from flask_app.models import user, book

#CREATE
@app.route('/books/create', methods=['POST'])
def create_book():
    book.Book.save(request.form)
    return redirect('/books')

#READ
@app.route('/books')
def show_books():
    return render_template('show_books.html', books = book.Book.get_all())

@app.route('/books/<int:id>')
def show_book(id):
    data = {
        "id": id
    }
    return render_template('show_book.html', book = book.Book.get_by_id(data), unfavorited = user.User.unfavorited(data))

@app.route('/join/user',methods=['POST'])
def join_user():
    data = {
        'user_id': request.form['user_id'],
        'book_id': request.form['book_id']
    }
    user.User.favorite(data)
    return redirect(f"/books/{request.form['book_id']}")