bill = float(input("How much was bill?  "))
level = input("Level of service? good, fair, or bad: ")
level_lower = level.lower()
amount_of_people = int(input("Split how many ways? "))

if level_lower == "good":
    tip = (bill * 0.20)
elif level_lower == "fair":
    tip = (bill * 0.15)
elif level_lower == "bad":
    tip = (bill * 0.10)
else:
    print("error")


total = (bill + tip)
per_person = (total/amount_of_people)

print("Bill amount is " + str(bill))
print("Level of service was " + level_lower)
print("Tip Amount: " + str(tip))
print("Total Amount: " + str(total))
print("Amount per person: " + str(per_person))
