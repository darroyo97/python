cel = float(input("Type celsius: "))


def conv(cel):
    far = (cel * 9 / 5) + 32
    return far


far = conv(cel)
print(far)
