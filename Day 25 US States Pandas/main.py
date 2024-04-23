import turtle
import pandas as pd
screen = turtle.Screen()
screen.setup(height=491, width=725)
screen.title("U.S States Game")
screen.bgpic("blank_states_img.gif")
score = 0
answers = []
data = pd.read_csv("50_states.csv")
data_list = data.set_index("state").T.to_dict("list")
missing_states = []


def create_turtle(x, y, name):
    global answers
    tim = turtle.Turtle()
    tim.ht()
    tim.penup()
    tim.goto(x, y)
    tim.write(name, align='center', font=("Casper", 8, "normal"))


while score < 50:
    choice = screen.textinput(title=f"{score}/50 Guess the state", prompt="Enter the name of a state")
    choice = choice.title()
    if choice == "Exit":
        missing_states = [n for n in data_list if n not in answers]
        df = pd.DataFrame(missing_states)
        df.to_csv("missing_states.csv")
        break
    if choice in data_list.keys():
        answers.append(choice)
        score += 1
        create_turtle(data_list[choice][0], data_list[choice][1], choice)
turtle.mainloop()
