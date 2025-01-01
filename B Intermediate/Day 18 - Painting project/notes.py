# Ways to import a module
#
# import turtle
# angel = turtle.Turtle()
#
# from turtle import Turtle
# tortuga = Turtle()
#
# from turtle import *

# Alias modules
# import turtle as t
# We give the module an alias
# import turtle as t
# tortuga = t.Turtle()

# from turtle import Screen
# import turtle as t
#
# tortuga = t.Turtle()
# tortuga.shape("turtle")
#
# def square():
#     for _ in range(0, 4):
#         tortuga.forward(100)
#         tortuga.right(90)
#
# def dashed_line():
#     for _ in range(0, 10):
#         tortuga.forward(10)
#         tortuga.color("white")
#         tortuga.forward(10)
#         tortuga.color("black")
#
# dashed_line()
#
# screen = Screen()
# screen.screensize(50, 50)
# screen.exitonclick()

# Shapes exercise
# from turtle import Turtle, Screen
# from random import choice
# from colors import colores
#
# t = Turtle()
# t.shape("classic")
# t.width(2)
# t.speed(10)
# s = Screen()
#
#
# def draw_shape(sides):
#     angle = 360 / sides
#     for _ in range(sides):
#         t.forward(100)
#         t.right(angle)
#
#
# for shape_side in range(3, 21):
#     t.color(choice(colores))
#     draw_shape(shape_side)
#
# s.exitonclick()

# Random walk

# from random import choice, randint
# from turtle import Turtle, Screen
#
# t = Turtle()
# t.shape("turtle")
# t.speed(0)
# t.width(7)
#
# s = Screen()
# s.colormode(255)
#
# directions = [0, 90, 180, 270]
#
#
# def create_colors():
#     red = randint(0, 255)
#     green = randint(0, 255)
#     blue = randint(0, 255)
#     color = (red, green, blue)
#     print(color)
#     return color
#
#
# for _ in range(500):
#     t.pencolor(create_colors())
#     t.forward(30)
#     t.setheading(choice(directions))
#
# s.exitonclick()

from turtle import Turtle, Screen

t = Turtle()
t.shape("classic")
t.speed(0)
t.color("black")


def draw_circle(size):
    for _ in range(int(360 / size)):
        t.circle(100)
        t.setheading(t.heading() + size)


draw_circle(5)

s = Screen()
s.colormode(255)
s.exitonclick()
