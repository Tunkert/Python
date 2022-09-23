is_student = False
age = 17
is_gifted = True

if is_student:
    if age < 18 and age >= 14:
        print("You are in secondary school.")
    elif age < 14:
        print("You are in primary school.")
    elif age > 18:
        print("You are in college")
else:
    if age < 18:
        if is_gifted:
            print("You finished high school early.")
        else:
            print("Stop skipping, bro.")
    else:
        print("You are working.")
