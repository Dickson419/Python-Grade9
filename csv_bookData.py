import csv

# Load the CSV file into a list
def open_file(file_path):
    with open("names.csv", newline='') as file:
        books = list(csv.reader(file))
        return books

booklist = open_file('best_sellers.csv')


"""Display each row with its index"""

book_row = 0
for row in booklist:
    display = booklist[book_row]
    print(display)
    book_row += 1


"""Get the contents of a specific column (for example, column 2)"""

column_index = 1  # Choose the column you want to display (indexing starts from 0)

# Print the contents of the specified column
for row in booklist:
    print(row[column_index])


"read into an array - what have we previously done with arrays?"
name_arr = []
for name in booklist:
    name_arr.append(name[column_index])

for i in name_arr:
    print(i, end=' ')

"""Sort the names"""



