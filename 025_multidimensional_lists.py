info = [
    ["Tim", 46],
    ["Sarah", 48],
    ["Sean", 47],
    ["Joe", 46],
    ["Aaron", 47],
    ["Will", 16]
]

for row in info:
    for column in row:
        if column != row[-1]:
            print(column, end=", age: ")
        else:
            print(column)
