from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
    return "hello world ya'll"


@app.route('/sucess')

def sucess():
    return "This was successful"

@app.route('/hello/<string:name>/<int:num>')

def greet(name, num = 1):
    return f'I want to say hello {name * num}'

if __name__ == "__main__":
    app.run(debug = True, port=3000, host="localhost")
