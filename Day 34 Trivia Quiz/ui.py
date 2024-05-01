from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)
        self.score = 0
        self.score_var = StringVar()
        self.score_var.set(f"Score : 0")
        self.scoreboard = Label(textvariable=self.score_var, fg="white", bg=THEME_COLOR, font=("Arial", 10, "bold"))
        self.scoreboard.grid(column=1, row=0)
        self.flasher = None

        self.canvas = Canvas(height=250, width=300, background="white")
        self.question = self.canvas.create_text(150, 100, text="This is a sample text and it has a lot and lot and lot "
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
        if self.flasher is not None:
            self.canvas.after_cancel(self.flasher)
        if option is not None:
            if self.quiz.check_score(option):
                self.flash("Green")
                self.score += 1
                self.score_var.set(f"Score : {self.score}")
                self.scoreboard.grid(column=1, row=0)
            else:
                self.flash("Red")
        q_text = self.quiz.next_question()
        self.canvas.itemconfigure(self.question, text=q_text)

    def check_true(self):
        if self.quiz.still_has_question():
            self.get_next_question("True")
        else:
            self.game_over()

    def check_false(self):
        if self.quiz.still_has_question():
            self.get_next_question("False")
        else:
            self.game_over()

    def game_over(self):
        self.true.destroy()
        self.false.destroy()
        self.scoreboard.destroy()
        self.canvas.itemconfigure(self.question, text=f"Quiz Completed\n Score : {self.score}")

    def flash(self, colour):
        self.canvas.configure(background=colour)
        self.flasher = self.canvas.after(100, self.reset_background)

    def reset_background(self):
        self.canvas.configure(background="White")
        self.flasher = None
