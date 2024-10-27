# Lecture File I/O

# 1. Reading a file
# 2. Writing to a file
# 3. Appending to a file

# Reading a file
file = open("demo.txt", "r")
data = file.read() # Read the entire file
print(data, "Type of file: ", type(file))
file.close() # It is important to close the file after reading it

# Reading a file line by line
file = open("demo.txt", "r")
data = file.readlines() # Read the entire file line by line
# print(data, "Type of file: ", type(file))
file.close() # It is important to close the file after reading it

# Writing to a file
file = open("write.txt", "w") # If the file does not exist, it will be created
file.write("I want to become a good programmer")
file.close()

# Appending to a file
file = open("write.txt", "a")
file.write("\nCurrently I am learning Python")
file.close()

# Mode details:
# r - Read only
# w - Write only
# a - Append only
# r+ - Read and Write

# Detailed explanation of file modes:

# 'r' (Read Only):
# - Opens the file for reading only.
# - Raises FileNotFoundError if the file doesn't exist.
# - The file pointer is placed at the beginning of the file.

# 'w' (Write Only):
# - Opens the file for writing only.
# - Creates a new file if it doesn't exist.
# - If the file exists, it truncates (empties) the file.

# 'a' (Append Only):
# - Opens the file for appending.
# - Creates a new file if it doesn't exist.
# - If the file exists, the file pointer is placed at the end of the file.

# 'r+' (Read and Write):
# - Opens the file for both reading and writing.
# - Raises FileNotFoundError if the file doesn't exist.
# - The file pointer is placed at the beginning of the file.

# 'w+' (Write and Read):
# - Opens the file for both writing and reading.
# - Creates a new file if it doesn't exist.
# - If the file exists, it truncates the file.

# 'a+' (Append and Read):
# - Opens the file for both appending and reading.
# - Creates a new file if it doesn't exist.
# - If the file exists, the file pointer is placed at the end of the file for appending.

# Example usage:
# Example usage:
# Writing to a file
with open('example.txt', 'w') as file:
    file.write('This is an example of writing to a file.')

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print("File contents:", content)

# Appending to a file
with open('example.txt', 'a') as file:
    file.write('\nThis line is appended to the file.')

# Reading and writing (r+)
with open('example.txt', 'r+') as file:
    content = file.read()
    file.write('\nAdding this line using r+ mode.')

# Writing and reading (w+)
with open('example.txt', 'w+') as file:
    file.write('Overwriting the file with w+ mode.')
    file.seek(0)  # Move the cursor to the beginning of the file
    new_content = file.read()
    print("New file contents:", new_content)

# Appending and reading (a+)
with open('example.txt', 'a+') as file:
    file.write('\nAppending with a+ mode.')
    file.seek(0)  # Move the cursor to the beginning of the file
    final_content = file.read()
    print("Final file contents:", final_content)

# Note: It's recommended to use the 'with' statement as it automatically closes the file
# after the block of code is executed, even if an exception occurs.

# import os

# os.remove("example.txt") # This will delete the file


# os.rename("write.txt", "write_new.txt") # This will rename the file

# os.path.exists("write.txt") # This will check if the file exists

# os.path.getsize("write.txt") # This will get the size of the file

# os.path.getctime("write.txt") # This will get the creation time of the file

# os.path.getmtime("write.txt") # This will get the modification time of the file

# os.path.abspath("write.txt") # This will get the absolute path of the file


# Practice Questions:
# 1. Write a program to read a file and count the number of words in it.
with open("write.txt", "r") as file:
    data = file.read()
    words = data.split()
    print("Number of words: ", len(words))

# 2. Write a program to read a file and count the number of lines in it.
with open("write.txt", "r") as file:
    data = file.readlines()
    print("Number of lines: ", len(data))

# 3. Write a program to read a file and count the number of characters in it.
with open("write.txt", "r") as file:
    data = file.read()
    print("Number of characters: ", len(data))

# 4. Write a program to read a file and count the number of vowels in it.
with open("write.txt", "r") as file:
    data = file.read()
    vowels = "aeiouAEIOU"
    count = sum(1 for char in data if char in vowels)
    print("Number of vowels: ", count)

# 5. Replace a word in a file with another word.
with open("write.txt", "r") as file:
    data = file.read()
    data = data.replace("Python", "JavaScript")
    with open("write.txt", "w") as file:
        file.write(data)

# 6. Write a program to read a file and count the number of times a word appears in it.
def count_word(word):
    with open("write.txt", "r") as file:
        data = file.read()
        return data.count(word)
print(count_word("Python"))

def print_even_numbers():
    with open("number.txt", "r") as file:
        data = file.read()
        numbers = data.split(", ")
        count_even = 0
        for number in numbers:
            if int(number) % 2 == 0:
                print(number)
                count_even += 1
        print("Number of even numbers: ", count_even)
print_even_numbers()
