from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_var = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_time():
    global reps
    if timer_var is not None:
        tomato.after_cancel(timer_var)
    check_box.configure(text="")
    work_mode.configure(text="Timer")
    tomato.itemconfigure(timer_text, text="00:00")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps, work_mode
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        work_mode.configure(text="Long Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        work_mode.configure(text="Short Break", fg=PINK)
        count_down(short_break_sec)
        checks = "✔" * int(reps / 2)
        check_box.configure(text=checks)
    else:
        work_mode.configure(text="Focus", fg=GREEN)
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minutes = int(count / 60)
    seconds = count % 60
    if minutes < 10:
        if minutes == 0:
            minutes = "00"
        else:
            minutes = f"0{minutes}"
    if seconds < 10:
        if seconds == 0:
            seconds = "00"
        else:
            seconds = f"0{seconds}"
    if count > 0:
        tomato.itemconfigure(timer_text, text=f"{minutes}:{seconds}")
        global timer_var
        timer_var = window.after(1000, count_down, count - 1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=20, pady=20, bg=YELLOW)
window.title("Pomodoro")

tomato = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
tomato.create_image(100, 112, image=image)
timer_text = tomato.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
tomato.grid(column=1, row=1)

start = Button(text="Start",  font=(FONT_NAME, 15, "normal"), command=start_timer)
start.grid(column=0, row=2,)

reset = Button(text="Reset",  font=(FONT_NAME, 15, "normal"), command=reset_time)
reset.grid(column=2, row=2,)

check_box = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
check_box.grid(column=1, row=3)

work_mode = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
work_mode.grid(column=1, row=0)

window.mainloop()
