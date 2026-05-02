class AnimalBase:
    def display(self):
        print("This is Animal")

class DogH(AnimalBase):
    def display(self):
        print("Dog is an animal")

class CatH(AnimalBase):
    def display(self):
        print("Cat is an animal")


d1 = DogH()
d1.display()

c1 = CatH()
c1.display()