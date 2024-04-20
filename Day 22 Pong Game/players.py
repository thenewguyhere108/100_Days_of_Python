from turtle import Turtle
MOVE_DISTANCE = 20

class Players(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.create_stick(pos)

    def create_stick(self, pos):
        self.shape('square')
        self.color('white')
        self.speed('fastest')
        self.resizemode(rmode='user')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(x=pos, y=-20)

    def move_up(self):
        if self.ycor() < 200:
            self.goto(x=self.xcor(), y=self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        if self.ycor() > -200:
            self.goto(x=self.xcor(), y=self.ycor() - MOVE_DISTANCE)
