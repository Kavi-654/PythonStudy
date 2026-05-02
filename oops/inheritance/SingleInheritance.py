class A:
    def display(self):
        print("Inside A class")

class B(A):

    def display(self):
        super().display()
        print("Inside B class")

b1=B()
b1.display()
