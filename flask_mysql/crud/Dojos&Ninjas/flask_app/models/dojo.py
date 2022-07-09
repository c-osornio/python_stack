from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    db = "dojos_and_ninjas"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

#CREATE
    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO dojos (name)
        VALUES (%(name)s)
        ; """
        dojo_id = connectToMySQL(cls.db).query_db(query, data)
        return dojo_id

#READ
    @classmethod 
    def get_all(cls):
        query = """
        SELECT *
        FROM dojos
        ;"""
        results = connectToMySQL(cls.db).query_db(query)
        dojos = []
        print('++++++++++', results)
        for row in results:
            dojos.append(cls(row))
        return dojos

    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * 
        FROM dojos
        WHERE id = %(id)s 
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        dojo = cls(row)
        return dojo

    @classmethod
    def get_dojo_with_ninjas( cls , data ):
        query = """
        SELECT * 
        FROM dojos 
        LEFT JOIN ninjas 
        ON ninjas.dojo_id = dojos.id 
        WHERE dojos.id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db( query , data )
        dojo = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append( ninja.Ninja( ninja_data ) )
        return dojo