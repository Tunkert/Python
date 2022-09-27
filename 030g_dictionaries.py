# use kwargs in function
def print_dict(**kwargs):
    for k, v in kwargs.items():
        print(k, ":", v)


my_dict = {
    "name": "Timothy Unkert",
    "age": 46,
    "GPA": 4.0
}

print_dict(**my_dict)
