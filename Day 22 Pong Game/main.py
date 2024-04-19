from turtle import Screen
from score import Score
from time import sleep
from players import Players


USER1_POS = -380
USER2_POS = 380
screen = Screen()
screen.bgcolor('black')
screen.tracer(0)
screen.setup(height=500, width=800)
score = Score()
screen.update()
player_1, player_2 = Players(USER1_POS), Players(USER2_POS)
screen.listen()
screen.onkeypress(fun=player_1.move_up, key='Up')
screen.onkeypress(fun=player_2.move_up, key='w')
screen.onkeypress(fun=player_1.move_down, key='Down')
screen.onkeypress(fun=player_2.move_down, key='s')

while True:
    screen.update()
screen.exitonclick()
