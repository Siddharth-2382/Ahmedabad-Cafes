from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from brick import Bricks
import time


def exit_game():
    global game_is_on
    game_is_on = False
    return game_is_on


def pause():
    global game_paused
    if not game_paused:
        game_paused = True
        t1.goto(0, 0)
        t1.write("Press SPACE to continue and ESC to exit.", align="center", font=("Courier", 24, "normal"))
    else:
        t1.clear()
        game_paused = False


def close():
    global game_paused
    game_paused = True
    t1.clear()
    t1.goto(0, 0)
    t1.write("Press ESC again to exit and SPACE to continue.", align="center", font=("Courier", 24, "normal"))
    screen.onkey(exit_game, "Escape")
    screen.onkey(pause, "space")


def restart():
    global game_paused, lives, game_just_started
    lives = 3
    t1.clear()
    t2.clear()
    paddle.reset_paddle()
    reset_bricks()
    ball.restart()
    game_paused = False
    game_just_started = True


def reset_bricks():
    global bricks
    for brick in bricks.bricks:
        brick.clear()
        brick.goto(3000, 3000)
    bricks.bricks = []
    bricks = Bricks()


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
screen.onkey(restart, "y")
screen.onkey(pause, "space")
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.protocol("WM_DELETE_WINDOW", close)

t1, t2 = Turtle(), Turtle()
writers = [t1, t2]
for writer in writers:
    writer.speed(0)
    writer.color("white")
    writer.penup()
    writer.hideturtle()


def check_collision_with_walls():
    if ball.ycor() > 280:
        return ball.bounce(x_bounce=False, y_bounce=True)
    if ball.xcor() > 370 or ball.xcor() < -370:
        return ball.bounce(x_bounce=True, y_bounce=False)


def check_collision_with_paddle():
    global lives
    if ball.ycor() < -220 and ball.distance(paddle) < 50:
        return ball.rebound()
    if ball.ycor() < -270:
        lives -= 1
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


def play_again():
    t2.goto(0, -30)
    t2.write("Press Y to play again and Esc to exit.", align="center", font=("Courier", 24, "normal"))


def game_over(msg):
    global game_paused
    game_paused = True
    t1.goto(0, 0)
    t1.write(f"You {msg}!", align="center", font=("Courier", 24, "normal"))
    play_again()


game_is_on = True
lives = 3
game_paused = False
game_just_started = True

while game_is_on:
    if game_just_started:
        ball.launch()
        game_just_started = False

    if lives < 0:
        game_over(msg="lose")
    time.sleep(0.05)
    screen.update()
    if not game_paused:
        ball.move()

        check_collision_with_walls()
        check_collision_with_paddle()
        check_collision_with_brick()

    if len(bricks.bricks) == 0:
        game_over(msg="win")


screen.bye()
