from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
import re   

class Email:
    db = "email_validation_with_db_schema"
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        if not cls.validate_email(data):
            return False
        query = """
        INSERT INTO emails(email)
        VALUES (%(email)s)
        ; """
        email_id = connectToMySQL(cls.db).query_db(query, data)
        return email_id

    @classmethod 
    def get_all(cls):
        query = """
        SELECT *
        FROM emails
        ;"""
        results = connectToMySQL(cls.db).query_db(query)
        if len(results) < 1:
            return False
        emails = []
        for row in results:
            emails.append(cls(row))
        return emails

    @classmethod
    def get_by_email(cls, email):
        data = {
        "email": email
        }
        query = """
        SELECT * 
        FROM emails
        WHERE email = %(email)s 
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        email_id = cls(row)
        return email_id

    @classmethod
    def delete(cls, id):
        data = {
            'id': id
        }
        query = """
        DELETE FROM emails
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.db).query_db(query, data)


#Validate
    @staticmethod
    def validate_email(data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address")
            is_valid = False
        if Email.get_by_email(data['email']):
            flash('Email address has already been added to database')
            is_valid = False
        return is_valid