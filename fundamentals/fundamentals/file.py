"""
RECOGNIZE PYTHON ASSIGNMENT
"""


# this is a single line comment
"""
This is
a multiline
comment
"""

num1 = 42 # - variable declaration, number initialized
num2 = 2.3 # - variable declaration, decimal/float initialized
boolean = True # - variable declaration, boolean initialized
string = 'Hello World' # - variable declaration, string initialized

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, list initialized
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # - variable declaration, Boolean, Numbers, Strings, dictionary, initialize
fruit = ('blueberry', 'strawberry', 'banana')# - variable declaration, Strings, tuples, initialize
print(type(fruit))# - log statement, type check 
print(pizza_toppings[1]) # - log statement, List, access value 
pizza_toppings.append('Mushrooms')  #  - Strings, Lists, add value, 
print(person['name'])# - log statement, Strings, lists, access value,
person['name'] = 'George' # - variable declaration, Strings, dictionary, change value
person['eye_color'] = 'blue' # - variable declaration, Strings, dictionary, change value
print(fruit[2])# - log statement, list, access value,

if num1 > 45: # - conditional, if 
    print("It's greater")# - log statement, Strings
else: # - conditional, else 
    print("It's lower")# - log statement, Strings

if len(string) < 5:  # - conditional, if
    print("It's a short word!")# - log statement, Strings
elif len(string) > 15:  # -  Numbers, conditional, else if
    print("It's a long word!")# - log statement, Strings
else:    # - conditional, else 
    print("Just right!") # - log statement, Strings

for x in range(5):   # - length check, for loop, start, stop
    print(x) # - log statement
for x in range(2,5):  # - length check, for loop, start, stop
    print(x)# - log statement
for x in range(2,10,3):  # - length check, for loop, start, stop, increment 
    print(x)# - log statement
x = 0 # - variable declaration, Numbers
while(x < 5):  #  - while loop, start, stop
    print(x)# - log statement
    x += 1   # - increment 

pizza_toppings.pop() # - list, delete value
pizza_toppings.pop(1) # - list, delete value
print(person)# - log statement
person.pop('eye_color') # - dictionary, delete value
print(person) # - log statement, dictionary, access value

for topping in pizza_toppings:  # - for loop, start
    if topping == 'Pepperoni':     # -  Strings, if
        continue  # - continue
    print('After 1st if statement') # - log statement, Strings
    if topping == 'Olives':   # - Strings, if
        break # - break 

def print_hello_ten_times(): # -  function, 
    for num in range(10):  # - length check, for loop, start, stop
        print('Hello') # - log statement, Strings

print_hello_ten_times() # - function

def print_hello_x_times(x): # - function, parameter
    for num in range(x):  # - length check, for loop, start, stop, parameter
        print('Hello') # - log statement, Strings

print_hello_x_times(4) # - function, argument

def print_hello_x_or_ten_times(x = 10): # -  Numbers, function, parameter
    for num in range(x):  # - length check, for loop, start, end, parameter
        print('Hello') # - log statement, Strings

print_hello_x_or_ten_times() # - function
print_hello_x_or_ten_times(4) # - function, argument


"""
Bonus section  - multiline comment
"""

print(num3) # - log statement, NameError: name <variable name> is not defined
num3 = 72 # - variable declaration, Numbers
fruit[0] = 'cranberry' # - variable declaration, Strings, list, initialize
print(person['favorite_team']) # - log statement, Strings, dictionary, access value
print(pizza_toppings[7]) # - log statement, list, access value,
print(boolean) # - log statement, Boolean
fruit.append('raspberry') # - Strings, AttributeError: 'tuple' object has no attribute 'append'
fruit.pop(1) # - AttributeError: 'tuple' object has no attribute 'pop'

num1 = 42 # variable declaration, number initialized
num2 = 2.3 # variable declaration, decimal/float initialized
boolean = True # variable declaration, boolean initialized
string = 'Hello World' # variable declaration, string initialized

# variable declaration, list initialized
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

# variable declaration, dictionary initialized
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

# variable declaration, tuple initialized
fruit = ('blueberry', 'strawberry', 'banana')
# print to console, type check
print(type(fruit))

# print to console, List access value
print(pizza_toppings[1])

#list add value
pizza_toppings.append('Mushrooms')

# print to console, Dictionary access value
print(person['name'])

# Dictionary change value
person['name'] = 'George'
# Dictionary change value
person['eye_color'] = 'blue'

# print to console, Tuple access data
print(fruit[2])

# Conditional if, evaluation, print to console, Conditional else, print to console
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

# Conditional if - elif - else, print to console.
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# For Loop start at 0 and goes up to until 5
for x in range(5):
    print(x)
# For Loop start at 2 and goes up to until 5
for x in range(2,5):
    print(x)
# For loop start at 2 goes up to until 10, increments by 3
for x in range(2,10,3):
    print(x)

#While Loop, variblae declaration
x = 0
while(x < 5):
    # printing to console
    print(x)
    # incrementing x
    x += 1

# List delete value at end
pizza_toppings.pop()
# list delete value at index
pizza_toppings.pop(1)

# print to console of dictionary
print(person)
# Dictionary delete value
person.pop('eye_color')
#print to console of dictionary
print(person)

# for loop through a list
for topping in pizza_toppings:
    #Conditional if
    if topping == 'Pepperoni':
        # Conintues
        continue
    # print to console
    print('After 1st if statement')
    # Conditional if
    if topping == 'Olives':
        # stops the loop
        break

# function declaration
def print_hello_ten_times():
    # for loop starts at 0 goes up until 10
    for num in range(10):
        # print to console
        print('Hello')

# Function Call
print_hello_ten_times()

# function Declaration with parameter x
def print_hello_x_times(x):
    # For loop up until a given number x
    for num in range(x):
        # print to console
        print('Hello')

# function call arguement of 4
print_hello_x_times(4)

# function declaration with default parameter
def print_hello_x_or_ten_times(x = 10):
    # For loop until x
    for num in range(x):
        # print to console
        print('Hello')

# Function call goes to 10
print_hello_x_or_ten_times()
# function call goes to 4
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
