import csv

with open('dad_jokes.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)          # skip first row in the csv file

    for row in csv_reader:
        joke = row[1]
        rating = row[2]

        print(f'"{joke}": joke rating is {rating}')