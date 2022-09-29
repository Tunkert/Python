import my_module

print(f"The name of this file is {__name__}.")

print(f"The name of my module is {my_module.__name__}")

# also we can use my module functions

print(f"3 squared is {my_module.square(3)}.")
print(f"5 cubed is {my_module.cube(5)}.")

# this is a great way to organize files
