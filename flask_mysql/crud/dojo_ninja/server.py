from flask_app import app
from flask_app.controllers import dojo_ninja_controller

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=3000)


