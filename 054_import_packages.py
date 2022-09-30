import mypackage.feature.copyright as mycopy
# import mypackage.feature.subfeature.number_methods as numb  # or
from mypackage.feature.subfeature.number_methods import *

print("I created a package and gave it a copyright date of " + str(mycopy.date_of_copyright) + ", bro!")
# print("9 squared is " + str(numb.square(9)) + "!")
print("3 cubed is " + str(cube(3)) + ".")
print(f"5 to the sixth power is {exponent(5, 6)}.")
