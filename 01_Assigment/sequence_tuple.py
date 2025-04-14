# Assignment: Access elements in a tuple
my_tuple = (10, 20, 30, 40, 50)
index = int(input("Enter an index (0-4): "))
if 0 <= index < len(my_tuple):
    print(f"Element at index {index}: {my_tuple[index]}")
else:
    print("Invalid index")