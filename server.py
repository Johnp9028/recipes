from flask_app import app
from flask_app.controller import guest_controller, recipe_controller

if __name__ == "__main__":
        app.run(debug=True)