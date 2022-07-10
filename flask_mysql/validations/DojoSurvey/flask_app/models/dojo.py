from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    db =     db = "dojo_survey_schema"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language= data['language']
        self.comment= data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate(dojo):
        is_valid = True
        if len(dojo['name']) < 1:
            flash("Name must be at least 1 character")
            is_valid = False
        if (dojo['location']) == "-- Select A Location --":
            flash("Please select a location")
            is_valid = False
        if (dojo['language']) == "-- Select A Language --":
            flash("Please select a language")
            is_valid = False
        if len(dojo['comment']) < 3:
            flash("Comment must be at least 3 characters")
            is_valid = False
        return is_valid