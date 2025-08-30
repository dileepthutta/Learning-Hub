import csv

with open('csv_data.csv','r') as data_file:
    data_rds = csv.DictReader(data_file)
    data_rows = [i for i in data_rds]

with open('csv_data1.csv','r') as header_file:
    header_rds = csv.DictReader(header_file)
    header_rows = [j for j in header_rds]


print(data_rows[2:6])
print(header_rows[:2])
