import time
from turtle import Turtle
from food import Food
from snake import Snake, FRAME_WIDTH, FRAME_HEIGHT, k
from turtle import Screen
from score import Score

my_screen = Screen()
my_screen.listen()
my_screen.setup(width=FRAME_WIDTH, height=FRAME_HEIGHT)
my_screen.screensize(FRAME_WIDTH - k, FRAME_HEIGHT - k)
my_screen.bgcolor("Blue")
my_screen.tracer(0)
my_snake = Snake()
my_food = Food()
my_score = Score()
GAME_ON = True
till_time = 0.18


def check_game_off():
    global GAME_ON
    for seg in my_snake.segments:
        if my_snake.head == seg:
            pass
        elif my_snake.segments[0].distance(seg) < 10:
            GAME_ON = False
    if my_snake.head.ycor() > (FRAME_HEIGHT / 2) - k or my_snake.head.xcor() > (FRAME_WIDTH / 2) - k or \
            my_snake.head.ycor() < -(FRAME_HEIGHT / 2) + k or my_snake.head.xcor() < -(FRAME_WIDTH / 2) + k:
        GAME_ON = False
        t = Turtle(visible=False)
        t.color("White")
        t.write(f"GAME OVER", font=("Helvetica", 24, "bold italic"))


def move():
    global till_time
    my_snake.move()
    check_game_off()
    my_screen.update()
    time.sleep(till_time)
    till_time -= 0.0001
    my_food.check_collision(my_snake, my_score)


while GAME_ON:
    my_screen.onkey(key="Right", fun=my_snake.Right)
    my_screen.onkey(key="Up", fun=my_snake.Up)
    my_screen.onkey(key="Down", fun=my_snake.Down)
    my_screen.onkey(key="Left", fun=my_snake.Left)
    move()

my_screen.exitonclick()
