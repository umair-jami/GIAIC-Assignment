# control flow refers to the order in which statements are executed in a program
# if statement
num:int=10
if num > 0:
    print("The number is positive")
    
# the else statemetn
num: int = -5

if num > 0:
    print("The number is positive.")
else:
    print("The number is not positive.")
    
# elif statement
num: int = 0

if num > 0: # Program execution step# 1 if condition = False
    print("The number is positive.")
elif num < 0: # Program execution step# 2 if condition = False
    print("The number is negative.")
else: # Program execution step# 3 python will execute the else block
    print("The number is zero.")

# nested if statement

num: int = 10
# num: int = -10

if num>0:
    if num % 2==0:
        print("Even")
    else:
        print("ODD")
else:
    print("The num is negative")
    
# practical example
operation: str = input("Enter the operation (+, -, *, /): ")
num1: float = float(input("Enter the first number: "))
num2: float = float(input("Enter the second number: "))

if operation == "+":
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 !=0:
        result=num1 / num2
    else:
        result = "Error : Division by Zero"
else:
    result="Invalid Operator"
print("Result", result)