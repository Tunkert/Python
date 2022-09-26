# let's say you have someone enter integers with a space
# and you want to change it to a list
int_str_arr = input("Enter a bunch of integers separated with a space: ").split(" ")  # split by a space

# print out the int_str_arr
print(int_str_arr)  # notice these are strings

# put them into a list as integers
int_arr = []  # create an empty list
for int_str in int_str_arr:
    int_arr.append(int(int_str))

# print out integer list
print(int_arr)
