def square(num=3):
    """This function squares a number passed into it, if nothing is passed in it squares 3."""
    return num * num


print(square())  # 9
print(square(4))  # 16


def exponent(base=2, power=3):
    """This function takes in a base and a power and returns an exponent result. If nothing is passed in it raises 2 to
    the 3rd power"""
    return base ** power


print(exponent())  # 8
print(exponent(4, 3))  # 64
