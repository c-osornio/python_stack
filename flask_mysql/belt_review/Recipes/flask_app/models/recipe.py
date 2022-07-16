from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash, session
from flask_app.models import user

class Recipe:
    db = "recipes"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.under30 = data['under30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.chef = None

# Create
    @classmethod
    def save(cls, data):
        if not cls.validate_recipe_data(data):
            return False
        query = """
        INSERT INTO recipes(name, description, instructions, date, under30, user_id )
        VALUES (%(name)s, %(description)s, %(instructions)s, %(date)s, %(under30)s, %(user_id)s)
        ; """
        recipe_id = connectToMySQL(cls.db).query_db(query, data)
        return recipe_id

# Read
    @classmethod 
    def get_all_recipes(cls):
        query = """
        SELECT *
        FROM recipes
        JOIN users
        ON recipes.user_id = users.id
        ;"""
        results = connectToMySQL(cls.db).query_db(query)
        all_recipes = []
        if not results:
            return results
        for row in results:
            recipe = cls(row)
            chef_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'birthday': row['birthday'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at'],
            }
            chef = user.User(chef_data)
            recipe.chef = chef
            all_recipes.append(recipe)
        return all_recipes

    @classmethod
    def get_recipe_by_id_with_chef(cls, id):
        data = {
            'id': id,
        }
        query = """
        SELECT *
        FROM recipes
        JOIN users
        ON recipes.user_id = users.id
        WHERE recipes.id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        recipe= cls(results[0])
        for row in results:
            chef_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'birthday': row['birthday'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at'],
            }
            chef = user.User(chef_data)
            recipe.chef = chef
        return recipe

# Update
    @classmethod
    def update(cls, data):
        query = """
        UPDATE recipes 
        SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date = %(date)s, under30 = %(under30)s
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.db).query_db(query, data)

# Delete
    @classmethod
    def delete(cls, id):
        data = {
        'id':id
        }
        query = """
        DELETE FROM recipes
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.db).query_db(query, data)

# Validate 
    @staticmethod
    def validate_recipe_data(data):
        is_valid = True
        if len(data['name']) < 3:
            flash("Your recipe name must be at least three characters long.", "recipe")
            is_valid = False
        if len(data['description']) < 3:
            flash("Your decription must be at least three characters long.", "recipe")
            is_valid = False
        if len(data['instructions']) < 3:
            flash("Your instructions must be at least three characters long.", "recipe")
            is_valid = False
        if len(data['date']) < 1:
            flash("Please enter a date cooked date.", "recipe")
            is_valid = False
        if 'under30' not in data:
            flash("Please select either 'yes' or 'no' to confirm if recipe can be cooked within 30 minutes.", "recipe")
            is_valid = False
        return is_valid
