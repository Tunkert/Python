student_info = [
    {
        "name": "Timothy Unkert",
        "age": 46,
        "GPA": 4.0
    },
    {
        "name": "Sarah",
        "age": 49,
        "GPA": 3.0
    },
    {
        "name": "Sean",
        "age": 47,
        "GPA": 3.5
    }
]

# iterate through students
for student in student_info:
    print("================")
    for k, v in student.items():
        print(k, ":", v)
    