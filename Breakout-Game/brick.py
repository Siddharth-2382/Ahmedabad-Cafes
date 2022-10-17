from turtle import Turtle
import random

BRICK_PROP = {
    "red": 3.5,
    "yellow": 4,
    "green": 5.5,
    "blue": 6
}


class Brick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(list(BRICK_PROP.keys())[random.choice(range(4))])
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.goto(position)
        self.left_wall = self.xcor() - 5
        self.right_wall = self.xcor() + 5
        self.upper_wall = self.ycor() + 5
        self.bottom_wall = self.ycor() - 5


class Bricks:
    def __init__(self):
        self.y_start = 35
        self.y_end = 280
        self.bricks = []
        self.create_all_lanes()

    def create_lane(self, y_cord):
        for i in range(-340, 370, 96):
            brick = Brick((i, y_cord))
            self.bricks.append(brick)

    def create_all_lanes(self):
        for i in range(self.y_start, self.y_end, 34):
            self.create_lane(i)
