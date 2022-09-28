names1 = {"Tim", "Sarah", "Joe"}
names2 = {"Tim", "Timothy", "Sarah", "Sara", "Joe", "Joseph"}

print(names1.issubset(names2))  # prints the boolean value 'True'

print(names2.issubset(names1))  # prints 'False'

print(names2.issuperset(names1))  # prints 'True'
