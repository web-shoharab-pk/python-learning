name = "John" 
age = 23
price = 19.99
discount = 0.2
print("I am", name, "and I am", age, "years old")
print("The price is: ", price * (1-discount))

# Variables are used to store data in a program. They are like containers that hold values. 
# types of variables: int, float, str, bool
print(type(name))
print(type(age))
print(type(price)) 

# type casting: converting one data type to another
print(float(age))
print(int(price))
print(type(str(age)))
print(bool(age))

a = None
print(type(a))

# Data Types in Python: int, float, str, bool, list, tuple, set, dict
# 1. int: whole numbers, positive or negative, no decimal point
# 2. float: decimal numbers, positive or negative
# 3. str: strings of text, enclosed in quotes
# 4. bool: boolean values, True or False
# 5. list: ordered collection of items, enclosed in square brackets, can contain different data types
# 6. tuple: ordered collection of items, enclosed in parentheses, can contain different data types
# 7. set: unordered collection of unique items, enclosed in curly braces, can contain different data types
# 8. dict: unordered collection of key-value pairs, enclosed in curly braces, keys and values can be different data types

#  Python reserved words: and, as, assert, break, class, continue, def, del, elif, else, except, False, finally, for, from, global, if, import, in, is, lambda, None, nonlocal, not, or, pass, raise, return, True, try, while, with, yield
a = 200
b = 330
diff = a - b
print("diff is", diff)
print("A") if a > b else print("B")

# Arithmetic Operators: +, -, *, /, %, **, //
# Comparison Operators: ==, !=, >, <, >=, <=
# Logical Operators: and, or, not
# Assignment Operators: =, +=, -=, *=, /=, %=, **=, //=
# Identity Operators: is, is not
# Membership Operators: in, not in
# Bitwise Operators: &, |, ^, ~, <<, >>

# Type Conversion: int(), float(), str(), bool()
# Type Casting: int(), float(), str(), bool()
 

# Practice Questions
# 1. Write a program to add two numbers
# 2. Write a program to find the area of a circle
# 3. Write a program to find the volume of a cylinder
# 4. Write a program to find the simple interest
# 5. Write a program to find the compound interest

# input1 = int(input("Enter first number: "))
# input2 = int(input("Enter second number: "))
# print("The sum of the two numbers is: ", input1 + input2) # sum of two numbers

# 2. Write a program to find the area of a circle
radius = float(input("Enter the radius of the circle: "))
print("The area of the circle is: ", 3.14 * radius ** 2) # area of a circle

# 3. Write a program to find the volume of a cylinder
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
print("The volume of the cylinder is: ", 3.14 * radius ** 2 * height) # volume of a cylinder

# 4. Write a program to find the simple interest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest per annum: "))
time = float(input("Enter the time period in years: "))
print("The simple interest is: ", principal * rate * time / 100) # simple interest

# 5. Write a program to find the compound interest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest per annum: "))
time = float(input("Enter the time period in years: "))
print("The compound interest is: ", principal * (1 + rate / 100) ** time - principal) # compound interest

