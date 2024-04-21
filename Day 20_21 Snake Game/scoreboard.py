from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.x = 0
        with open('high_score.txt') as file:
            score = int(file.read())
        self.high_score = score
        self.penup()
        self.goto(x=-30, y=470)
        self.ht()
        self.color('white')
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f'Score : {self.x} High Score : {self.high_score}', align='center', font=('Courier', 16, 'bold'))

    def reset(self):
        if self.x > self.high_score:
            self.high_score = self.x
            with open('high_score.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.x = 0
        self.update()

    def game_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write(arg=f'Game Over !!! \nScore : {self.x}', align='center', font=('Courier', 16, 'bold'))
