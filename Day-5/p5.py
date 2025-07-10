# Strings

#Defining a string
"""
A string is a sequence of characters enclosed in single quotes '...' 
or double quotes "...".
Both single and double quotes can be used to define a string.
However, it's generally recommended to use single quotes for strings 
that contain double quotes and vice versa.
"""

#Examples:
string1 = 'Hello, World!' # Single quotes
string2 = "Hello, World!" # Double quotes
print(string1) # Output: Hello, World!
print(string2) # Output: Hello, World!


#Accessing elements of the string
"""
You can access characters using indexing and slicing.
Strings are sequences, so you can access their elements using indexing.
The indexing starts at 0, so the first character of the string is at index 0.
"""

#Example :

#Indexing (starts at 0):
word = "Python"
print(word[0])  # Output: P
print(word[2])  # Output: t

#Negative indexing (starts from -1 at the end):
print(word[-1])  # Output: n
print(word[-3])  # Output: h

#Slicing (returns a substring):
print(word[1:4])  # Output: yth (characters at index 1,2,3)
print(word[:3])   # Output: Pyt (from start to index 2)
print(word[3:])   # Output: hon (from index 3 to end)


#String methods
"""
Strings have several methods that can be used to perform various operations.
Some of the most commonly used string methods are:
- len() : returns the length of the string
- lower() : returns a lowercase version of the string
- upper() : returns an uppercase version of the string
- title() : returns a title-cased version of the string
- strip() : returns a copy of the string with leading and trailing characters removed
- replace() : returns a copy of the string with all occurrences of a substring replaced with another substring
- split() : returns a list of the words in the string, using the space character as the delimiter
- join() : returns a string in which the elements of the list have been joined by the string
"""

text = "hello world"

print(text.upper())       # HELLO WORLD
print(text.lower())       # hello world
print(text.capitalize())  # Hello world
print(text.title())       # Hello World
print(text.strip())       # removes spaces at start/end
print(text.replace("world", "Python"))  # hello Python
print(text.split())       # ['hello', 'world']
print(text.find("world")) # 6 (index of 'world')
print(text.rfind("world")) # 6 (index of 'world' from right to left)
print(text.count("world")) # 1 (number of 'world')
print(text.startswith("hello")) # True (checks if string starts with 'hello')
print(text.endswith("world")) # True (checks if string ends with 'world')
print(text.center(20)) # centers the string in a field of length 7 or 20
print(text.ljust(20)) # left justifies the string in a field of length 7 or 20
print(text.rjust(20)) # right justifies the string in a field of length 7 or 20


#Type-Casting
"""
Type-casting is the process of converting a value from one data type to another.
For example, converting an integer to a float or a string to an integer.
"""

num = 100
text = str(num)
print(text)        # Output: '100'
print(type(text))  # Output: <class 'str'>

#Converting a string to an integer
print(int("123"))  # Output: 123
#Converting a string to a float
print(float("123.45"))  # Output: 123.45
#Converting a string to a boolean
b1 = "True"
print(bool(b1))  # Output: True
b2 = "False"
print(bool(b2))  # Output: False
print(bool("0"))  # Output: False
print(bool("1"))  # Output: True
"""
In Python, Any non-empty string evaluates to True when passed to bool(), regardless of its content.
as- 
bool("False") → True
bool("0")     → True
bool("anything") → True

Only an empty string "" evaluates to False
"""

print(bool("False")) #True
print(bool("0")) #True
print(bool("anything")) #True
print(bool("")) #False

#Converting a string to a list
print(list("123"))  # Output: ['1', '2', '3']
#Converting a string to a tuple
print(tuple("123"))  # Output: ('1', '2', '3')
#Converting a string to a dictionary
#print(dict("key=value"))  # Output: {'k': 'e', 'e': '}
#Converting a string to a set
print(set("123"))  # Output: {'1', '2', '3'}
#Converting a string to a complex number
print(complex("123.45"))  # Output: (123+45j)


#Input and output
"""
You can get input from the user using input() and print output using print().
"""
name = input("What is your name? ")  # gets input from user
print("Hello, " + name)  # prints output to user

print("This is an example of output")


#String formatting
"""
You can format strings to include variables dynamically.
"""

#✅ Using f-strings (Python 3.6+):
#f-strings are a more readable and efficient way to format strings in Python.
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

#✅ Using the % operator:
#The % operator is a simple way to format strings in Python.
name = "Bob"
age = 30
print("My name is %s and I am %d years old." % (name, age))

#✅ Using format() method:
#The format() method returns a string with the values inserted into the string.
print("My name is {} and I am {} years old.".format(name, age))
#✅ Using string concatenation:
#String concatenation is a way to combine two or more strings into one string.
name = "Charlie"
age = 35
print("My name is " + name + " and I am " + str(age) + "years old")
#✅ Using string multiplication:
#String multiplication is a way to repeat a string a specified number of times.
print("Hello, " * 5)  # prints "Hello, Hello, Hello, Hello


#Print function
""" 
The print() function displays text or values on the screen.
"""
#Basic usage:
print("Hello, World!")

#Printing multiple items:
a, b = 5, 10
print("The values are:", a, b)  # The values are: 5 10

#Using separator:
print("apple", "banana", "cherry", sep=", ")  # apple, banana, cherry

#Using end:
print("Hello", end=" ")  
print("World!")  # Output: Hello World!