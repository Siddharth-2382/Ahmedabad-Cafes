from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Bricks
import time


def close():
    global game_is_on
    game_is_on = False
    return game_is_on


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
screen.onkey(close, "Escape")
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.protocol("WM_DELETE_WINDOW", close)


def check_collision_with_walls():
    if ball.ycor() > 280:
        return ball.bounce(x_bounce=False, y_bounce=True)
    if ball.xcor() > 370 or ball.xcor() < -370:
        return ball.bounce(x_bounce=True, y_bounce=False)


def check_collision_with_paddle():
    if ball.ycor() < -220 and ball.distance(paddle) < 50:
        return ball.rebound()
    if ball.ycor() < -270:
        return ball.reset_position()


def check_collision_with_brick():
    for brick in bricks.bricks:
        if ball.distance(brick) < 40:
            brick.clear()
            brick.goto(3000, 3000)
            bricks.bricks.remove(brick)

            # detect collision from left
            if ball.xcor() < brick.left_wall:
                ball.bounce(x_bounce=True, y_bounce=False)

            # detect collision from right
            elif ball.xcor() > brick.right_wall:
                ball.bounce(x_bounce=True, y_bounce=False)

            # detect collision from bottom
            elif ball.ycor() < brick.bottom_wall:
                ball.bounce(x_bounce=False, y_bounce=True)

            # detect collision from top
            elif ball.ycor() > brick.upper_wall:
                ball.bounce(x_bounce=False, y_bounce=True)


game_is_on = True

while game_is_on:
    time.sleep(0.08)
    screen.update()
    ball.move()

    check_collision_with_walls()
    check_collision_with_paddle()
    check_collision_with_brick()

screen.bye()
