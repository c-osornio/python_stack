from os import link
import unittest
import random
fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
salad = 3 * vegetables
print(salad)

for count in range(0, 5):
    print("looping =", count)

countries = ["Uganda", "Chile", "Albania", "Saudi Arabia"]

# Challenge 1: Fix the range!
for integer in range(0, len(countries)):
    print("Index:", integer)
    # Challenge 2: print the index here
    print("Country:", countries[integer])
    # Challenge 3: print the country here

# Looping over values only...
for country in countries:
    print("Country: ", country)
    # Challenge 4: print the country here

y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")


def add(a, b):
    x = a + b
    return x


sum1 = add(4, 6)
sum2 = add(1, 4)
sum3 = sum1 + sum2
print(sum3)


def multiply(num_list, num):
    for x in num_list:
        x *= num
    return num_list


a = [2, 4, 10, 16]
b = multiply(a, 5)
print(b)


def multiply(num_list, num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list


a = [2, 4, 10, 16]
b = multiply(a, 5)
print(b)
# output: >>>[10,20,50,80]

my_dict = {
    'name': 'Charlie',
    'age': 30,
    'stack': 'Python'
}
my_dict2 = {
    'name': 'Carlos',
    'age': 31,
}


print(my_dict)
my_dict.update(my_dict2)
print(my_dict)

my_string = f'{my_dict["name"]} is {my_dict["age"]} years old and is taking {my_dict["stack"]}'
print(my_string)
print(my_dict.keys())
print(my_dict.values())
for key in my_dict.keys():
    print(key)

num = 5
num2 = 10
while num <= 10:
    num += 1
    print(num)

mylist = [{"name": 'Charlie', "age": 30, 'email': 'charlie@gmail.com'}, {"name": 'Stephen',
                                                                         "age": 31, 'email': 'stephen@gmail.com'}, {"name": 'Alex', "age": 27, 'email': 'alex@gmail.com'}]

for item in mylist:
    print(
        f"Student's Name: {item['name']}, Age: {item['age']}, Email: {item['email']}\n")

print("hello")


def repeat_phrase(phrase, repeat):
    print(phrase * repeat)


repeat_phrase("hello \n", 4)

# List of dictionaries
users = [
    {"first": "Ada", "last": "Lovelace"},  # index 0
    {"first": "Alan", "last": "Turing"},  # index 1
    {"first": "Eric", "last": "Idle"}  # index 2
]
# Dictionary of lists
resume_data = {
    #        	     0                     1                         2
    "skills": ["front-end", "back-end", "database"],
    #                          0                 1
    "languages": ["Python", "JavaScript"],
    #                            0                    1
    "hobbies": ["rock climbing", "knitting"]
}
print(users[0]["last"])  # prints Lovelace


print(resume_data["skills"][1])  # prints back-end
print(users[2]["first"])  # prints Eric

# Print the first listed languange of the second resume

resumes = [
    {
        "skills": ["front - end", "back - end", "database"],
        "languages": ["Python", "JavaScript"],
        "hobbies": ["rock climbing", "knitting"]
    },
    {
        "skills": ["front - end", "back - end", "database"],
        "languages": ["FIND ME: Python", "JavaScript"],
        "hobbies": ["rock climbing", "knitting"]
    },
    {
        "skills": ["front - end", "back - end", "database"],
        "languages": ["Python", "JavaScript"],
        "hobbies":["rock climbing", "knitting"]
    }
]
print(resumes[1]["languages"][0])
# resume is a  list so we search through it first with a number
# the 2nd index hold a dictionary so we now need a string key
# dictionary language list has 2 indexes so we seach it through another number


class User:
    # instance method or constructor method
    def __init__(self):
        self.first_name = "Ada"
        self.last_name = "Lovelace"
        self.age = 42


user_ada = User()
print(user_ada.first_name)

# Create another user called user_2!
user2 = User()
# Print user_ada's last name.
print(user_ada.last_name)
# Print user_2's last name. (Yes, they should be the same)
print(user2.last_name)
# Run the code, pause, go back and step through one line at a time
# What do you notice about the order it runs in?
# Write down any other questions you have.

# Sensei Exercise: try just printing the variable, user_ada.
#   What prints to the terminal? Location
print(user_ada)


# declare a class and give it name Shoe
class Shoe:
    def __init__(self):
        self.brand = "Vans"
        self.type = "Classic Sk8-Hi"
        self.price = 69.99
        self.in_stock = True


skater_shoe = Shoe()
dress_shoe = Shoe()
# Accessing the instance's attributes
print(skater_shoe.type)  # Classic Sk8-Hi
print(dress_shoe.type)  # Classic Sk8-Hi

skater_shoe.type = "Low-top Trainers"
print(skater_shoe.type)
# output: Low-top Trainers
dress_shoe.type = "Ballet Flats"
print(dress_shoe.type)
# output: Ballet Flats


class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
        # we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
# the status is set to True by default
        self.in_stock = True

# Takes a float/percent as an argument and reduces the
# price of the item by that percentage.
    def on_sale_by_percent(self, percent):
        self.price = self.price * (1 - percent)

# Returns a total with tax added to the price.
    def total_with_tax(self, tax_rate):
        tax = self.price * tax_rate
        total = self.price + tax
        return total

# Reduces the price by a fixed dollar amount.
    def cut_price_by(self, amount):
        if amount < self.price:
            self.price -= amount
        else:
            print("Price deduction too large.")


skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
print(skater_shoe.type)  # output: Low-top Trainers
print(dress_shoe.type)  # output: Ballet Flats

print(skater_shoe.price)
skater_shoe.on_sale_by_percent(0.2)
print(skater_shoe.price)
dress_shoe.on_sale_by_percent(0.5)
print(dress_shoe.price)

my_shoe = Shoe("Vans", "ankle-cut", 60.00)
print(my_shoe.total_with_tax(0.08))
my_shoe.cut_price_by(10)
print(my_shoe.price)

# Ninja Challenges!
# Open this code on the Trace website to get a better view of all the variables and their attributes.
# Make a new instance of a shoe
# Update the in_stock attribute to False

# #skater shoes go on sale by 20% reduced price
# skater_shoe.price = skater_shoe.price * (1 - 0.2)
# #dress shoes go on sale by 10% reduced price
# dress_shoe.price =dress_shoe.price * (1 - 0.1)
# #skater shoes go on sale AGAIN by another 10%
# skater_shoe.price = skater_shoe.price * (1 - 0.1)


class User:
    # ! Class Attribute
    population = 0
    # ! CONSTRUCTOR FUNCTION!!!  CREATES THE INSTANCE OF AN OBJECT
    # first parameter always refers to self but can be names anything

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        User.population += 1

    def greeting(self):
        print(f"Hello my name is {self.first_name}!")

# decorator
    @classmethod
    def user_population(cls):  # cls is the repersentation of the class not instance
        print(f"{cls.population} users in the program.")

    @classmethod
    def get_random_user(cls):
        list_of_names = ["alice", "bob", "charlie"]
        return cls(list_of_names[random.randint(0, len(list_of_names))], "Johnson", random.randint(13, 100))

    @staticmethod
    def validate_age(age):
        is_valid = True
        if age < 18:
            is_valid = False
        return is_valid


print
carlos = User("Carlos", "Osornio", 30)
aidee = User("Aidee", "Aguilar", 26)
kai = User("Kai", "Osornio", 1)
carlos.greeting()

User.user_population()
User.get_random_user()

# Lecture OOP in Python

person_1 = {
    'id': 9,
    'name': "David",
    'height': 5.6,
    'gender': "male",
    'money': 35,
    'age': 28
}


class Student:
    quantity_of_students = 0  # class atrribute
    all_students = []  # class atrribute

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.height = data['height']
        self.gender = data['gender']
        self.money = data['money']
        self.age = data['age']
        Student.all_students.append(self)
        Student.quantity_of_students += 1

    def make_money(self, amount):
        self.money += amount
        print(f'{self.name} added ${amount} dollars and now has ${self.money} dollars.')

    @classmethod
    def recession(cls):
        for student in cls.all_students:
            student.money *= .9
            print(
                f'{student.name} now has ${student.money} dollars due to recession.')


person_1 = Student(person_1)
# print(Student.all_students, Student.quantity_of_students)
Student.recession()

# chaining methods always have to return something, retrurn self
Student.all_students[0].make_money(50)

# Association methods


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)  # added this line


