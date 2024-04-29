from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flipper
    window.after_cancel(flipper)
    current_card = random.choice(to_learn)
    card_front.itemconfig(canvas_image, image=card_image_french)
    card_front.itemconfig(card_title, text="French", fill='black')
    card_front.itemconfig(card_word, tex=current_card["French"], fill='black')
    flipper = window.after(3000, flip)


def remove():
    to_learn.remove(current_card)
    df = pd.DataFrame(to_learn)
    df.to_csv("./data/words_to_learn.csv")
    next_card()


def flip():
    global current_card
    card_front.itemconfig(canvas_image, image=card_image_english)
    card_front.itemconfig(card_title, text="English", fill='white')
    card_front.itemconfig(card_word, tex=current_card["English"], fill='white')


window = Tk()
window.title("Flash Cards")
window.configure(bg=BACKGROUND_COLOR, pady=50, padx=50)
flipper = window.after(3000, flip)

card_image_french = PhotoImage(file="./images/card_front.png")
card_image_english = PhotoImage(file="./images/card_back.png")
card_front = Canvas(width=800, height=700, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = card_front.create_image(400, 263, image=card_image_french)
card_title = card_front.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = card_front.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
card_front.grid(column=0, row=0, columnspan=2)

right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")
button_right = Button(image=right, command=remove)
button_wrong = Button(image=wrong, command=next_card)
button_right.grid(column=1, row=1)
button_wrong.grid(column=0, row=1)

next_card()
window.mainloop()
