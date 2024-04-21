from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.create()

    def create(self):
        self.penup()
        self.teleport(x=-280, y=280)
        self.ht()
        self.write(f'Level : {self.score}', align='left', font=('Cascade', 10, "bold"))

    def update(self):
        self.clear()
        self.write(f'Level : {self.score}', align='left', font=('Cascade', 10, "bold"))

    def game_over(self):
        self.goto(x=-0, y=0)
        self.write("Game Over !!!", align='center', font=('Cascade', 16, "bold"))