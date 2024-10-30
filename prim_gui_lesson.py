import tkinter as tk
from tkinter import messagebox

"""All functions for the program"""
def add_to_listbox():
    """Used to add a name to list display"""
    name = entry.get()
    if name:
        listbox.insert(tk.END, name)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a name.")

def save_to_file():
    """A function to save items to a text file - needs finishing!"""

    #with open("", "w") as f:
        # Iterate over all items in the listbox
        #for item in listbox.get(0, tk.END):
            #f.write()
    #messagebox.showinfo("Success", "Listbox items saved to listbox_items.txt")
    pass

def delete_from_listbox():
    """A function to delete the selected item from the listbox"""
    try:
        # Get the currently selected item index
        selected_index = listbox.curselection()[0]
        # Delete the selected item from the listbox
        listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select an item to delete.")

def read_from_file():
    """A function to read names from a text file and add them to the listbox"""
    try:
        with open("listbox_items.txt", "r") as f:
            listbox.delete(0, tk.END)  # Clear the current listbox content
            for line in f:
                name = line.strip()  # Remove any extra whitespace/newline
                listbox.insert(tk.END, name)
        messagebox.showinfo("Success", "Names loaded from listbox_items.txt")
    except FileNotFoundError:
        messagebox.showerror("Error", "listbox_items.txt not found.")

# Initialize the main window
root = tk.Tk()
root.title("Tkinter Example")
root.geometry("400x400")

# Frame
frame = tk.Frame(root, bd=2, relief="sunken")
frame.pack(pady=10)

# Label
label = tk.Label(frame, text="Enter your name:")
label.pack(side="left", padx=5)

# Entry
entry = tk.Entry(frame)
entry.pack(side="left", padx=5)




# Button
button = tk.Button(root, text="Add to List", command=add_to_listbox)
button.pack(pady=10)

# Listbox
listbox = tk.Listbox(root)
listbox.pack(pady=10)

# Save to file Button
save_btn = tk.Button(root, text='Save', command=save_to_file)
# something missing?

# Delete item button --> add later!
# TO DO!


# Menu - top bar menu (top of page)
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)




# Start the main event loop
root.mainloop()
