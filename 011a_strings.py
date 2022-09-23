# noinspection PyInterpreter
my_str = "This is my string"

# Find the length of a string
print(len(my_str))  # 17 - includes spaces

# Print the first character
print(my_str[0])  # prints 'T'

# Print the last character
print(my_str[-1])  # prints 'g'

# Strings are immutable - you can't change them once created so ... TypeError
# my_str[0] = "G"
# will throw an error
