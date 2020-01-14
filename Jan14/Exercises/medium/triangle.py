# _ unused variable


def triangle(n):
    k = 2*n - 2
    for i in range(0, n):
        for _ in range(0, k):
            print(end=" ")
        k = k - 1
        for _ in range(0, i+1):
            print("* ", end="")
        print("\r")


n = 5
triangle(n)
