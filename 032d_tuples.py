# unpacking a tuple
def exponent(base, power):
    return base ** power


def find_product(*args):
    product = 1
    for num in args:
        product = product * num
    return product


my_powers_tup = (2, 5)

print(exponent(*my_powers_tup))

my_nums_tup = (1, 2, 3, 4, 5)

print(find_product(*my_nums_tup))
