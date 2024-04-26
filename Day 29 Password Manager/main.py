from tkinter import *
from password_generator import generate_password
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def passwd():
    box_password.delete(0, END)
    box_password.insert(0, generate_password())
    pyperclip.copy(box_password.get())

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = box_website.get()
    email = box_email.get()
    password = box_password.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Empty fields", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail:{email} \n"
                                                              f"Password: {password}\nConfirm?")
        box_website.delete(0, END)
        box_password.delete(0, END)
        if is_ok:
            data = f"{website} | {email} | {password}\n"
            with open(file="data.txt", mode="a") as file:
                file.write(data)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manger")
window.configure(bg="white", padx=50, pady=50)

canvas = Canvas(height=200, width=200, bg="white", highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:", fg="black", bg="white")
label_website.grid(column=0, row=1, )
box_website = Entry(width=35)
box_website.grid(column=1, row=1, columnspan=2)

label_email = Label(text="Email / Username:", fg="black", bg="white")
label_email.grid(column=0, row=2, )
box_email = Entry(width=35)
box_email.insert(0, "sandyorton7@gmail.com")
box_email.grid(column=1, row=2, columnspan=2)

label_password = Label(text="Password:", fg="black", bg="white")
label_password.grid(column=0, row=3)
box_password = Entry(width=21)
box_password.grid(column=1, row=3)

button_generate = Button(text="Generate Password", command=passwd)
button_generate.grid(column=2, row=3)
button_add = Button(text="Add", justify="center", command=save, width=36)
button_add.grid(row=4, column=1, columnspan=2)
window.mainloop()
