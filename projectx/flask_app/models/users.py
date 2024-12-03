from flask_app.config.mysqlconnection import connectToMySQL



class User:  #db
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']


@classmethod
def save(cls,data):
    query = "INSERT INTO users (username, password) VALUES (%(username)s, %(password)s);"
    return connectToMySQL("exam_schema").query_db(query, data)