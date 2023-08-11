from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        self.left_score = 0
        self.right_score = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto((800 / -4, 200))
        self.write(f"{self.left_score}", font=("Helvetica", 50, "bold italic"))
        self.goto((800 / 4, 200))
        self.write(f"{self.right_score}", font=("Helvetica", 50, "bold italic"))

    def l_score(self):
        self.clear()
        self.left_score += 1
        self.goto((800 / -4, 200))
        self.write(f"{self.left_score}", font=("Helvetica", 50, "bold italic"))
        self.goto((800 / 4, 200))
        self.write(f"{self.right_score}", font=("Helvetica", 50, "bold italic"))

    def r_score(self):
        self.clear()
        self.right_score += 1
        self.goto((800 / -4, 200))
        self.write(f"{self.left_score}", font=("Helvetica", 50, "bold italic"))
        self.goto((800 / 4, 200))
        self.write(f"{self.right_score}", font=("Helvetica", 50, "bold italic"))