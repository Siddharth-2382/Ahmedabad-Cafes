from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Bricks
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)
screen.listen()

paddle = Paddle((0, -250))
bricks = Bricks()
ball = Ball()

screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280:
        ball.rebounce()

    if ball.xcor() > 370 or ball.xcor() < -370:
        ball.bounce()

    if ball.ycor() < -220 and ball.distance(paddle) < 50:
        ball.rebound()

    if ball.ycor() < -270:
        ball.reset_position()
        

screen.exitonclick()
