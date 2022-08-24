from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
# model the class after the user table from our database
class Dojo:
    def __init__( self ,data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_dojo_with_ninjas(cls , data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query , data)
        dojo = cls( results[0])
        for row_from_db in results:
            ninja_data = {
                "id": row_from_db["ninjas.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "age": row_from_db["age"],
                "dojo_id": row_from_db["dojo_id"],
                "created_at": row_from_db["ninjas.created_at"],
                "updated_at": row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        # Create an empty list to append our instances of users
        dojos = []
        # Iterate over the db results and create instances of users with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def create_dojo(cls, data):
        # data is a dictionary that will be passed into the save method from server.py
        query = "INSERT INTO dojos ( name , created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        return connectToMySQL('dojos_and_ninjas').query_db( query, data )

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos where id=%(id)s;"
        result = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE dojos SET name = %(name)s , updated_at = NOW() where id=%(id)s;"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM dojos WHERE id=%(id)s;"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)