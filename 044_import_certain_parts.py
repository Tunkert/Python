import my_module
from my_module import cube

print(f"The cube of 4 is {cube(4)}.")  # notice we can just call it without pre-pending my_module

print(f"The square of 9 is {my_module.square(9)}.")  # to get this to work we need to import my_module
# pycharm does this for me but without there would be an error.
