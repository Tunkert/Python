# create a class
class Student:
    def __init__(self, f_name, l_name, age):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age


s1 = Student("Sean", "Smith", 42)

print(s1.f_name + " " + s1.l_name + " is " + str(s1.age) + " years old.")
