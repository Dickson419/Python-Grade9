import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from tkinter import ttk

def load_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        try:
            global data
            data = pd.read_csv(file_path)
            populate_treeview()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV: {e}")

def populate_treeview():
    for item in tree.get_children():
        tree.delete(item)

    for _, row in data.iterrows():
        tree.insert("", "end", values=row.tolist())

def select_isbn():
    isbn = data[data['ISBN'].str.lower() == 'ISBN']
    if not isbn.empty:
        for item in tree.get_children():
            tree.delete(item)

        for _, row in isbn.iterrows():
            tree.insert("", "end", values=row.tolist())
    else:
        messagebox.showinfo("Info", "No cats found.")

# Create main window
root = tk.Tk()
root.title("Animal Viewer")

# Load CSV button
load_button = tk.Button(root, text="Load CSV", command=load_csv)
load_button.pack(pady=10)

# Treeview for displaying data
columns = ("ISBN", "Title", "Author")  # Adjust as needed
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.pack(pady=10)

for col in columns:
    tree.heading(col, text=col)

# Select Cats button
select_isbn_button = tk.Button(root, text="ISBN", command=select_isbn)
select_isbn_button.pack(pady=10)

# Initialize global variable for data
data = None

# Start the application
root.mainloop()
