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

# Slicing en python

piano_keys = ["a","b","c","d","e","f","g","g"]
piano_tuple = ("do","re","mi","fa","sol")
print(piano_keys[2:5])
print(piano_keys[2:])
print(piano_keys[:5])
print(piano_keys[2:5:2])
print(piano_keys[::2])
print(piano_keys[::-1]) # Reverse list

print(piano_tuple[2:5])