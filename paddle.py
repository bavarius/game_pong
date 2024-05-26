from turtle import Turtle

STEP_WIDTH = 20


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.create_paddle(pos)

    def create_paddle(self, pos):
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.goto(pos)

    def up(self):
        new_y = self.ycor() + STEP_WIDTH
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - STEP_WIDTH
        self.goto(self.xcor(), new_y)
