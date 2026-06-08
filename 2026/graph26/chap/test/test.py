import tkinter as tk

root = tk.Tk()
root.title("test")
root.geometry("300x200")

label = tk.Label(root, text="hello tkinter")
label.pack()

button = tk.Button(root, text="exit", command=root.destroy)
button.pack()

root.mainloop()