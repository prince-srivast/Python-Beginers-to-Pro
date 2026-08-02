#=======================
#   List Comprehensions
#=======================
 # List comprehensions provide a concise way to create lists.
 # They can replace loops when building list values.

# Simple list comprehension
squares = [x * x for x in range(1, 6)]
print(squares)

# Conditional list comprehension
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)

# Nested list comprehension
pairs = [(x, y) for x in range(1, 4) for y in range(1, 4)]
print(pairs)

# Use functions inside comprehensions
words = ["apple", "banana", "cherry"]
lengths = [len(word) for word in words]
print(lengths)

# Dictionary comprehension
square_dict = {x: x * x for x in range(1, 6)}
print(square_dict)

# Set comprehension
unique_lengths = {len(word) for word in words}
print(unique_lengths)
