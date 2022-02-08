from crypt import methods
from distutils.log import debug
from flask import Flask, render_template, redirect, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)


@app.route('/')
def show_counter():
    counter = 1
    if 'counter' in session:
        counter = session['counter']
    
    return render_template('index.html', counter = counter)

@app.route('/add', methods = ['POST'])
def add_counter():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 2
    
    return redirect('/')

@app.route("/destory_session", methods=['POST'])
def clear_session():
    if 'counter' in session:
        session.pop('counter')
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=3000)

