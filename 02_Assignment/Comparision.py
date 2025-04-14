# ==	Equal	5 == 5 → True
# !=	Not equal	5 != 3 → True
# >	Greater than	5 > 3 → True
# <	Less than	5 < 3 → False
# >=	Greater than or equal	5 >= 5 → True
# <=	Less than or equal	5 <= 3 → False
x: int = 10
y: int = 5

print("x == y = ", x == y)  # False, Equal
print("x != y = ", x != y)  # True, Not equal
print("x > y  = ", x > y)   # True, Greater than
print("x < y  = ", x < y)   # False, Less than
print("x >= y = ", x >= y)  # True, Greater than or equal
print("x <= y = ", x <= y)  # False, Less than or equal