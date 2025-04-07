# intro to loops
# loops are used to repeat bloack of code mulitiple times
# for loop:used to iterate over a sequence (e.g. lists,strings, or range)
# while loop:Used to reapeat a bloack  of code as long as a condition if True

# for loops
fruits: list = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# Iterate over a string
word: str = "Python"
for letter in word:
    print(letter)

# for loop with else bloack

numbers = [1,2,3,4,5]

# In Python, a for loop can have an else block. The else block runs only if the loop completes without a break statement.
for num in numbers:
    print(num)
else:
    print("No more numbers")
    
# for loop with break and else block
for num in numbers:
    print(num)
    if num == 3:
        break
else:
    print("No more numbers")
    
# searching with else
for num in numbers:
    if num == 7:
        print("Number found!")
        break
else:
    print("Number not found")
    
    
# Range funtion in for loop
for i in range(2,11,2):
    print(i)
    
    
# Underscore in for loop
for _ in range(10): # Just to show that _ is a loop variable, but its throwaway variable
    # Code to be executed 100,000 times
    print(f"Hello, World! Iteration { _ }")
    
    
# Controlling loops
# break and continue statement
for i in range(10):
    if i == 5:
        break
    print(i)  # Prints 0, 1, 2, 3, 4
    
for i in range(5):
    if i == 3:
        continue
    print(i)  # Prints 0, 1, 2, 4
    
# Nested for loop
for outer in range(1,6):
    print(f"Multiplication tabel for {outer}:")
    for inner in range(1,6):
        print(f"{outer} * {inner} = {outer * inner}")
    print()
    
total:int=0
for i in range(1,101):
    total+=i
print(total)

# Find factors of a number
num:int=24
factor=[]
for i in range(1,num+1):
    if num % i ==0:
        factor.append(i)
print(f"Factors of {num}: {factor}")