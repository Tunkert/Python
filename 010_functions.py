def say_hello():
    """This function prints hello to the screen"""
    print("Hello!")


def say_hello_with_return():
    """This function returns the string 'hello'"""
    return "Hello!"


def say_hello_w_arg(f_name):
    return "Hello, " + f_name + "!"


say_hello()

print(say_hello_with_return())

print(say_hello_w_arg("Tim"))

print(type(say_hello()))  # <class 'NoneType'>
print(type(say_hello_w_arg("Tim")))  # <class 'str'>
