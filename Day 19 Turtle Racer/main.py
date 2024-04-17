import turtle as t
import random as r

colors = ['red', 'blue', 'green', 'orange', 'purple', 'pink']
screen = t.Screen()
screen.title('Turtle Racer')
screen.setup(width=500, height=400)
is_race_on = True


class Cars:
    def __init__(self):
        self.turtle = t.Turtle(shape='turtle')
        self.color = r.choice(colors)
        self.turtle.color(self.color)
        colors.remove(self.color)


racers = [Cars(), Cars(), Cars(), Cars(), Cars(), Cars()]
y = 150

for i in racers:
    i.turtle.penup()
    i.turtle.goto(y=y, x=-230)
    y -= 60

user_bet = screen.textinput('Place your bet', 'Enter the color of the turtle that you want to bet on?').lower()

while is_race_on:
    for i in racers:
        i.turtle.fd(r.randint(0, 10))
        if i.turtle.xcor() > 230:
            is_race_on = False
        if not is_race_on:
            winner = i.turtle.pencolor()
            if user_bet == winner:
                print(f"You've won !! , The {winner} turtle is the winner")
            else:
                print(f"You've lost , The {winner} turtle is the winner")
            break

screen.exitonclick()
