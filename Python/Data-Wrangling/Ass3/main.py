import xml.etree.ElementTree as ET

from pandas import read_xml

tree = ET.parse("data.xml")
root = tree.getroot()

# To Extract text from the each row element
string_list = [row.text for row in root.findall('row')]

print(string_list)