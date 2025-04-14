# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is:

# unordered
# unchangeable
# unindexed
# mutable
# An object cannot appear more than once in a set, whereas in List and Tuple, same object can appear more than once.

new_set={}
new_set=set()
print(type(new_set))

# sets can't hold mutable objects like lists, sets, or dictionaries, but they can hold immutable objects like strings, tuples, and numbers.

# It can hold multiple data types at once.
multi_type_set={1,2,3,"umair",(1,2,2)}
print(multi_type_set)

# sets are immutable, but you can add or remove items from them.
my_set={1,2,3,4,5}
print(my_set)

try:
    my_set[0]
except TypeError as e:
    print(e)
    
# Adding items to a set
my_set.add(6)
print(my_set)
# removing items from a set
my_set.remove(6)
print(my_set)


my_set: set = {1, 2, 3, 4, 5, 'A', 'a'}
print("my_set = ", my_set)

print("discard method")

print(my_set.discard(1))
print("my_set = ", my_set)
# for removing different element wo iterate and use discard method
for item in {1,2,3}:
    my_set.discard(item)
print("After removing multiple elements, iterate and discard each one indiviually:",my_set)

# use difference_update() method to remove the items from the set that are present in the specified set.
# 🔹 What is difference_update()?
# difference_update() is a set method in Python that removes all elements in another set (or iterable) from the original set.

# 🧠 Think of it like this:

# "Hey, remove from my set whatever is present in that other set."

a = {1, 2, 3, 4, 5}
b = {3, 4, 6}

a.difference_update(b)

print(a)  # Output: {1, 2, 5}


print("difference_update method")
my_set.difference_update({1,5,3})
print("my_set = ", my_set)

# use update method to add items from the specified set to the current set
my_set.update({1,5,3,"hello"})
print("my_set = ", my_set)

# 🔁 Quick Summary
# Method	    Purpose	Error           if not found?	Accepts multiple values?
# remove()	    Removes element	        ❌ Yes (KeyError)	❌ No
# discard()	    Removes element	        ✅ No	            ❌ No
# add()	Adds    single element	        ✅ No	            ❌ No
# update()	    Adds multiple elements	✅ No	            ✅ Yes

# Using the union() method or the | operator to combine two sets
# The union() method returns a new set with all items from both sets
# The | operator returns a new set with all items from both sets
set1={1,2,3}
set2={4,5,6}
my_set3=set1.union(set2)
my_set3=set1 | set2
print(my_set3)


#When you call `my_set.pop()`, it removes and returns an arbitrary element from the set.
#Since sets are unordered data structures, the element that is removed and returned is not predictable.
my_set={1,2,3}
my_set.remove(1)
print(my_set)
print(my_set.pop())
print(my_set)

# The Inner Working of SET (Advaced Topic)
# 🔐 What is Hashing?
# Hashing is a process of converting data (like numbers, strings, etc.) into a fixed-size value called a hash, using a function called a hash function.

# Think of it like this:

# 🧠 "Hashing is like giving a unique ID number to every item, so Python can find it super fast!"
a:str="hello"
b:str="world"
print(hash(a))
print(hash(b))
print(hash("hello"))

# Even if a set in only allows immutable but set itself in mutable, so it can be changed.
# But the elements inside it should be immutable.
# In Python, a dictionary key must be an immutable object, meaning its value cannot be changed after it's created. This is because dictionaries use a hash table to store key-value pairs, and mutable objects cannot be hashed.
my_set:set={1,2,3,4,5,"Hello"}
my_dic={my_set:"Hlleo"}
# print(my_dic)
# The above code will throw an error because set is mutable and dictionary key must be immutable.