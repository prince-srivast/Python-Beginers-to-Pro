#=======================
#   Loops
#=======================
 # Loops repeat code multiple times until a condition is met.
 # `for` loops iterate over sequences, while `while` loops repeat until a condition becomes False.

# for loop example
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# for loop with range()
for i in range(1, 6):
    print(i)

# for loop with index using enumerate()
for index, fruit in enumerate(fruits):
    print(index, fruit)

# while loop example
count = 1
while count <= 5:
    print(count)
    count += 1

# while loop with break
number = 1
while True:
    if number > 3:
        break
    print(number)
    number += 1

# while loop with continue
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i)  # prints only odd numbers
