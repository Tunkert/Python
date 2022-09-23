keep_looping = 1

while keep_looping:
    print("We are still looping.")
    keep_looping = int(input("Do you want to keep looping? 0 for no, 1 for yes. "))

# will loop if you enter any integer besides 0 (truthy / falsey)

index = 0

while index < 100:
    print(index)
    index += 1
    