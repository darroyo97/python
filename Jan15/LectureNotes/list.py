# List a value that contains multiple values in an ordered sequence

# Lists are zero-based, which means the first index,
# the first element in the list, is considered to be at index 0, not index 1

food = ["pizza", "chicken soup", "tacos", "eggroll", "gorditas", "lasagna"]

print(food[2])

# len()
# get the number of elements

print(len(food))


# Modtify a list, add, remove, replace

# Replace value of tacos into hotpocket
food[2] = "hotpocket"

print(food)

# Append add items, adds to end of the list

food.append("tamales")
print(food)
