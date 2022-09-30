f = open("my-test.html", "r")

file_lines = f.readlines()

f.close()

for line in file_lines:
    print(line)
