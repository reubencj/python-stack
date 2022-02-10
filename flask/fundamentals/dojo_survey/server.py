from crypt import methods
from distutils.log import debug
from unicodedata import name
from flask import Flask, render_template, redirect, request, session
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)
@app.route("/")
def render_index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def sumbit_form():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    print(session)
    return redirect('/result')

@app.route('/result')
def show_results():
    return render_template("result.html")

app.run(debug=True, host="localhost", port=3000)