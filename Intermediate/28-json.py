#=======================
#   JSON
#=======================
 # JSON is a data format for storing and exchanging structured data.
 # Python uses the `json` module to parse and write JSON.

import json

# Python dictionary to JSON string
person = {"name": "Prince", "age": 31, "city": "Mumbai"}
json_str = json.dumps(person)
print(json_str)

# JSON string to Python dictionary
data = json.loads(json_str)
print(data["name"])

# Write JSON to a file
with open("person.json", "w", encoding="utf-8") as file:
    json.dump(person, file, indent=4)

# Read JSON from a file
with open("person.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)
print(loaded_data)
