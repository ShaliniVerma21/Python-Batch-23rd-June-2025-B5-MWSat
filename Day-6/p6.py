
#----------------------------------------- List ----------------------------------------

#Defining a list

""" 
A list is a collection of items enclosed in square brackets []. 
Lists are ordered, mutable, and can store heterogeneous data.
A list is a built-in data structure in Python.

Lists are:
- Ordered: The position of items is fixed.
- Mutable: We can change elements after creating the list.
- Heterogeneous: Can hold items of different types (int, str, bool, etc.)
- Defined using square brackets [ ]
"""

# A list can hold different types of elements
my_list = [10, "Python", 3.14, True]

# Example 1: List of integers
numbers = [1, 2, 3, 4, 5]

# Example 2: List of strings
names = ["Shalini", "Sharad", "Sudhakar"]

# Example 3: List with mixed data types
mixed = [42, "Data", False, 5.5]

# Example 4: Empty list
empty = []

# Example 5: List containing other lists (nested list)
nested = [[1, 2], [3, 4]]



#Creating list
#You can create a list using brackets or the list() constructor.

# Example 1: Using []
colors = ["Red", "Green", "Blue"]

# Example 2: Using list() constructor
letters = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']

# Example 3: From a range
numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]

# Example 4: Repeating elements
zeros = [0] * 5  # [0, 0, 0, 0, 0]
print(zeros)

zeros1 = [1,2,3]*5
print(zeros1)

# Example 5: List from another iterable
data = list((10, 20, 30))


#Accessing list elements of list

#Use indexing ([]) and slicing ([:]) to access list elements.

# Example 1: Indexing
fruits = ["Apple", "Banana", "Cherry"]
print(fruits[0])  # Apple

# Example 2: Negative indexing
print(fruits[-1])  # Cherry

# Example 3: Slicing
print(fruits[0:2])  # ['Apple', 'Banana']

# Example 4: Full list
print(fruits[:])  # ['Apple', 'Banana', 'Cherry']

# Example 5: Access nested list
nested = [[1, 2], [3, 4]]
print(nested[1][0])  # 3



#List methods
"""
Common methods to modify or work with lists:

Method	Description
append()- Add item at the end
insert()- Insert item at specific position
remove()- Remove specific item
pop()- Remove item by index
extend()- Add multiple items
"""
# Example 1: append()
items = [1, 2]
items.append(3)  # [1, 2, 3]

# Example 2: insert()
items.insert(1, "a")  # [1, 'a', 2, 3]

# Example 3: remove()
items.remove("a")  # [1, 2, 3]

# Example 4: pop()
items.pop(1)  # Removes 2, result [1, 3]

# Example 5: extend()
items.extend([4, 5])  # [1, 3, 4, 5]


#Functions used with list
"""
Built-in functions used to analyze list contents:

len()- Length of list
max()- Maximum value
min()- Minimum value
sum()- Sum of elements
sorted()- Returns a sorted copy
"""

nums = [10, 5, 30, 25]

# Example 1
print(len(nums))  # 4

# Example 2
print(max(nums))  # 30

# Example 3
print(min(nums))  # 5

# Example 4
print(sum(nums))  # 70

# Example 5
print(sorted(nums))  # [5, 10, 25, 30]



#Sorting list
"""
There are two ways to sort a list:

sort()     ➤ Sorts list in-place (modifies original list)  
sorted()   ➤ Returns a new sorted list (original stays unchanged)
"""

# Example 1: Ascending sort
marks = [85, 92, 75, 60]
marks.sort()
print(marks)  # [60, 75, 85, 92]

# Example 2: Descending sort
marks.sort(reverse=True)
print(marks)  # [92, 85, 75, 60]

# Example 3: sorted()
scores = [33, 11, 44]
new_scores = sorted(scores)
print(new_scores)  # [11, 33, 44]

# Example 4: Sort strings
names = ["Jay", "Mahi", "Amit"]
names.sort()  # ['Amit', 'Jay', 'Mahi']

# Example 5: Sort mixed case
words = ["banana", "Apple", "cherry"]
print(sorted(words))  # ['Apple', 'banana', 'cherry']
