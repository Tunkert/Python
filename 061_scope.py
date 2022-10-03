# create a variable with global scope
my_name = "Timothy Unkert"


def return_meaning():
    # local scope
    meaning_of_life = 42
    return meaning_of_life


def print_my_name(my_name):
    return my_name


# print(meaning_of_life)  # will return exit code 1 - NameError, meaning_of_life is not defined

print(return_meaning())
print(f"My name is {print_my_name(my_name)}.")  # we can pass the global variable to this function
