#==========================
#1- Arithmetic Operators
#==========================
 # Arithmetic operators perform basic math operations like addition, subtraction, and multiplication.
 # They work with numeric data types such as integers and floats.

# Addition
a = 5
b = 10
c = a + b
print(c)

# Subtraction
a = 10
b = 5
c = a - b
print(c)

# Multiplication
a = 5
b = 10
c = a * b
print(c)

# Division
a = 10
b = 5
c = a / b
print(c)

# Modulus  
a = 10
b = 3
c = a % b
print(c)

# Exponentiation
a = 2
b = 3
c = a ** b
print(c)

# Floor Division
a = 10
b = 3
c = a // b
print(c)

#==========================
#2- Comparison Operators
#==========================
 # Comparison operators compare values and return a Boolean result.
 # They are used in conditions and decision-making logic.

a = 10
b = 5
print(a > b)  # True
print(a < b)  # False
print(a == b)  # False
print(a != b)  # True
print(a >= b)  # True
print(a <= b)  # False

#==========================
#3- Logical Operators
#==========================
 # Logical operators combine Boolean values and return True or False.
 # They are often used to build compound conditions.

a = True
b = False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False

#==========================
#4- Assignment Operators
#==========================
 # Assignment operators assign values to variables and can also update them.
 # Compound assignment operators combine an operation with assignment.

a = 10
print(a)  # 10
a += 5  # a = a + 5
print(a)  # 15
a -= 3  # a = a - 3
print(a)  # 12
a *= 2  # a = a * 2
print(a)  # 24
a /= 4  # a = a / 4
print(a)  # 6.0

#===========================
#5- Bitwise Operators
#===========================
 # Bitwise operators work at the binary level on integer values.
 # They manipulate individual bits using AND, OR, XOR, shifts, and inversion.

a = 10  # 1010 in binary
b = 6   # 0110 in binary
print(a & b)  # 2 (0010 in binary)
print(a | b)  # 14 (1110 in binary)
print(a ^ b)  # 12 (1100 in binary)
print(~a)     # -11 (-1011 in binary)
print(a << 1) # 20 (10100 in binary)
print(a >> 1) # 5 (0101 in binary)

#===========================
#6- Membership Operators
#===========================
 # Membership operators test whether a value is present in a sequence or collection.
 # They return True or False based on membership.

my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # True
print(6 not in my_list)  # True

#===========================
#7- Identity Operators
#===========================
 # Identity operators compare whether two variables refer to the same object in memory.
 # They are different from equality comparisons, which compare values.

a = 10
b = 10
c = 15
print(a is b)  # True
print(a is not c)  # True

#===========================
#8- Ternary Operator
#==========================
 # The ternary operator chooses one of two values based on a condition.
 # It provides a compact way to write simple conditional assignments.

a = 10
b = 20
c = a if a > b else b
print(c)  # 20

