my_dict = {
    "name": "Timothy Unkert",
    "age": 46,
    "GPA": 4.0
}

print(sorted(my_dict.items()))  # notice it sorts based on Ascii values

# print(sorted(my_dict.items(), key=lambda item: item[1]))  # throw an error because of int and str mismatch

my_other_dict = {
    "name": "Timothy Unkert",
    "age": '46',
    "GPA": '4.0'
}

print(sorted(my_other_dict.items(), key=lambda item: item[1]))