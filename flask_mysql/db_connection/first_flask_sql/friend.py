from mysqlconnection import connectToMySQL

class Friend:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"

        results = connectToMySQL('first_flask').query_db(query)

        friends = []

        for friend in results:
            friends.append(cls(friend))
        
        return friends
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO friends (first_name, last_name, occupation) VALUES(%(first_name)s,%(last_name)s,%(occupation)s);"
        return connectToMySQL('first_flask').query_db(query,data)