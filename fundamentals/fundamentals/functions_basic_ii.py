#  Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
newlist = []
def countdown(number):
    for i in range(number, -1, -1):
        newlist.append(i)
    return newlist
print(countdown(5))

# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
def print_and_return(mylist):
    print(mylist[0])
    return(mylist[1])
print(print_and_return([1,2])) 

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def first_plus_length(list):
    return list[0] + len(list)
print(first_plus_length([1,2,3,4,5]))

# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False

def values_greater_than_second(list2):
    if len(list2) < 2:
        return False
    list3 = []
    for i in list2:
        if (i > list2[1]):
            list3.append(i)
    print(len(list3))
    return list3
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def length_and_value(size, value):
    list4 = []
    for i in range (size):
        list4.append(value)
    return list4
print(length_and_value(4,7))
print(length_and_value(6,2))
