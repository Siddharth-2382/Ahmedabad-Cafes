from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=7.5)
        self.goto(position)

    def go_right(self):
        new_x = self.xcor() + 50
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 50
        self.goto(new_x, self.ycor())

    def reset_paddle(self):
        self.goto((0, -250))
