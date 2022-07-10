from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models import dojo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if not dojo.Dojo.validate(request.form):
        return redirect('/')
    session['name']= request.form['name']
    session['location']= request.form['location']
    session['language']= request.form['language']
    session['comment']= request.form['comment']
    session['contact']= request.form['contact']
    return redirect('/result')

@app.route('/result')
def results():
    return render_template('result.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')