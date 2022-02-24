from crypt import methods
from telnetlib import DO
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask_app import app
from flask import request, redirect, render_template


@app.route('/ninjas', methods=['POST','GET'])
def create_form():
    if request.method == 'POST':
        data = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'], 
            "age": int(request.form['age']),
            "dojo_id": int(request.form['dojo_id'])
        }
        print(Ninja.save(data))
        url = "/dojos/" + request.form['dojo_id']
        return redirect(url)
    else:
        dojos = Dojo.all_dojos()
        return render_template('ninjas.html', all_dojos = dojos)
    

@app.route("/dojos/<int:dojo_id>")
def ninja_in_dojo(dojo_id):
    ninjas = Ninja.get_ninjas_by_dojo(dojo_id)
    dojo = Dojo.get_dojo_by_id(dojo_id)

    return render_template("ninjas_in_dojo.html", all_ninjas = ninjas, dojo_name = dojo.name)


@app.route("/dojos", methods=['POST','GET'])
def get_index():
    if request.method == 'GET':
        dojos = Dojo.all_dojos()
        return render_template('index.html',dojos = dojos)
    elif request.method == 'POST':
        data = {
            "name": request.form['name']
        }
        print(Dojo.save(data))
        return redirect("/dojos")