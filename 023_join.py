# change a nums list back into a single string with spaces in between the numbers
my_nums = [1, 2, 3, 4, 5]

# create empty string arr
my_nums_as_str = []

for num in my_nums:
    my_nums_as_str.append(str(num))

my_str = ' '.join(my_nums_as_str)

print(my_str)
