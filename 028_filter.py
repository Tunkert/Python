import math

def is_perfect_square(num):
    if math.sqrt(num) == int(math.sqrt(num)):
        return True
    else:
        return False

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

perfect_squares = filter(is_perfect_square, nums)

print(list(perfect_squares))
