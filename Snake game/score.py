from turtle import Turtle
from snake import FRAME_HEIGHT, FRAME_WIDTH, k


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.my_score = Turtle()
        self.my_score.hideturtle()
        self.my_score.penup()
        self.my_score.color("white")
        self.my_score.goto(0, FRAME_HEIGHT/2 - k)
        self.score = 0
        self.my_score.write(f"score : {self.score}", font=("Helvetica", 24, "bold italic"))

    def update_score(self):
        self.my_score.clear()
        self.score += 1
        self.my_score.write(f"score : {self.score}", font=("Helvetica", 24, "bold italic"))

