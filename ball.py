from turtle import Turtle

COLOR = "white"
SHAPE = "square"
WIDTH = 20
HEIGHT = 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(SHAPE)
        self.color(COLOR)
        self.forward(100)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.paddle_bounce()

