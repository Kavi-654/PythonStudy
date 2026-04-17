# Functions
def add(a, b):
    return a + b


ans = add(7, 8)
print("Answer is:", ans)


# Passing function as an argument (Higher Order Functions)
def alter(func, a):
    return func(a)


def square(a):
    return a * a


ans = alter(square, 5)
print(ans)


# Built-in higher order functions

# map
l = [1, 2, 3]
x = list(map(lambda i: i * i, l))
print(x)


# filter
arr = [1, 2, 3, 4, 5, 6]
y = list(filter(lambda x: x % 2 == 0, arr))
print(y)


# sorted
arr2 = ["java", "python", "javascript"]
d = sorted(arr2, key=len)
print(d)


# Lambda Functions
multiply = lambda a, b: a * b
print(multiply(3, 4))


# Lambda returning multiple values
calc = lambda a, b: (a + b, a - b)
result = calc(50, 6)
print(result)


# Decorator-like function (simple example)
def deco(f):
    def wrapper():
        print("Before Execution")
        f()
        print("After Execution")
    return wrapper


@deco
def fun():
    print("Inside the function")


fun()


# Variable length arguments (*args)
def varargs(*args):
    total = 0
    for i in args:
        total += i
    return total


print(varargs(9, 10, 11))


# Keyword arguments (**kwargs)
def dics(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


dics(name='kavi', placed='Developer')