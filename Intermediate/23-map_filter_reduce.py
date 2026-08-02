#=======================
#   Map, Filter, Reduce
#=======================
 # map applies a function to every item in a sequence.
 # filter keeps items that match a condition.
 # reduce combines items into a single value.

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map example
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# filter example
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# reduce example
sum_numbers = reduce(lambda a, b: a + b, numbers)
print(sum_numbers)

# Use a named function instead of lambda
def square(x):
    return x * x

squared = list(map(square, numbers))
print(squared)
