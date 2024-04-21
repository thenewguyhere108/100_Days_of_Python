from turtle import Turtle
from random import randint,choice

colors = ['black', 'pink', 'orange', 'green', 'purple', 'yellow']


class Cars:
    def __init__(self):
        self.cars = []
        for i in range(10):
            tim = Turtle('square')
            tim.ht()
            tim.setheading(180)
            tim.penup()
            tim.color(choice(colors))
            tim.shapesize(stretch_len=2, stretch_wid=1)
            tim.teleport(x=320, y=randint(-260, 260))
            self.cars.append(tim)

    def move(self):
        for i in self.cars:
            i.fd(10)