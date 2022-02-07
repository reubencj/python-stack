from distutils.log import debug
from re import L
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<int:column>')
@app.route('/<int:column>/<int:row>')
@app.route('/')
def render_page(row = 8, column = 8):
    return render_template('index.html', column=column,row=row)

app.run(debug=True, host='localhost', port=3000)