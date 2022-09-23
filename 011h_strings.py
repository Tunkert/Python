my_str = "This is my string"
print(my_str.replace("string", "cat."))

print(my_str)  # notice this string stays the same - still immutable

# but ...

my_new_str = my_str.replace("string", "dog.")

print(my_new_str)
