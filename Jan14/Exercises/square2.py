size = int(input("How big is the square? "))

# for i in range(size):
#     for i in range(size):
#         print("*", end=" ")
#     print()

i = 0
while (i < size):
    x = 0
    while (x < size):
        x = x + 1
        print("*", end=" ")
    i = i + 1
    print(" ")
