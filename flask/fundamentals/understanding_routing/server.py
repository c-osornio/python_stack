from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)  # Create a new instance of the Flask class called "app"

# 1.  localhost:5000/ - have it say "Hello World!"


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# 2 localhost:5000/dojo - have it say "Dojo!"


@app.route('/dojo')
def dojo():
    return "Dojo!"

# 3 Create one url pattern and function that can handle the following examples
# for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'


# NINJA BONUS: Ensure the names provided in the 3rd task are strings
@app.route('/say/<string:name>')
def hi(name):
    return f'Hi {name}!'

# 4 Create one url pattern and function that can handle the following examples (HINT: int() will come in handy! For example int("35") returns 35):


# NINJA BONUS: For the 4th task, ensure the 2nd element in the URL is an integer, and the 3rd element is a string
@app.route('/repeat/<int:amount>/<string:word>')
def repeat(amount, word):
    string = ''
    for i in range(amount):
        string += word + ' '
    return string

# @app.route('/name/<user_name>')
# def hello(user_name):
#     return render_template('index.html', name=user_name)
# in HTML - use an if method in Jinja2 to check if a name was provided with {%  if name %}


# app.run(debug=True) should be the very last statement!
if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
