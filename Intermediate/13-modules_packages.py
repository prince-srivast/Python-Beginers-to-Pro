#=======================
#   Modules and Packages
#=======================
 # Modules group related Python code into files.
 # Packages are collections of modules organized in directories.

# Import a module and use a function from it
import math
print(math.pi)
print(math.sqrt(16))

# Import specific names from a module
from math import factorial, ceil
print(factorial(5))
print(ceil(3.2))

# Alias a module for shorter use
import random as rnd
print(rnd.randint(1, 10))

# Use a module from the Python standard library
import datetime
today = datetime.date.today()
print("Today:", today)

# Example of a custom module import
# Suppose `helper.py` contains a function `greet()` in the same folder.
# from helper import greet
# greet()

# Packages are directories with an __init__.py file.
# Example: import package.module
