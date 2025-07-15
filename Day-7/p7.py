
#-------------------------------------------Tuple------------------------------------------
""" 
A tuple is a built-in data structure in Python that allows you to store multiple items 
in a single variable.
Tuples are:

--> Ordered (items have a fixed position)
--> Immutable (cannot be changed after creation)
--> Can contain duplicate values
--> Represented using parentheses ( )
"""

#Defining a tuple

# Defining a tuple with integers
numbers = (1, 2, 3, 4)
print(numbers)
print(type(numbers))

# Tuple with mixed data types
info = ("Alice", 25, 5.6, True)
print(info)
print(type(info))

# Tuple with a single element (add a comma)
single_element = (10,)
print(single_element)
print(type(single_element))

single_element1 = (10)
print(single_element1)
print(type(single_element1))

# Empty tuple
empty = ()
print(empty)
print(type(empty))


#Creating a tuple

# Example 1: Tuple of fruits
fruits = ("apple", "banana", "cherry")
print(fruits)

# Example 2: Tuple using tuple() constructor from list
colors = tuple(["red", "green", "blue"])
print(colors)

# Example 3: Tuple with mixed datatypes
person = ("John", 30, "Engineer", True)
print(person)

# Example 4: Tuple with nested tuple
nested = ((1, 2), (3, 4))
print(nested)

# Example 5: Tuple from a string (each character becomes an element)
chars = tuple("HELLO")
print(chars)


#Accessing elements of the tuple

# Example 1: Indexing
t = ("a", "b", "c", "d")
print(t[0])   # Output: a

# Example 2: Negative indexing
print(t[-1])  # Output: d

# Example 3: Slicing
print(t[1:3]) # Output: ('b', 'c')

# Example 4: Iterating through a tuple
for item in t:
    print(item)

# Example 5: Length of a tuple
print(len(t)) # Output: 4


#What is Immutability
""" 
Tuples are immutable, meaning once created, their elements cannot be changed, added, or removed.
"""
# Example of immutability
my_tuple = (10, 20, 30)
# my_tuple[1] = 50     # ❌ This will raise TypeError

# However, we can replace the whole tuple
my_tuple = (100, 200)
print(my_tuple)


#List vs tuples

""" 
List vs Tuple -->

Lists are mutable, meaning their elements can be changed, added, or removed after creation.
Tuples are immutable, meaning their elements cannot be changed, added, or removed after creation.

-------------------------------------------------------------------------
Feature	      |       List	              |         Tuple
-------------------------------------------------------------------------
Syntax	      |        []	              |          ()
Mutability	  |    Mutable (changeable)	  |      Immutable (unchangeable)
Performance	  |      Slower	              |         Faster
Methods	Many  |   built-in methods	      |       Fewer methods
Use Case	  |   Frequent updates needed |	      Fixed data or read-only
--------------------------------------------------------------------------
"""

# Tuple Operations –

# Example 1: Concatenation(Combines both tuples into one)
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)  # Output: (1, 2, 3, 4)

# Example 2: Repetition (Repeats the elements of the tuple 3 times)
print(t1 * 3)   # Output: (1, 2, 1, 2, 1, 2)

# Example 3: Membership test (Checks if the element 2 exists in the tuple)
print(2 in t1)  # Output: True

# Example 4: Count of an element (Counts how many times 2 occurs in the tuple)
t3 = (1, 2, 2, 3, 2)
print(t3.count(2))  # Output: 3

# Example 5: Index of an element (Returns the index (position) of the first occurrence of 3)
print(t3.index(3))  # Output: 3

# Example 6: Converting a list to tuple (Useful when you want to make a list immutable)
my_list = [10, 20, 30]
converted_tuple = tuple(my_list)
print(converted_tuple)  # Output: (10, 20, 30)

# Example 7: Tuple unpacking (Allows assigning individual values from tuple to variables)
student = ("John", 21, "BBA")
name, age, course = student
print(f"Name: {name}, Age: {age}, Course: {course}")
# Output: Name: John, Age: 21, Course: BBA

# Example 8: Nested tuple access (Accessing inner element from a nested tuple)
data = (("Alice", "HR"), ("Bob", "IT"), ("Charlie", "Sales"))
print(data[1][0])  # Output: Bob

# Example 9: Iterating over tuple (Prints each color one by one from the tuple)
colors = ("Red", "Green", "Blue")
for color in colors:
    print(color)

# Example 10: Tuple with mixed data and type checking (Prints type of each element in the tuple)
employee = ("E001", "Shalini", 28, True)
for item in employee:
    print(f"{item} -> {type(item)}")


#  Real-World Data Analysis Example Using Tuple

""" 
Problem:
You are analyzing a product sales dataset where each record is a tuple:
(Product_Name, Category, Price, Quantity_Sold)

Objective:
Calculate total sales and find the most sold product.
"""

# List of sales records (tuples)
sales_data = [
    ("Laptop", "Electronics", 50000, 10),
    ("Mouse", "Electronics", 500, 50),
    ("Shirt", "Clothing", 800, 30),
    ("Book", "Stationery", 300, 40),
    ("Pen", "Stationery", 20, 200)
]

total_sales = 0
max_sold = 0
top_product = ""

for item in sales_data:
    name, category, price, qty = item
    sale = price * qty
    total_sales += sale

    if qty > max_sold:
        max_sold = qty
        top_product = name

print("Total Sales (Rs):", total_sales)
print("Top Sold Product:", top_product)
