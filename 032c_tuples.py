# make a tuple

my_tup = tuple([1, 2, 3, 4, 5])

print(my_tup)

my_other_tup = tuple({"name": "Timothy Unkert", "age": 46, "GPA": 4.0})

print(my_other_tup)  # will work but will only print values.

my_other_other_tup = tuple({"name": "Timothy Unkert", "age": 46, "GPA": 4.0}.items())

print(my_other_other_tup)  # this prints a tuple of tuples ... whoa!
