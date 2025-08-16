""" 
1. Introduction to Functions

--> What is a function?
A function is a block of reusable code that performs a specific task.
Instead of writing the same code again and again, we can write it 
once inside a function and call it whenever needed.

Example-- find area of 100 circles of different size in a playground
So, we can write 1 function to find area of circle and can call it 100 times.

--> Importance of functions in programming :
a. Breaks large programs into smaller parts.
b. Increases readability and maintainability.
c. Encourages code reuse.

--> Advantages:
a. Code Reusability - Write once, use many times.
b. Readability - Clean and understandable code.
c. Modularity - Breaks program into smaller logical parts.
d. Easy Debugging - Errors can be easily identified in specific functions.

--> Function naming rules
a. Must start with a letter or underscore (_)
b. Cannot start with a digit
c. Can contain letters, digits, underscore
d. Avoid Python keywords (def, for, while, etc.)

--> Indentation importance
a. Python uses indentation to define blocks of code.
b. Wrong indentation → IndentationError.

3. Types of Functions
In Python, functions are divided into two major categories:
1. Built-in functions
2. user defined functions

--> Built-in functions (e.g., print(), len(), type())
    
    a. These are functions that are already defined in Python.
    b. We don’t need to create them; just use them directly.
    c. They make development faster and easier.
    d. Python provides hundreds of built-in functions.
    
--> Examples of commonly used built-in functions:

a. print() → Displays output.
b. len() → Returns the length of a sequence.
c. type() → Returns the data type of a variable.
d. max() / min() → Find maximum / minimum values.
e. sorted() → Returns a sorted list.
f. sum() → Calculates the sum of elements.
g. abs() → Returns the absolute value.
h. round() → Rounds a floating number.
i. input() → Takes input from the user.
j. zip() → Combines multiple iterables.
"""

# Types of Built-in functions
"""
1. Numeric Functions
These work with numbers (integers, floats, complex). They help in mathematical operations.

a. abs(x) → Returns absolute value.
b. round(x, n) → Rounds number to n decimal places.
c. pow(x, y) → Returns 𝑥^𝑦
d. min(), max() → Minimum / Maximum.
e. sum(iterable) → Sum of numbers.
"""
# 1. abs() with positive and negative
print(abs(-25))
print(abs(15))

# 2. round() with floating numbers
print(round(3.14159, 2))
print(round(9.876, 1))

# 3. pow() to calculate powers
print(pow(2, 3))   # 2^3 = 8
print(pow(5, 2))   # 25

# 4. max() to find largest
print(max(10, 20, 5, 99))

# 5. min() to find smallest
print(min([44, 11, 67, 3]))

# 6. sum() with list
nums = [10, 20, 30, 40]
print("Sum:", sum(nums))

# 7. round() without decimal
print(round(45.678))  # rounds to nearest integer

# 8. abs() with complex number magnitude
print(abs(3+4j))  # returns sqrt(3^2 + 4^2) = 5

# 9. pow() with negative power
print(pow(2, -2))  # 1/(2^2) = 0.25

# 10. Combining min, max, sum
marks = [75, 88, 92, 60, 85]
print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Total:", sum(marks))


""" 
2. Type Conversion Functions
These convert one data type into another.

a. int(x) → Convert to integer.
b. float(x) → Convert to float.
c. str(x) → Convert to string.
d. list(x) → Convert to list.
e. tuple(x) → Convert to tuple.
f. set(x) → Convert to set.
"""
# 1. int() from float
print(int(9.99))

# 2. int() from string
print(int("123"))

# 3. float() from int
print(float(10))

# 4. float() from string
print(float("45.67"))

# 5. str() from number
num = 99
print("Converted to string:", str(num))

# 6. list() from tuple
tup = (1, 2, 3)
print(list(tup))

# 7. tuple() from list
lst = [10, 20, 30]
print(tuple(lst))

# 8. set() from list (removes duplicates)
lst2 = [1, 2, 2, 3, 4, 4, 5]
print(set(lst2))

# 9. str() from boolean
print(str(True))

# 10. Nested conversions
print(list("Python"))  # converts string to list of chars


""" 
3. String-related Functions
These work on strings and characters.

a. len(string) → Returns length.
b. ord(ch) → ASCII code of a character.
c. chr(num) → Character of ASCII code.
d. str.upper(), str.lower() → Convert case.
e. str.split() → Splits into list.
f. str.join() → Joins list into string.
"""
# 1. len() with string
print(len("Programming"))

