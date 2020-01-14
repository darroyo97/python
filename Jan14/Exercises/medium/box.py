def print_box(w, h):
    for i in range(1, w+1):
        for j in range(1, h+1):
            if (i == 1 or i == w or
                    j == 1 or j == h):
                print("*", end="")
            else:
                print(" ", end="")

        print()


width = int(input("Width? "))
height = int(input("Height? "))
print_box(width, height)
