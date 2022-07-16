from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import recipe, user

# Create
@app.route('/recipe/create_new', methods=['POST'])
def create_recipe():
    if "user_id" in session:
        if recipe.Recipe.save(request.form):
            return redirect(f'/users/profile/{session["user_id"]}')
        return render_template('create_recipe.html', info = request.form)
    return redirect('/')

# Read
@app.route('/recipe/create')
def show_create_recipe_form():
    return render_template('create_recipe.html', info = request.form)

@app.route('/recipe/<int:id>')
def show_recipe(id):
    return render_template('recipe.html', recipe = recipe.Recipe.get_recipe_by_id_with_chef(id), user = user.User.get_user_by_id(session["user_id"]))

@app.route('/recipe/<int:id>/edit')
def show_edit_form(id):
    return render_template('edit_recipe.html', recipe = recipe.Recipe.get_recipe_by_id_with_chef(id))

# Update
@app.route('/recipe/<int:id>/update', methods=['POST'])
def update_recipe(id):
    if recipe.Recipe.validate_recipe_data(request.form):
        recipe.Recipe.update(request.form)
        return redirect(f'/users/profile/{session["user_id"]}')
    return redirect(f'/recipe/{id}/edit')

# Delete
@app.route('/recipe/<int:id>/delete')
def delete_recipe(id):
    this_recipe = recipe.Recipe.get_recipe_by_id_with_chef(id)
    if this_recipe.user_id == session['user_id']:
        recipe.Recipe.delete(id)
        return redirect(f'/users/profile/{session["user_id"]}')
    return render_template('/users/logout')