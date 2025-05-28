import math
# class Person:
#     def __init__(self,name):
#         self.name=name
#         self.state="Idle"
#     def running(self):
#         self.state="Running"
#         print(f"{self.name} is now walking")
#     def sleeping(self):
#         self.state = "Sleeping"
#         print(f"{self.name} is now sleeping.")

#     def show_state(self):
#         print(f"{self.name} is currently in '{self.state}' state.")
        
# # person1=Person("Ali")
# # person1.show_state()
# # person1.running()
# # person1.show_state()
# # person1.sleeping()
# # person1.show_state()

# class Car:
#     # Parameterized constructor
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     # Destructor
#     def __del__(self):
#         print(f"The {self.brand} {self.model} has been destroyed.")


# # Create an object of the Car class
# my_car = Car("Toyota", "Corolla")
# # Explicitly delete the object (triggers the destructor)
# del my_car  # Output: The Toyota Corolla has been destroyed.

# class Car:
#     type = "anonymous"

#     def __init__(self, car_type):
#         self.type = car_type

#     @classmethod
#     def change_name(cls, new_type):
#         cls.type = new_type

#     @staticmethod
#     def start():
#         print("Car started")

#     @staticmethod
#     def stop():
#         print("Car stopped")


# class CarType(Car):
#     def __init__(self, car_type):
#         super().__init__(car_type)
#         # No need to call start here unless required explicitly


# # Create an object of CarType
# myCar = CarType("Corolla")
# myCar.start()
# print(myCar.type)

# # Change the class attribute
# Car.change_name("Civic")
# print(myCar.type)  # Instance attribute remains unchanged
# print(Car.type)    # Class attribute is updated 
 
 
# class Percentage:
#     def __init__(self,phy,math,bio):
#         self.phy=phy
#         self.math=math
#         self.bio=bio
        
#     @property
#     def percentage(self):
#         return str((self.phy + self.math + self.bio) / 3) + "%" 

# stud1=Percentage(12,23,80)
# print(stud1.percentage)
# stud1.bio=90
# print(stud1.percentage)

# Polymorphism operators overloading
# Addition of complex numbers
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showNumber(self):
        print(self.real,"i +", self.img,"j")
    
    def __add__(self,num2):
        newReal=self.real + num2.real
        newImg=self.img + num2.img
        return Complex(newReal,newImg)
   
num1=Complex(1,3) 
num1.showNumber()

num2=Complex(2,5)
num2.showNumber()

# Before using __add__ dunder function
# num3=num1.add(num2)
# num3.showNumber()

# After using __Add__ dunder function
num3=num1 + num2
num3.showNumber()