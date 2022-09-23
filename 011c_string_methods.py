# string slicing
my_str = "This is my string"

# make a slice of the string to print string
# [start:stop:step]
my_slice = my_str[11::]

# print out the slice
print(my_slice)

# print out original string
print(my_str)  # note the slice does not persist

# reverse string with the slice and print to the console
print(my_str[::-1])

# jump every step - print
print(my_str[::2])

# play with slicing and see what you can do!
