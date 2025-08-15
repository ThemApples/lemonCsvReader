import csv
#Python reading program

with open('data.csv', 'r') as file:
     csv_read = csv.reader(file)
     header = next(csv_read)
     for row in csv_read:
         print(row)
