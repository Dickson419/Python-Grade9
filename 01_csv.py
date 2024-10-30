import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import title

"""Open a csv file"""
with open('books.csv', 'r') as file:
    csv_reader = csv.reader(file) #reader creates an object which is used to iterate over a csv file
    for row in csv_reader:
        if row:
            print(row[1])


print("\n\n")

"""Open the CSV file but use the column headings - this makes use of a dictionary data structure"""
with open('books.csv', 'r') as file:
    # read the CSV file into dictionaries where the keys are the headers and the values are the data in each row.
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)  # Each row is a dictionary with column names as keys


"""Processing data"""

print("\n\n")

count = 0
with open('books.csv', 'r') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        if float(row["RRP"]) > 10.00:
            count += 1
            print(f"{row['Title']} costs {row['RRP']}")

    print(f"\ntotal count of books over $10.00 = {count}")


"""Adding data"""
# Get user input for a new book entry

isbn = int(input("Enter the ISBN: "))
title = input("Enter the book title: ")
author = input("Enter the author name: ")
publisher = input("Enter the publisher of the book: ")
price = float(input("Enter the RRP of the book: "))
year = input("Enter the year of publication: ")

# Open the CSV file in append mode to add a new row
with open('books.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    # Write the user input as a new row in the CSV file
    writer.writerow([isbn, title, author, publisher, price, year])









#
# # Load the CSV data
# file_path = 'books.csv'  # Change this to the actual path of your CSV file
# df = pd.read_csv(file_path)
#
# # Sort the data by publication date
# df = df.sort_values('Publ Date')
#
# # Example: Creating a bar chart showing the number of books per author
# author_counts = df['Author'].value_counts()
#
# # Plotting the bar chart
# author_counts.plot(kind='bar', color='skyblue')
#
# # Adding labels and title
# plt.xlabel('Author')
# plt.ylabel('Number of Books')
# plt.title('Number of Books by Author')
#
# # Show the chart
# plt.show()