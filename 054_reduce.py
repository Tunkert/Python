# find the sum of a list using reduce
# import reduce
from functools import reduce


def sum(x, y):
    return x + y


# other syntax
def accumulator(x, y):
    return x - y


def multiplier(acc, item):
    return acc * item


nums = [1, 2, 3, 4, 5]
print(reduce(sum, nums))
print(reduce(accumulator, nums))
print(reduce(multiplier, nums))

# reduce accepts two arguments in the function - the accumulator (x) and the item (y)
