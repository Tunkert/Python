def say_hello():
    return "hello"


class Car:
    def __init__(self, f_name):
        self.name = f_name

    def return_name(self):
        return self.name


class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def return_complex(self):
        return f"{self.real} + {self.imaginary}j"


print(type(3))  # <class 'int'>
print(type(3.14))  # <class 'float'>
print(type("Hello"))  # <class 'str'>
print(type(4 + 3j))  # <class 'complex'>
print(type([1, 2, 3, 4, 5]))  # <class 'list'>
print(type(say_hello()))  # this is a function that returns a string
print(type((1, 2, 3, 4, 5)))  # <class 'tuple'>
print(type({"name": "Tim", "age": 46}))  # <class 'dict'>
print(type(Car("Ferrari")))  # <class '__main__.Car'>
complex_1 = Complex(3, 4)
print(complex_1.return_complex())
print(type(complex_1.return_complex()))  # <class 'str'>
print(type(True)) # <class 'bool'>
