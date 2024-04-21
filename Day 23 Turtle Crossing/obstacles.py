from turtle import Turtle
from random import choice
from time import sleep


colors = ['black', 'pink', 'orange', 'green', 'purple', 'yellow']
y_cor = [-200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
TIME = 0.2

class Cars:
    def __init__(self):
        self.cars = []
        self.time = TIME

    def create_cars(self):
        tim = Turtle('square')
        tim.setheading(180)
        tim.penup()
        tim.color(choice(colors))
        tim.shapesize(stretch_len=2, stretch_wid=1)
        tim.teleport(x=320, y=choice(y_cor))
        tim.fd(20)
        self.cars.append(tim)

    def move(self):
        for i in self.cars:
            i.fd(20)
        sleep(self.time)