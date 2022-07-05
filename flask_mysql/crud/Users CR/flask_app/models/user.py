from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app import app

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
    def create_user(cls, data):
        query = """
        INSERT INTO users(first_name, last_name, email)
        VALUES (%(first_name)s, %(last_name)s, %(email)s)
        ; """
        return connectToMySQL(cls.db).query_db(query,data)

#READ
    @classmethod 
    def get_all_users(cls):
        query = """
        SELECT *
        FROM users
        ;"""
        result = connectToMySQL(cls.db).query_db(query)
        users = []
        print('++++++++++', result)
        for person in result:
            users.append(cls(person))
        return users