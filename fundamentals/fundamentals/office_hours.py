# Write a function that takes a list of numbers and returns the sum 

my_list = [1,2,3,4,5,6,7,8,9]

def sum_list(list):
    sum = 0
    if not list:  # validation of the input
        return sum
    for number in list:
        sum += number
    return sum

print(sum_list([1,2,3,4,5]))
print(sum_list(my_list))
print(sum_list(None))


