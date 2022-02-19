from crypt import methods
from distutils.log import debug
from unittest import result
from flask import Flask, render_template, redirect, request
from user import User


app = Flask(__name__)

@app.route('/users')
def render_home():
    results = User.get_all_users()
    return render_template('index.html',all_users = results)


@app.route('/users/new', methods=['GET','POST'])
def create_users():
    if request.method == 'POST':
        data = {"first_name": request.form['first_name'], 
                "last_name": request.form['last_name'],
                "email": request.form['email']}
        result =  User.create_user(data)
        print(result)
        return redirect('/users')
    else:
        return render_template("form.html")

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=3000)