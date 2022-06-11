# fruits = ['apple', 'banana', 'orange', 'strawberry']
# vegetables = ['lettuce', 'cucumber', 'carrots']
# fruits_and_vegetables = fruits + vegetables
# print(fruits_and_vegetables)
# salad = 3 * vegetables
# print(salad)

# for count in range(0,5):
#     print("looping =", count)

# countries = ["Uganda", "Chile", "Albania", "Saudi Arabia"]

# # Challenge 1: Fix the range!
# for integer in range(0, len(countries)):
#     print("Index:", integer)
#     # Challenge 2: print the index here
#     print("Country:", countries[integer])
#     # Challenge 3: print the country here

# # Looping over values only...
# for country in countries:
#     print("Country: ", country)
#     # Challenge 4: print the country here

# y = 3
# while y > 0:
#     print(y)
#     y = y - 1
# else:
#     print("Final else statement")

# def add(a, b):
#     x = a + b
#     return x
# sum1 = add(4,6)
# sum2 = add(1,4)
# sum3 = sum1 + sum2
# print(sum3)

# def multiply(num_list,num):
#     for x in num_list:
#         x *= num
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)

# def multiply(num_list,num):
#     for x in range(len(num_list)):
#         num_list[x] *= num
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)
# # output: >>>[10,20,50,80]

# my_dict = {
#     'name': 'Charlie',
#     'age': 30,
#     'stack': 'Python'
# }
# my_dict2 = {
#     'name': 'Carlos',
#     'age': 31,
# }


# print(my_dict)
# my_dict.update(my_dict2)
# print(my_dict)

# my_string = f'{my_dict["name"]} is {my_dict["age"]} years old and is taking {my_dict["stack"]}'
# print(my_string)
# print(my_dict.keys())
# print(my_dict.values())
# for key in my_dict.keys():
#     print(key)

# num = 5
# num2 = 10
# while num <=10:
#     num+= 1
#     print(num)

mylist = [{"name":'Charlie', "age":30, 'email': 'charlie@gmail.com'}, {"name":'Stephen', "age":31, 'email': 'stephen@gmail.com'} , {"name":'Alex', "age":27, 'email': 'alex@gmail.com'}]

for item in mylist:
    print(f"Student's Name: {item['name']}, Age: {item['age']}, Email: {item['email']}\n")

print("hello")

def repeat_phrase(phrase, repeat) : 
    print(phrase * repeat)

repeat_phrase("hello \n", 4)