from crypt import methods
from datetime import datetime
from flask import redirect, render_template, flash, session, request
from flask_app.models.recipe import Recipe
from flask_app import app
from datetime import datetime


@app.route('/dashboard')
def logged_in():
    if not session: 
        return redirect('/log_off')
    
    if  not session['logged_in']:
        
        return redirect('/log_off')
    
    recipes = Recipe.get_all_recipes()
    
    return render_template('dashboard.html',all_recipes = recipes)


@app.route('/recipes/new', methods = ['POST', 'GET'])
def create_recipe():
    if not session: 
        return redirect('/log_off')
    
    if  not session['logged_in']:
        
        return redirect('/log_off')
    

    if request.method == 'GET':
        return render_template('recipe_form.html')
    elif request.method == 'POST':

        if not Recipe.validate_recipe(request.form):
            return redirect('/recipes/new')
        data = dict(request.form)
        data['made_on'] = datetime.strptime(data['made_on'],'%Y-%m-%d')
        data['users_id'] = session['id']
        Recipe.save(data)
        return redirect('/dashboard')


@app.route('/recipes/<int:id>/edit', methods = ['POST', 'GET'])
def edit (id):
    if not session: 
        return redirect('/log_off')
    
    if  not session['logged_in']:
        
        return redirect('/log_off')
    

    if request.method == 'GET': 
        recipe = Recipe.get_recipe_by_id(id)
        return render_template('edit.html', recipe = recipe)
    elif request.method == 'POST':
        if not Recipe.validate_recipe(request.form):
            redirect_url = '/recipes/'+str(id)+'/edit'
            return redirect(redirect_url)
        data = dict(request.form)
        data['made_on'] = datetime.strptime(data['made_on'],'%Y-%m-%d')
        data['id'] = id
        Recipe.update_recipe(data)
        return redirect('/dashboard')

@app.route('/recipes/<int:id>')
def view(id):
    if not session: 
        return redirect('/log_off')
    
    if  not session['logged_in']:
        
        return redirect('/log_off')
    recipe = Recipe.get_recipe_by_id(id)
    recipe.made_on = recipe.made_on.strftime('%B, %d, %Y')
    return render_template('view.html',recipe = recipe)

@app.route('/recipes/<int:id>/delete')
def delete(id):
    if not session: 
        return redirect('/log_off')
    
    if  not session['logged_in']:
        
        return redirect('/log_off')
    
    Recipe.delete_recipe_by_id(id)
    return redirect('/dashboard')



    
