#Comments in python

# Single Line Comments

"""
Multi
Line 
Comments
"""

"""
1. Comments in python are denoted by the # symbol
2. Any text after the # symbol on the same line is ignored by the interpreter
3. Comments are used to explain the code and make it easier to understand
4. Comments can be used to disable a block of code temporarily
5. Comments can be used to document the code and make it easier to understand for other developers
"""
# -----------------------------------------------------------------------------------------

# Task: Print your full name using print()
print("My name is Shalini Verma")

# Task: Store your age and city in variables and print them
age = 27
city = "Mumbai"
print("Age:", age)
print("City:", city)

# Task: Concatenate first and last name
first_name = "Shalini"
last_name = "Verma"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# Task: Take 2 numbers from the user and print the sum
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)

# Task: Print multiplication table of a number
number = int(input("Enter a number: "))
print("Multiplication Table of", number)
print(number, "* 1 =", number * 1)
print(number, "* 2 =", number * 2)
print(number, "* 3 =", number * 3)
# ... and so on


# Task: Explain what a variable does
# This variable stores the user's country
country = "India"
print("Country:", country)


# Task: Swap values of two variables
a = 5
b = 10
print("Before Swap: a =", a, "b =", b)
a, b = b, a
print("After Swap: a =", a, "b =", b)


# Task: Check if Python is case sensitive
name = "Shalini"
Name = "Verma"
print(name)  # Shalini
print(Name)  # Verma


# Task: Take two numbers and do all arithmetic operations
x = float(input("Enter number 1: "))
y = float(input("Enter number 2: "))

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)


# Task: Show the data types of different values
a = 10         # int
b = 3.14       # float
c = "Python"   # str
d = True       # bool

print(type(a))
print(type(b))
print(type(c))
print(type(d))

