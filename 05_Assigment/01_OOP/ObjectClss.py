#There all content is alla bout the object class
# Object class is the base class for all classes in Python. It provides a set of methods and attributes that are common to all objects. The object class is the root of the class hierarchy in Python, and all classes inherit from it. The object class provides a set of methods that can be used to create, manipulate, and destroy objects. It also provides a set of attributes that can be used to access the properties of an object.

# Base class for all classes in Python
# Default methods object class provides default implementations for several imporant methods, such as __init__, __str__, __repr__, __eq__, and __hash__. These methods can be overridden in user-defined classes to provide custom behavior.
# Universal behavior object class provides a set of methods that can be used to perform common operations on objects, such as comparison, hashing, and string representation. These methods are used by the Python interpreter to perform various operations on objects, such as sorting, hashing, and printing.

class Car:
    # __new__: Controls object creation (rarely overridden)
    def __new__(cls, model, color):
        print(f"Creating a new {cls.__name__} instance")
        instance = super().__new__(cls)  # Call the default object creation
        return instance

    # __init__: Initializes the object with attributes
    def __init__(self, model, color):
        print(f"Initializing {model} with color {color}")
        self.model = model
        self.color = color
        self._protected_attr = "I'm protected"

    # __repr__: Developer-friendly string representation
    def __repr__(self):
        return f"<Car model={self.model}, color={self.color}>"

    # __str__: User-friendly string representation
    def __str__(self):
        return f"A {self.color} {self.model} car"

    # __eq__: Defines equality comparison (==)
    def __eq__(self, other):
        if not isinstance(other, Car):
            return False
        return self.model == other.model and self.color == other.color

    # __hash__: Provides a hash value for the object
    def __hash__(self):
        return hash((self.model, self.color))

    # __ne__: Defines inequality comparison (!=)
    def __ne__(self, other):
        return not self.__eq__(other)

    # __getattribute__: Controls access to attributes
    def __getattribute__(self, name):
        print(f"Accessing attribute: {name}")
        return super().__getattribute__(name)

    # __setattr__: Controls setting of attributes
    def __setattr__(self, name, value):
        print(f"Setting attribute {name} to {value}")
        if name == "color" and not isinstance(value, str):
            raise ValueError("Color must be a string")
        super().__setattr__(name, value)

    # __delattr__: Controls deletion of attributes
    def __delattr__(self, name):
        print(f"Deleting attribute: {name}")
        if name == "model":
            raise AttributeError("Cannot delete model attribute")
        super().__delattr__(name)

    # __dir__: Customizes the list of attributes
    def __dir__(self):
        return ["model", "color", "drive"]  # Only show these attributes

    # A sample method for demonstration
    def drive(self):
        return f"{self.model} is driving!"

# Testing the Car class
if __name__ == "__main__":
    # Create two Car objects
    print("--- Creating cars ---")
    car1 = Car("Toyota", "Red")
    car2 = Car("Toyota", "Red")
    car3 = Car("Honda", "Blue")

    # Test __str__ and __repr__
    print("\n--- Testing string representations ---")
    print(str(car1))  # Calls __str__
    print(repr(car1))  # Calls __repr__

    # Test __eq__ and __ne__
    print("\n--- Testing equality ---")
    print(f"car1 == car2: {car1 == car2}")  # Should be True
    print(f"car1 != car3: {car1 != car3}")  # Should be True

    # Test __hash__
    print("\n--- Testing hash ---")
    print(f"Hash of car1: {hash(car1)}")
    print(f"Hash of car2: {hash(car2)}")  # Should match car1's hash
    print(f"Using cars in a set: {len({car1, car2, car3})}")  # Should be 2

    # Test attribute access (__getattribute__, __setattr__, __delattr__)
    print("\n--- Testing attribute access ---")
    print(f"car1.model: {car1.model}")  # Access attribute
    car1.color = "Green"  # Set attribute
    try:
        del car1.color  # Delete attribute
    except AttributeError as e:
        print(f"Error: {e}")

    # Test __class__ and __dict__
    print("\n--- Testing class and dict ---")
    print(f"car1's class: {car1.__class__}")
    print(f"car1's attributes: {car1.__dict__}")

    # Test __dir__
    print("\n--- Testing dir ---")
    print(f"Attributes of car1: {dir(car1)}")

    # Test a regular method
    print("\n--- Testing drive method ---")
    print(car1.drive())
    