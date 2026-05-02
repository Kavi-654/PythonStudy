class A1:
    def display(self):
        print("Display from A")

class B1(A1):
    def show(self):
        print("Inside B")

class C1(B1):
    def take(self):
        print("Inside C")


c1 = C1()
c1.display()
c1.show()
c1.take()