try:
    result=10/0
except:
    print("An Error occurred")
    
    
try:
    result=10/0
except ZeroDivisionError:
    print("You cannot divide by zero")
except Exception as e:
    print("An error occurred:",e)
    

# the else block
try:
    result=10/2
except ZeroDivisionError:
    print("You cannot divide by zero")
else:
    print("The result is:",result)
    
# Putting ll example together
print("Putting all example together")
def divided_numbers(a,b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("You cannot divide by zero")
    except TypeError:
        print("Invalid input type. Numbers required")
    else:
        print(f"Devision successful. Result: {result} ")
    finally:
        print("Operation completed.\n")
divided_numbers(10,"2")


# Raise an exception

def divide(a,b):
    if b==0:
        raise ValueError("You cannot divide by zero")
    else:
        return a/b
    
print(divide(10,22))


print("Using try except")
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed!")
    return a / b

try:
    result = divide(5, 0)  # This will raise an exception
    print(result)  # This line won't run if exception occurs
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Division by zero is not allowed!

print("Program continues...")  # This line will always execute