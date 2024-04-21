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

