
from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:


    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
    
    DOJO_NINJA = 'dojos_and_ninjas_schema'


    @classmethod
    def save(cls, data):
        query = 'INSERT INTO ninjas(first_name, last_name, age, dojo_id) values(%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);'
        return connectToMySQL(cls.DOJO_NINJA).query_db(query,data)

    @classmethod
    def get_ninjas_by_dojo(cls, dojo_id):
        data = {"dojo_id":dojo_id}
        query = 'SELECT * from ninjas where dojo_id = %(dojo_id)s'
        ninjas = []
        result = connectToMySQL(cls.DOJO_NINJA).query_db(query,data)
        
        for ninja in result:
            ninjas.append(cls(ninja))
        
        return ninjas
    






