class Person:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def __str__(self):
        return f"Name of the Person is: {self.__name}, Age of the Person is: {self.__age}, Salary of the Person is: {self.__salary}"

    def getSalary(self):
        return self.__salary

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age

    def setName(self, name):
        self.__name = name

    def setSalary(self, salary):
        self.__salary = salary


p1 = Person("Kavi", 21, 40000)

print(p1)

# Here i have showcased the use of both encapsulation and then Access Modifiers