from flask_app.config.mysqlconnection import connectToMySQL, MySQLConnection
from flask_app import app
from flask_app.models import user
from flask import flash, session
from datetime import datetime
import math

class Message:
    db = "private_wall"
    def __init__(self,data):
        self.id = data['id']
        self.sender_id = data['sender_id']
        self.recipient_id= data['recipient_id']
        self.message = data['message']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None
        self.time = None

# Create
    @classmethod
    def save(cls, data):
        if not cls.validate_message_data(data):
            return False
        query = """
        INSERT INTO messages(sender_id, recipient_id, message)
        VALUES (%(sender_id)s, %(recipient_id)s, %(message)s)
        ; """
        message_id = connectToMySQL(cls.db).query_db(query, data)
        return message_id

# Read
    @classmethod
    def get_all_received_by_id(cls, id):
        data = {
            "id": id
        }
        query = """
        SELECT * 
        FROM messages 
        WHERE recipient_id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        messages = []
        for row in results:
            messages.append(cls(row))
        return messages

    @classmethod
    def get_all_sent_by_id(cls, id):
        data = {
            "id": id
        }
        query = """
        SELECT * 
        FROM messages 
        WHERE sender_id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        messages = []
        for row in results:
            messages.append(cls(row))
        return messages

    @classmethod
    def get_all_messages_to_user_by_id(cls, id):
        data = {
            "id": id
        }
        query = """
        SELECT *
        FROM users
        LEFT JOIN messages
        ON users.id = messages.sender_id
        LEFT JOIN users AS users2
        ON users2.id = messages.recipient_id
        WHERE recipient_id = %(id)s 
        ORDER BY users.first_name DESC;
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        print('###############', results)
        if len(results) < 1:
            return False
        messages = []
        for row in results:
            message_data = {
                'id' : row['messages.id'],
                'sender_id' : row['sender_id'],
                'recipient_id' : row['recipient_id'],
                'message' : row['message'],
                'created_at' : row['messages.created_at'],
                'updated_at' : row['messages.updated_at']
            }
            message = cls(message_data)
            message.creator = user.User(row)
            message.time = Message.get_time_between(message.created_at)
            messages.append(message)
        return messages

    @classmethod
    def get_message_by_id(cls, id):
        data = {
            'id': id,
        }
        query = """
        SELECT *
        FROM messages
        WHERE id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        message= cls(row)
        return message

# Delete 
    @classmethod
    def delete(cls, id):
        data = {
        'id':id
        }
        query = """
        DELETE FROM messages
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.db).query_db(query, data)



# Validate 
    @staticmethod
    def validate_message_data(data):
        is_valid = True
        if len(data['message']) < 5:
            flash("Your message must be at least five characters long.", "message")
            is_valid = False
        return is_valid

    @staticmethod
    def get_time_between(created_at):
        now = datetime.now()
        # time_differenc is a time delta
        time_difference = now - created_at
        # time deltas only have total_seconds() and days
        days = time_difference.days
        seconds = math.floor(time_difference.total_seconds())
        minutes = math.floor(time_difference.total_seconds() / 60)
        hours = math.floor(minutes / 60)
        if days > 0:
            return f"{days} days ago"
        elif hours >= 1:
            return f'{hours} hours ago'
        elif minutes >= 1:
            return f'{minutes} minutes ago'
        else:
            return f'{seconds} seconds ago'