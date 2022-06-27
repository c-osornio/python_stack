from flask import Flask, render_template
app = Flask(__name__)

# Have the /play route render a template with 3 blue boxes


@app.route('/play')
def level_1():
    return render_template('index.html', color="blue", amount=3)

# Have the /play/<x> route render a template with x number of blue boxes


@app.route('/play/<int:x>')
def level_2(x):
    return render_template('index.html', color="blue", amount=x)

# Have the /play/<x>/<color> route render a template with x number of boxes the color of the provided value


@app.route('/play/<int:x>/<string:color>')
def level_3(x, color):
    return render_template('index.html', color=color, amount=x)

# NINJA BONUS: Use only one template for the whole project - done


if __name__ == "__main__":
    app.run(debug=True)
