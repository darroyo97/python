# # type()
# # returns a method of class type
# num = type(5)
# print(num)

# dec = type(3.4)
# print(dec)

# is_raining = False

# bool = type(is_raining)
# print(bool)


# # isinstance()
# # The isinstance() function returns True if the specified object is of the specified type, otherwise False.

# check = isinstance(5, int)
# check2 = isinstance(5, str)
# print(check2)


# # print()
# # The print command causes output to appear on your terminal screen.
# print('This prints on console')


# # input()
# # Python also has a feature which lets you interact with the outside world to get input.
# # The input() function waits for the user to type some input and press return. It then gets whatever was typed.

# userName = input("Whats is your name?")
# output = f'Hello {userName}'
# dataType = type(userName)

# print(dataType)


# int()
input_user_age = input("How old are you?")
print(type(input_user_age))

casted_output = int(input_user_age)
print(type(casted_output))

some_math = casted_output * 7
print(some_math)

# Math functions
