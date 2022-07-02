# Create a new Flask project called great_number_game
from flask import Flask, render_template, session, redirect, request
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'secret-code'

# NINJA BONUS: Allow the user to keep guessing until they get it correct
@app.route('/')
def homepage():
    if 'number' not in session:
        session['number'] = random.randint(1,100)
    if 'counter' not in session:
        session['counter'] = 0
    if 'log' not in session:
        session['log'] = ' '
    return render_template('index.html')
# Create a route that determines whether the number submitted is too high, too low, or correct. Show this status on the HTML page.
@app.route('/analyze', methods=['POST'])
def check_guess():
    if int(request.form['guess']) == session['number']:
        session['result'] = "Correct"
    elif int(request.form['guess']) > session['number']:
        session['result'] = "High"
    elif int(request.form['guess']) < session['number']:
        session['result'] = "Low"
    session['counter'] += 1
    return redirect('/')

@app.route('/reset')
def destroy():
    session.pop('number')
    session.pop('counter')
    session.pop('result')
    return redirect('/')

@app.route('/clear')
def clear_leaderboard():
    session.clear()
    return redirect('/')

@app.route('/add_to_leaderboard', methods=['POST'])
def add_to_leaderboard():
    winner = request.form['name']
    now = datetime.now().strftime("%b %d, %Y at %I:%M %p")
    session['log'] = f"<p style='color:green'>Winner: {winner} // Attempts: {session['counter']} // Time: {now}</p>" + session['log']  
    return redirect('/leaderboard')

@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')

if __name__=="__main__":
    app.run(debug=True)