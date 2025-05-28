# class Dog:
#     def __init__(self):
#         self.name="Dog"
#         self.sound="Bark"
# dog1=Dog()
# print(dog1.name)
# print(dog1.sound)

# Destructor
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         print(f"A {self.brand} {self.model} has been created.")
#     def __del__(self):
#         print(f"{self.brand} destroyed")
#     def display(self):
#         print(f"Brand: {self.brand}, Model: {self.model}")
# my_car = Car("Toyota", "Corolla")
# my_car.display()
# del my_car
# my_car.display()  # This will raise an error because my_car has been deleted



# class Dog:
#     # Class attribute (shared by all instances)
#     species = "Canis familiaris"

#     # Constructor (instance attributes)
#     def __init__(self, name, age):
#         self.name = name  # Instance attribute
#         self.age = age    # Instance attribute

#     # Method to display dog details
#     def display(self):
#         print(f"{self.name} is {self.age} years old and is a {self.species}.")

# # Create instances of the Dog class
# dog1 = Dog("Buddy", 5)
# dog2 = Dog("Max", 3)

# # Access class attribute
# print(f"Dog species: {Dog.species}")  # Output: Dog species: Canis familiaris
# print(f"Buddy's species: {dog1.species}")  # Output: Buddy's species: Canis familiaris
# print(f"Max's species: {dog2.species}")    # Output: Max's species: Canis familiaris

# # Access instance attributes
# print(f"Buddy's name: {dog1.name}")  # Output: Buddy's name: Buddy
# print(f"Max's age: {dog2.age}")       # Output: Max's age: 3

# # Modify class attribute (affects all instances)
# Dog.species = "Canis lupus"
# print(f"Buddy's species after modification: {dog1.species}")  # Output: Buddy's species after modification: Canis lupus
# print(f"Max's species after modification: {dog2.species}")    # Output: Max's species after modification: Canis lupus

# # Modify class attribute through an instance (creates a new instance attribute)
# dog1.species = "Canis aureus"
# print(f"Buddy's species after shadowing: {dog1.species}")  # Output: Buddy's species after shadowing: Canis aureus
# print(f"Max's species remains: {dog2.species}")            # Output: Max's species remains: Canis lupus

# # Inspect attributes using __dict__
# print(f"Dog class attributes: {Dog.__dict__}")
# print(f"dog1 instance attributes: {dog1.__dict__}")
# print(f"dog2 instance attributes: {dog2.__dict__}")

# class MyClass:
#     class_var="Class Variable"  # Class variable
#     def __init__(self):
#         self.instance_var="Instance Variable"
        
#     def instance_method(self):
#         print("This is an instance method." + str(self))
#         print("Calling instance variable: ", self.instance_var)
    
#     @classmethod
#     def class_method(cls):
#         print("This is a class method.")
#         print("Calling class variable: ", cls.class_var)
    
#     @staticmethod
#     def static_method():
#         print("This is a static method.")
#         # print("Calling instance variable: ", self.instance_variable)  # This will raise an error
#         # print("Calling class variable: ", cls.class_var)  # This will raise an error
        
# obj=MyClass()
# obj.instance_method()
# obj.class_method()
# obj.static_method()

# different types of methods
class Person:
    species ="Homo sapiens"

    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def display(self):
        print(f"{self.name} is {self.age} years old and is a {self.species}.")
        
    @classmethod
    def update_species(cls,new_species):
        cls.species=new_species
        print(f"Species updated to {cls.species}")
    
    @staticmethod
    def is_adult(age):
        return age >=18
    
person1=Person("Alice",25)

person1.display()

Person.update_species("Homo")

# Encapsulation
# To access or modify private or protected attribute, getter and setter methods are used. These methods provide controlled provide controlled access to the data, ensuring that any changes are validated or processed appropriately

