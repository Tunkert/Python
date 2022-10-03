# create a class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student_type(self):
        if self.age < 6:
            return f"{self.name} is a pre-school student."
        elif 6 <= self.age <= 10:
            return f"{self.name} is an elementary school student."
        elif 11 <= self.age <= 13:
            return f"{self.name} is a middle school student."
        elif 14 <= self.age <= 17:
            return f"{self.name} is a high school student."
        elif 18 <= self.age <= 21:
            return f"{self.name} is an undergraduate student."
        else:
            return f"{self.name} is a graduate, post graduate, or adult learner."


s1 = Student("Timothy Unkert", 46)
s2 = Student("Johnny", 5)
s3 = Student("Billy", 15)
s4 = Student("Mary", 19)

print(s1.student_type())
print(s2.student_type())
print(s3.student_type())
print(s4.student_type())