class User:
    def example_method(self):
        # we can call the BankAccount instance's methods
        self.account.deposit(100)
        # or access its attributes
        print(self.account.balance)

    # def __repr__(self):
    #     return "Player: {}, {} y/o, pos: {}, team: {}".format(self.name, self.age, self.position, self.team)
    # # __repr__(self) is a python system method that
    # tells python how to handle representing that class
    # when, for example the object is printed to the terminal.

# Ex 1 of Inheritance


# class RetirementAccount(BankAccount):
#     def __init__(self, int_rate, is_roth, balance=0):
#         self.int_rate = int_rate
#         self.balance = balance
#         self.is_roth = is_roth


# class BankAccount:
#     def __init__(self, int_rate, balance=0):
#         self.int_rate = int_rate
#         self.balance = balance

# better to do


# class RetirementAccount(BankAccount):
#     def __init__(self, int_rate, is_roth, balance=0):
#         super().__init__(int_rate, balance)
#         self.is_roth = is_roth


class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

# Ex 2


# class RetirementAccount(BankAccount):
#     def withdraw(self, amount, is_early):
#         if is_early:
#             amount = amount * 1.10
#         if (self.balance - amount) > 0:
#             self.balance -= amount
#         else:
#             print("INSUFFICIENT FUNDS")
#         return self


