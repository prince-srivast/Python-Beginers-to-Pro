#=======================
#   CSV
#=======================
 # CSV files store tabular data in plain-text rows and columns.
 # Python uses the `csv` module to read and write CSV files.

import csv

# Write CSV data to a file
rows = [
    ["name", "age", "country"],
    ["Prince", 31, "India"],
    ["Riya", 20, "USA"]
]
with open("people.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

# Read CSV data from a file
with open("people.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Use DictReader to work with dictionaries
with open("people.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["age"], row["country"])
