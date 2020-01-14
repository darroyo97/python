# A conditional statement tells a program to execute different actions
# depending on whether a condition is True or False.
# -Conditional Operators
# -Logical Operators
# -the keywords “if, elif, else.”

# Comparison Operators

# Equal to: ==
# Not equal to: !=
# Less than: <
# Greater than: >
# Less than or equal to: <=
# Greater than or equal to: >=

# Logical Operators

# 'and' operator – returns True if both the operands (right side and left side) are True
# 'or' operator - returns True if either of the operand (right side or left side) is True
# 'not' operator - returns True if operand is False
# Examples
# print(not ("testing" == "testing" and "Zed" == "Cool Guy"))
# print(1 == 1 and (not ("testing" == 1 or 1 == 0)))
# print("chunky" == "bacon" and (not (3 == 4 or 3 == 3)))
# print(3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")))


# if statement

# age = 21
# name = "Sunny"

# if (age == 21):
#     print("Whats good lil ma!")

# if (age <= 21):
#     print("No No No")


# name = input("Enter your name: ")

# if (name == "Sunny"):
#     print(name)


# if else statement
# if condition:
#   write statement here
# else:
#   write statement here

# age = int(input("Enter age:"))

# if age >= 21:
#     print("You get free beer")
# else:
#     print("Sorry no beer for you")

# elif statement
# if condition :
#   write statement here
# elif condition 2:
#   write statement here
# else:
#   write statement here

# age = int(input("Enter age:"))
# if age >= 21:
#     print("You get free beer")
# elif age <= 18:
#     print("What are you even doing here?")
# else:
#     print("Sorry no beer for you")


name_of_user = input("What is your name ?")
length_of_name = len(name_of_user)

if length_of_name > 0:
    name_of_friend = input("What is your friend's name?")
    greeting = f'Hello {name_of_user}, its very nice to meet you and your friend{name_of_friend}'
    print(greeting)
else:
    print("Ok ill ask again some other time")
