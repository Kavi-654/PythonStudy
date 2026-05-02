class AnimalSuper:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Animal name is {self.name}")


class DogSuper(AnimalSuper):
    def __init__(self, name):
        super().__init__(name)

    def display(self):
        super().display()
        print("It barks")


d2 = DogSuper("Leo")




 # Method Resolution Order
class A:
    def fun(self):
        print("In A")

class B(A):
    def fun(self):
        print("In B")

class C(A):
    def fun(self):
        print("In C")

class D(B, C):
    pass


d = D()
d.fun()

print(D.mro())