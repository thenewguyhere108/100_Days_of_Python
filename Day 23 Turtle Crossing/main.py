from player import Player
from turtle import Screen
from scoreboard import Score
from obstacles import Cars
from time import sleep

cars = Cars()
score = Score()
player = Player()
screen = Screen()
screen.setup(width=600, height=600)
screen.title(titlestring='Turtle Crossing')
screen.tracer(0)
screen.listen()
screen.onkeypress(fun=player.move_up, key='Up')
is_game = True
while is_game:
    screen.update()
    if player.ycor() > 260:
        score.score += 1
        score.update()
        player.teleport(x=0, y=-280)
    cars.move()
    sleep(0.1)

screen.exitonclick()