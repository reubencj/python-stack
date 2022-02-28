import re
from flask_app.config.mysqlconnection import connectToMySQL
import flask_app.models.user as user
from flask import flash
class Recipe:
    
    def __init__(self,data) :
        self.id = data['id']
        self.name = data['name']
        self.description  = data['description']
        self.instruction = data['instruction']
        self.made_on = data['made_on']
        self.under_30_min = data['under_30_min']
        self.created_on = data['created_at']
        self.updated_on = data['updated_at']

        self.users_id = data['users_id']
    

    @classmethod
    def get_all_recipes(cls):
        query = "select * from recipes"
        result = connectToMySQL('recipe_schema').query_db(query)
        all_recipes = []
        for recipe in result:
            all_recipes.append(cls(recipe))
        
        return all_recipes
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO recipes(name, description, instruction, made_on, under_30_min, users_id) VALUES(%(name)s,%(description)s, %(instruction)s, %(made_on)s, %(under_30_min)s, %(users_id)s );"
        return connectToMySQL('recipe_schema').query_db(query,data)
    
    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, made_on = %(made_on)s, under_30_min = %(under_30_min)s where id = %(id)s;"
        return connectToMySQL('recipe_schema').query_db(query,data)
    
    @classmethod
    def delete_recipe_by_id(cls, id):
        data = {'id':id}
        query = "DELETE from recipes where id = %(id)s"
        return connectToMySQL('recipe_schema').query_db(query,data)

    @classmethod
    def get_recipe_by_id(cls, id):
        data = {'id':id}
        result = connectToMySQL('recipe_schema').query_db("SELECT * FROM recipes where id = %(id)s",data)
        return cls(result[0])

    @staticmethod
    def validate_recipe(data):
        is_valid = True

        if  not len(data['name']) > 2:
            flash('name needs to more than two characters', 'name')
            is_valid = False
        
        if   not len(data['description']) > 2:
            flash('Description needs to more than two characters', 'description')
            is_valid = False
        
        if  not len(data['instruction']) > 2:
            flash('Instruction needs to more than two characters', 'instruction')
            is_valid = False
        
        if not len(data['made_on']) > 2:
            flash('you need a date', 'made_on')
            is_valid = False
        
        if not 'under_30_min' in data: 
            flash('select yes or no', 'under_30_min')
            is_valid = False
        
        return is_valid





    
