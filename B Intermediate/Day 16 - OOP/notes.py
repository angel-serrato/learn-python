# Object-oriented programming OOP
# Pascal case for the name of the class => Car
# An object has attributes car.speed => object.attribute
# An object does methods car.move(): => object.method
class CarBlueprint:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.arrancar = False

    def start(self):
        self.arrancar = True
        print(f"El coche {self.brand} está arrancando.")

car = CarBlueprint("Ford", "Black")

car.arrancar()
# Turtle graphics
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# timmy.left(50)
# timmy.forward(100)
# timmy.left(100)
# timmy.forward(100)
# my_screen = Screen()
# my_screen.canvheight
# my_screen.exitonclick()