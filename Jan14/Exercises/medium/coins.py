total = 0
print("You have " + str(total) + " coins.")
answer = input("Do you want another coin: ")
answer_lower = answer.lower()
if answer_lower == "yes":
    new_answer = (total + 1)
    print("You have " + str(new_answer) + " coins.")
elif answer_lower == "no":
    print("Bye")
