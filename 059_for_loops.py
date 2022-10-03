# unpack a range into a list
nums = [*range(1, 101)]  # will unpack numbers 1 through 100

# iterate through list - fizzbuzz
for num in nums:
    if num % 3 == 0 and num % 5 == 0:
        print("Fizzbuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# could also do
for number in range(1, 101):
    print(number)
