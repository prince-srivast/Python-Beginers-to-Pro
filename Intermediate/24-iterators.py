#=======================
#   Iterators
#=======================
 # Iterators provide a way to access elements one at a time.
 # Iterables return iterators with the iter() function.

# Create an iterator from a list
numbers = [1, 2, 3]
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))

# StopIteration is raised when the iterator is exhausted
try:
    print(next(iterator))
except StopIteration:
    print("Iterator finished")

# Create a custom iterator class
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

countdown = CountDown(3)
for num in countdown:
    print(num)
