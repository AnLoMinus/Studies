from tkinter import *
from tkinter import messagebox

root = Tk()
root.withdraw()

result = messagebox.askretrycancel("Warning","Failed, try again?")
if result is True:
    print("Trying")
else:
    print("Give up")
    