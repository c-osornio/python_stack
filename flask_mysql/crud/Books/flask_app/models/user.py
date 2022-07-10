from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class User:
    db = "books_schema"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []

#CREATE
    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO users(first_name, last_name)
        VALUES (%(first_name)s, %(last_name)s)
        ; """
        user_id = connectToMySQL(cls.db).query_db(query, data)
        return user_id

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
        FROM users
        ;"""
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        print('++++++++++', results)
        for author in results:
            users.append(cls(author))
        return users

    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * 
        FROM users
        WHERE id = %(id)s 
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        user = cls(row)
        return user

    @classmethod
    def get_by_id( cls , data ):
        query = """
        SELECT * 
        FROM users
        LEFT JOIN favorites
        ON favorites.user_id = users.id 
        LEFT JOIN books
        ON favorites.book_id = books.id 
        WHERE users.id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db( query , data )
        user = cls(results[0])
        for row_from_db in results:
            if row_from_db['books.id'] == None:
                break
            book_data = {
                "id" : row_from_db["books.id"],
                "title" : row_from_db["title"],
                "num_of_pages" : row_from_db["num_of_pages"],
                "created_at" : row_from_db["books.created_at"],
                "updated_at" : row_from_db["books.updated_at"]
            }
            user.books.append( book.Book( book_data ) )
        return user

    @classmethod
    def unfavorited(cls,data):
        query = """
        SELECT * 
        FROM users
        WHERE users.id 
        NOT IN (SELECT user_id FROM favorites WHERE book_id = %(id)s)
        ;"""
        users = []
        results = connectToMySQL(cls.db).query_db(query, data)
        for row in results:
            users.append(cls(row))
        return users