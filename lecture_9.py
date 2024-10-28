# OOP in Python (Part 2)

# del keyword
# del is used to delete objects
# del can be used to delete variables, lists, tuples, dictionaries, etc.

# del keyword with variables
a = 10
del a
# print(a) # NameError: name 'a' is not defined

# del keyword with lists
my_list = [1, 2, 3, 4, 5]
del my_list[0:2]
print(my_list) # Output: [3, 4, 5]


class Student:
  def __init__(self, name):
    self.name = name

s1 = Student("John Doe")
print(s1.name) # Output: John Doe
del s1.name
# print(s1.name) # AttributeError: 'Student' object has no attribute

class Account:
  def __init__(self, acc_no, acc_pass):
    self.acc_no = acc_no
    self.__acc_pass = acc_pass # Private attribute
  def change_password(self, new_pass):
    self.__acc_pass = new_pass
    print("Password changed successfully", self.__acc_pass)
  def __account_info(self): # Private method
    print("Account number:", self.acc_no)

acc1 = Account(12345, "password123")

acc1.change_password("new_password")
# print(acc1.acc_no, acc1.acc_pass) # Output: 12345 password123 (Error: 'Account' object has no attribute '__acc_pass')

# Inheritance
class Car:
  @staticmethod
  def start_engine():
    print("Engine started")
  @staticmethod
  def stop_engine():
    print("Engine stopped")

class Toyota(Car):
  def __init__(self,  model):
    self.name = 'Toyota car'
    self.model = model

car1 = Toyota("Camry")
car2 = Toyota("Civic")

print(car1.name, car1.model) # Output: Toyota Camry
print(car1.start_engine()) # Output: Engine started

# Inheritance types
# 1. Single inheritance
# 2. Multiple inheritance
# 3. Multilevel inheritance

# Multiple inheritance example
class Vehicle:
  varA = "Vehicle variable"

class Car():
  varB = "Car variable"

class MotorVehicle(Vehicle, Car):
  varC = "Motor vehicle variable"

m1 = MotorVehicle()
print(m1.varA, m1.varB, m1.varC) # Output: Vehicle variable Car variable Motor vehicle variable

# Multi-level inheritance
class Fortuner(Toyota):
  def __init__(self, model, type):
    self.model = model
    self.type = type

for1 = Fortuner("Fortuner", "SUV")
for1.start_engine() # Output: Engine started


# Super Method
class Car:
  def __init__(self, model):
    self.model = model

  @staticmethod
  def start_engine():
    print("Engine started")
  
  @staticmethod
  def stop_engine():
    print("Engine stopped")

class Toyota(Car):
  def __init__(self, name, model):
    self.name = name
    super().__init__(model) # Calling the parent class constructor
    # self.model = model # Overriding the parent class method

car1 = Toyota("Thar", "Camry")
print(car1.name, car1.model) # Output: Thar Camry

# Static methods
class Person:
  name = "anonymous"

  def change_name(self, new_name):
    self.name = new_name
    # Person.name = new_name # Changing the class variable directly
    # self.__class__.name = new_name # Changing the class variable indirectly
  @classmethod
  def changeName(cls, name):
    cls.name = name

p1 = Person()
p1.change_name("John Doe")
print(p1.name) # Output: John Doe
print(Person.name) # Output: anonymous
p1.changeName("Mahir Khan")
print(Person.name) # Output: Mahir Khan


# Property decorators
class Student:
  def __init__(self, phy, chem, math):
    self.phy = phy
    self.chem = chem
    self.math = math
    # def calculate_percentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
  @property # Decorator to make a method callable as an attribute
  def percentage(self):
      return str((self.phy + self.chem + self.math) / 3) + "%"



stu1 = Student(85, 90, 80)

print(stu1.percentage) # Output: 85.0%

stu1.phy = 95
print(stu1.percentage) # Output: 90.0%
# Getters and Setters
# Example of getter and setter
class Student:
  def __init__(self, phy, chem, math):
    self._phy = phy
    self._chem = chem
    self._math = math

  @property
  def phy(self):
    return self._phy

  @phy.setter
  def phy(self, value):
    if value < 0 or value > 100:
      raise ValueError("Physics marks must be between 0 and 100")
    self._phy = value

  @property
  def percentage(self):
    return str((self._phy + self._chem + self._math) / 3) + "%"

# Polymorphism
# OOP have 4 pillars: Encapsulation, Inheritance, Polymorphism, and Abstraction

print(1+2) # Output: 3 addition

print("1"+"2") # Output: 12 concatenation

# Polymorphism is the ability of an object to take on multiple forms
# In Python, polymorphism is achieved through method overriding
print([1,2,3]+[4,5,6]) # Output: [1, 2, 3, 4, 5, 6] merging (concatenation) two lists
 
# Complex numbers 
# Complex numbers are numbers that have a real part and an imaginary part
# The imaginary part is denoted by j
print(1+2j) # Output: (1+2j)
print(type(1+2j)) # Output: <class 'complex'>
print(1+2j+3+4j) # Output: (4+6j)

class Complex:
  def __init__(self, real, imaginary):
    self.real = real
    self.imaginary = imaginary + 1j

  def showNumber(self):
    print(self.real, self.imaginary)
  # Overriding the addition operator
  def __add__(self, other): # Overriding the addition operator
    return Complex(self.real + other.real, self.imaginary + other.imaginary)
  def __str__(self): # Overriding the string representation of the object
    return f"{self.real} + {self.imaginary}"
  
  def __mul__(self, other): # Overriding the multiplication operator
    return Complex(self.real * other.real, self.imaginary * other.imaginary)
  
  def __truediv__(self, other): # Overriding the division operator
    return Complex(self.real / other.real, self.imaginary / other.imaginary)

c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 + c2) # Output: 4 + 6j
c1.showNumber() # Output: 1 2
c2.showNumber() # Output: 3 4

# Practice questions
class Circle:
  def __init__(self, radius):
    self.radius = radius
  def area(self):
    return (22/7) * self.radius * self.radius
  def perimeter(self):
    return 2 * (22/7) * self.radius

c1 = Circle(5)
print(c1.area()) # Output: 78.5
print(c1.perimeter()) # Output: 31.4


class Employee:
  def __init__(self, name, department, role, salary):
    self.name = name
    self.department = department
    self.role = role
    self.salary = salary
  def show_details(self):
    print(f"Name: {self.name}, Department: {self.department}, Role: {self.role}, Salary: {self.salary}")

class Engineer(Employee):
  def __init__(self, name, age):
    self.name = name
    self.age = age
    super().__init__(name, 'Engineering', 'Engineer', 50000)

e1 = Engineer("John Doe", 25)
e1.show_details() # Output: Name: John Doe, Department: IT, Role: Developer, Salary: 50000


class Order:
  def __init__(self, item, quantity, price):
    self.item = item
    self.quantity = quantity
    self.price = price
  def calculate_total(self):
    return self.quantity * self.price
  def __gt__(self, order2):
    return self.calculate_total() > order2.calculate_total()
  
  def __str__(self):
    return f"Order: {self.item}, Quantity: {self.quantity}, Price: {self.price}"

o1 = Order("Laptop", 2, 50000)
print('Total price of the order is', o1.calculate_total()) # Output: Total price of the order is 100000

o2 = Order("Mouse", 2, 333000)
print(o1 > o2) # Output: True
print(o1) # Output: Order: Laptop, Quantity: 2, Price: 50000
print(o2) # Output: Order: Mouse, Quantity: 2, Price: 333000
