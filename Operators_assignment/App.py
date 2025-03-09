# Operator and Operand
# OPerator: A symbol that perform an operatoion
# Operand : The value or vairale that work with operator

x:int=12
y:int=13
z:int=x+y

# There x and y are Operends and z is Result and + and = is Operators

# Unary and Binary Operators

# Unary operators work with one operand (a single value or variable). They perform operations on just one thing.
# Negative(-)

x:int=5
y=-x
print(y)

# Logical Not
#   Reverse a Boolean value
a=True
b=not a
print("b =", b)

# Bitwise Not(~)
x: int = 5  # Binary: 0101
y: int = ~x  # y is now -6 (binary: 1010, but in two's complement form)
print("y = ", y)
print("bin(x) =",bin(x),type(bin(x)))


# Binary Operators
# Binary operators work with two operands (two values or variables). They perform operations between two things.

# Examples:
# Arithmetic Operators (+, -, *, /, etc.):

# Perform basic math operations.
# Comparison Operators (==, !=, >, <, etc.):

# # Compare two values and return True or False.
# Logical Operators (and, or):
# # 
# # Combine boolean values.
# # Assignment Operators (=, +=, -=, etc.):

# # Assign values to variables or perform operations while assigning.
# #
# # Note: (we will see these operators in action in next topic)