#Start a new Flask project
from flask import Flask, render_template
app = Flask(__name__)

# Create a route in which the data above is declared and then sent to the template engine to be rendered
# Create the template that displays the data in a table
@app.route('/')
def homepage():
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template('index.html', users = users)

if __name__=="__main__":
    app.run(debug=True)