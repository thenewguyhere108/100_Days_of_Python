from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)
        self.score_var = StringVar()
        self.score_var.set(f"Score : 0")
        self.scoreboard = Label(textvariable=self.score_var, fg="white",  bg=THEME_COLOR, font=("Arial", 10, "bold"))
        self.scoreboard.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, background="white")
        self.question = self.canvas.create_text(150, 50, text="This is a sample text and it has a lot and lot and lot "
                                                              "of texts", font=("cascade", 16, "normal"),
                                                              fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, columnspan=2, row=1, pady=20)

        true_image = PhotoImage(file="./images/true.png")
        false_image = PhotoImage(file="./images/false.png")
        self.true = Button(image=true_image, command=self.check_true)
        self.false = Button(image=false_image, command=self.check_false)
        self.true.grid(column=0, row=2)
        self.false.grid(column=1, row=2)
        self.get_next_question(None)
        self.window.mainloop()

    def get_next_question(self, option):
        q_text = self.quiz.next_question(option)
        self.update_score()
        self.canvas.itemconfigure(self.question, text=q_text)

    def update_score(self):
        self.score_var.set(f"Score : {self.quiz.score}")
        self.scoreboard.grid(column=1, row=0)

    def check_true(self):
        self.get_next_question(True)

    def check_false(self):
        self.get_next_question(False)
