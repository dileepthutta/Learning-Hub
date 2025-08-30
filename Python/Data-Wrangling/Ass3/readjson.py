# READ EACH ROW FROM A JSON FILE AND PRINT A LIST OF STRINGS.
import json

from pandas import read_json

with open('json_data.json','r',encoding='utf-8') as file_data:
    data = json.load(file_data)

string_list = [str(item) for item in data]
print(f"JSON Data :\n{read_json('json_data.json')}\n")

print(f"Converted into list \n{string_list}")
