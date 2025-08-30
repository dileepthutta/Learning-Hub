# import json
# data = {
#             "Name" : "Vijay",
#             "Age"  :  30,
#             "City" : "Vizag",
#             "married": "No"
# }
# with open('bio_data.json',mode='w')as file:
#     json.dump(data,file,indent=4)
#
# #Reading xml file:
























import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('data.xml')
root = tree.getroot()

for employee in root.findall('employee'):
    name = employee.find('name').text
    age = employee.find('age').text
print(f"Name: {name}, Age: {age}")