from snake import Turtle, FRAME_WIDTH, FRAME_HEIGHT, k
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.food = None
        self.create_food()
        self.hideturtle()

    def refresh(self):
        x = random.randint(int(FRAME_WIDTH / -2) + k, int(FRAME_WIDTH / 2) - k)
        y = random.randint(int(FRAME_HEIGHT / -2) + k, int(FRAME_HEIGHT/2 - k))
        self.food.goto(x, y)

    def create_food(self):
        self.food = Turtle("circle")
        self.food.showturtle()
        self.food.color("red")
        self.food.penup()
        self.refresh()

    def check_collision(self, my_snake, my_score):
        if my_snake.segments[0].distance(self.food) < 20:
            self.refresh()
            my_score.update_score()
            my_snake.create_segments()
