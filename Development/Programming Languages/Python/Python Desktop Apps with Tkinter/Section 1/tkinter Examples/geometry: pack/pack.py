from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

l1 = Label(frame, text="Tkinter Label", bg="red", fg="white")
l1.pack()

l2 = Label(frame, text="Tkinter Label", bg="yellow", fg="black")
l2.pack()

l3 = Label(frame, text="Tkinter Label", bg="blue", fg="white")
l3.pack()

mainloop()
