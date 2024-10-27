# Object Oriented Programming (OOP) in Python

# Classes vs Functions
# Classes are used to create objects and define their properties and methods.
# Functions are used to perform specific tasks.

# Class & Objects
# Class is a blueprint for creating objects.
# Object is an instance of a class.

# Creating a Class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        return sum(self.marks) / len(self.marks)

# Creating an Object
student = Student("John", [90, 80, 70, 60])
print(student.name)  # Output: John
print(student.marks)   # Output: [90, 80, 70, 60]
print(student.get_avg())  # Output: 75.0
# create Bike class
class Bike:
    # Default Constructor
    def __init__(self):
        print("Default Constructor")
    # Parameterized Constructor
    brand = "Honda"
    def __init__(self, name, gear, color, cc, model):
        self.name = name
        self.gear = gear
        self.color = color
        self.cc = cc
        self.model = model
    def buy(self):
        print(f"Bike Details:")
        print(f"Name: {self.name}")
        print(f"Color: {self.color}")
        print(f"Gear: {self.gear}")
        print(f"CC: {self.cc}")
        print(f"Model: {self.model}")
        print(f"Brand: {self.brand}")


bike1 = Bike("Mountain Bike", 6, "Red", 250, "2024")
bike2 = Bike("Road Bike", 11, "Blue", 350, "2023")
bike1.buy()
bike2.buy()
print(f"Gear: {bike1.gear}")
print(f"CC: {bike1.cc}")

# Class & Instance Attributes
# Class Attributes are shared by all instances of a class.
# Instance Attributes are unique to each instance of a class.

# Abstraction
# Abstraction is the process of hiding the complex details of an object and exposing only the necessary parts to the outside world.
# Abstraction is achieved by using access modifiers.
# Access modifiers are used to restrict access to the class members.
# There are three access modifiers in Python: public, protected, and private.
# Example:
class Car:
    def __init__(self):
        self.acc = False 
        self.brk = False
        self.clutch = False
    def start(self):
        self.acc = True 
        self.clutch = True
        print("Car Started")
    def stop(self):
        self.acc = False
        self.clutch = False
        self.brk = True
        print("Car Stopped")

# Encapsulation
# Encapsulation is the process of hiding the internal details of an object and exposing only the necessary parts to the outside world.
# Encapsulation is achieved by using access modifiers.
# Access modifiers are used to restrict access to the class members.
# There are three access modifiers in Python: public, protected, and private.
# Example:
class Car:
    def __init__(self):
        self.__speed = 0
    def set_speed(self, speed):
        self.__speed = speed
    def get_speed(self):
        return self.__speed

# Practice Questions
# 1. Create a class called "Car" with the following attributes: make, model, year, color.
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
# 2. Create a method called "drive" that prints "Driving the car".
    def drive(self):
        print("Driving the car")
# 3. Create an object called "my_car" with the following values: make = "Toyota", model = "Corolla", year = 2020, color = "Red".
my_car = Car("Toyota", "Corolla", 2020, "Red")
# 4. Call the drive method on the my_car object.
my_car.drive()

class Account:
    def __init__(self, name, balance, acc_no):
        self.name = name
        self.balance = balance
        self.acc_no = acc_no
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def get_balance(self):
        return f"The balance is {self.balance}"


acc1 = Account("John", 1000, 1234567890)
acc1.deposit(500)
print(acc1.get_balance())  # Output: The balance is 1500
acc1.withdraw(200)
print(acc1.get_balance())  # Output: The balance is 1300

# Static Methods
# Static methods are methods that belong to the class and not to any specific instance of the class.
# Static methods are defined using the @staticmethod decorator.
# Static methods are called using the class name.
class Math:
    @staticmethod # decorator
    def add(a, b):
        return a + b
print(Math.add(1, 2))  # Output: 3
