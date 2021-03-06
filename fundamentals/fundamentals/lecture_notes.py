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

mylist = [{"name": 'Charlie', "age": 30, 'email': 'charlie@gmail.com'}, {"name": 'Stephen',"age": 31, 'email': 'stephen@gmail.com'}, {"name": 'Alex', "age": 27, 'email': 'alex@gmail.com'}]

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
#   What prints to the terminal?
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

    @staticmethod
    def validate_age(age):
        is_valid = True
        if age < 18:
            is_valid = False
        return is_valid


carlos = User("Carlos", "Osornio", 30)
aidee = User("Aidee", "Aguilar", 26)
kai = User("Kai", "Osornio", 1)
carlos.greeting()

User.user_population()

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
            print(f'{student.name} now has ${student.money} dollars due to recession.')


person_1 = Student(person_1)
# print(Student.all_students, Student.quantity_of_students)
Student.recession()

#chaining methods always have to return something
Student.all_students[0].make_money(50)
