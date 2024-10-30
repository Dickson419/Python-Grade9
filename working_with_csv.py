import csv

def open_csv(file_path):
    """ function to read in a csv file. What are the roles of try and catch doing? We have them? """
    try:
        with open(file_path, 'r') as file:
            items = list(csv.reader(file))
            return items
    except FileNotFoundError:
        print(f"{file_path} not found")
        return None

csv_items = open_csv('best_sellers.csv')
books = []
for i in csv_items:
    #print(i)
    books.append(i)

print("\n\n\n")

"""Attempt using the books array"""

book_titles = 2 #an index number can be set this way...
print(books[book_titles])

# alternatively - use the .index() to get the correct column number
#book_title = books[0].index('title')

"""
print(books) - all rows and columns
print(books[1]) - first row
splice - print(books[1:]) - exclude the column headings

"""

all_titles = []
book_title = books[0].index('title') #can be used to search/get the correct index
for title in books[1:]:
    print(title[book_title])
    all_titles.append(title[book_title])

print(all_titles)
all_titles.sort() #how else could we sort?
print(all_titles)

#IF Hamlet in all_titles:
#   OUTPUT found!
# ^^^ How could a search be implemented?

