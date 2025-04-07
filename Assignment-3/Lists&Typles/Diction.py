# Dictionary in python
# Dictionaries are created using curly braces {} with key-value pairs separated by commas.
american_cities: dict = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
person: dict = {
    "name": "Alice",
    "age": 25,
    "visited_cities": american_cities
}
print(person)

print(person["name"])
print(person.get("age","99"))
print(person.get("country","my_default_value_if_key_not_found"))

# Modifying dict values
person["email"]="info@gmail.com"
print(person)

# Removing a key-value pair
# We can use the pop() method and also del key to remove differnce is that pop() return the removed value and del key does not return anything
deleted=person.pop("age")
print(person)
print(deleted)
del(person["email"])
print(person)

# Dictionary methods
# Python provides several useful methods for working with  dictionaries.
# keys()
# values()
# items()
# clear()
# copy()
# update()

print("start from there")

print(person.keys())
print(person.values())
print(person.items())
# print(person.clear(),person)
print("Copied")
print(person.copy())

for key in person:
    print(key,person[key])
    
for key,value in person.items():
    print(key,value)
    
    
# Paractical example of dictionary
# Building a Phonebook
phonebook: dict = {
    "umair": "123-456-7890",
    "Raza": "987-654-3210",
    "Asharib": "555-555-5555"
}
name:str=input("Enter the name to search:")
if name in phonebook:
    print(f"{name} phone number is {phonebook[name]}")
else:
    print(f"{name} not found in phonebook")
    
# Counting Word Frequencies in a Text

sentence = """
**Projected Economy Size of AI:**

The projected economy size of AI is significant, with estimates varying depending on the source and methodology. Here are some notable projections:

1. **Global AI Market Size:**
	* By 2025: $190 billion (Source: MarketsandMarkets)
	* By 2030: $1.5 trillion (Source: PwC)
2. **AI-Driven Economic Growth:**
	* By 2025: AI is expected to contribute 10% to global GDP growth (Source: Accenture)
	* By 2030: AI is expected to contribute 14% to global GDP growth (Source: PwC)
3. **AI-Generated Revenue:**
	* By 2025: AI is expected to generate $15.7 trillion in revenue (Source: IDC)
	* By 2030: AI is expected to generate $33.5 trillion in revenue (Source: McKinsey)
4. **Job Market Impact:**
	* By 2025: AI is expected to create 133 million new jobs globally (Source: World Economic Forum)
	* By 2030: AI is expected to automate 30% of current jobs globally (Source: McKinsey)

**Industry-Specific Projections:**

1. **Healthcare:**
	* By 2025: AI is expected to generate $150 billion in revenue (Source: MarketsandMarkets)
2. **Financial Services:**
	* By 2025: AI is expected to generate $100 billion in revenue (Source: Accenture)
3. **Manufacturing:**
	* By 2025: AI is expected to generate $50 billion in revenue (Source: IDC)
4. **Transportation:**
	* By 2025: AI is expected to generate $20 billion in revenue (Source: MarketsandMarkets)

**Regional Projections:**

1. **North America:**
	* By 2025: AI is expected to generate $100 billion in revenue (Source: MarketsandMarkets)
2. **Europe:**
	* By 2025: AI is expected to generate $50 billion in revenue (Source: IDC)
3. **Asia-Pacific:**
	* By 2025: AI is expected to generate $200 billion in revenue (Source: MarketsandMarkets)

Note: These projections are based on various assumptions, including the pace of AI development, adoption rates, and economic trends. The actual economy size of AI may vary depending on several factors.

"""

words:list=sentence.split()
word_count={}
# print(words)
for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
# print(word_count)

# Sort the Word_count dictionary in the descending order of the word frequency
sorted_word_count=dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
print(sorted_word_count)

print(person.get("name_1","No Name Found"))

my_dict = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
my_dict.update({"email":"info@gmail.com","age":40})
print(my_dict)

print("\n11. Creating a dictionary from iterable")
iterable = [("key1", "value1"), ("key2", "value2"), ("key3", "value3")]
new_dict = dict(iterable)
print("new dictionary:", new_dict)

# 12. Copying a dictionary
print("\n12. Copying a dictionary")
copied_dict = my_dict.copy()
print("Copied dictionary:", copied_dict)

# dictionary comprehension
original_dict = {'a': 1, 'b': 2, 'c': 3}
print("original_dict = ", original_dict)
double_dict={key: value*2 for key,value in original_dict.items()}
print("double_dict = ", double_dict)

# Try to create a dictionary comprehension that converts a list of temperatures in Celsius to Fahrenheit. The formula to convert Celsius to Fahrenheit is F = (C * 9/5) + 32.
temperatures = [0, 10, 20, 30, 40]
fahrenheit={c:(c * 9/5) + 32 for c in temperatures}
print(fahrenheit)