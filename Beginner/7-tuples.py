#=======================
#  Tuples
#=======================
 # Tuples are ordered collections of items that cannot be changed.
 # They are similar to lists, but immutable after creation.

# Create a tuple
a = (1, 2, 3, 4, 5)
print(a)
print(type(a))

# Access items by index
print(a[0])  # 1
print(a[2])  # 3

# Negative index counts from the end
print(a[-1])  # 5
print(a[-2])  # 4

# Tuple slicing returns a new tuple
print(a[1:4])  # (2, 3, 4)
print(a[:3])   # (1, 2, 3)
print(a[2:])   # (3, 4, 5)

# Tuples are immutable, so the next line is not allowed
# a[0] = 10

# You can combine tuples
a2 = (6, 7, 8)
combined = a + a2
print(combined)

# Get tuple length
print(len(a))

# Single-item tuple requires a comma
single_item = (10,)
print(single_item)
print(type(single_item))

# Convert a list to a tuple
list_to_tuple = tuple([1, 2, 3])
print(list_to_tuple)

# Example: unpack tuple values
x, y, z = (100, 200, 300)
print(x, y, z)
