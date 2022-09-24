names = ["Tim", "Sarah", "Sean"]
print(names)

# append to lists - you can add one item at a time
names.append("Joe")
print(names)

# extend - add multiple items at once
names.extend(["Matt", "Barry", "Chet"])
print(names)

# pop
last_name = names.pop()
print(last_name)

# pop with index
third_name = names.pop(2)
print(third_name)

# print names after the pops
print(names)

# notice how the pop persists
