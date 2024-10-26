# List in python
marks = [95, 98, 97]
print(marks)
print(marks[0])
print(marks[-1])
print(type(marks) == list)

# slicing
print(marks[0:2])
print(marks[:2])
print(marks[0:])
print(marks[:])

# List functions
print(len(marks))
print(max(marks))
print(min(marks))
print(sum(marks))

# List methods
marks.append(99)
print("After appending: ", marks)

marks.insert(0, 94)
print("After inserting: ", marks)

marks.extend([90, 91])
print("After extending: ", marks)

marks.remove(94)
print("After removing: ", marks)

marks.pop()
print("After popping: ", marks)

marks.pop(1)
print("After popping at index 1: ", marks)  


marks.reverse()
print("After reversing: ", marks)

marks.sort()
print("After sorting: ", marks)

marks.clear()
print("After clearing: ", marks)

# Tuple in python
tuple_marks = (95, 98, 97)
print(tuple_marks)
print(tuple_marks[0])
print(type(tuple_marks) == tuple)

# Practice questions
print("Practice questions")

# mov1 = input("Enter the first movie: ")
# mov2 = input("Enter the second movie: ")
# mov3 = input("Enter the third movie: ")
# # or movies.append(input("Enter the movie: "))
# movies = [mov1, mov2, mov3]
# print(movies)

# Palindrome
pal_list = [1, 2, 3, 2, 1, 1]

if pal_list == pal_list[::-1]: # [::-1] is used to reverse the list or we can use reverse() method
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")

#  Write a tuple with Grade A, B, C, D, E and count of students who got A
grades = ("A", "B", "C", "D", "E")
count_A = grades.count("A")
print(count_A)

