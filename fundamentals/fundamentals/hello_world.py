# 1. TASK: print "Hello World"
print('Hello World')
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle!"
print("Hello", name)  # with a comma
print("Hello " + name)  # with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello", name)  # with a comma
print("Hello " + str(name))  # with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(
    fave_food1, fave_food2))  # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.")  # with an f string
# 5 Store your name in a variable, and then use it to print the string “Hello {{your name}}!” using a comma in the print function (#2a)
name = "Charlie"
print("Hello", name)
# 6 Store your name in a variable, and then use it to print the string “Hello {{your name}}!” using a + in the print function (#2b)
name = "Charlie"
print("Hello " + name)
# 7 Store your favorite number in a variable, and then use it to print the string “Hello {{num}}!” using a comma in the print function (#3a)
fav_numb = 26
print("Hello", fav_numb)
# 8 Store your favorite number in a variable, and then use it to print the string “Hello {{num}}!” using a + in the print function (#3b)
fav_numb = 26
print("Hello " + str(fav_numb))
# NINJA BONUS: Figure out how to resolve the error from above, without changing the + sign to a comma
print("Hello " + str(name))
# Store 2 of your favorite foods in variables, and then use them to print the string “I love to eat {{food_one}} and {{food_two}}.” with the format method (#4a)
fav_food1 = "mexican"
fav_food2 = "pizza"
print("I love to eat {} and {}.".format(
    fav_food1, fav_food2))  # with .format()
# Store 2 of your favorite foods in variables, and then use them to print the string “I love to eat {{food_one}} and {{food_two}}.” with f-strings (#4b)
print(f"I love to eat {fav_food1} and {fav_food2}.")
