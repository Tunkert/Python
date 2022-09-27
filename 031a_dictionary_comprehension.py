nums_str = ['1', '2', '3', '4', '5']
nums = [1, 2, 3, 4, 5]

nums_dict = dict(zip(nums_str, nums))

print(nums_dict)

cubes_dict = {k:v ** 3 for (k, v) in nums_dict.items()}

print(cubes_dict)
