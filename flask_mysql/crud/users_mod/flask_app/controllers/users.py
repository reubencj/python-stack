from flask_app import app
from flask_app.models.user import User
from flask import redirect, render_template, request


@app.route('/users')
def render_home():
    results = User.get_all_users()
    return render_template('index.html',all_users = results)


@app.route('/users/new', methods=['GET','POST'])
def create_users():
    if request.method == 'POST':
        data = {'first_name': request.form['first_name'], 
                'last_name': request.form['last_name'],
                'email': request.form['email']}
        result =  User.create_user(data)
        print(result)
        return redirect('/users')
    else:
        return render_template('form.html')

@app.route('/users/<int:id>')
def show_one(id):
    user_id = {'id':id}
    user = User.show_one_user(user_id)
    print(user)
    return render_template('show_user.html',user = user)

@app.route('/users/<int:id>/delete')
def delete_user(id):
    user_id = {'id': id}
    print(User.delete_user(user_id))
    return redirect('/users')

@app.route('/users/<int:id>/edit', methods=['POST','GET'])
def edit_user(id):
    if request.method == 'POST':
        data = {'id': id, 'first_name':request.form['first_name'], 'last_name':request.form['last_name'], 'email': request.form['email']}
        print(data)
        print(User.update_user(data))
        return redirect("/users")
    else:
        result = User.show_one_user({'id':id})
        return render_template('edit_user.html',one_user=result)