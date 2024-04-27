import json
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


def search():
    website = box_website.get()
    if website == "":
        messagebox.showerror(title="Search", message="Website field empty")
    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror(title="Search", message="Data File not found")
        else:
            try:
                messagebox.showinfo(title="Search", message=f"Website: {website}\nEmail: {data[website.title()]["email"]}\n"
                                                            f"Password: {data[website.title()]["password"]}")
            except KeyError:
                messagebox.showerror(title="Search", message="Website not found")


def save():
    website = box_website.get()
    email = box_email.get()
    password = box_password.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Empty fields", message="Please don't leave any fields empty")
    else:
        data = {website.title(): {"email": email.lower(), "password": password}}
        try:
            with open(file="data.json", mode="r") as file:
                data_old = json.load(file)
        except FileNotFoundError:
            with open(file="data.json", mode="w") as file:
                json.dump(data, file, indent=4)
        else:
            data_old.update(data)
            with open(file="data.json", mode="w") as file:
                json.dump(data_old, file, indent=4)
        finally:
            box_password.delete(0, END)
            box_website.delete(0, END)

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
box_website = Entry(width=25)
box_website.grid(column=1, row=1)

label_email = Label(text="Email / Username:", fg="black", bg="white")
label_email.grid(column=0, row=2,)
box_email = Entry(width=25)
box_email.insert(0, "sandyorton7@gmail.com")
box_email.grid(column=1, row=2, columnspan=1)

label_password = Label(text="Password:", fg="black", bg="white")
label_password.grid(column=0, row=3)
box_password = Entry(width=25)
box_password.grid(column=1, row=3)

button_generate = Button(text="Generate Password", command=passwd)
button_generate.grid(column=2, row=3)
button_add = Button(text="Add", justify="center", command=save, width=36)
button_add.grid(row=4, column=1, columnspan=2)
button_search = Button(text="Search", command=search, width=15)
button_search.grid(column=2, row=1)
window.mainloop()
