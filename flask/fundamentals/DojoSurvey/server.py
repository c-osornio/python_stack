from flask import Flask, render_template, redirect, request, session
# Create a new Flask application
app = Flask(__name__)
app.secret_key = 'secret-code'

# Have the root route ("/") show a page with the form
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name']= request.form['name']
    session['location']= request.form['location']
    session['language']= request.form['language']
    session['comment']= request.form['comments']
    session['contact']= request.form['contact']
    return redirect('/result')

# Have the "/result" route display the information from the form on a new HTML page
@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)