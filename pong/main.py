from turtle import Screen
from ball import Ball
from paddle import Paddle
from score import Score

FRAME_WIDTH = 800
FRAME_HEIGHT = 600
GAME_ON = True

my_screen = Screen()
my_screen.title("PONG GAME")
my_screen.setup(FRAME_WIDTH, FRAME_HEIGHT)
my_screen.tracer(0)
my_screen.listen()
my_screen.bgcolor("Black")

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
my_score = Score()
my_ball = Ball()

while GAME_ON:

    my_screen.onkey(key="Up", fun=r_paddle.up)
    my_screen.onkey(key="Down", fun=r_paddle.down)
    my_screen.onkey(key="w", fun=l_paddle.up)
    my_screen.onkey(key="s", fun=l_paddle.down)
    my_ball.wall_collision()

    if my_ball.xcor() > (FRAME_WIDTH / 2):
        my_score.r_score()
        my_ball.goto(0, 250)
        my_ball.setheading(225)

    if my_ball.xcor() < (FRAME_WIDTH / -2):
        my_score.l_score()
        my_ball.goto(0, 250)
        my_ball.setheading(315)

    my_ball.l_paddle_collision(l_paddle)
    my_ball.r_paddle_collision(r_paddle)
    my_ball.move()
    my_screen.update()

my_screen.exitonclick()
