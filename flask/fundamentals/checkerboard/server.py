from flask import Flask, render_template
app = Flask(__name__)

#Have the root route render a template with a checkerboard on it
@app.route('/')
def checkerboard():
    return render_template('index.html', x = 8, y = 8, color1 = 'red', color2 = 'blue')  

# Have another route accept a single parameter (i.e. "/<x>") and render a checkerboard with x many rows, with alternating colors
@app.route('/<int:x>')
def single_parameter(x):
    return render_template('index.html', x = x, y = 8, color1 = 'red', color2 = 'blue')

# NINJA BONUS: Have another route accept 2 parameters (i.e. "/<x>/<y>") and render a checkerboard with x rows and y columns, with alternating colors
@app.route('/<int:x>/<int:y>')
def two_parameters(x, y):
    return render_template('index.html', x = x, y = y, color1 = 'red', color2 = 'blue')

#SENSEI BONUS: Have another route accept 4 parameters (i.e. "/<x>/<y>/<color1>/<color2>") and render a checkerboard with x rows and y columns, with alternating colors, color1 and color2
@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def four_parameters(x, y, color1, color2):
    return render_template('index.html', x = x, y = y, color1 = color1, color2 = color2)

if __name__=="__main__":
    app.run(debug=True)