name = input("What is your name? ")
mood = input("how you feeling from a scale from 1-10")
user_mood = int(mood)
if user_mood >= 5:
    greeting = f'{name} is feeling great '
    print(greeting)
elif user_mood < 5:
    greeting = f'{name} oh no sorry to hear that'
    print(greeting)
else:
    print("ill ask again later")
# code breaks at else statement
# Traceback (most recent call last):
#   File "my_refactor.py", line 2, in <module>
#     mood = int(input("how you feeling from a scale from 1-10"))
# ValueError: invalid literal for int() with base 10: ''
