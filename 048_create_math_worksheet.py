import random as rand

f = open("math-wksht.html", "w")

for i in range(1, 101):
    num1 = rand.randint(1, 20)
    num2 = rand.randint(1, 20)
    f.write(f"<p>{i}. Solve for x: x + {num1} = {num2}</p>\n")

f.close()
