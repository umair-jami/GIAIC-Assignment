# Encapsulation in Python
class Car:
    def __init__(self):
        self.__fuel = 100
        self.__engine_on = False

    def start_engine(self):
        if self.__fuel > 0:
            self.__engine_on = True
            print("Engine started.")
        else:
            print("No fuel. Cannot start engine.")

    def drive(self):
        if self.__engine_on and self.__fuel > 0:
            self.__fuel -= 10
            print("Driving... Fuel level:", self.__fuel)
        else:
            print("Cannot drive. Check if engine is on and fuel is available.")


# my_car = Car()
# my_car.start_engine()
# my_car.drive()
# my_car.drive()
# print("Fuel level after driving:", my_car._Car__fuel)  # Accessing private attribute for demonstration purposes

# Abstraction in Python
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print("Car is moving.")


# my_car = Car()
# my_car.move()

# Inheritance in Python
class BasicCar:  # Parent class
    def __init__(self):
        self.speed = 0

    def accelerate(self):
        self.speed += 10
        print(f"Speed: {self.speed} km/h")


class SportsCar(BasicCar):  # Child class
    def turbo_boost(self):
        self.speed += 20
        print(f"Turbo Boost! Speed: {self.speed} km/h")


# my_sports_car = SportsCar()
# my_sports_car.accelerate()
# my_sports_car.turbo_boost()

# Polymorphism in Python
class RegularCar:
    def drive(self):
        print("Vromm! Engine roaring to life.")


class ElectricCar:
    def drive(self):
        print("Silent hum ... Electric engine engaged.")


def start_drive(car):
    car.drive()


# my_regular_car = RegularCar()
# my_electric_car = ElectricCar()

# start_drive(my_regular_car)
# start_drive(my_electric_car)

# Decorators in OOP
class MyClass(object):
    # Class attribute
    class_variable = "Class Variable"

    def __init__(self):
        self.instance_variable = "Instance Variable"  # Instance Variable
        print("Constructor")

    def instance_method(self):
        print("\n\nInstance Method: " + str(self))
        print("Calling instance variable: ", self.instance_variable)
        # print("Calling class variable: ", self.class_variable)
        # MyClass.class_variable = "Modified Class Variable"

    @classmethod
    def class_method(cls):
        print("\n\nClass Method: " + str(cls))
        print("Calling class variable: ", cls.class_variable)
        # print("Calling instance variable: ", cls.instance_variable)
        # cls.instance_variable = "Modified Instance Variable"

    @staticmethod
    def static_method():
        print("\n\nStatic Method")
        print("Calling class variable: ", MyClass.class_variable)
        # print("Calling instance variable: ", MyClass.instance_variable)
        # MyClass.instance_variable = "Modified Instance Variable"
        
# obj=MyClass()
# obj.instance_method()
# MyClass.class_method()
# MyClass.static_method()
# obj.class_method()


# getter and setter in OOP
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public attribute
        self._balance = balance               # Protected attribute
        self.__pin = "1234"                   # Private attribute

    # Getter method for balance
    def get_balance(self):
        return self._balance

    # Setter method for balance
    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
            print(f"Balance updated to {self._balance}.")
        else:
            print("Invalid amount. Balance cannot be negative.")

    # Getter method for pin (private attribute)
    def get_pin(self):
        return "Access denied. PIN is private."

    # Method to display account details
    def display(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self._balance}")

# Create an instance of the BankAccount class
account = BankAccount("Alice", 1000)

# Access public attribute
print(f"Account Holder: {account.account_holder}")  # Output: Account Holder: Alice

# Access protected attribute (not recommended, but possible)
print(f"Balance: {account._balance}")  # Output: Balance: 1000

# Access private attribute (name mangling makes it harder)
# This will raise an AttributeError:
# print(account.__pin)

# Use getter method for private attribute
print(account.get_pin())  # Output: Access denied. PIN is private.

# Use getter and setter methods for protected attribute
print(f"Initial Balance: {account.get_balance()}")  # Output: Initial Balance: 1000
account.set_balance(1500)  # Output: Balance updated to 1500.
account.set_balance(-500)  # Output: Invalid amount. Balance cannot be negative.

# Display account details
account.display()  # Output: Account Holder: Alice, Balance: 1500

# Polymorphism is one of th core principles of OOP
# Method Overriding
# Operator Overloading
# Duck Typing
# Method Overriding: When a child class provides a specific implementation of a method that is already defined in its parent class.
class Animal:
    def speek(self):
        return "Animal sound"
    
class Dog(Animal):
    def speek(self):
        return "Bark"
class Cat(Animal):
    def speek(self):
        return "Meow"

def animal_sound(animal):
    print(animal.speek())

dog=Dog()
cat=Cat()

animal_sound(dog)  # Output: Bark
animal_sound(cat)  # Output: Meow

# Operator Overloading
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    # Overloading the + operator
    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)
    def __str__(self):
        return f"Point({self.x},{self.y})"

p1=Point(1,2)
p2=Point(3,4)
p3=p1+p2
print(p3)

# Duck typing
class Duck:
    def quack(self):
        return self.__repr__() + ": Quack!"
class Person:
    def quack(self):
        return self.__repr__() + ": I can quack like Duck!"
    
def make_it_quack(thing):
    print(thing.quack())
    
duck=Duck()
person=Person()
make_it_quack(duck)
make_it_quack(person)

# abstract method

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass