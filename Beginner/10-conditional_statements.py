#=======================
#   Conditional Statements
#=======================
 # Conditional statements execute code only when a condition is True.
 # They are used to make decisions in a program.

# if statement
x = 10
if x > 5:
    print("x is greater than 5")

# if-else statement
y = 3
if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")

# if-elif-else statement
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D or below")

# Nested if statements
num = 15
if num > 0:
    print("Number is positive")
    if num % 3 == 0:
        print("Number is divisible by 3")
    else:
        print("Number is not divisible by 3")
else:
    print("Number is zero or negative")

# Ternary conditional expression
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)

# Conditions can use comparisons and logical operators
a = 5
b = 10
if a < b and b < 20:
    print("a is less than b and b is less than 20")
