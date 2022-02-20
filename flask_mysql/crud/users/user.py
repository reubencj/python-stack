import re
from mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_users(cls):
        query = 'SELECT * FROM users;'

        result = connectToMySQL('users_schema').query_db(query)

        users = []
        for user in result:
            users.append(cls(user))
        
        return users
    
    @classmethod
    def create_user(cls, data):
        query = 'INSERT INTO users(first_name, last_name,email) VALUES(%(first_name)s,%(last_name)s,%(email)s);'
        return connectToMySQL('users_schema').query_db(query,data)
    
    @classmethod
    def show_one_user(cls,id):
        query = 'SELECT * from users where id = %(id)s'
        result =  connectToMySQL('users_schema').query_db(query,id)
        return result[0]
    
    @classmethod
    def update_user(cls,data):
        query = 'UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s'
        return connectToMySQL('users_schema').query_db(query,data)
    
    @classmethod
    def delete_user(cls, id):
        query = 'DELETE from users where id = %(id)s'
        return connectToMySQL('users_schema').query_db(query,id)







if __name__ == '__main__':

    

    print(User.show_one_user({"id":1}))