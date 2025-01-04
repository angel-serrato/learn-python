# Class inheritance
# Attributes, behaviour

class Animal:
    def __init__(self, name):
        self.name = name
        self.eyes = 2

    def breathe(self):
        print("Respirando desde Animal")

    def jump(self):
        print("Saltando desde Animal")


class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print("Nadando desde Fish")

    def breathe(self):
        print("Respirando desde Fish")

    def jump(self):
        super().jump()
        print("no se")


animaluno = Fish(name="Angel")
animaluno.name = "Asignando otro nombre"
animaluno.breathe()
animaluno.swim()
animaluno.jump()
print(animaluno.name)
