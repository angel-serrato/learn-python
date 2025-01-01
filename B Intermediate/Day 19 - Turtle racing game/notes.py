# Pasar una funcion como argumento a otra funcion
# Cuando usemos esto es mejor usar keyword arguments en lugar de positional arguments
# keyword arguments => s.onkey(key="space", fun=move)
# positional arguments => s.onkey("space", move)

from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
s = Screen()


def move():
    t.forward(10)


s.listen()
s.onkey(key="space", fun=move)
s.exitonclick()
