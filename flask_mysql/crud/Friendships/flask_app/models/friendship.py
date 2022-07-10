from flask_app.config.mysqlconnection import connectToMySQL

class Friendship:
    db = "friendships_schema"
    def __init__(self,data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = """
        INSERT INTO friendships(user_id, friend_id)
        VALUES (%(user_id)s, %(friend_id)s)
        ;"""
        friendship_id = connectToMySQL(cls.db).query_db(query, data)
        return friendship_id

    @classmethod
    def check_if_already_friends(cls, data):
        query = """
        SELECT * 
        FROM friendships 
        WHERE (user_id = %(user_id)s 
        AND friend_id = %(friend_id)s) 
        ;"""
        if len(connectToMySQL(cls.db).query_db(query, data)) > 0:
            return True