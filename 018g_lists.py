names = ["Tim", "Sean", "Joe", "Aaron", "Chet"]

# clear a list
print(names.clear())  # notice we get None - because this method doesn't return anything

# but ...
print(names)  # oh no, the list is empty ...

# let's add
names.extend(["Tim", "Sean", "Sarah", "Aaron", "Chet"])
print(names)

# remove first item of the list and assign to variable
f_name = names.pop(0)
print(f_name)
print(names)

# another way - just remove first item of the list
del names[0]
print(names)

# insert into a list
names.insert(2, "Billy")
print(names)
