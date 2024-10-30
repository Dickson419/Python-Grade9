import csv


""" open a csv file """

with open('books.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if row:
            print(row) # or... row[1]

""" count data/identify data"""

print("\n\n")

count = 0
with open('books.csv', 'r') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        if float(row["RRP"]) > 10.00:
            #count = count + 1
            count += 1
            print(f"{row['Title']} costs {row['RRP']} ")

    print("The total count of books over 10.00 is ", count)

"""Add data i.e title, author etc"""

isbn = int(input("Enter the ISBN: "))
title = input("Enter the title of the book: ")
author = input("Enter the author of the book: ")
publisher = input("Enter the publisher of the book: ")
rrp = float(input("Enter the price: "))
date = input("Enter the date: ")


with open('books.csv', 'a', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow([isbn, title, author, publisher, rrp, date])






