#=======================
#   Generators
#=======================
 # Generators are functions that yield values one at a time.
 # They save memory because they do not store the entire sequence.

# Simple generator function
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for value in count_up_to(5):
    print(value)

# Generator expression
squares = (x * x for x in range(1, 6))
for square in squares:
    print(square)

# Use next() to get generator values
gen = count_up_to(3)
print(next(gen))
print(next(gen))
print(next(gen))

try:
    print(next(gen))
except StopIteration:
    print("Generator done")
