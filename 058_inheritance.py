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


class ElementaryStudent(Student):
    def subjects(self):
        return f"{self.name} has classes in reading, mathematics, and world history."


class HighSchoolStudent(Student):
    def trouble(self):
        if self.name == "Billy":
            return f"{self.name} got in trouble with the coppers for vandalism of the bridge \
where the troll lives."
        return f"{self.name} did not get in any trouble during high school."


s1 = ElementaryStudent("Kim", 7)
s2 = HighSchoolStudent("Sarah", 16)
s3 = HighSchoolStudent("Billy", 17)


print(s1.subjects())
print(s2.trouble())
print(s3.trouble())
