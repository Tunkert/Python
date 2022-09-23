"""
print out numbers 1 through 100 except when:
divisible by 3 print "fizz"
divisible by 5 print "buzz"
divisible by 3 and 5 print "fizzbuzz"
"""

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizzbuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
