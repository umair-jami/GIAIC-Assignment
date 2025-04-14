# UnderStanding the functions

# A python function is a block of organized, reusable code that is used to perform a single,related action.
# Functions provide better modularity for your application and a high degree of code reusing.

def my_function():
    print("Hello from my function!")
my_function()

# A global function is a function that is defined outside of any class or object and can be accessed from anywhere in the code. A global function can be called from within any other function or method, as long as it is in the same module or imported into the module where it is being called.
# A global function is not bound to any specific object or instance, and it does not require an object to be created in order to be called. Global functions are typically used for utility functions or helper functions that can be used throughout the codebase.

# Types of functions in python
# 1. Built-in functions: These are the functions that are pre-defined in Python and can be used directly without any import. Examples include print(), len(), type(), etc.
# 2. User-defined functions: These are the functions that are defined by the user to perform specific tasks. They can take arguments and return values.
# 3. Lambda functions: These are anonymous functions that are defined using the lambda keyword. They can take any number of arguments but can only have one expression. They are often used for short, throwaway functions.
# Example:
lambda_function = lambda x:x**2
print(lambda_function(5))  # Output: 25

# 4. Recursive functions: These are functions that call themselves in order to solve a problem. They are often used for problems that can be broken down into smaller subproblems.
# example:
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))  # Output: 120
# In this example, the factorial function calls itself with a smaller value of n until it reaches the base case of n=0.

# 5. Higher-order functions: These are functions that take other functions as arguments or return functions as their result. They are often used in functional programming and can be used to create more complex behavior in your code.
# Example:
def square(x):
    return x**2
def apply_function(func,value):
    return func(value)
print(apply_function(square,5))

# 6. Generator functions: These are functions that use the yield keyword to return a generator object. They can be used to create iterators and are often used for lazy evaluation.
# Example:
def count_up_to(n):
    count=1
    while count<=n:
        yield count
        count+=1
for number in count_up_to(5):
    print(number)

# 7. Decorator functions: These are functions that take another function as an argument and extend its behavior without modifying it. They are often used for logging, authentication, and other cross-cutting concerns.

# Example:
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

# 8. Coroutines: These are special types of functions that can be paused and resumed, allowing for asynchronous programming. They are often used in conjunction with the async and await keywords.
# example:

# Syntax of funtion in python

def function_name():
    """This is a docstring of greeting function"""
    greet="Hello world"
    return greet
print(function_name())

# Pass by Reference vs Pass by value

# In Python, all arguments are passed by reference. This means that when you pass an object to a function, you are passing a reference to that object, not a copy of it. If you modify the object inside the function, the changes will be reflected outside the function as well.

def modify_value(my_value):
    x=10
    print("Inside function:",x)
    
x=5
print("Original ",x)
modify_value(x)
print("Outside function",x)
    
    
    
# In this example, the value of x is modified inside the function, but the original value of x outside the function remains unchanged. This is because integers are immutable in Python, and a new integer object is created when we assign a new value to x inside the function.


# However, if we pass a mutable object like a list or a dictionary, the changes made inside the function will be reflected outside the function as well.

def modify_list(list_value):
    list_value.append(4)
    print("Inside function:", list_value)

list_value = [1, 2, 3]
print("Original list:",list_value)
modify_list(list_value)
print("outside function:", list_value)

# Arguments in python functions
# Arguments are the values that are passed to a function when it is called. In Python, there are several types of arguments that can be used in functions:
# 1. Positional arguments: These are the most common type of arguments. They are passed to the function in the order in which they are defined in the function signature.
# Example:
def add(a, b):
    return a + b

print(add(2, 3))  # Output: 5

# 2. Keyword arguments: These are arguments that are passed to the function using the name of the parameter. They can be passed in any order.
# Example:
def add(a, b):
    return a + b


print(add(b=3, a=2))  # Output: 5

def greeting(name):
    """This is a docstring of greeting function"""
    print("Hello {}".format(name))
    return

