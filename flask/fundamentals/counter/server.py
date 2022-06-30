#Create a new Flask project called counter
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'counter123'

#Have the root route render a template that displays the number of times the client has visited this site. Refresh the page several times to ensure the counter is working.
@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    if 'count' not in session:
        session['count'] = 1
    else:    
        session["count"] += 1
    return render_template('index.html')

@app.route('/counter', methods=['POST'])
def count():
    if request.form['count'] == "add":
        return redirect('/')
    else:
        return redirect('/destory_session')

# NINJA BONUS: Add a +2 button underneath the counter and a new route that will increment the counter by 2
@app.route('/plus2', methods=['POST'])
def plus2():
    session['counter'] += 2
    return redirect('/')

# Add a "/destroy_session" route that clears the session and redirects to the root route. Test it.
@app.route('/destory_session')
def destroy():
    session.clear()
    return redirect('/')

#SENSEI BONUS: Add a form that allows the user to specify the increment of the counter and have the counter increment accordingly
@app.route('/pick', methods=['POST'])
def pick():
    session['counter'] += int(request.form['pick']) 
    return redirect('/')


# SENSEI BONUS: Adjust your code to display both how many times the user has actually visited the page, as well as the value of the counter, given the above functionality

if __name__ == '__main__':
    app.run(debug=True)