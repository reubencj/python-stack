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
    signed_up_user = User.get_user(request.form['email'].lower().strip())
    session['first_name'] = signed_up_user.first_name
    session['id'] = signed_up_user.id
    session['logged_in'] = True

    return redirect('/dashboard')


    
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
    session['id'] = login_user.id
    session['logged_in'] = True
    return redirect('/dashboard')
        
@app.route('/log_off')
def log_off():
    session.clear()
    return redirect('/')