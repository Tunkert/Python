my_init_dict = {
    "name": "Timothy Unkert",
    "age": 46,
    "GPA": 4.0,
}

print(my_init_dict)

my_init_dict["years old"] = my_init_dict["age"]
del my_init_dict["age"]

print(my_init_dict)

my_init_dict["full_name"] = my_init_dict.pop("name")

print(my_init_dict)
