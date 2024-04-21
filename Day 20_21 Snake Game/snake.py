from turtle import Turtle

STARTING_POSITIONS = [(-40, 0), (-20, 0), (0, 0), (20, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake = []
        self.pos = []
        self.temp_pos = None
        self.x_loc = 0
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def add_segment(self, position):
        tim = Turtle("square")
        tim.penup()
        tim.color('white')
        tim.goto(position)
        self.snake.append(tim)

    def move(self):
        self.pos = []
        for i in range(0, len(self.snake)):
            if i == 0:
                self.pos = list(self.snake[i].pos())
                self.snake[i].fd(MOVE_DISTANCE)
            else:
                self.temp_pos = list(self.snake[i].pos())
                self.snake[i].teleport(x=self.pos[0], y=self.pos[1])
                self.pos = self.temp_pos

    def left(self):
        if self.snake[0].heading() == 90 or self.snake[0].heading() == 270:
            self.snake[0].setheading(180)

    def right(self):
        if self.snake[0].heading() == 90 or self.snake[0].heading() == 270:
            self.snake[0].setheading(0)

    def up(self):
        if self.snake[0].heading() == 0.00 or self.snake[0].heading() == 180:
            self.snake[0].setheading(90)

    def down(self):
        if self.snake[0].heading() == 0.00 or self.snake[0].heading() == 180:
            self.snake[0].setheading(270)

    def reset(self):
        for i in self.snake:
            i.ht()
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
