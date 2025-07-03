#Example -1 : Calculate total marks of a students. Subjects : Hindi,English, Maths, History,Arts
marks_hindi = float(input("Enter marks in Hindi: "))
marks_english = float(input("Enter marks in English: "))
marks_math = float(input("Enter marks in Maths: "))
marks_history = float(input("Enter marks in History: "))
marks_arts = float(input("Enter marks in Arts: "))
marks_total = marks_hindi + marks_english + marks_math + marks_history + marks_arts
print("Total marks =", marks_total)


"""
Remember to use int() or float() when you're working with numbers.
The input() function always returns a string, so you need to convert it to a number if
you want to perform mathematical operations on it.
"""

# Without conversion
a = input("Enter number: ")  # string
b = input("Enter another: ")  # string
print(a + b)  # concatenates

# With conversion
a = int(input("Enter number: "))  # integer
b = int(input("Enter another: "))
print(a + b)  # adds


# ===============================
# Greet the user
# ===============================

# input() is used to take input from the user
name = input("Enter your name: ")  
print(f"Welcome, {name}!")  # f-string used to include variable in string

age = input("Enter your age : ")
print(f"Your age is {age}")  # f-string used to include variable in string

# ==================================
# VARIABLES
# ==================================
# A variable is a named container to store data.
# Python is dynamically typed. No need to declare data types.

# Syntax:
# variable_name = value
name =123
name ="hello"

# Examples:
name = "Shalini"
age = 28
city = "Mumbai"
fees = 5000.75
is_available = True
temperature = 37.5
mobile = "9876543210"
email = "shalini@example.com"
grade = 'A'
distance_km = 12.3

# ==================================
# DATA TYPES
# ==================================
"""
Python supports the following data types:
1. int         - Integer (e.g., 10)
2. float       - Decimal numbers (e.g., 5.67)
3. str         - Text data (e.g., "hello")
4. bool        - Boolean (True/False)
5. list        - Ordered, changeable, allows duplicates
6. tuple       - Ordered, unchangeable, allows duplicates
7. set         - Unordered, no duplicates
8. dict        - Key-value pairs
9. NoneType    - Represents no value
"""

# Real-world examples:
units = 10                 # int
price = 99.99              # float
product = "Laptop"         # str
is_active = True           # bool
items = ["pen", "book"]    # list
dimensions = (20, 15, 10)  # tuple
unique_ids = {101, 102}    # set
student = {"name": "Shalini", "age": 22}  # dict
data = None                # NoneType

# Type checking
print(type(price))  # Output: <class 'float'>


# ==================================
# OPERATORS IN PYTHON
# ==================================
"""
Operators are used to perform operations on variables and values.
Types:
1. Arithmetic
2. Relational (Comparison)
3. Assignment
4. Logical
5. Bitwise
6. Membership
7. Identity
"""

# ==================================
# 1. ARITHMETIC OPERATORS
# +, -, *, /, %, **, //

a = 15
b = 4

print(a + b)  # Addition: 19
print(a - b)  # Subtraction: 11
print(a * b)  # Multiplication: 60
print(a / b)  # Division: 3.75
print(a % b)  # Modulus: 3
print(b ** 2)  # Exponent: 16
print(a // b)  # Floor Division: 3

# Real-life:
price = 50
quantity = 3
print("Total:", price * quantity)

marks = (80 + 70 + 90) / 3
print("Average:", marks)

seconds = 250
print("Minutes:", seconds // 60)

# ==================================
# 2. RELATIONAL OPERATORS
# ==, !=, >, <, >=, <=

age = 20
print(age >= 18)  # True

marks = 45
print(marks >= 40)  # True

amount = 999
print(amount < 1000)  # True

entered_pin = 1234
real_pin = 4321
print(entered_pin == real_pin)  # False

temp = 25
print(temp != 30)  # True

height = 154
print(height > 150)  # True

weight = 65
print(weight <= 70)  # True

name = "Shalini"
print(name == "Shalini")  # True

price = 200
print(price >= 100 and price <= 500)  # True

num = 6
print(num % 2 == 0)  # Even check: True

# ==================================
# 3. ASSIGNMENT OPERATORS
# =, +=, -=, *=, /=, %=, **=, //=

x = 10
x += 5
x -= 3
x *= 2
x /= 4
x %= 4

# Use case:
salary = 10000
salary += 2000  # 12000

steps = 1000
steps += 500

total = 0
item_price = 250
total += item_price

lives = 3
lives -= 1

wallet = 1000
wallet -= 250