# class BankAccount:
#     def withdraw(self, amount):
#         if (self.balance - amount) > 0:
#             self.balance -= amount
#         else:
#             print("INSUFFICIENT FUNDS")
#         return self

# better to do


class RetirementAccount(BankAccount):
    def withdraw(self, amount, is_early):
        if is_early:
            amount = amount * 1.10
        super().withdraw(amount)
        return self


class BankAccount:
    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("INSUFFICIENT FUNDS")
        return self


class Parent:
    def method_a(self):
        print("invoking PARENT method_a!")


class Child(Parent):
    def method_a(self):
        print("invoking CHILD method_a!")


dad = Parent()
son = Child()
dad.method_a()
son.method_a()  # notice this overrides the Parent method!

# input takes a prompt, which needs to be a string
favorite_color = input('What is your favorite color? ')
# output, prints the color given to the console
print(f'Your favorite color is: {favorite_color}')

# Singly Linked Node


class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class SList:
    def __init__(self):
        self.head = None
# Just as we would pass in a value to a Python list's append method, our add_to_front method should accept a value to be added to the list:

    def add_to_front(self, val):
        # Create a node with the given value, with the SLNode
        new_node = SLNode(val)
        # Set the new node's next to be the current head
        new_node.next = self.head
        # Set the list's head to the new node
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head  # pointer to the list's first node
        while (runner != None):  # iterating while runner is a node and not None
            print(runner.value)
            runner = runner.next  # set the runner to its neighbor
        return self    # once the loop is done, allow for chaining

    def add_to_back(self, val):  # accepts a value
        if self.head == None:   # if the list is empty
            self.add_to_front(val)  # run the add_to_front method
            return self  # lets make sure the rest of this function doesnt happen if we add to the front
        # create a new instance of our Node class with the given value
        new_node = SLNode(val)
        runner = self.head  # set an iterator to start at the front of the list
        while (runner.next != None):  # iterator until the iterator doesnt have a neighbor
            runner = runner.next  # increment the runner to the next node in the list
        runner.next = new_node  # increament the runner to the next node in the list
        return self  # chaining

# my_list = SList()
# my_list.add_to_front("Jim")
# my_list.add_to_front("Dwight")
# my_list.add_to_front("Andy")
# my_list.print_values()


my_list = SList()  # create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back(
    "fun!").print_values()          # chaining, yeah!
# output should be:
# Linked lists
# are
# fun!

# Anonymous functions


