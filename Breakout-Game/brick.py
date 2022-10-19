from turtle import Turtle
import random

BRICK_COLOR = ["red", "yellow", "green", "blue"]


class Brick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(BRICK_COLOR[random.choice(range(4))])
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.goto(position)
        self.left_wall = self.xcor() - 30
        self.right_wall = self.xcor() + 30
        self.upper_wall = self.ycor() + 15
        self.bottom_wall = self.ycor() - 15


class Bricks:
    def __init__(self):
        self.y_start = 70
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
