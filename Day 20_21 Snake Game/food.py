from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('green')
        self.speed('fastest')
        self.move()
    
    def move(self):
        random_x = randint(-480, 480)
        random_y = randint(-480, 480)
        self.goto(random_x, random_y)
        print(self.pos())
