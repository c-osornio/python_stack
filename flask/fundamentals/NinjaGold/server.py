from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)
app.secret_key = 'secret-code'

@app.route('/')
def homepage():
    if 'gold' not in session:
        session['gold'] = 0
    if 'log' not in session:
        session['log'] = ' '
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['location'] == "Farm":
        gold_found = random.randint(10, 20)
        session['gold'] += gold_found
        session['log'] += f"<p style='color:green'>You just found {gold_found} gold!</p>"
    if request.form['location'] == "Cave":
        gold_found = random.randint(5, 10)
        session['gold'] += gold_found
        session['log'] += f"<p style='color:green'>You just found {gold_found} gold!</p>"        
    if request.form['location'] == "House":
        gold_found =  random.randint(2, 5)
        session['gold'] += gold_found
        session['log'] += f"<p style='color:green'>You just found {gold_found} gold!</p>"
    if request.form['location'] == "Casino":
        gold_found =  random.randint(-50, 50)
        session['gold'] += gold_found
        if gold_found > 0:
            session['log'] += f"<p style='color:green'>You just found {gold_found} gold!</p>"
        else: 
            session['log'] += f"<p style='color:red'>You lost {gold_found} gold!</p>"
    return redirect ('/')

@app.route('/reset')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)