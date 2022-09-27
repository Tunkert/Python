# create a dictionary with two lists and zip
my_data_values = ["Timothy Unkert", 46, 4.0]
my_data_keys = ["name", "age", "GPA"]

my_info_dict = dict(zip(my_data_keys, my_data_values))

print(my_info_dict)
