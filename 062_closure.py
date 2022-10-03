def incrementor():
    incrementor.counter += 1
    return incrementor.counter


incrementor.counter = 0

print(incrementor())
print(incrementor())
print(incrementor())
print(incrementor())
print(incrementor())
