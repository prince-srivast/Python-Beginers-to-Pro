#=======================
#   Exceptions
#=======================
 # Exceptions handle errors that occur during program execution.
 # Use try/except to catch and respond to problems safely.

# Basic try/except
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: division by zero is not allowed.")
        return None

print(divide(10, 2))
print(divide(10, 0))

# Catch multiple exception types
def parse_int(value):
    try:
        return int(value)
    except ValueError:
        print("Error: value is not an integer.")
        return None

print(parse_int("123"))
print(parse_int("abc"))

# Use else and finally
try:
    number = int("42")
except ValueError:
    print("Conversion failed")
else:
    print("Conversion succeeded", number)
finally:
    print("This always runs")

# Raise an exception explicitly
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    check_age(-1)
except ValueError as error:
    print("Caught error:", error)

# Define a custom exception
class CustomError(Exception):
    pass

try:
    raise CustomError("Something went wrong")
except CustomError as error:
    print(error)
