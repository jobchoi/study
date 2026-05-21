from tkinter import *


root = Tk()

button = Button(root, text="Click me")

button["fg"] = "yellow"
button["bg"] = "green"

button.pack()


root.mainloop()