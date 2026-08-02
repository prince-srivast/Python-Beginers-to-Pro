#=======================
#   Dictionaries
#=======================
 # Dictionaries store data as key-value pairs.
 # Keys are unique, and each key maps to a value.

# Create a dictionary
person = {"name": "Prince", "age": 31, "country": "India"}
print(person)
print(type(person))

# Access values by key
print(person["name"])
print(person["age"])

# Add or update a key-value pair
person["city"] = "Mumbai"
print(person)
person["age"] = 32
print(person)

# Remove a key-value pair
del person["country"]
print(person)

# Use get() to safely access a value
print(person.get("name"))
print(person.get("country", "Not found"))

# Dictionary keys can be many types, but must be immutable
mixed_dict = {"name": "Python", 1: "one", (2, 3): "tuple_key"}
print(mixed_dict)

# Iterate over dictionary items
for key, value in person.items():
    print(key, "->", value)

# Get keys and values separately
print(person.keys())
print(person.values())

# Example: nested dictionary
student = {
    "student1": {"name": "Riya", "age": 20},
    "student2": {"name": "Amit", "age": 22}
}
print(student["student1"]["name"])
