from turtle import Turtle
MOVE_DISTANCE = 20


class Players:
    def __init__(self, pos):
        self.bar = self.create_stick(pos)

    def create_stick(self, pos):
        stick = []
        for i in (40, 20, 0, -20, -40):
            tim = Turtle('square')
            tim.color('white')
            tim.speed('fastest')
            tim.penup()
            tim.goto(x=pos, y=i)
            stick.append(tim)
        return stick

    def move_up(self):
        pos = None
        if self.bar[0].ycor() < 240:
            print(self.bar[0].ycor())
            for i in range(5):
                if i == 0:
                    self.bar[i].setheading(90)
                    pos = list(self.bar[i].pos())
                    self.bar[i].fd(20)
                else:
                    temp_pos = list(self.bar[i].pos())
                    self.bar[i].goto(x=pos[0], y=pos[1])
                    pos = temp_pos

    def move_down(self):
        pos = None
        if self.bar[-1].ycor() > -240:
            print(self.bar[0].ycor())
            for i in range(-1, -6, -1):
                if i == -1:
                    self.bar[i].setheading(270)
                    pos = list(self.bar[i].pos())
                    self.bar[i].fd(20)
                else:
                    temp_pos = list(self.bar[i].pos())
                    self.bar[i].goto(x=pos[0], y=pos[1])
                    pos = temp_pos

