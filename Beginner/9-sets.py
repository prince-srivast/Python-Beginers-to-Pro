#=======================
#   Sets
#=======================
 # Sets are unordered collections of unique values.
 # They do not allow duplicate items and are useful for membership tests.

# Create a set
fruits = {"apple", "banana", "cherry"}
print(fruits)
print(type(fruits))

# Sets are unordered, so the output order may vary.

# Add an item to the set
fruits.add("orange")
print(fruits)

# Remove an item from the set
fruits.remove("banana")
print(fruits)

# Use discard() to remove an item without error if missing
fruits.discard("banana")
print(fruits)

# Check membership
print("apple" in fruits)   # True
print("banana" in fruits)  # False

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a.union(set_b))        # {1, 2, 3, 4, 5, 6}
print(set_a.intersection(set_b)) # {3, 4}
print(set_a.difference(set_b))   # {1, 2}
print(set_a.symmetric_difference(set_b))  # {1, 2, 5, 6}

# Convert a list with duplicates to a set to remove duplicates
numbers = [1, 2, 2, 3, 3, 3]
unique_numbers = set(numbers)
print(unique_numbers)
