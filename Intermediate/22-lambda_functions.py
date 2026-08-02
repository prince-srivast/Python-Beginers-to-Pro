#=======================
#   Lambda Functions
#=======================
 # Lambda functions are small anonymous functions defined with `lambda`.
 # They are often used for short operations in a single expression.

# Basic lambda function
add = lambda a, b: a + b
print(add(3, 5))

# Use lambda in sorted()
names = ["Riya", "Amit", "Zara"]
print(sorted(names, key=lambda name: name.lower()))

# Lambda used with map()
numbers = [1, 2, 3, 4]
doubles = list(map(lambda x: x * 2, numbers))
print(doubles)

# Lambda used with filter()
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)
