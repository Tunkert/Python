# the basic format
if (True):
    # do this code
    print("This is true.")
else:
    # do this code
    print("This is false.")

# common example ...
age = 15

if age >= 21:
    print("You can enter the bar.")
else:
    print("Get lost dude.")

# else if is elif in python ...
if age >= 21:
    print("You can enter the bar.")
elif age >= 18:  # this will only be reached is age is less than 21
    print("You can't enter the bar but you can go to war.")
else:  # this will only be reached if age is less than 18
    print("You are a minor.")