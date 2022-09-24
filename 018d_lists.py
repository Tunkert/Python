# list iteration
names_list = ["Tim", "Sarah", "Sean", "Joe", "Aaron", "Matt", "Barry", "Chet"]

# iterate through list
for name in names_list:
    print(name)

print("========================================")

# iterate through list in reverse
for name in names_list[::-1]:
    print(name)

print("=========================================")

# iterate through every other item in the list
for name in names_list[::2]:
    print(name)

print("=========================================")

# iterate in reverse through every item in the list
for n in names_list[::-2]:
    print(n)

print("============================================")

# iterate with a perhaps less "Pythonic" method
for i in range(len(names_list)):  # goes from 0 to 1 less than the length of the names list
    print(names_list[i])
