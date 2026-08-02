#=======================
#   Input and Output
#=======================
 # Input and output are used to interact with users.
 # Input reads data from the user, and output displays data on screen.

# Output using print()
message = "Hello, World!"
print(message)

# Input using input()
# Ask the user for their name and show it back.
user_name = input("Enter your name: ")
print("Hello, " + user_name)

# Ask the user for details and print them.
user_age = input("Enter your age: ")
user_country = input("Enter your country: ")
# The f-string allows us to insert variable values directly into the text.
print(f"Name: {user_name}, Age: {user_age}, Country: {user_country}")

# Convert input to a number
# Uncomment the next three lines to read and convert a number.
# number = int(input("Enter a number: "))
# print("Number + 5 =", number + 5)

# Output with formatted strings
name = "Prince"
age = 31
print(f"Name: {name}, Age: {age}")
