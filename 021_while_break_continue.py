index = 0

# print a loop 1 through 10 and skip 7
while index < 10:
    index += 1
    if index == 7:
        continue  # go back to start of the loop
    print(index)

while True:
    keep_looping = int(input("Do you want to keep looping? (0 / 1) "))
    if keep_looping == 0:
        break
