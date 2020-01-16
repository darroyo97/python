# Functions

# def is the keyword for a function


# Structure of a function
# def nameoffunction(paramater or paramaters):
# body

# def greeting():
#     print("Hello World")


# # if you run this it does not run anything,
# # you must call the function
# greeting()

# print("Day 1: Students in SRE class")
# print("lecture: git 101")
# print("Shu")
# print("Thomas")
# print("Gustavo")
# print("Alim")
# print("Day 2: Students in SRE class")
# print("lecture: git 102")
# print("Shu")
# print("Thomas")
# print("Gustavo")
# print("Alim")
# print("Day 3: Students in SRE class")
# print("lecture: python 101")
# print("Shu")
# print("Thomas")
# print("Gustavo")
# print("Alim")


# not functanial beacause we could get a mistake if we change a name we woudl have to
# change it in every single line when we could just make the name into a function

# def names():
#     print("Shu Pei")
#     print("Thomas")
#     print("Gustavo Fette")
#     print("Alim")

# print("Day 1: Students in SRE class")
# print("lecture: git 101")
# names()
# print("Day 2: Students in SRE class")
# print("lecture: git 102")
# names()
# print("Day 3: Students in SRE class")
# print("lecture: python 101")
# names()

# we cam put a loop inside a fucntion

# def myFunction():
#     for i in range(10):
#         print('Hi')


# myFunction()

# def getGroceries():
#     print('milk')
#     print('flour')
#     print('sugar')
#     print('butter')
#     print()


# getGroceries()
# getGroceries()
# getGroceries()


# Nested Functions

# def separateRuns():
#     print('******************')
#     print()


# def getGroceries():
#     print('milk')
#     print('flour')
#     print('sugar')
#     print('butter')
#     separateRuns()


# getGroceries()
# getGroceries()

# Calling a function with parameters
# Receiving data in a user-defined function: parameters

# A parameter is a variable that an argument is stored in when a function is called.

# def funcName(parameters):

# indented block of code

# def greeting(person):
#     print(f'Hello {person}')


# greeting("Kazim")

# The argument replaces the value of the param in the function


# def add(num1, num2):
#     # print(num1 + num2)
#     return (num1 + num2)
#     # example for showing result is important


# # add(2, 5)
# # print(num1)
# # we  cannot acces this, error because that store in our local memory

# result = add(2, 5)
# print(result)
# # this would not work because result had no value we going to need a return
# # we get nothing (line 117) with no return

# showing how important the order of an argument is
# def make_formal_greeting(name, title):
#     return f"This is {name}, the {title}!"


# result = make_formal_greeting("Rob Stark", "King in the North")
# print(result)
# oops = make_formal_greeting("King in the North", "Rob Stark")
# print(oops)


# def concat(list1, list2):
#     conca = list1 + list2
#     return conca


# c_result = concat([1, 2, 3], [4, 5, 6])

# print(c_result)

# def cal_avg(num1, num2, num3, num4):
#     sum = num1 + num2 + num3 + num4
#     avg = sum / 4
#     return avg


# # result = cal_avg(4, 6, 9, 0)
# # print(result)
# # or
# print(cal_avg(4, 6, 9, 0))


# user_input = input(
#     "Please provide a list of numbers seprated ny a comma: example. 1,2,3,4:  ")
# https://stackoverflow.com/questions/29358402/python-turning-user-input-into-a-list

# def avg(user_list):
#     return sum(user_list) / len(user_list)


# # found this code on stackoverflow to use user input
# # user_list = list(map(float, user_input.split(',')))
# user_list = [1, 2, 3, 4]
# average = avg(user_list)
# print(average)
