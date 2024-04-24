from tkinter import *

window = Tk()
window.title("Mile to KM Convertor")
window.minsize()
window.config(height=500, width=500, padx=20, pady=20)


def miles_to_km():
    miles_value = int(miles.get())
    global km, label
    km = round((miles_value*1.6), 2)
    label["ans"] = Label(text=km)
    label["ans"].grid(column=2, row=1, padx=5)


miles = Entry(width=10, justify="center")
miles.focus()
miles.grid(column=2, row=0)
km = 0

label = {"miles": Label(text="Miles")}
label["miles"].grid(column=3, row=0)
label["str"] = Label(text=f"is equal to")
label["str"].grid(column=1, row=1)
label["ans"] = Label(text=km)
label["ans"].grid(column=2, row=1, padx=5)
label["KM"] = Label(text="KM")
label["KM"].grid(column=3, row=1)
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=2, row=2)
window.mainloop()
