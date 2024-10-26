# String

str1 = "Hello, World! 'Shoharab'"
str2 = 'This is a single quoted string'
str3 = """This is a triple quoted string"""

multiple_line_string = """This is a \n multiple line string \t that spans multiple lines \r in the code."""
print(str1)
print(str2)
print(str3)
print(multiple_line_string)

# String concatenation
hello = "Hello"
world = "World"
print(hello + world)

#  length of a string
print(len(hello))

# String indexing
print(hello[0])
print(hello[-1])
print(hello[0:3]) # slicing
print(hello[0:]) # [0:len(hello)]
print(hello[:3]) # [0:3]

# String functions
python_string = "I am learning Python"

print(python_string.endswith("on"))

print(python_string.startswith("I"))

print(python_string.replace("Python", "Java"))

print(python_string.find("Python"))

print(python_string.upper())
print(python_string.lower())
print(python_string.capitalize())
print(python_string.title())
print(python_string.count("l"))

# String methods
# print(hello.isalnum())
# print(hello.isalpha())
# print(hello.isdigit())
# print(hello.islower())
# print(hello.isupper())

# Practice questions
name = input("Enter your name: ")
print("The number of 'a' in your name is: ", name.count("a"))
print("Length of your name is: ", len(name))

#  Conditional statements
x = 10
y = 20

if x > y:
    print("x is greater than y")
else:
    print("y is greater than x")

light = "green"

if light == "green":
    print("Go")
elif light == "yellow":
    print("Prepare to stop")
else:
    print("Stop")

#  conditional nesting
age = 18

if age >= 18:
    print("You are an adult")
    if age >= 65:
        print("You are a senior citizen")
    else:
        print("You are a young adult")
else:
    print("You are a minor")

# Practice questions
grade = int(input("Enter your grade: "))

if grade >= 90:
    print("You got an A")
elif grade >= 80:
    print("You got a B")
elif grade >= 70:
    print("You got a C")
else:
    print("You failed")

# Gratest number of four numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

if num1 > num2 and num1 > num3 and num1 > num4:
    print("The greatest number is: ", num1)
elif num2 > num1 and num2 > num3 and num2 > num4:
    print("The greatest number is: ", num2)
elif num3 > num1 and num3 > num2 and num3 > num4:
    print("The greatest number is: ", num3)
else:
    print("The greatest number is: ", num4) 

