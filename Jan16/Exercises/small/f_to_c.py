far = float(input("Type celsius: "))


def conv(far):
    cal = (far - 32) * 5/9
    return cal


cal = conv(far)
print(cal)
