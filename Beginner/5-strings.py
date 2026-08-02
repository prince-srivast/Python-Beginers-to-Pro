#=======================
#   Strings
#=======================
 # Strings are sequences of characters used to store text.
 # Each character has a position called an index, starting at 0.

# Create a string
text = "Hello, Python"
print(text)
print(type(text))

# Access characters by index
# The first character is at index 0.
print(text[0])  # H
print(text[1])  # e

# Negative index counts from the end
print(text[-1])  # n
print(text[-2])  # o

# String slicing returns a substring
# text[start:end] gives characters from start to end-1.
print(text[0:5])  # Hello
print(text[7:13])  # Python

# Omit start or end to slice from beginning or to the end
print(text[:5])   # Hello
print(text[7:])   # Python

# Get the length of a string
the_length = len(text)
print("Length:", the_length)

# Strings are immutable, so you cannot change a character directly
# The following would cause an error if uncommented:
# text[0] = 'h'

# Use string methods to transform text
print(text.upper())   # HELLO, PYTHON
print(text.lower())   # hello, python
print(text.replace("Python", "World"))  # Hello, World

# Check if a substring exists in the text
print("Python" in text)  # True
print("java" in text)    # False

# Example using formatted strings with indexes and variables
first_word = text.split()[0]
second_word = text.split()[1]
print(f"First word: {first_word}, Second word: {second_word}")
