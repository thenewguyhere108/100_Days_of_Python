import turtle as t


def move_forward():
    tim.fd(10)

def move_backward():
    tim.bk(10)

def anti_clock():
    tim.left(10)

def clock():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

tim = t.Turtle()
screen = t.Screen()
screen.listen()
screen.onkeypress(move_forward,'w')
screen.onkeypress(move_backward,'s')
screen.onkeypress(anti_clock,'a')
screen.onkeypress(clock,'d')
screen.onkey(clear,'c')

screen.exitonclick()
