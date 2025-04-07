import sys
# Here are some commonly used string methods
# split method
my_String="hello world"
words:str=my_String.split()
print(words)

# join method is very important string method
print(" ".join(words))
# antoher example
list1=["hello","world"]
print(" ".join(list1))

# replace method
# replace method is used to replace a substring with another substring
# syntax: string.replace(old,new)
print(my_String.replace("hello","hi"))

# find method
# find method is used to find the index of a substring in a string
# syntax: string.find(substring)
print(my_String.find("world"))

my_String="hello world hello"
print(my_String.find("hello"))

first_string_ind=my_String.find("hello")
second_string_ind=first_string_ind + len("hello")
print(my_String[second_string_ind:].find("hello"))

# index method will returh -1 if substring not found
print(my_String.find("worlddd"))
# raise error if substring not found
print(my_String.index("world"))

# rfind method
# rfind method is used to find the index of a substring in a string from right side
# syntax: string.rfind(substring)
# print(my_String.rfind("hello"))


# count method
# count method is used to count the number of occurences of a substring in a string
# syntax: string.count(substring)
# print(my_String.count("l"))

# String formating
# % operator


name: str = 'Umar'
age: int = 20
first_letter: str = name[0]
my_weight: float = 70.532000 # 70.536000

#uncomment to see type
print(type((name, first_letter, age, my_weight)))
my_string: str = '''My name is %s, first letter of my name is \'%c\', I am %d years old and my weight id %f Kg.''' % (name, first_letter, age, my_weight)
my_string = '''My name is %s, first letter of my name is \'%c\', I am %d years old and my weight id %.2f Kg.''' % (name, first_letter, age, my_weight) # Dont forget period %.2f
print(my_string)

# using str.format() method
my_string ='''My name is {}, first letter of my name is \'{}\', I am {} years old and my weight is {} kg.'''.format(name,first_letter,age,my_weight)
print(my_string)

# Manual interning of strings
a=sys.intern("hello")
b=sys.intern("hello")
print(a is b)

# print list of str functions
string_methods:str=dir(str)
# print(string_methods)
filtered_string=[method for method in string_methods if not method.startswith("_")]
print(filtered_string)

# string repetition
separator = "-" * 30
print(separator)

pattern = "* "
repeated_pattern = pattern * 5
print(repeated_pattern)

empty_string = "Test" * 0
print(f"Empty string: '{empty_string}'")

# using string repitition in loop
for i in range(1,6):
    print("*" * i)
    
# implicit type casting
num_str = "100"
num_int = 5

#print(num_str + num_int) # TypeError: can only concatenate str (not "int") to str

# Boolean to integer
print(int(True)) # 1
print(int(False)) #0

# list of Tuples => Dictionary
lst:list=[("name","Alice"),("age",25)]
print(lst[0][0])