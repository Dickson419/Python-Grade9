import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("My First GUI")
root.geometry("1000x700")

btn_one = Button(root, text='Button One')
btn_one.pack(padx=20, pady=30)

btn_two = Button(root, text='Button Two')
btn_two.pack(pady=10)


root.mainloop()