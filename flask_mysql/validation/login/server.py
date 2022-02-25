from distutils.log import debug
from flask_app import app
import flask_app.controller.users

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=3000)