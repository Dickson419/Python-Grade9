import tkinter as tk
from tkinter import Label


class MyGUI():
    def __init__(self):
        self.root = tk.Tk()

        self.label = Label(self.root, text="Message", font=('Arial', 18))
        self.label.pack(padx=10 ,pady=10)

        self.txt_box = tk.Text(self.root, height=5, font=('Arial', 16))
        self.txt_box.pack(padx=10, pady=10)

        self.check = tk.Checkbutton(self.root, text='Show Message Box')


        self.root.mainloop()
