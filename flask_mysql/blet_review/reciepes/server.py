
from flask_app import app
import flask_app.controller.users
import flask_app.controller.recipes

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=3000)