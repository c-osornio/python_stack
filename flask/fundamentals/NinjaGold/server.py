#Create a new Flask project called ninja_gold
from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)
app.secret_key = 'secret-code'

# Have the root route render this page
@app.route('/')
def homepage():
    if 'gold' not in session:
        session['gold'] = 0
    if 'log' not in session:
        session['log'] = ' '
    if 'counter' not in session:
        session['counter'] = 0
    return render_template('index.html')
# Have the "/process_money" POST route increase/decrease the user's gold by an appropriate amount and redirect to the root route
# NINJA BONUS: Display all the activities performed by the user in a log on the HTML, as shown in the wireframe
# NINJA BONUS: Have the activities be color-coded as shown above (+ money is green, - money is red)
# SENSEI BONUS: Have the activities display in descending order, with the most recent activity first
@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['location'] == "Farm":
        gold_found = random.randint(10, 20)
        session['gold'] += gold_found
        session['log'] = f"<p style='color:green'>You just found {gold_found} gold!</p>" + session['log']
    if request.form['location'] == "Cave":
        gold_found = random.randint(5, 10)
        session['gold'] += gold_found
        session['log'] = f"<p style='color:green'>You just found {gold_found} gold!</p>" + session['log']        
    if request.form['location'] == "House":
        gold_found =  random.randint(2, 5)
        session['gold'] += gold_found
        session['log'] = f"<p style='color:green'>You just found {gold_found} gold!</p>" + session['log']  
    if request.form['location'] == "Casino":
        gold_found =  random.randint(-50, 50)
        session['gold'] += gold_found
        if gold_found > 0:
            session['log'] = f"<p style='color:green'>You just found {gold_found} gold!</p>" + session['log']  
        else: 
            session['log'] = f"<p style='color:red'>You lost {gold_found} gold!</p>" + session['log']
    session['counter'] += 1
    return redirect ('/')

#NINJA BONUS: Add a reset button to restart the game
@app.route('/reset')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)