#=======================
#   Lists
#=======================
 # Lists are ordered collections of items that can be changed.
 # They can contain mixed data types and allow duplicate values.

# Create a list
numbers = [10, 20, 30, 40, 50]
print(numbers)
print(type(numbers))

# Access items by index
print(numbers[0])  # 10
print(numbers[2])  # 30

# Negative index counts from the end
print(numbers[-1])  # 50
print(numbers[-2])  # 40

# List slicing returns a new list
print(numbers[1:4])  # [20, 30, 40]
print(numbers[:3])   # [10, 20, 30]
print(numbers[2:])   # [30, 40, 50]

# Change list items
numbers[0] = 15
print(numbers)  # [15, 20, 30, 40, 50]

# Add items to the list
numbers.append(60)
print(numbers)

# Insert an item at a specific position
numbers.insert(2, 25)
print(numbers)

# Remove items from the list
numbers.remove(40)
print(numbers)

# Pop removes and returns the last item by default
last_item = numbers.pop()
print(last_item)
print(numbers)

# Get list length
print(len(numbers))

# Lists can contain different data types
mixed_list = ["Python", 3.14, True, 42]
print(mixed_list)

# Example: loop over a list
for item in numbers:
    print(item)