def square(num):
    x = num ** 2
    return x


# Python code to Demonstrate the Exponential Operactor
a = 2
b = 5
# using double asterisk operator
c = a**b
print(c)
# using double asterisk operator
z = 2 * (4 ** 2) + 3 * (4 ** 2 - 10)
print(z)

lambda num: num ** 2
lambda num1, num2: num1+num2

# create a new list, with a lambda as an element
my_list = ['test_string', 99, lambda x: x ** 2]
# access the value in the list
print(my_list[2])  # will print a lambda object stored in memory
# invoke the lambda function, passing in 5 as the argument
print(my_list[2](5))

# define a function that takes one input that is a function


def invoker(callback):
# invoke the input pass the argument 2
    print(callback(2))


invoker(lambda x: 2 * x)
invoker(lambda y: 5 + y)

add10 = lambda x: x + 10  # store lambda expression in a variable
add10(2)  # returns 12
add10(98)  # returns 108


def incrementor(num):
    start = num
    return lambda x: num + x


# create a list
my_arr = [1, 2, 3, 4, 5]
# define a function that squares values


def square(num):
    return num ** 2


# invoke map function
print(map(square, my_arr))
print(list(map(square, my_arr)))
print(list(map(lambda num: num ** 2, my_arr)))

my_arr = [1, 2, 3, 4, 5]
# invoke map, pass in a lambda as the first argument
print(list(map(lambda x: x ** 2, my_arr)))

my_list = [99, 4, 2, 5, -3]
my_tuple = (99, 4, 2, 5, -3)
my_str = "sequoia"
print(my_list[:])
# output: [99,4,2,5,-3]
print(my_tuple[1:])
# output: (4,2,5,-3)
print(my_str[:3])
# output: "seq"
print(my_tuple[2:4])
# output: (2,5)
print(my_list, my_tuple, my_str)
# output: [99,4,2,5,-3] (99,4,2,5,-3) 'sequoia' -- note the original values have not changed

# Other Built-In Sequence Methods

# Here are a few commonly used built-in functions for sequences:

# max(sequence) returns the largest value in the sequence
# sum(sequence) returns the sum of all values in sequence
# map(function, sequence) applies the function to every item in the sequence you pass in. Returns a list of the results.
# min(sequence) returns the lowest value in a sequence.
# sorted(sequence) returns a sorted list of the sequence's values

my_list = [99, 4, 2, 5, -3]
my_tuple = (99, 4, 2, 5, -3)
my_str = "sequoia"
print(my_list[:])
# output: [99,4,2,5,-3]
print(my_tuple[1:])
# output: (4,2,5,-3)
print(my_str[:3])
# output: "seq"
print(my_tuple[2:4])
# output: (2,5)
print(my_list, my_tuple, my_str)
# output: [99,4,2,5,-3] (99,4,2,5,-3) 'sequoia' -- note the original values have not changed


def map(list, function):
    for i in range(len(list)):
        list[i] = function(list[i])
    return list


print(map([1, 2, 3, 4], (lambda num: num*num)))
print(map([1, 2, 3, 4], (lambda num: num*3)))
print(map([1, 2, 3, 4], (lambda num: num % 2)))

# import the python testing framework
import unittest
# our "unit"
# this is what we are running our test on


def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False
# our "unit tests"
# initialized by creating a class that inherits from unittest.TestCase


class IsEvenTests(unittest.TestCase):
    # each method in this class is a test to be run
    def testTwo(self):
        self.assertEqual(isEven(2), True)
        # another way to write above is
        self.assertTrue(isEven(2))
    def testThree(self):
        self.assertEqual(isEven(3), False)
        # another way to write above is
        self.assertFalse(isEven(3))
        # any task you want run before any method above is executed, put them in the setUp method
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
    # add the tearDown tasks
        print("running tearDown tasks")
if __name__ == '__main__':
    unittest.main() # this runs our tests

class Post: 
    def __init__(self, user, content):
        self.user = user
        self.content = content

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.posts = [] 

#User should have a method to create a post and add the newest post to the list of posts

    def create_post(self, content):
        self.posts.append(Post(self, content))
        return self

