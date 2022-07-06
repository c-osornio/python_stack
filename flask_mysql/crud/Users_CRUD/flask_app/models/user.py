from flask_app.config.mysqlconnection import connectToMySQL
from datetime import datetime

class User:
    db = "users_schema"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#CREATE
    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO users(first_name, last_name, email)
        VALUES (%(first_name)s, %(last_name)s, %(email)s)
        ; """
        user_id = connectToMySQL(cls.db).query_db(query, data)
        return user_id


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
        for user in results:
            users.append(cls(user))
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

#UPDATE
    @classmethod
    def update(cls, data):
        query = """
        UPDATE users 
        SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.db).query_db( query, data )

#DELETE
    @classmethod
    def delete(cls, data):
        query = """
        DELETE FROM users
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.db).query_db(query, data)