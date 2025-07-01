import csv

with open('expensive_pets.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(['name', 'species', 'favorite_snack', 'monthly_cost'])

    csv_writer.writerows([['Max', 'dog', 'bacon strips', '4754'],
                          ['Cal', 'cat', 'edibles', '1142'],
                          ['Lena', 'cat', 'sheba', '1420'],
                          ['Bruiser', 'fish', 'fish pellets', '540']])