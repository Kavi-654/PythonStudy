# Functions with default arguments
def add_numbers(a, b=10):
    return a + b


print(add_numbers(11))


# Parameterized functions
def calc(a, b, c):
    return a * b * c


print(calc(10, 20, 30))


# Keyword arguments
def keys(name, age):
    print("Name is:", name, "| Age is:", age)


keys(age=23, name="John")