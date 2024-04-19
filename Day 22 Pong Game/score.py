from turtle import Turtle

FONT = 'Arial'
FONT_SIZE = 50


class Score:
    def __init__(self):
        self.middle_line = []
        self.create_middle_line()
        self.user_score, self.user2_score = 0, 0
        self.usr_board = self.score_board('user', -140, 180)
        self.usr2_board = self.score_board('pc', 100, 180)
        pass

    def create_middle_line(self):
        j = 0
        for i in range(-480, 481, 20):
            if j < 2:
                square = Turtle('square')
                square.shapesize(stretch_wid=0.3, stretch_len=0.2)
                square.color('white')
                square.penup()
                square.speed('fastest')
                square.goto(x=0, y=i)
                self.middle_line.append(square)
            else:
                j = 0

    def score_board(self, name, pos_x, pos_y):
        score = Turtle()
        score.ht()
        score.color('white')
        score.penup()
        score.goto(x=pos_x, y=pos_y)
        if name == 'user':
            score.write(self.user_score, font=(FONT, FONT_SIZE, "bold"))
        elif name == 'pc':
            score.write(self.user2_score, font=(FONT, FONT_SIZE, "bold"))
        return score

    def update_score(self):
        self.usr_board.clear()
        self.usr2_board.clear()
        self.usr_board.write(self.user_score, font=(FONT, FONT_SIZE, "bold"))
        self.usr2_board.write(self.user2_score, font=(FONT, FONT_SIZE, "bold"))
