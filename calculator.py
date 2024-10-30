import tkinter as tk
from tkinter import *

# Variables

button_press = ""

# Functions

def press(button):
    global button_press
    button_press += str(button)
    lbl_display.config(text=button_press)

def press_clear():
    global button_press
    button_press = ""
    lbl_display.config(text=button_press)


def add():
    #does the calculator know I press + or - or *...
    #is there a better way?
    pass

def evaluate():
    global button_press
    try:
        result = str(eval(button_press))  #what is the whole calculation?
        lbl_display.config(text=result)
        button_press = result  # Store result for further operations
    except:
        lbl_display.config(text="Error")
        button_press = ""


# Create the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("600x400")
root.configure(bg='#acb2b1')

""" Widgets """

# Buttons
btn_one = Button(root, fg='#67df32', text='1',command=lambda :press('1'))
btn_two = Button(root, text='2',command=lambda :press('2'))
btn_three = Button(root, text='3',command=lambda :press('3'))
btn_four = Button(root, text='4',command=lambda :press('4'))
btn_five = Button(root, text='5',command=lambda :press('5'))
btn_six = Button(root, text='6',command=lambda :press('6'))
btn_seven = Button(root, text='7',command=lambda :press('7'))
btn_eight = Button(root, text='8',command=lambda :press('8'))
btn_nine = Button(root, text='9',command=lambda :press('9'))
btn_zero = Button(root, text='0',command=lambda :press('10'))
btn_addition = Button(root, text='+',command=lambda :press('+'))
btn_subtraction = Button(root, text='-',command=lambda :press('-'))
btn_multiplication = Button(root, text='*',command=lambda :press('*'))
btn_division = Button(root, text='/',command=lambda :press('/'))
btn_clear = Button(root, text='C', command=lambda :press_clear())
btn_decimal = Button(root, text='.',command=lambda :press('.'))
btn_equals = Button(root, text='=',command= lambda :evaluate())


# Display
lbl_display = Label(root, text='', fg='red')

""" Define the grid - take window/frame and configure """

root.columnconfigure(0, weight=1, uniform='a') #takes starting index and how wide column will be
root.columnconfigure(1, weight=1,uniform='a')
root.columnconfigure(2, weight=1,uniform='a')
root.columnconfigure(3, weight=1,uniform='a')

root.rowconfigure(0, weight=1,uniform='a')
root.rowconfigure(1, weight=1,uniform='a')
root.rowconfigure(2, weight=1,uniform='a')
root.rowconfigure(3, weight=1,uniform='a')
root.rowconfigure(4, weight=1,uniform='a')
root.rowconfigure(5, weight=1,uniform='a')

""" Place the widgets """
btn_zero.grid(row=5,column=0, columnspan=2, sticky='nesw',pady=1,padx=1, ipadx=4,ipady=4)
btn_decimal.grid(row=5,column=2, columnspan=1, sticky='nesw',pady=1,padx=1, ipadx=4,ipady=4)
btn_equals.grid(row=5,column=3, columnspan=1, sticky='nesw',pady=1,padx=1, ipadx=4,ipady=4)


btn_one.grid(row=4, column=0, sticky='nesw',pady=1, padx=1, ipadx=4,ipady=4)
btn_two.grid(row=4, column=1, sticky='nesw',pady=1, padx=1, ipadx=4,ipady=4)
btn_three.grid(row=4, column=2, sticky='nesw',pady=1, padx=1, ipadx=4,ipady=4)
btn_addition.grid(row=4, column=3, sticky='nesw',pady=1, padx=1, ipadx=4,ipady=4)

btn_four.grid(row=3, column=0, sticky='nesw',pady=1, padx=1, ipadx=4,ipady=4)
btn_five.grid(row=3, column=1, sticky='nesw',pady=1, padx=1, ipadx=4,ipady=4)
btn_six.grid(row=3, column=2, sticky='nesw',pady=1, padx=1, ipadx=4,ipady=4)
btn_subtraction.grid(row=3, column=3, sticky='nesw',pady=1, padx=1, ipadx=4,ipady=4)

btn_seven.grid(row=2, column=0, sticky='nesw',pady=1, padx=1, ipadx=4,ipady=4)
btn_eight.grid(row=2, column=1, sticky='nesw',pady=1, padx=1, ipadx=4,ipady=4)
btn_nine.grid(row=2, column=2, sticky='nesw',pady=1, padx=1, ipadx=4,ipady=4)
btn_multiplication.grid(row=2, column=3, sticky='nesw',pady=1, padx=1, ipadx=4,ipady=4)

btn_clear.grid(row=1,column=0, columnspan=3, sticky='nesw',pady=1,padx=1, ipadx=4,ipady=4)
btn_division.grid(row=1, column=3, sticky='nesw',pady=1, padx=1, ipadx=4,ipady=4)

lbl_display.grid(row=0, columnspan=4,sticky='nesw')




















# Start the Tkinter event loop
root.mainloop()
