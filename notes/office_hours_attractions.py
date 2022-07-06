# Office Hours

from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'password123'

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/users/create', methods=['POST'])
def users():
    if 'attractions' not in session: 
        session['attractions'] = []
    if 'x' not in session: 
        session['x'] = ' '
    session['username'] = request.form['name']
    return redirect('/attractions')

@app.route('/attractions')
def homepage():
    if 'username' not in session:
        return redirect('/')
    return render_template('attractions.html')

@app.route('/attractions/create', methods=['POST'])
def create_attraction():
    if 'attractions' not in session: 
        session['attractions'] = []
    temp = session['attractions']
    temp.append(f"{request.form['attraction']} in {request.form['city']}")
    session['x'] += f"<p>{request.form['attraction']} in {request.form['city']}</p>"
    session['attractions'] = temp
    session['attractions'].append(request.form['attraction'])
    print(session['attractions'])
    return redirect('/attractions')


@app.route('/reset')
def reset_user():
    session.pop('attractions')
    return redirect('/attractions')

@app.route('/return')
def return_home():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)