# Assignment: Create a dictionary to store student grades
grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
name = input("Enter student name: ")
if name in grades:
    print(f"{name}'s grade is {grades[name]}")
else:
    print("Student not found")