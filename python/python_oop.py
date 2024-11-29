"""
Assignment 1: Design Your Own Class! 🏗️
    Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
    Add attributes and methods to bring the class to life!
    Use constructors to initialize each object with unique values.
    Add an inheritance layer to explore polymorphism or encapsulation.
"""
class Smartphone:
    def __init__(self, brand, model, battery_level, os):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level
        self.os = os

    def charge(self, amount):
        """Charges the smartphone by the given amount."""
        self.battery_level += amount
        if self.battery_level > 100:
            self.battery_level = 100  # Maximum battery level is 100%
        print(f"{self.brand} {self.model} is now charged to {self.battery_level}%")

    def make_call(self, contact):
        """Simulates making a call."""
        if self.battery_level > 10:
            print(f"Calling {contact} from {self.brand} {self.model}...")
            self.battery_level -= 10  # Simulating battery usage for making a call
        else:
            print(f"Battery too low to make a call!")
    
    def check_battery(self):
        """Checks the current battery level."""
        print(f"{self.brand} {self.model} battery: {self.battery_level}%")

# case
phone1 = Smartphone("Apple", "iPhone 15", 50, "iOS")
phone1.make_call("John") # Output: Calling John from Apple iPhone 15...
phone1.check_battery() # Output: Apple iPhone 15 battery: 40%
phone1.charge(30) # Output: Apple iPhone 15 is now charged to 70%
phone1.check_battery() # Output: Apple iPhone 15 battery: 70%

# Inheritance
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_level, os, camera_resolution):
        super().__init__(brand, model, battery_level, os)
        self.camera_resolution = camera_resolution

    def take_picture(self):
        """Simulates taking a picture with the camera."""
        print(f"Taking a picture with {self.brand} {self.model}'s {self.camera_resolution} MP camera!")

# case
phone2 = SmartphoneWithCamera("Samsung", "Galaxy S23", 80, "Android", 108)
phone2.take_picture() # Output: Taking a picture with Samsung Galaxy S23's 108 MP camera!
phone2.make_call("Alice") # Output: Calling Alice from Samsung Galaxy S23...
phone2.check_battery() # Output: Samsung Galaxy S23 battery: 70%
phone2.charge(20) # Output: Samsung Galaxy S23 is now charged to 90%



"""
Activity 2: Polymorphism Challenge! 🎭
    Create a program that includes animals or vehicles with the same action (like move()). 
    However, make each class define move() differently 
    (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).
"""

class Car:
    def move(self):
        print("The car is driving 🚗")

class Plane:
    def move(self):
        print("The plane is flying ✈️")

class Fish:
    def move(self):
        print("The fish is swimming 🐟")

def test_move(animal_or_vehicle):
    animal_or_vehicle.move()

# instances of each class
car = Car()
plane = Plane()
fish = Fish()

# polymorphism test
test_move(car)    # Output: The car is driving 🚗
test_move(plane)  # Output: The plane is flying ✈️
test_move(fish)   # Output: The fish is swimming 🐟
