from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.x = 0
        self.penup()
        self.goto(x=-30, y=470)
        self.ht()
        self.color('white')
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f'Score : {self.x}', align='center', font=('Courier', 16, 'bold'))

    def game_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write(arg=f'Game Over !!! \nScore : {self.x}', align='center', font=('Courier', 16, 'bold'))
