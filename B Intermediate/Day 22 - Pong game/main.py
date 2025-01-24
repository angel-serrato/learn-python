from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
bola = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(bola.move_speed)
    screen.update()
    bola.move()
    if bola.ycor() > 280 or bola.ycor() < -280:
        bola.bounce_y()

    if bola.distance(r_paddle) < 50 and bola.xcor() > 320 or bola.distance(l_paddle) < 50 and bola.xcor() < -320:
        bola.bounce_x()

    if bola.xcor() > 380:
        bola.reset_position()
        scoreboard.l_point()

    if bola.xcor() < -380:
        bola.reset_position()
        scoreboard.r_point()

screen.exitonclick()
