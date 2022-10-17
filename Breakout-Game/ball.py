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
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.x_move *= -1

    def rebounce(self):
        self.y_move *= -1

    def rebound(self):
        self.y_move *= -1
        self.move_speed *= 0.95

    def reset_position(self):
        self.goto(0, -229)
        self.rebound()
        self.move_speed = 0.1
