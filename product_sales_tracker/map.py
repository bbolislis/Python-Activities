import csv
import datetime

product_map = {'P001':['Wireless Headphones',100],
               'P002':['Laptop Backpack',60],
               'P003':['Bluetooth Speaker',50],
               'P004':['USB Flash Drive',20],
               'P005':['Mobile Phone Case',15],
               'P006':['Wireless Mouse',30],
               'P007':['Laptop Stand',40],
               'P008':['HDMI Cable',15],
               'P009':['Smartphone',600],
               'P010':['External Hard Drive',100]}

product_map_csv = []
product_id_list = []
with open('product_sales.txt', 'r') as sales_file:
    reader = sales_file.readlines()
    for line in reader:
        product_id_list.append(line)
        map_item = product_map.get(line.strip())
        date = datetime.date.today()

        new_data = [line.strip(), map_item[0], map_item[1], date]
        product_map_csv.append(new_data)

with open('product_map.csv', 'w', newline='') as new_file:
    writer = csv.writer(new_file)

    writer.writerow(['Product ID', 'Product Name', 'Unit Price', 'Date'])
    writer.writerows(product_map_csv)