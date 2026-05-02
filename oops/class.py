#  1. Class with Class Variable and Instance Variables

class Dog:
    sound = "Bark"   #  Class Variable

    def __init__(self, name, age):
        self.name = name      #  Instance Variable
        self.age = age

    def display(self):
        print(self.name, Dog.sound, self.age)


d1 = Dog("Messi", 3)
d1.display()


# 2. Class with Constructor (Init Method)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


p1 = Person("John", 23)
p1.display()


#  3. Default Parameters

class Cow:
    def __init__(self, name, age, breed="Kangeyan"):
        self.name = name
        self.age = age
        self.breed = breed

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Breed: {self.breed}")


c1 = Cow("Bujju", 5)
c1.display()



#  5. __str__ Method (String Representation)

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


e1 = People("Bob", 21)
print(e1)


#  6. Class Method (IMPORTANT)

class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name


Student.change_school("XYZ School")
print(Student.school)


#  7. Static Method (IMPORTANT)

class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b


print(MathUtils.add(5, 3))


