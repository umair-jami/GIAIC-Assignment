# Encapsulation
# class Car:
#     def __init__(self,color,speed):
#         self.color=color
#         self.__speed=speed
        
#     def accerlate(self):
#         self.__speed+=10
#     def get_speed(self):
#         return self.__speed
    
# car=Car("red",0)
# print(car.get_speed())
# for i in range(10):
#     car.accerlate()
# print(car.get_speed())

# Abstraction 
# abstraction mean hiding complex implementation details and exposing only the necessary features of an object.
# define a car class with abstraction and idle stop engine feature

# Define a Car class with abstraction and idle stop engine feature
# from rich import print
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         self._engine_status = False
#         self._idling_time = 0
#         self._traffic_signal = None

#     # Expose a drive method without revealing internal mechanics
#     def drive(self):
#         if self._engine_status and self._traffic_signal == "green":
#             print(f"You are driving a {self.brand} {self.model}.")
#         elif self._traffic_signal == "red":
#             print(f"You stopped at the red light in a {self.brand} {self.model}.")
#             self._idle_stop_engine()
#         else:
#             self._start_engine()
#             print(f"You are driving a {self.brand} {self.model}.")

#     # Expose a stop method to stop the car
#     def stop(self):
#         if self._engine_status:
#             print(f"You stopped the {self.brand} {self.model}.")
#             self._idle_stop_engine()
#         else:
#             print(f"The {self.brand} {self.model} is already stopped.")

#     # Expose a set_traffic_signal method to set the traffic signal
#     def set_traffic_signal(self, signal):
#         self._traffic_signal = signal
#         if signal == "red":
#             print(f"Traffic signal turned red. You stopped in a {self.brand} {self.model}.")
#             self._idle_stop_engine()
#         elif signal == "green":
#             print(f"Traffic signal turned green. You can drive your {self.brand} {self.model}.")
#             if not self._engine_status:
#                 self._start_engine()

#     # Internal method to start the engine (hidden from user)
#     def _start_engine(self):
#         self._engine_status = True
#         self._idling_time = 0
#         print("Engine started.")

#     # Internal method to stop the engine if idling for 5 seconds (hidden from user)
#     def _idle_stop_engine(self):
#         import time
#         print("Engine is idling...")
#         for i in range(5):
#             print(f"Idling time: {i+1} seconds")
#             time.sleep(1)
#             self._idling_time += 1
#         if self._idling_time >= 5:
#             self._engine_status = False
#             print("Engine stopped (idle stop) to save fule.")
            
# my_car = Car("Toyota", "Camry")
# my_car.set_traffic_signal("green")
# my_car.drive()
# my_car.set_traffic_signal("red")
# my_car.set_traffic_signal("green")
# my_car.drive()

# class ShopingMall:
#     def basement_parking():
#         my_car=Car("Toyota", "Camry")
#         my_car._start_engine()
#     basement_parking()
#     my_car._start_engine()
    
# # iNHERITANCE
# class BMW(Car):
#   def __init__(self, brand, model):
#     super().__init__(brand, model)

#   def start_engine(self):
#     self._start_engine() # Car class private method is visible in child class

#   def _start_engine(self): # Overrides the parent method with the same name
#     print("BMW engine started") # Even you can override it

# bmw: BMW = BMW("BMW", "i5")
# bmw.start_engine()


# Example of Inheritance
# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def start_engine(self):
#         print(f"{self.brand} {self.model} engine started.")

#     def stop_engine(self):
#         print(f"{self.brand} {self.model} engine stopped.")
        
# class Car(Vehicle):
#     def __init__(self, brand, model):
#         super().__init__(brand, model)
    
    
# class Truck(Vehicle):
#     def __init__(self, brand, model):
#         super().__init__(brand, model)

# car=Car("Toyota", "Camry")
# car.start_engine()
# car.stop_engine()
# truck=Truck("Ford", "F-150")
# truck.start_engine()
# truck.stop_engine()


# Polymorphism

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self) -> None:
        pass
    
class Dog(Animal):
    def sound(self) -> None:
        print("Woof! Woof!")
class Cat(Animal):
    def sound(self) -> None:
        print("Meow! Meow!")
        
def animal_sound(animal:Animal) -> None:
    animal.sound()

dog=Dog()
cat=Cat()
animal_sound(dog)
animal_sound(cat)