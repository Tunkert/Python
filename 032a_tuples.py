# tuples are immutable
my_names = ["Sarah", "Tim", "Joe", "Sean", "Aaron"]
my_ages = [49, 46, 46, 47, 47]

my_tuple = tuple(zip(my_names, my_ages))

print(my_tuple) # this is a tuple of tuples - I'm getting ahead of myself!
