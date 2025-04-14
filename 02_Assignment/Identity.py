#  Identity Operators
# Used to compare memory locations.


# Operator	Name	Example
# is	Returns True if objects have the same memory location	x is y
# is not	Returns True if objects do not have the same memory location	x is not y

a: list = [1, 2, 3]
b: list = [1, 2, 3]
c: list = a
print("a is c     =  ",a is c)       # True  (same object, sharing same memmory space)
print("a is b     =  ",a is b)       # False (different objects, seperate memmory space)
print("a == b     =  ", a == b)      # True  (same values, different memmory space but having same vlaues)
print("a is not b =  ", a is not b)  # True  (True because of different memmory space, although having same memmory space)

print('\n-----\n') # seperator for better output readability

print("id(a) = ", id(a))
print("id(b) = ", id(b))
print("id(c) = ", id(c))