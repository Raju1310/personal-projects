from  turtle import Turtle

NUMBER_OF_SEGMENTS = 3
SEGMENT_LENGTH = 10
FRAME_WIDTH = 1000
FRAME_HEIGHT = FRAME_WIDTH/2
k = int(FRAME_HEIGHT/12)

class Snake:

    head = None

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_segments(self):
        # adding attributes
        self.segments.append(Turtle("square"))
        self.segments[-1].color("White")
        self.segments[-1].penup()
        # adding new segment postion to tail
        location = (self.segments[-1].xcor() - SEGMENT_LENGTH, self.segments[-1].ycor())
        self.segments[-1].goto(location)

    def create_snake(self):
        # creating Head
        self.segments.append(Turtle("square"))
        self.segments[0].color("Red")
        self.head = self.segments[0]
        self.head.penup()
        # creating segments, adding new segment and postion set to tail
        for i in range(NUMBER_OF_SEGMENTS-1):
            self.create_segments()



    def move(self):
        for i in range(1, len(self.segments), 1):
            location = (self.segments[-(i + 1)].xcor(), self.segments[-(i + 1)].ycor())
            self.segments[-i].goto(location)
        self.segments[0].forward(20)



    def Up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def Down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def Right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def Left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)