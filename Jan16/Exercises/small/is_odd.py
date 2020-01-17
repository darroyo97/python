number = int(input("Pick a whole number"))


def even_check(number):
    if (number % 2) == 0:
        return True
    else:
        return False


def odd_check():
    if even_check(number) is not True:
        return True
    else:
        return False


print(odd_check())