# 2. ord() with character
print(ord('A'))

# 3. chr() with ASCII number
print(chr(66))

# 4. upper() method
print("python".upper())

# 5. lower() method
print("HELLO".lower())

# 6. split() into words
sentence = "I love Python programming"
print(sentence.split())

# 7. join() to join list with space
words = ["I", "love", "Python"]
print(" ".join(words))

# 8. join() with comma
print(",".join(words))

# 9. combine len + upper
s = "functions"
print(len(s.upper()))

# 10. mix ord + chr
code = ord('Z')
print("Code:", code, "-> Character:", chr(code))

""" 
4. Iterable & Collection Functions
These are useful with lists, tuples, sets, dictionaries.

a. sorted(iterable) → Returns sorted list.
b. enumerate(iterable) → Gives index & element.
c. zip(iter1, iter2) → Combines sequences.
d. map(func, iterable) → Applies function.
e. filter(func, iterable) → Filters elements.
"""
# 1. sorted() on list
nums = [5, 2, 9, 1, 7]
print(sorted(nums))

# 2. sorted() on string
print(sorted("python"))

# 3. enumerate() with list
fruits = ["apple", "banana", "mango"]
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)

# 4. zip() with two lists
names = ["Amit", "Neha", "Raj"]
marks = [90, 85, 88]
print(list(zip(names, marks)))

# 5. zip() with three lists
subjects = ["Math", "Science", "English"]
print(list(zip(names, marks, subjects)))

# 6. map() with lambda to square numbers
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)

# 7. filter() to find even numbers
evens = list(filter(lambda x: x % 2 == 0, range(1, 11)))
print(evens)

# 8. map() with str.upper
words = ["python", "java", "c++"]
print(list(map(str.upper, words)))

# 9. filter() to find names starting with A
names2 = ["Amit", "Ravi", "Anita", "Kiran"]
print(list(filter(lambda x: x.startswith("A"), names2)))

# 10. combine map + filter
nums = [1, 2, 3, 4, 5, 6]
result = list(map(lambda x: x**2, filter(lambda y: y % 2 == 0, nums)))
print(result)

""" 
5. Input/Output Functions
Used for interaction with users.

a. print() → Display output.
b. input() → Take input.
"""
# 1. Basic print
print("Hello, Python!")

# 2. Print multiple values
print("Sum of 5 and 10 is", 5+10)

# 3. Print with separator
print("Python", "Java", "C++", sep=" | ")

# 4. Print with end parameter
print("Hello", end=" ")
print("World")

# 5. Input string
name = input("Enter your name: ")
print("Welcome,", name)

# 6. Input integer
age = int(input("Enter your age: "))
print("You are", age, "years old")

# 7. Input float
price = float(input("Enter price: "))
print("Final Price:", price)

# 8. Using input() in calculations
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a+b)

# 9. Print formatted string
print(f"Name: {name}, Age: {age}")

# 10. Print with format()
print("The price is {:.2f}".format(price))


"""
--> User-defined functions (custom created by programmers)

a. Functions that are created by the programmer using the def keyword.
b. Useful when we want to perform a task repeatedly with our own logic.

--> Steps to use User-defined Function:

a. Define the function using def.
b. Call the function by its name.
c. (Optional) Pass parameters and use return if needed.

--> Structure of a user-defined function:
"""
def function_name(parameters):
    """docstring (optional)"""
    # body of function
    return value  # optional


# 1. Simple function without parameter
def greet():
    print("Hello, Welcome to Python Functions!")
greet()

# 2. Function with parameter
def welcome(name):
    print("Hello", name)
welcome("Shalini")

# 3. Function with multiple parameters
def add(a, b):
    print("Sum:", a + b)
add(10, 5)

# 4. Function with return statement
def cube(num):
    return num ** 3
print("Cube of 4:", cube(4))

# 5. Function returning multiple values
def math_operations(a, b):
    return a+b, a-b, a*b, a/b
print("Results:", math_operations(20, 5))

# 6. Function with default parameter
def info(city="Mumbai"):
    print("I live in", city)
info()
info("Delhi")

# 7. Function to check even/odd
def check_even(num):
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")
check_even(13)

# 8. Function to reverse a string
def reverse_string(s):
    return s[::-1]
print("Reverse:", reverse_string("Python"))

# 9. Function with loop
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
print("Factorial of 5:", factorial(5))

# 10. Nested function (function inside function)
def outer():
    def inner():
        print("This is Inner Function")
    print("This is Outer Function")
    inner()
outer()
