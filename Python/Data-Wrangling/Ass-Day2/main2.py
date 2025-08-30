import xml.etree.ElementTree as ET

# Create the root element
root = ET.Element("employees")

employee1 = ET.SubElement(root, "employee")

name1 = ET.SubElement(employee1, "name")
name1.text = "Sai Kumar"
age1 = ET.SubElement(employee1, "age")
age1.text = "28"

tree = ET.ElementTree(root)
with open("employees.xml", "wb") as file:
    tree.write(file, encoding="utf-8", xml_declaration=True)