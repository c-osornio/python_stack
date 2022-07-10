from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Book:
    db = "books_schema"
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_favorited = []

#CREATE
    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO books(title, num_of_pages)
        VALUES (%(title)s, %(num_of_pages)s)
        ; """
        book_id = connectToMySQL(cls.db).query_db(query, data)
        return book_id

    @classmethod
    def favorite(cls,data):
        query = """
        INSERT INTO favorites (user_id,book_id) 
        VALUES (%(user_id)s, %(book_id)s)
        ;"""
        return connectToMySQL(cls.db).query_db(query,data)

#READ
    @classmethod 
    def get_all(cls):
        query = """
        SELECT *
        FROM books
        ;"""
        results = connectToMySQL(cls.db).query_db(query)
        books = []
        print('++++++++++', results)
        for row in results:
            books.append(cls(row))
        return books

    @classmethod
    def get_by_id( cls , data ):
        query = """
        SELECT * 
        FROM books
        LEFT JOIN favorites
        ON favorites.book_id = books.id 
        LEFT JOIN users
        ON favorites.user_id = users.id 
        WHERE books.id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db( query , data )
        book = cls(results[0])
        for row_from_db in results:
            if row_from_db['users.id'] == None:
                break
            user_data = {
                "id" : row_from_db["users.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "created_at" : row_from_db["users.created_at"],
                "updated_at" : row_from_db["users.updated_at"]
            }
            book.users_favorited.append( user.User( user_data ) )
        print('********', book)
        return book

    @classmethod
    def unfavorited(cls,data):
        query = """
        SELECT * 
        FROM books
        WHERE books.id 
        NOT IN (SELECT book_id FROM favorites WHERE user_id = %(id)s)
        ;"""
        books = []
        results = connectToMySQL(cls.db).query_db(query, data)
        for row in results:
            books.append(cls(row))
        return books