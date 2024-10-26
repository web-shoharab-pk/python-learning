# Dictionary in python
info = {
  "name": "John",
  "age": 20,
  "city": "New York",
  "marks": [95, 98, 97],
  "subjects": {
    "Maths": 95,
    "Science": 98,
    "English": 97
  }
}
print(info)
print(info["name"])
info["name"] = "Jane"
print(info)
print(type(info) == dict)

print("Maths marks: ", info["subjects"]["Maths"])
print("Keys: ", info.keys())
print("Values: ",   info.values())
print("Items: ", info.items())

null_dict = {}
null_dict["name"] = "John"
print(null_dict)
print(null_dict.get("name"))
print(null_dict.get("age", 20)) # if age is not present in the dictionary, it will return 20
null_dict.update({"subjects": {"Maths": 95, "Science": 98, "English": 97}})
print(null_dict)

# Sets in python
collection = {1, 2, 3, 3, 4, 5, "Hello", "World", "Hello", 6}
print(collection)
print(type(collection) == set)
print(collection.pop())
# empty set
empty_set = set() 

# add elements to set
empty_set.add(1)
empty_set.add(2)
empty_set.add(3)
print(empty_set)

# remove elements from set
empty_set.remove(1)
print(empty_set)

# Frozenset
frozen_set = frozenset([1, 2, 3, 4, 3, 5]) # immutable set
print(frozen_set)
 
# Union and Intersection
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))
print(set1.intersection(set2))

# Practice Questions
# 1. Write a program to check if a key exists in a dictionary
# 2. Write a program to remove duplicates from a list
# 3. Write a program to find the intersection of two sets
# 4. Write a program to find the union of two sets

# 1
info = {"name": "John", "age": 20, "city": "New York"}
print("name" in info)

# 2
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = list(set(list1))
print(list2)

# 3
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.intersection(set2))

# 4
print(set1.union(set2))

dictionary = {
  "cat": "a small animal",
  "dog": "a big animal",
  "horse": "a big animal",
  "table": ["a piece of furniture", "a table"]
}
print(dictionary)
print(dictionary["table"][1])

# Practice Questions
subjects = {"Maths", "Science", "English", "python", "Java", "C++", "Javascript", "C#", "C++", "Python", "Maths" }
# unique_subjects = list(set(subjects))
print("Required number of class rooms: ", len(subjects))

marks = {}
marks.update({"physics": int(input("Enter physics marks: "))})
marks.update({"chemistry": int(input("Enter chemistry marks: "))})
marks.update({"maths": int(input("Enter maths marks: "))})
print(marks)

numbers = {9, 9.0, 9.00}
numbers = {('int', 9), ('float', 9.0), ('float', 9.00)}
print(numbers)
