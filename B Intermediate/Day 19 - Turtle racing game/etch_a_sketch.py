from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
s = Screen()


def move_forward():
    t.forward(14)


def move_backward():
    t.backward(14)


def counter():
    t.right(10)


def clockwise():
    t.left(10)


def clear():
    t.clear()
    t.reset()
    t.home()


s.listen()
s.onkey(key="w", fun=move_forward)
s.onkey(key="s", fun=move_backward)
s.onkey(key="a", fun=counter)
s.onkey(key="d", fun=clockwise)
s.onkey(key="c", fun=clear)
s.exitonclick()
