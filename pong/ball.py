import time
from turtle import Turtle
from paddle import FRAME_WIDTH, FRAME_HEIGHT
from score import Score


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(1, 1)
        self.penup()
        self.goto(30, 250)
        self.setheading(225)

    def move(self):
        time.sleep(0.05-0.0001)
        self.forward(10)

    def wall_collision(self):
        if self.ycor() > (FRAME_HEIGHT / 2) - 20 or self.ycor() < (FRAME_HEIGHT / -2) + 20:
            self.setheading(self.heading() + 90)

    def l_paddle_collision(self, l_paddle):
        if self.distance(l_paddle) < 50 and self.xcor() < (FRAME_WIDTH / -2) + 80:
            self.setheading(self.heading() + 90)

    def r_paddle_collision(self, r_paddle):
        if r_paddle.distance(self) < 50 and self.xcor() > (FRAME_WIDTH / 2) - 80:
            self.setheading(self.heading() + 90)
