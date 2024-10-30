import csv
import tkinter as tk
from tkinter.ttk import Label

# Define a counter variable
counter = 0
books = []  # Declare the global books list

def add():
    global counter
    counter += 1
    label.config(text=f"Count: {counter}")

def subtract():
    global counter
    counter -= 1
    label.config(text=f"Count: {counter}")

def load_csv():
    """Function to load a CSV file into the application and store it in the global books list."""
    global books
    try:
        with open('best_sellers.csv', 'r') as file:
            books = list(csv.reader(file))  # Load the CSV data into the global books list
            # Clear the text box before displaying new content
            csv_display.delete(1.0, tk.END)
            for book in books:
                csv_display.insert(tk.END, f"{', '.join(book)}\n")  # Display each row in the text box
    except FileNotFoundError:
        csv_display.insert(tk.END, "File not found. Please make sure 'best_sellers.csv' exists.")

def display_books():
    """Function to display books data from the global books list into the display_box."""
    pass


# Create the window
root = tk.Tk()

# Setup a title and establish geometry
root.title("My GUI")
root.geometry("800x800")

# Text box for displaying CSV content
csv_display = tk.Text(root, font=('Arial', 14), height=10, width=80)
csv_display.pack(padx=20)

# Text box for other input or display
txt_entry = tk.Entry(root, borderwidth=1, relief="solid")
txt_entry.pack()

# Button to load and display CSV data
btn_load_csv = tk.Button(root, text="Load CSV", font=('Arial, 14'), command=load_csv)
btn_load_csv.pack(pady=10)

# Label for displaying the count
label = tk.Label(root, text="Numbers!", font=('Arial', 18))
label.pack(padx=20, pady=20)

# Another text box for displaying other content
txt_box = tk.Text(root, font=('Arial, 14'), height=3, width=80)
txt_box.pack(padx=20)

# Text box specifically for displaying array (books) values
display_box = tk.Text(root, font=('Arial, 14'), height=3, width=80)
display_box.pack(padx=20)

# Button to display array values
btn_display = tk.Button(root, text='Display Array Values', font=('Arial, 14'), command=display_books)
btn_display.pack(padx=20)

# Entry field
txt_entry = tk.Entry(root, borderwidth=1, relief="solid")
txt_entry.pack()

# Buttons for incrementing and decrementing the count
btn_add = tk.Button(root, text='Add', font=('Arial, 14'), command=add)
btn_add.pack()

btn_sub = tk.Button(root, text='Subtract', font=('Arial, 14'), command=subtract)
btn_sub.pack()

### GRID LAYOUT ###

btn_frame = tk.Frame(root, borderwidth=1, relief="solid")  # raised, sunken, groove, ridge, flat
btn_frame.pack(fill='x')

btn_frame.columnconfigure(0, weight=1)
btn_frame.columnconfigure(1, weight=1)
btn_frame.columnconfigure(2, weight=1)
btn_frame.columnconfigure(3, weight=1)

grid_btn_1 = tk.Button(btn_frame, text='One', font=('Arial, 14'))
grid_btn_1.grid(row=0, column=0, sticky='news')

grid_btn_2 = tk.Button(btn_frame, text='Two', font=('Arial, 14'))
grid_btn_2.grid(row=0, column=1, sticky='news')

grid_btn_3 = tk.Button(btn_frame, text='Three', font=('Arial, 14'))
grid_btn_3.grid(row=0, column=2, sticky='news')

grid_btn_4 = tk.Button(btn_frame, text='Four', font=('Arial, 14'))
grid_btn_4.grid(row=0, column=3, sticky='news')

### Widgets in a specific spot using place() ###
new_btn = tk.Button(root, text='Place', padx=40, pady=10)
new_btn.place(x=200, y=600) #root.geometry("800x800")

# Exit the program
root.mainloop()
