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


def add(num1, num2):
    print(num1 + num2)


add(2, 5)
# print(num1)
# we  cannot acces this, error because that store in our local memory
