# lambda expressions - these are anonymous functions like in javascript - nice to assign to variable
# good for functions you only need to use once

y = lambda x: x * x
cuby = lambda x: x ** 3

print(y(3))  # 9
print(cuby(3))  # 27
