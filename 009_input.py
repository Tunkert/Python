your_name = input("What is your name?")
print("Your name is " + your_name + ".")
your_fav_num = input("What is your favorite number?")
print("Your favorite number is " + your_fav_num + ".")
# print(2 + your_fav_num) #- this will cause an error TypeError - unsupported operand type
# You must convert it
fav_num_as_int = int(your_fav_num)
print(2 + fav_num_as_int)
