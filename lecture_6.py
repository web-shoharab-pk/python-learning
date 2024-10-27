# Functions in Python
# def keyword is used to define a function

# Function definition
def add(a, b): # a and b are parameters
    sum = a + b
    # return add(sum, 10)
    return sum # return statement

print(add(111111, 233333333))

# Calculate average of five numbers
def average(a, b, c, d, e):
    return (a + b + c + d + e) / 5

print(average(10, 20, 30, 40, 50))

print("Shoharab",  end=" ");

print("Pk")

# Default parameter

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Shoharab")
# Keyword argument
def greet(name="Guest", age = 20): # default argument should be after non-default argument
    print("Hello", name, "you are", age, "years old")

greet(age=21, name="Shoharab")

# Practice Questions
# 1. Write a function to calculate the area of a rectangle
def area_rectangle(length, breadth):
    return length * breadth

# 2. Write a function to calculate the area of a triangle
def area_triangle(base, height):  
    return 0.5 * base * height

# 3. Write a function to calculate the area of a circle
def area_circle(radius):
    return 3.14 * radius * radius

# 4. Write a function to calculate the area of a square
def area_square(side):
    return side * side

# 5. Write a function to calculate the area of a trapezium
def area_trapezium(a, b, h):
    return 0.5 * (a + b) * h

heroes = ["spider man", "thor", "hulk", "iron man", "captain america"]

# print in one line using function
def print_heros(heroes):
    for hero in heroes:
        print(hero, end=" ")

print_heros(heroes)

# find the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1) # 1 * 2 * 3 * 4 * 5 = 120

print(factorial(5))

# Convert a number to binary
def binary(n):
    if n == 0:
        return 0
    return n % 2 + 10 * binary(n//2)

print(binary(13))

# Convert USD to BDT
def usd_to_bdt(usd):
    return usd * 130

print(usd_to_bdt(10))

#  Check user input odd or even
def odd_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(odd_even(int(input("Enter a number: "))))

# Recursion function
# Recursion is a function that calls itself 

def recursion(n):
    if n == 0:
        return 0
    return n + recursion(n-1)

print(recursion(5))
#  write a recursion function explaination
#  recursion is a function that calls itself
#  it is used to solve problems that can be broken down into smaller problems
#  it is a powerful tool in programming
#  it is used in many algorithms like quicksort, mergesort, binary search, etc.

# Practice Questions
# 1. Write a recursion function to calculate the sum of first n natural numbers
def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n-1)

print(sum_natural(5))
# 2. Write a recursion function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
# 3. Write a recursion function to calculate the nth Fibonacci number
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))
# 4. Write a recursion function to calculate the sum of digits of a number
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n//10)

print(sum_digits(12345))
# 5. Write a recursion function to calculate the power of a number
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent-1)

print(power(2, 3))

