import pandas as pd
import csv
import json


# #Reading a CSV File.
data = pd.read_csv('data.csv')
print(data)


#Writing  to a csv FIle.
data1 = [
    ["Name","Age"],
    ["Arjun",39],
    ["Vijay",30],
    ["Suriya",39],
]
with open('new_data.csv',mode='w',newline='\n') as file:
    writer = csv.writer(file)
    writer.writerow(data1)
    print("File created succesfully !")


#Reading JSON Data:
with open ('data.json',mode='r') as file:
    data = json.load(file)
print(f"JSON Data\n{data}")












