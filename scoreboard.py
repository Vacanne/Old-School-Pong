from turtle import Turtle

COLOR = "white"
ALIGN = "center"
FONT = ("Courier", 80, "normal")
LEFT_SCORE = (-100, 200)
RIGHT_SCORE = (100, 200)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(LEFT_SCORE)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.goto(RIGHT_SCORE)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def l_point(self):
        self.clear()
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.update_scoreboard()
