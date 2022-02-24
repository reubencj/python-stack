
import pymysql.cursors


class MySQLConnection:
    def __init__(self, db) :
        self.connection = pymysql.connect(
        host = 'localhost', 
        db = db, 
        user = 'root',          
        password = 'rootroot',
        charset = 'utf8mb4',
        cursorclass = pymysql.cursors.DictCursor, 
        autocommit = True                   
        )
    

    def query_db(self,query, data = None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query: ", query)
                cursor.execute(query,data)

                if query.lower().find("select") >= 0:
                    return cursor.fetchall()
                else:
                    self.connection.commit()

            except Exception as e:
                print("Something went wrong, ", e)
            
            finally:
                self.connection.close()


def connectToMySQL(db):
    return MySQLConnection(db)




