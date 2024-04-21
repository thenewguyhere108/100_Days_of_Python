from player import Player
from turtle import Screen
from scoreboard import Score
from obstacles import Cars
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.title(titlestring='Turtle Crossing')
screen.tracer(0)
screen.listen()
is_game = True
cars = Cars()
score = Score()
player = Player()
screen.onkeypress(fun=player.move_up, key='Up')

i = 0
while is_game:
    random_choice = randint(1,5)
    cars.move()
    if random_choice == 1:
        cars.create_cars()
    if player.ycor() > 260:
        score.score += 1
        cars.time *= 0.75
        score.update()
        player.teleport(x=0, y=-280)
    for car in cars.cars:
        if car.distance(player) < 30 and car.ycor() == player.ycor():
            score.update()
            score.game_over()
            is_game = False
    screen.update()

screen.exitonclick()