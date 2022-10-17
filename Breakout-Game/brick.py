from turtle import Turtle
import random

BRICK_PROP = {
    "red": 3.5,
    "yellow": 4,
    "green": 5.5,
    "blue": 6
}


class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(list(BRICK_PROP.keys())[random.choice(range(5))])
        self.shapesize(stretch_wid=1, stretch_len=BRICK_PROP[self.color])

