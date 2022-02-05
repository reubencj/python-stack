from distutils.log import debug
import re
from flask import Flask

app = Flask(__name__)


@app.route('/')
def testing():
    return 'Hello World'

@app.route('/dojo')

def dojo():
    return 'Dojo'

@app.route('/say/<name>')

def say(name):
    return f'hello {name}'

@app.route('/repeat/<num>/<word>')

def repeat(num, word):
    return f'{word * int(num)}'

app.run(debug = True, host='localhost', port=3000)