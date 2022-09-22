def square_number(num):
    """This function squares the number passed into it"""
    return num * num


def exponent(base, power):
    """This function takes in a base number and a power, and raises the base to the power"""
    return base ** power


print(square_number(3))  # 9
print(exponent(2, 3))  # 8

"""
In the exponent function, base and power are the parameters of the function.
The arguments 2 and 3 are passed into the function.
parameter = name in function definition
argument = what's passed in during the function call.
"""