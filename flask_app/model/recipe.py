from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.model import guest
from flask import flash

db = "recipe_schema"
class Recipe:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.recipe_name = db_data['recipe_name']
        self.description = db_data['description']
        self.instructions = db_data['instructions']
        self.date_made = db_data['date_made']
        self.under = db_data['under']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.guest_id = db_data['guest_id']
        self.chef = None



    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM recipes
                JOIN guests on recipes.guest_id = guests.id;
                """
        results = connectToMySQL(db).query_db(query)
        recipes = []
        for row in results:
            this_recipe = cls(row)
            guest_data = {
                "id": row['guests.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": "",
                "created_at": row['created_at'],
                "updated_at": row['updated_at']
            }
            this_recipe.chef = guest.Guest(guest_data)
            recipes.append(this_recipe)
        return recipes

    @classmethod
    def save(cls, recipe_data):
        query = """
                INSERT INTO recipes (recipe_name,description,instructions,date_made,under,guest_id)
                VALUES (%(recipe_name)s,%(description)s,%(instructions)s,%(date_made)s,%(under)s,%(guest_id)s);
                """
        return connectToMySQL(db).query_db(query,recipe_data)

    @classmethod
    def delete(cls,data):
        query = """
                DELETE FROM recipes
                WHERE id = %(id)s;
                """
        return connectToMySQL(db).query_db(query,data)
    

    @classmethod
    def get_by_id(cls,data):
        query = """
                SELECT * FROM recipes
                JOIN guests on recipes.guest_id = guests.id
                WHERE recipes.id = %(id)s;
                """
        result = connectToMySQL(db).query_db(query,data)
        if not result:
            return False

        result = result[0]
        this_recipe = cls(result)
        guest_data = {
                "id": result['guests.id'],
                "first_name": result['first_name'],
                "last_name": result['last_name'],
                "email": result['email'],
                "password": "",
                "created_at": result['created_at'],
                "updated_at": result['updated_at']
        }
        print(guest_data)
        this_recipe.creator = guest.Guest(guest_data)
        return this_recipe

    @classmethod
    def delete(cls,data):
        query = """
                DELETE FROM recipes
                WHERE id = %(id)s;
                """
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def update(cls,recipe_data):
        query = """
                UPDATE recipes
                SET recipe_name = %(recipe_name)s,
                description = %(description)s,
                instructions = %(instructions)s ,
                date_made = %(date_made)s,
                under = %(under)s
                WHERE
                id=%(id)s
                """
        return connectToMySQL(db).query_db(query,recipe_data) 