class AnimalM:
    def display(self):
        print("It is an Animal")

class Mammal:
    def type_of_mammal(self):
        print("Type: Dog")

class DogM(AnimalM, Mammal):
    def show(self):
        print("Woof Woof!")


d3 = DogM()
d3.show()
d3.type_of_mammal()
d3.display()