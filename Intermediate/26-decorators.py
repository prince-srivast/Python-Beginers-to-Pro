#=======================
#   Decorators
#=======================
 # Decorators wrap a function to add behavior before or after it runs.
 # They are often used for logging, validation, or timing.

# Basic decorator function
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling function")
        result = func(*args, **kwargs)
        print("After calling function")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Prince")

# Decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hi, {name}")

greet("Amit")
