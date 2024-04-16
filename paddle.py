from turtle import Turtle

SHAPE = "square"
COLOR = "white"


# SHAPE_SIZE = (stretch_wid=5, stretch_len=1)


class Paddle(Turtle):

    def __init__(self, location):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.penup()
        self.goto(location)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
