# todos = ["cook breakfest", "feed dogs", "put gas",
#          "shop for groceries", "go to school"]
# print(todos)

# todos.append("take a nap")
# todos.append("workout")
# print(todos)


# This while loop allows to show it as a list with number
# index = 0
# while index < len(todos):
#     #print(f'{index}: {todos[index]}')
#     print(f'{index + 1 }: {todos[index]}')
#     index += 1


# alternative you can use the concatenation to combine two list like append +
# todos = ["cook breakfest", "feed dogs", "put gas",
#          "shop for groceries", "go to school"]
# # print(todos)

# todos = todos + ["take a nap", "go to sleep "]
# print(todos)


# Extend() Method

todos = ["pet the cat", "go to work",
         "shop for groceries", "go home", "feed the cat"]

todos.extend(["binge watch a show", "go to sleep"])

print(todos)
