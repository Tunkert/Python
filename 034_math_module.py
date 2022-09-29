import math

# importing math allows us to use a lot of math functions
# trig functions (take in the angle as radians - most cases)
print(math.sin(math.pi / 4))  # this will give you the square root of 2 over 2
print(math.cos(0))  # 1.0 - returns a float
print(math.tan(math.pi / 4))  # really 1 but returns 0.9 repeating as there is some approximation
print(math.asin(0.707))  # returns ~pi/4 radians
print(math.acos(1))  # returns the angle 0
print(math.cosh(math.pi / 3))  # returns 1.6 - this is a hyperbolic function

# convert radians to degrees
print(math.degrees(math.pi / 3))  # should be 60 - you get 59.9 repeating

# convert degrees to radians
print(math.radians(45))  # 0.785 - which is pi/4

# roots
print(math.sqrt(9))  # 3.0
print(math.isqrt(10))  # returns the integer part of the square root

# ceil, floor
print(math.ceil(3.1))  # returns 4
print(math.floor(3.1))  # returns 3

# factorial
print(math.factorial(5))  # 120 because 5 x 4 x 3 x 2 x 1 = 120

