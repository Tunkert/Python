nums = [*range(1, 101)]  # unpack a range from 1 to 100 to make a list

print(list(filter(lambda x: x % 3 == 0, nums)))
