my_tuple = (1, 2, 3, 4, 5, "True", True, False, "cat")

for item in my_tuple:
    print(item)

# That worked fine but ...

# my_tuple[0] = "dog"  # this will throw an error

# however ... this works fine
print(my_tuple[0])

print(my_tuple[1])
