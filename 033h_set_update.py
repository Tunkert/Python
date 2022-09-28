names_set = {"Tim", "Joe", "Aaron"}
other_names = {"Matt", "Mark"}
more_names = {"Sarah", "Amy"}

names_set.update(other_names, more_names, [1, 2, 3])  # can take any number of iterable arguments
# names_set.update(1, 2, 3) - this will throw an error

print(names_set)
