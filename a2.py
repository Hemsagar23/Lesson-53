from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def msg():
    messagebox.showwarning("#^@#^ Getting Hacked %#@%#","Attention Please, You are being hacked.. pay 100$ immedietly to save your computer.")

button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=80)

root.mainloop()