greeting("Ali")
greeting(name="Akram")

# Keyword arguments example
def add(a,b):
    return a+b
print(add(a=2,b=3))  # Output: 5
print(add(b=3,a=2))  # Output: 5

# Unpacking iterables
# Unpacking iterables is a way to pass multiple values to a function as arguments. This can be done using the * operator for positional arguments and the ** operator for keyword arguments.
# Example:
def my_sum(*numbs):
    print(type(numbs),", ",numbs)
    return sum(numbs)

print(my_sum(1, 2, 3))  # Output: 6
print(my_sum(*[1,2,3,4,5,6,7,8]))
print(my_sum(*(1,2,3,4,5,6,7,89,9,10)))


# 3. Default arguments: These are arguments that have a default value assigned to them. If the argument is not passed when the function is called, the default value will be used.
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
printinfo( age=50, name="Arif" )
printinfo( name="Arif" )

# Positional-only arguments: These are arguments that can only be passed positionally and cannot be passed as keyword arguments. They are defined using a / in the function signature.
def posfun(x,y,/,z):
    return x+y+z
print(posfun(1,2,z=5))

# keywords-only arguments
def posFun(*, num1, num2, num3):
    print(num1 * num2 * num3)

print("Evaluating keyword-only arguments: ")
posFun(num1=6, num2=8, num3=5)

posFun(num3=6, num1=8, num2=5)


# mixing
def posFun(num1, num2, /, *, num3):
    return num1 + num2 + num3
print(posFun(1,2,num3=5))


# Arbitrary or variable length arguments

def printinfo(agg1,*vartuple):
    "This prints a variable passed arguments into this function"
    print("Output is ",agg1)
    for var in vartuple:
        print("*",var)
    return
printinfo(10)
printinfo(70,60,50)
printinfo(70,60,50,80,90)

# Anonymus functions
# the functions are called anonymus when they are not declared in thes standard manner by using the def keyword. instead they are defined using the lambda keyword
# the syntax of lambda function contains only single statement and the return statement is not used in this function. the lambda function can take any number of arguments but can have only one expression. the expression is evaluated and returned.

# one parameter
lambda_function = lambda x:x+2
print(lambda_function(5))

# multiple parameters
lambda_function = lambda x,y:x+y
print(lambda_function(5,10))

my_dict = {"apple": 5, "banana": 2, "cherry": 8, "date": 1}
sorted_dict=dict(sorted(my_dict.items(),key=lambda item:item[1]))
print(sorted_dict)

# Arbitrary Keywords Arguments, **Kwargs

# If You don't know how many keyword arguments that will be passed to your function, add two asterisk: ** before the parameter name in the function definition.

def my_function(**student):
    print("First name:", student["fname"])
    print("Last name:", student["lname"])
    
    for key , value in student.items():
        print(key, ":", value)
my_function(fname = "Ali", lname = "Osman")

my_function(fname = "Ali", lname = "Osman", course = "Python - 101", day="Saturday", time="1400 - 1800")
my_dict = {"fname": "Ali", "lname": "Osman", "course": "Python - 101", "day":"Saturday", "time":"1400 - 1800"}
my_function(**my_dict)

# Generator function
def simple_generator():
    yield 1
    yield 2
    yield 3
    
gen=simple_generator()
print(gen)
print(gen,":",type(gen))

for value in gen:
    print(value, ":", type(value))
    
    
def infinit_sequence():
    num=0
    while True:
        yield num
        num+=1
gen = infinit_sequence()

for _ in range(10):
    print(next(gen))
    
# Generator expression
print("Generator expression")

# Create a generator expression for squares of numbers from 0 to 9
gen = (x * x for x in range(10))

# Print the first value using next()
print(next(gen))  # Output: 0

# Print the rest of the values using a for loop
for value in gen:
    print(value)
# Recursive  Function in  python

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print("factorial")
print(factorial(5))

# Recursive function to calculate Fibonacci series
def fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print("Fibonacci")
print(fibonacci(20))