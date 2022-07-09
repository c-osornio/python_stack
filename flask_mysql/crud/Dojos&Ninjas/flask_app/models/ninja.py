from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

class Ninja:
    db = "dojos_and_ninjas"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO ninjas(dojo_id, first_name, last_name, age, created_at, updated_at)
        VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s, NOW(), NOW())
        ; """
        ninja_id = connectToMySQL(cls.db).query_db(query, data)
        return ninja_id