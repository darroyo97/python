bill = int(input("How much was bill?  "))
level = input("Level of service? good, fair, or bad: ")
level_lower = level.lower()

if level_lower == "good":
    tip = (bill * 0.20)
    total = (bill + tip)
elif level_lower == "fair":
    tip = (bill * 0.15)
    total = (bill + tip)
elif level_lower == "bad":
    tip = (bill * 0.10)
    total = (bill + tip)
else:
    print("error")

print("Bill amount is " + str(bill))
print("Level of service was " + level_lower)
print("Tip Amount: " + str(tip))
print("Total Amount: " + str(total))
