#=======================
#   File Handling
#=======================
 # File handling lets you read and write data to files.
 # Use `open()` with modes like read, write, and append.

# Write text to a file
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Hello, file handling!\n")
    file.write("This is a sample file.\n")

# Read text from a file
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
print(content)

# Append text to an existing file
with open("sample.txt", "a", encoding="utf-8") as file:
    file.write("Appending a new line.\n")

# Read lines from a file
with open("sample.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# Use `with` to automatically close the file
# Modes:
# r  - read
# w  - write (overwrite)
# a  - append
# r+ - read and write
