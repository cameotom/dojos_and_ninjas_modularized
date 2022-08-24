from flask_app.config.mysqlconnection import connectToMySQL

# model the class after the user table from our database
class Ninja:
    def __init__( self ,data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        # Create an empty list to append our instances of users
        ninjas = []
        # Iterate over the db results and create instances of users with cls.
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    @classmethod
    def create_ninja(cls, data):
        # data is a dictionary that will be passed into the save method from server.py
        query = "INSERT INTO ninjas ( first_name , last_name , age , dojo_id, created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(age)s , %(dojo_id)s, NOW() , NOW() );"
        return connectToMySQL('dojos_and_ninjas').query_db( query, data )

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas where id=%(id)s;"
        result = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE ninjas SET first_name = %(fname)s , last_name = %(lname)s , age= %(age)s , updated_at = NOW() where id=%(id)s;"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM ninjas WHERE id=%(id)s;"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)