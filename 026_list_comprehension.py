to_100 = [x for x in range(1, 101)]

# for num in to_100:
#     print(num)

# fizz_list = [x for x in to_100 if x % 3 == 0]
#
# for fizzy in fizz_list:
#     print(fizzy)

fizz_else_list = ["fizz" if x % 3 == 0 else x for x in to_100]

print(fizz_else_list)
