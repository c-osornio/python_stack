from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = "friendships_schema"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_users_friendships(cls):
        query = """
        SELECT users.first_name, users.last_name, users2.first_name as friend_first_name, users2.last_name as friend_last_name
        FROM users
        LEFT JOIN friendships
        ON friendships.user_id = users.id
        LEFT JOIN users AS users2
        ON users2.id = friendships.friend_id
        ;"""
        results = connectToMySQL(cls.db).query_db(query)
        return results

    @classmethod
    def save(cls,data):
        query = """
        INSERT INTO users(first_name, last_name)
        VALUES (%(first_name)s, %(last_name)s)
        ;"""
        user_id = connectToMySQL(cls.db).query_db(query, data)
        return user_id

    @classmethod 
    def get_all(cls):
        query = """
        SELECT *
        FROM users
        ;"""
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users