#User should have a method to edit the post 

    def edit_post(self, post_id, content):
        self.posts[post_id].content = content
        return self

#User should have a method to delete the post

    def delete_post(self, post_id):
        if self.posts[post_id] == None:
            print(f'Whoops, there is nothing in this index')
        else:
            self.posts[post_id] = None
        return self

#User should have a method to print all of their posts

    def print_all_posts(self):
        for post in self.posts:
            print(post.content)

user1 = User("Carlos", "coso@gmail.com")
user1.create_post("Hello World").create_post("Second Post").print_all_posts()
user1.edit_post(1, "Edited Post").print_all_posts()
user1.delete_post(1).delete_post(1)

class Car: 
    def __init__(self, year, make, model, type, color, mileage=0, fuel=0):
        self.year = year
        self.make = make
        self.model = model
        self.type = type
        self.color = color
        self.mileage = mileage
        self.fuel = fuel

    def __repr__(self):
        return f"This car is a {self.color} {self.year} {self.make} {self.model} {self.type} with {self.mileage} miles and {self.fuel} gallons of fuel"

    def fill_tank(self, amount=100):
        if self.fuel == 100:
            print("Tank is full")
        elif self.fuel + amount > 100:
            self.fuel = 100
        else:
            self.fuel += amount
        return self

    def drive(self):
        if self.fuel > 10:
            self.fuel -= 10 
            self.mileage += 10
        else: 
            print(f"Sorry get some fuel!")
        return self

    def paint_job(self, color):
        self.color = color
        return self

car1 = Car(2016, "Toyota", "FR-S", "Standard", "silver")
car2 = Car(2016, "Mercedes", "GLA-250", "4-matic", "dark gray")

print(car1)
car1.paint_job("blue").fill_tank()
print(car1)

car1.drive().drive().drive().drive()
print(car1)
car1.fill_tank(20)
print(car1)

# from flask import Flask, render_template  # added render_template!
# app = Flask(__name__)                     
    
# @app.route('/')                           
# def hello_world():
#     # Instead of returning a string, 
#     # we'll return the result of the render_template method, passing in the name of our HTML file
#     return render_template('index.html')  


# if __name__=="__main__":
#     app.run(debug=True)    

from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/home')
def home():
    return "Hello this is the main page <h1>HELLO</h1>"

@app.route('/users/<string:username>/<int:id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + str(id)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * 
        FROM users
        WHERE id = %(id)s 
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        user = cls(row)
        return user

#CREATE
    @classmethod
    def create_user(cls, data):
        query = """
        INSERT INTO users(first_name, last_name, email, age)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(age)s)
        ; """
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO users(first_name, last_name, email, age)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(age)s)
        ; """
        user_id = connectToMySQL(cls.db).query_db(query, data)
        return user_id


#UPDATE
    @classmethod
    def update(cls, data):
        query = """
        UPDATE users 
        SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, age = %(age)s
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.db).query_db( query, data )

#DELETE
    @classmethod
    def delete(cls, data):
        query = """
        DELETE FROM users
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.db).query_db(query, data)

from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import User

#CREATE
@app.route('/users/create', methods=['POST'])
def create_user():
    User.save(request.form)
    return redirect('/')

#READ
@app.route('/users/<int:id>')
def show_user(id):
    data = {
        "id": id
    }
    return render_template('show_user.html', user = User.get_one(data))

@app.route('/')
def dashboard():
    return render_template('dashboard.html', users = User.get_all())

@app.route('/users/<int:id>/edit')
def show_edit_form(id):
    data = {
        "id": id
    }
    return render_template('edit_user.html', user = User.get_one(data))

@app.route('/users/<int:id>/delete')
def show_delete_form(id):
    data = {
        "id": id
    }
    return render_template('delete_user.html', user = User.get_one(data))

#UPDATE
@app.route('/users/<int:id>/update', methods=['POST'])
def update_user(id):
    User.update(request.form)
    return redirect('/')

#DELETE
@app.route('/users/<int:id>/destroy')
def delete_user(id):
    User.delete(request.form)
    return redirect('/')