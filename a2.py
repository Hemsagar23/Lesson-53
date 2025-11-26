from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def msg():
    messagebox.showwarning("#^@#^ Getting Hacked %#@%#","ATT3NT10N PL3AS3! Y0UR SYS7EM H4S B33N C0MPR0M1S3D... P4Y $100 1MM3D14T3LY T0 SAV3 Y0UR MACH1N3")

button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=80)

root.mainloop()