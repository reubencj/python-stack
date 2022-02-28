from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
import flask_app.models.recipe as recipe



class User:

    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.recipes = []


    

    @classmethod
    def get_user(cls, email):
        query = 'SELECT * from users where email = %(email)s'
        data = {'email': email.lower().strip()}
        result = connectToMySQL('recipe_schema').query_db(query,data)
        if result : 
            return cls(result[0])
        else:
            return False
    
    @classmethod
    def save(cls, data):
        
        query = 'INSERT INTO users(first_name, last_name,email, password) VALUES(%(first_name)s,%(last_name)s,%(email)s, %(password)s);'
        return connectToMySQL('recipe_schema').query_db(query,data)
    

    @staticmethod
    def validate_user( user_data):
        name_validation = re.compile(r'[a-zA-Z]{2,}')
        email_validation = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        password_length_validation = re.compile(r'[a-zA-z!_#@0-9]{8,}')
        password_number_validation = re.compile(r'[0-9]+')
        password_letter_validation = re.compile(r'[a-zA-Z]+')

        is_valid = True

        if not name_validation.match(user_data['first_name']):
            is_valid = False
            flash('First Name needs to letters and more than 2 character','first_name')
        
        if not name_validation.match(user_data['last_name']):
            is_valid = False
            flash('Last Name needs to letters and more than 2 character','last_name')
        
        if not email_validation.match(user_data['email']):
            is_valid = False
            flash('Must have a valid','email')
        
        if not password_length_validation.match(user_data['password']):
            is_valid = False
            flash('Password needs to be more than 8 characters','password')
        if not password_number_validation.search(user_data['password']):
            is_valid = False
            flash('Password needs atleast one number','password')
        if not password_letter_validation.search(user_data['password']):
            is_valid = False
            flash('Password needs atleast one letter','password')
        if user_data['password'] != user_data['password_confirm']:
            is_valid = False
            flash('Password confirmation is not the same as password','password_confirm')
        
        return is_valid









