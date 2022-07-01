from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    # fruits selected shown in checkout
    strawberry_amt = request.form['strawberry']
    raspberry_amt = request.form['raspberry']
    apple_amt = request.form['apple']
    blackberry_amt = request.form['blackberry']
    # user info shown in checkout
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    # items ordered shown in checkout
    count = int(strawberry_amt) + int(raspberry_amt) + int(apple_amt) + int(blackberry_amt)
    # date and time shown in checkout
    now = datetime.now()
    # In the checkout method, add a print statement that says "Charging {{Customer name}} for {{count}} fruits"
    print(f"Charging { first_name } { last_name } for { count } fruit/s") 
    return render_template("checkout.html", now = now.strftime("%b %d, %Y at %I:%M %p"), item_count = count, first=first_name, last=last_name, studentid=student_id, strawberries = strawberry_amt, raspberries =raspberry_amt, apples = apple_amt, blackberries = blackberry_amt)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)

# While on the checkout screen, hit the refresh button in your browser. Then check your terminal--what do you notice? Charges order again after refresh