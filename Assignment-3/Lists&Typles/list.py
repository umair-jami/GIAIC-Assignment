# python provides powerful data types like list and tuples. These data structures help store and manage collection of data efficiently.

# list
# Ordered collection of items
# Mutable
# Indexed
# Dynamic size
# Heterogeneous
# Support duplicate values

# Creating lists with different data types
fruits: list  = ["apple", "banana", "cherry","apple"]
numbers: list = [10, 20, 30, 40]
mixed: list   = ["hello", 42, 3.14, True]

print("fruits  = ", fruits)
print("numbers = ", numbers)
print("mixed   = ", mixed)

# Accessing elements of a list
print(fruits[0])
print(fruits[-2])

# Modifying lists
fruits[1] = "mango"
print(fruits)

# list slicing
print(fruits[1:3])

# Commen list methods
fruits.append("orange")

fruits.extend(["grapes","Kiwi"])
print(fruits)

# Remove and Pop method
fruits.remove("apple")
print(fruits)

# pop
deleted=fruits.pop()
print(fruits)
print(deleted)

# Sorting a list
numbers:list[int] = [10, 20, 30, 40, 5, 1, 100]
numbers.sort()
print(numbers)
# sorting in descending order
numbers.sort(reverse=True)
print(numbers)

# sorting with key=len
words = ["apple", "kiwi", "banana"]
words.sort(key=len)
print(words)

# Sorting by Last Character (key=lambda word:word[-1])
words.sort(key=lambda word:word[-1])
print(words)

# Reverse sorting
numbers.reverse()
print(numbers)

# Iterating over a list
for fruit in fruits:
    print(fruit)
    
# Using list comprehension

# new_list=[expression for element in iterable if condition]

squared:list=[x*2 for x in range(10)]
print(squared)

squared:list=[x**2 for x in [1,2,3,4,5] if x > 3]
print(squared)

