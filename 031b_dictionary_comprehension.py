nums_str = [f'{x}' for x in range(1, 101)]
nums = [x for x in range(1, 101)]

print(nums_str)
print(nums)

nums_dict = dict(zip(nums_str, nums))

print(nums_dict)

fizz_dict = {k:"fizz" if v % 3 == 0 else v for k, v in nums_dict.items()}

print(fizz_dict)
