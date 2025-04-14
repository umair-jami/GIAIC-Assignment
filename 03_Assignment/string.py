# A string is a sequence of characters encloed in single or double or triple quotes.
my_string="Hello, World!"
# Single Quotes: 
# my_string = 'Hello, World!'
# Double Quotes: 
# my_string = "Hello, World!"
# Triple Quotes: 
# my_string = '''Hello, World!''' (can span multiple lines)
# Raw Strings: 
# my_string = r'Hello, World!' (treats backslashes as literal characters)

# Escape Sequences:
# In Python, escape sequence characters are used to represent special characters that have a specific meaning in a string. These characters are denoted by a backslash (\) followed by a character.
print("Hello, \nWorld")

# Unicode Characters:
print("\u0394")

# Performing Differrent Operations on String Object
# Concatenation
	
my_string = 'Hello, ' + 'World!'
# 2	Indexing
	
my_string = 'Hello, World!'; print(my_string[0])
	
my_string = 'Hello, World!'; print(my_string[7:]) 
# 4	Length
	
my_string = 'Hello, World!'; print(len(my_string)) 
# 5	Upper Case
	
my_string = 'Hello, World!'; print(my_string.upper()) 
	
my_string = 'Hello, World!'; print(my_string.lower())

# Here are some commonly used string methods:
# split
my_string="hello"
print(my_string.split("e"))