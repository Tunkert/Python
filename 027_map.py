def square_nums(num):
    return num * num


my_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = map(square_nums, my_nums)

for square in squares:
    print(square)
