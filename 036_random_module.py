import random as rando

print(rando.randint(1, 10))  # returns a random integer between 1 and 10, including both endpoints

print(rando.randrange(1, 11, 2))  # start, stop, step - doesn't include top of range - notice
# this will give all odds.

print(rando.choice([1, 2, 3, 4, 5]))  # returns a random value from an iterable passed in
print(rando.choice((1, 2, 3, 4, 5)))
print(rando.choice(["Tim", "Sarah", "Joe", "Ben", "Matt"]))

print(rando.gauss(5, 1.2))  # gaussian distribution, slightly faster than normalvariate method

print(rando.betavariate(2, 3))  # beta variate distribution

print(rando.random())  # returns float between 0 and 1
