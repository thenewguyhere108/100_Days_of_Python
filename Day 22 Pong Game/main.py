from turtle import Screen
from score import Score
from players import Players
from ball import Ball
from time import sleep


USER1_POS = -350
USER2_POS = 350
is_game_on = True
screen = Screen()
screen.bgcolor('black')
screen.tracer(0)
screen.setup(height=500, width=800)
score = Score()
ball = Ball()
screen.update()
player_1, player_2 = Players(USER1_POS), Players(USER2_POS)
screen.onkeypress(fun=player_1.move_up, key='w')
screen.onkeypress(fun=player_2.move_up, key='Up')
screen.onkeypress(fun=player_1.move_down, key='s')
screen.onkeypress(fun=player_2.move_down, key='Down')
screen.listen()

while is_game_on:
    score.update_score()
    ball.move()
    ball.detect_wall()
    if (player_1.distance(ball) <= 50 and ball.xcor() <= -320) or (player_2.distance(ball) <= 50 and ball.xcor() >= 320):
        ball.move_speed *= 0.9
        ball.x_change *= -1
    if ball.xcor() > 380:
        ball.ball_restart()
        score.user_score += 1
    elif ball.xcor() < -380:
        ball.ball_restart()
        score.user2_score += 1
    sleep(ball.move_speed)
    screen.update()

screen.exitonclick()
