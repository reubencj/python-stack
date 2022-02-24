
from  flask_app.config.mysqlconnection import connectToMySQL


class Dojo:
    def __init__ (self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    DOJO_NINJA = 'dojos_and_ninjas_schema'

    @classmethod
    def all_dojos(cls):
        query = ("select * from dojos")
        result = connectToMySQL(cls.DOJO_NINJA).query_db(query)

        dojos = []

        for dojo in result:
            dojos.append(cls(dojo))
        
        return dojos
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos(name) values(%(name)s);"
        return connectToMySQL(cls.DOJO_NINJA).query_db(query,data)

    @classmethod
    def get_dojo_by_id(cls,dojo_id):
        data = {"dojo_id": dojo_id}
        result = connectToMySQL(cls.DOJO_NINJA).query_db("SELECT * from dojos where id = %(dojo_id)s",data)
        return cls(result[0])
