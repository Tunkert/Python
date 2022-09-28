# frozen sets can be used to get keys in a dictionary
my_dict = {"name": "Tim", "age": 46, "GPA": 4.0}

my_frozen_set = frozenset(my_dict)

print(my_frozen_set)

my_other_frozen = frozenset({"name", "age", "GPA"})

my_list = ["Timothy", 46, 4.0]

print(dict(zip(my_other_frozen, my_list)))
# this kind of works ... play with it.
