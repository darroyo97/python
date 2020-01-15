todos = []
user_add = input("add a task: ")

while user_add != "":
    todos.append(user_add)
    print(todos)
    break
else:
    print("bye")
