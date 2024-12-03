from flask_app.config.mysqlconnection import connectToMySQL

class Post:  #db
    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.date = data['date']
        self.num_of_sas = data['num_of_sas']
        self.description = data['description']
        self.users_id = data['users_id']

    @classmethod
    def get_all(cls): #getting the db
        query = "SELECT * FROM posts;"
        results = connectToMySQL('exam_schema').query_db(query)
        posts = [] #empty list
        for d in results: # showing the dict
            posts.append( cls(d) ) # showing the dict
        return posts # returning the list

    @classmethod
    def save(cls, data): #inserting data to the db
        query = "INSERT INTO posts (location, date, num_of_sas, description, users_id) VALUES (%(location)s,%(date)s,%(num_of_sas)s,%(description)s,%(identifier)s);"
        results = connectToMySQL('exam_schema').query_db(query,data)

    @classmethod
    def update(cls, data):
        query = "UPDATE posts SET location = %(location)s, date = %(date)s,num_of_sas = %(num_of_sas)s,description = %(description)s WHERE id = %(post_id)s"
        results = connectToMySQL('exam_schema').query_db(query,data)