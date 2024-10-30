import pandas as pd

def load_file(file):
    data = pd.read_csv(file)
    print(data)

def delete_row(file, row_name):
    file.drop(row_name)


books = load_file('best_sellers.csv')
find = 'Breaking'



