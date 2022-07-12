from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process/email', methods=['POST'])
def create_email():
    if email.Email.save(request.form):
        session['email'] = request.form['email']
        return redirect('/success')
    return redirect('/')

@app.route('/success')
def success():
    return render_template('success.html', emails = email.Email.get_all())

@app.route('/destroy/<int:id>')
def delete(id):
    email.Email.delete(id)
    return redirect('/success')