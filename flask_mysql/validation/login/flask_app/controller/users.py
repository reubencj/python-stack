from crypt import methods
from flask_app import app
from flask import redirect, render_template, flash, request, flash, session
from flask_bcrypt import Bcrypt
from flask_app.models.user import User

bcrypt = Bcrypt(app)


@app.route('/')
def render_homepage():
    return render_template('index.html')

@app.route('/signup',methods=['POST'])
def signup_user():
    if not User.validate_user(request.form):
        return redirect('/')
    if User.get_user(request.form['email']):
        flash('email already exist, try another email or login', 'email')
        return redirect('/')

    password = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name': request.form['first_name'].lower().strip(),
        'last_name': request.form['last_name'].lower().strip(),
        'email': request.form['email'].lower().strip(),
        'password': password
    }
    User.save(data)
    session['first_name'] = request.form['first_name']
    session['logged_in'] = True

    return redirect('/logged_in')

@app.route('/logged_in')
def logged_in():
    if not session: 
        return redirect('/')
    
    return render_template('logged_in.html')
    
@app.route('/login', methods=['POST'])
def login():
    session['email'] = request.form['email']
    login_user = User.get_user(request.form['email'])
    if not login_user:
        flash('email does not exist, sign up or retype correct email','login_email')
        return redirect('/')

    if not bcrypt.check_password_hash(login_user.password, request.form['password']):
        flash('password does not match', 'login_password')
        return redirect('/')
    
    session['first_name'] = login_user.first_name
    session['logged_in'] = True
    return redirect('/logged_in')
        
@app.route('/log_off')
def log_off():
    session.clear()
    return redirect('/')