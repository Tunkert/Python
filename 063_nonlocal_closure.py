def incrementor():
    counter = 0

    def up():
        nonlocal counter
        counter += 1
        return counter

    return up


up = incrementor()

print(up())
print(up())
print(up())
print(up())
print(up())
