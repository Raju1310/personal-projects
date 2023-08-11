from turtle import Turtle

PADDLE_LENGTH = 5
FRAME_WIDTH = 800
FRAME_HEIGHT = 600


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.create_paddle(x, y)

    def create_paddle(self, x, y):
        self.shape('square')
        self.color("white")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto((x, y))

    def up(self):
        if self.ycor() > (FRAME_HEIGHT / 2) - 50:
            pass
        else:
            self.forward(25)

    def down(self):
        if self.ycor() < (FRAME_HEIGHT / -2) + 50:
            pass
        else:
            self.backward(25)
