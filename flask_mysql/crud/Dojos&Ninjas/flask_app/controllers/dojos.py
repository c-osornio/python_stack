from flask_app import app
from flask import render_template,redirect,request
from flask_app.models import dojo

# CREATE
@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    dojo.Dojo.save(request.form)
    return redirect('/dojos')

# READ
@app.route('/dojos')
def show_dojos():
    return render_template('show_dojos.html', dojos = dojo.Dojo.get_all())

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template('show_dojo.html', dojo= dojo.Dojo.get_dojo_with_ninjas(data))