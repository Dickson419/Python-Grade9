import tkinter as tk
from tkinter import *

# Create the main application window
root = tk.Tk()
root.title("Grid Layout")
root.geometry("600x400")
root.configure(bg='#acb2b1')

""" Widgets """

label_one = Label(root, text="One", background='red')
label_two = Label(root, text='Two', background='blue')
label_three = Label(root, text='Three', background='green')
label_four = Label(root, text='Four', background='yellow')
btn_one = Button(root, text='Button One')
btn_two = Button(root, text='Button Two')

""" Define the grid - take window/frame and configure """

root.columnconfigure(0, weight=1, uniform='a') #takes starting index and how wide column will be
root.columnconfigure(1, weight=1,uniform='a')
root.columnconfigure(2, weight=1,uniform='a')
root.columnconfigure(3, weight=1,uniform='a')
root.rowconfigure(0, weight=1,uniform='a')
root.rowconfigure(1, weight=1,uniform='a')
root.rowconfigure(2, weight=1,uniform='a')

""" Place the widgets """
label_one.grid(row=0, column=0, pady=10, padx=10, sticky='nesw')
label_two.grid(row=0, column=1, sticky='nesw', pady=10, padx=10)
label_three.grid(row=1, column=0, sticky='nesw',pady=10, padx=10)
label_four.grid(row=1, column=1, sticky='nesw',pady=10, padx=10)
btn_one.grid(row=0, column=3, rowspan=2, sticky='nesw',pady=10, padx=10)
btn_two.grid(row=2, column=0, columnspan= 4, sticky='nesw',pady=10, padx=10)



















# Start the Tkinter event loop
root.mainloop()
