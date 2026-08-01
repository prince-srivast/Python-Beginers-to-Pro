#Operators
#1- Arithmetic Operators

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

#2- Comparison Operators
a = 10
b = 5
print(a > b)  # True
print(a < b)  # False
print(a == b)  # False
print(a != b)  # True
print(a >= b)  # True
print(a <= b)  # False

#3- Logical Operators
a = True
b = False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False

#4- Assignment Operators
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

#5- Bitwise Operators
a = 10  # 1010 in binary
b = 6   # 0110 in binary
print(a & b)  # 2 (0010 in binary)
print(a | b)  # 14 (1110 in binary)
print(a ^ b)  # 12 (1100 in binary)
print(~a)     # -11 (-1011 in binary)
print(a << 1) # 20 (10100 in binary)
print(a >> 1) # 5 (0101 in binary)

#6- Membership Operators
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # True
print(6 not in my_list)  # True

#7- Identity Operators
a = 10
b = 10
c = 15
print(a is b)  # True
print(a is not c)  # True

#8- Ternary Operator
a = 10
b = 20
c = a if a > b else b
print(c)  # 20

