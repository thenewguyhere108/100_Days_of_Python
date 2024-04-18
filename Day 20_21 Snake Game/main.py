from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

is_game_on = True
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='a')
screen.onkey(fun=snake.right, key='d')
screen.onkey(fun=snake.up, key='w')
screen.onkey(fun=snake.down, key='s')
snake.move()

while is_game_on:
    screen.update()
    snake.move()
    time.sleep(0.1)
    if snake.head.distance(food) < 15:
        score.x += 1
        score.update()
        food.move()
        snake.extend()
    if snake.head.xcor() > 480 or snake.head.xcor() < -480 or snake.head.ycor() > 480 or snake.head.ycor() < -480:
        score.game_over()
        is_game_on = False
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()
