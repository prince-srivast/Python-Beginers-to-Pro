#=======================
#   Functions
#=======================
 # Functions are reusable blocks of code that perform a task.
 # They help organize code and avoid repetition.

# Define a function
def greet():
    print("Hello from the function!")

# Call the function
greet()

# Function with parameters
def add(a, b):
    # a and b are parameters used inside the function.
    result = a + b
    print("Sum:", result)

add(5, 7)

# Function with return value
def multiply(a, b):
    return a * b

product = multiply(3, 4)
print("Product:", product)

# Function with default parameter values
def power(base, exponent=2):
    return base ** exponent

print(power(5))      # uses default exponent 2
print(power(5, 3))   # exponent provided explicitly

# Function with keyword arguments
def describe_person(name, age, country):
    print(f"Name: {name}, Age: {age}, Country: {country}")

describe_person(name="Prince", age=31, country="India")

# Function with variable number of arguments
def print_scores(*scores):
    print("Scores:", scores)

print_scores(80, 90, 85)

# Function with keyword-only arguments
def show_info(name, *, city, job):
    print(f"Name: {name}, City: {city}, Job: {job}")

show_info("Riya", city="Delhi", job="Developer")

# Function with a docstring
def hello(name):
    """Print a greeting for the given name."""
    print(f"Hello, {name}!")

hello("Amit")
print(hello.__doc__)

# Example of scope: local and global variables
global_value = 10

def print_values():
    local_value = 20
    print("Global:", global_value)
    print("Local:", local_value)

print_values()
