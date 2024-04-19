from turtle import Screen
from score import Score
from time import sleep

screen = Screen()
screen.bgcolor('black')
screen.tracer(0)
screen.setup(height=1000, width=1000)
score = Score()
screen.update()
for i in range(10):
    screen.update()
    score.user_score = i
    score.pc_score = i
    score.update_score()
    sleep(0.1)
screen.exitonclick()
