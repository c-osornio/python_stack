from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_bcrypt import Bcrypt
from flask import flash, session
import re   
from datetime import date, datetime

bcrypt = Bcrypt(app)

class User:
    db = "login&registration"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.birthday = data['birthday']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# Create
    @classmethod
    def save(cls, data):
        if not cls.validate_user_reg_data(data):
            return False
        data = cls.parse_reg_data(data)
        query = """
        INSERT INTO users(first_name, last_name, email, password, birthday)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(birthday)s)
        ; """
        user_id = connectToMySQL(cls.db).query_db(query, data)
        session['user_id'] = user_id
        return user_id

# Read
    @classmethod
    def get_user_by_email(cls, email):
        data = {
            "email": email
        }
        query = """
        SELECT * 
        FROM users
        WHERE email = %(email)s 
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        user = cls(row)
        return user

    @classmethod
    def get_user_by_id(cls, id):
        data = {
            "id": id
        }
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

# Update
# Destory

# Validate
    @staticmethod
    def validate_user_reg_data(data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        print(data['terms'])
        if len(data['first_name']) < 2:
            flash("Your first name must be at least two characters long.", "registration")
            is_valid = False
        if not re.match("^[A-Za-z]*$", data['first_name']):
            flash("Your first name can only contain letters." , "registration")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Your last name must be at least two characters long." , "registration")
            is_valid = False
        if not re.match("^[A-Za-z]*$", data['last_name']):
            flash("Your last name can only contain letters." , "registration")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address." , "registration")
            is_valid = False
        if User.get_user_by_email(data['email']):
            flash('Email address is already in use.', "registration")
            is_valid = False
        if len(data['password']) < 8:
            flash("Your password must be at least eight characters long.", "registration")
            is_valid = False
        if not re.match("(?=.*?[A-Z])", data['password']):
            flash("Your password must contain at least one upper case letter." , "registration")
            is_valid = False
        if not re.match("(?=.*?[a-z])", data['password']):
            flash("Your password must contain at least one lower case letter." , "registration")
            is_valid = False
        if not re.match("(?=.*?[0-9])", data['password']):
            flash("Your password must contain at least one digit." , "registration")
            is_valid = False
        if not re.match("(?=.*?[#?!@$%^&*-])", data['password']):
            flash("Your password must contain at least one special character." , "registration")
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash("Your passwords do not match.", "registration")
            is_valid = False
        if (User.get_age(data['birthday'])) < 18:
            flash("You must be at least 18 years old to register.", "registration")
            is_valid = False
        if len(data['birthday']) < 1:
            flash("Please enter a birth date.", "registration")
            is_valid = False
        return is_valid

    @staticmethod
    def parse_reg_data(data):
        parsed_data = {
            'first_name' : data['first_name'],
            'last_name' : data['last_name'],
            'birthday' : data['birthday'],
            'email' : data['email'],
            'password' : bcrypt.generate_password_hash(data[ 'password']),
        }
        return parsed_data

    @staticmethod
    def get_age(birthday):
        print(birthday)
        today = date.today() 
        dob = datetime.strptime(birthday, '%Y-%m-%d')
        print(today, dob)
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        print('######', age)
        return age

    @staticmethod
    def login(data):
        this_user = User.get_user_by_email(data['email'])
        if this_user:
            if bcrypt.check_password_hash(this_user.password, data['password']):
                session['user_id'] = this_user.id
                return True
        flash('Login info is incorrect', 'login')
        return False