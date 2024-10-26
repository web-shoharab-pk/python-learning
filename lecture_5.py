# Loops in Python

# While loop
i = 0
while i < 10090:
    # print(i)
    i += 1

# for loop
# for i in range(10):
    # print(i)

# Practice Questions
i = 100
while i > 0:
    print(i)
    i -= 1

# Practice Questions
i = 1
while i <= 100:
    print(i)
    i += 3 * 1

#  table of 3
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(i * n)
    i += 1

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(nums):
    print(nums[i])
    i += 1

# continue and break
i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1

i = 0
while i < 10:
    if i == 5:
        i += 1
        print("skipping 5")
        continue
    print(i)
    i += 1
# For loop
vagitables = ["potato", "tomato", "onion", "garlic", "carrot"]
for i in vagitables:
    print(i)

str = "Shoharab Pk"
for i in str:
    print(i)
else:
    print("No items left")

# Practice Questions using for loop
# 1. Print the sum of first 10 numbers
sum = 0
n = int(input("Enter a number to find sum: "))
for i in range(1, n+1): # range(start, end, step)
    sum += i
print(sum)
# Search for a number in a list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search = int(input("Enter a number to search for: "))
for i in nums:
    if i == search: # linear search
        print("Number found at index", nums.index(i))
        break
else:
    print("Number not found")

for i in range(100, 0, -1):
    print(i)

# Pass statement
for i in range(10):
    pass # do nothing

# factorial of a number
n = int(input("Enter a number to find factorial: "))
factorial = 1
for i in range(1, n+1):
    factorial *= i
    print(n, "*", i, "=", factorial)
    # explanation of factorial of 5
    # 5 * 1 = 5
    # 5 * 2 = 10
    # 5 * 3 = 15
    # 5 * 4 = 20
    # 5 * 5 = 25
print(factorial)
