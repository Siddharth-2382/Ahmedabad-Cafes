import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.goto(0, -229)
        self.color("white")
        self.x_move = 10
        self.y_move = 10

    def launch(self):
        if random.choice([0, 1]):
            new_x = self.xcor() + random.choice(range(-60, 61, 10))
        else:
            new_x = self.xcor() + random.choice(range(-60, 61, 10))
            self.bounce(x_bounce=True, y_bounce=False)
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, x_bounce, y_bounce):
        if x_bounce:
            self.x_move *= -1
        if y_bounce:
            self.y_move *= -1

    def rebound(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(0, -229)
        self.rebound()

    def restart(self):
        self.goto(0, -229)
