from turtle import Turtle
from time import sleep

ANGLE = 90


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_change = 10
        self.y_change = 10
        self.choices = []
        self.move_speed = 0.1

    def create_ball(self):
        self.shape('circle')
        self.penup()
        self.color('red')
        self.speed('slowest')

    def move(self):
        self.goto(x=self.xcor()+self.x_change, y=self.ycor()+self.y_change)

    def detect_wall(self):
        if self.ycor() > 240 or self.ycor() < -240:
            self.y_change *= -1

    def ball_restart(self):
        self.move_speed = 0.1
        self.x_change *= -1
        self.teleport(x=0, y=0)
