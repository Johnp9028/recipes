from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.model.recipe import Recipe
from flask_app.model.guest import Guest



@app.route('/create/add', methods=['POST'])
def add():
    if 'guest_id' not in session:
        return redirect('/logout')
    recipe_data = {
        'guest_id': session['guest_id'],
        'recipe_name': request.form['recipe_name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_made': request.form['date_made'],
        'under': request.form['under'],
    }
    Recipe.save(recipe_data)
    return redirect('/dashboard')


@app.route('/edit/<int:id>')
def edit(id):
    if 'guest_id' not in session:
        return redirect('/logout')
    return render_template('editrecipe.html',recipe=Recipe.get_by_id({'id': id}))

@app.route('/view/<int:id>')
def view(id):
    if 'guest_id' not in session:
        return redirect('/logout')
    return render_template('onerecipe.html',recipe=Recipe.get_by_id({'id': id}))



@app.route('/delete/<int:id>')
def delete(id):
    if 'guest_id' not in session:
        return redirect ('/logout')
    Recipe.delete({'id':id})
    return redirect('/dashboard')

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    if 'guest_id' not in session:
        return redirect('/logout')
    recipe_data = {
        'id':id,
        'recipe_name': request.form['recipe_name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_made': request.form['date_made'],
        'under': request.form['under'],
    }
    Recipe.update(recipe_data)
    return redirect('/dashboard')
