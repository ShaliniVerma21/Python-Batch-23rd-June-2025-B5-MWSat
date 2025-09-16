""" 
Exception Handling is a mechanism in Python used to handle runtime errors 
(unexpected situations while executing the program).
Without exception handling, a program terminates abruptly when an error occurs.
With exception handling, we can catch the error, handle it gracefully, and allow the program to continue.

Types of Errors : 

1. Syntax Error – Errors in the structure/grammar of code (detected before execution).
2. Runtime Error – Errors during execution (e.g., divide by zero, invalid input).
3. Logical Error – Code runs but produces wrong output due to logic mistakes.
"""
# Example of Syntax Error
if True
    print("Missing colon")  #(This won’t run at all.)

# Example of Runtime Error
print(10 / 0)   # ZeroDivisionError

# Example of Logical Error
def area_of_square(side):
    return 4 * side   # Wrong (perimeter, not area)
print(area_of_square(5))  # Output: 20, but area should be 25


""" 
Exception Handling Keywords

1. try → Code that may raise an error.
2. except → Block that handles the error.
3. else → Runs if no exception occurs.
4. finally → Runs regardless of exception (cleanup code).
5. raise → Used to throw exceptions manually.
"""

# 1. Basic Exception Handling (try and except)
""" 
The simplest form of exception handling.
If error occurs in try, control shifts to except.

Examples:
"""

# Example 1: Division by zero
try:
    print(10 / 0)
except Exception as e:
    print("Error occurred:", e)

# Example 2: Invalid input
try:
    num = int("abc")
except Exception as e:
    print("Error:", e)

# Example 3: Handling specific exception
try:
    x = int("hello")
except ValueError as e:
    print("Value Error:", e)

# Example 4: Index out of range
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError as e:
    print("Index Error:", e)

# Example 5: Multiple except
try:
    a = 5 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print("Other error:", e)


# 2. try with else
""" 
else block runs only if no exception occurs.

Examples:
"""

# Example 1
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("You entered:", num)

# Example 2
try:
    x = 100 / 5
except ZeroDivisionError:
    print("Cannot divide")
else:
    print("Division successful:", x)

# Example 3
try:
    text = "Python"
    print(text.index("y"))
except ValueError:
    print("Character not found")
else:
    print("Search completed")

# Example 4
try:
    f = open("example.txt", "w")
    f.write("Hello Python")
except IOError:
    print("File error")
else:
    print("File written successfully")

# Example 5
try:
    data = {"name": "Shalini", "age": 28}
    print(data["name"])
except KeyError:
    print("Key not found")
else:
    print("Key found successfully")

# 3. finally Block
""" 
The finally block always runs, whether or not an error occurs.
Used for cleanup code (closing files, releasing resources).

Examples:
"""

# Example 1
try:
    print(10 / 2)
except ZeroDivisionError:
    print("Error")
finally:
    print("Execution finished")

# Example 2
try:
    f = open("data.txt", "w")
    f.write("Hello")
except IOError:
    print("File error")
finally:
    f.close()
    print("File closed")

# Example 3
try:
    nums = [1, 2, 3]
    print(nums[5])
except IndexError:
    print("Index error")
finally:
    print("Cleanup done")

# Example 4
try:
    x = int("abc")
except ValueError:
    print("Value error")
finally:
    print("Always executed")

# Example 5
try:
    print("No error here")
except:
    print("Error found")
finally:
    print("This will run anyway")


# 4. Raising Exceptions (raise)
""" 
raise keyword is used to manually throw exceptions when conditions are not met.

Examples:
"""
# Example 1
x = -5
if x < 0:
    raise ValueError("Negative value not allowed")

# Example 2
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# Example 3
name = ""
if not name:
    raise Exception("Name cannot be empty")

# Example 4
age = 15
if age < 18:
    raise PermissionError("Not eligible to vote")

# Example 5
salary = -1000
if salary < 0:
    raise ArithmeticError("Salary cannot be negative")

""" 
5. Custom Exceptions
We can create user-defined exceptions by defining a class that inherits from Exception.

Examples:
"""

# Example 1: Custom exception class
class MyError(Exception):
    pass

try:
    raise MyError("This is a custom error")
except MyError as e:
    print(e)

# Example 2
class NegativeNumberError(Exception):
    pass

def check_number(n):
    if n < 0:
        raise NegativeNumberError("Negative numbers not allowed")
    return n

try:
    check_number(-10)
except NegativeNumberError as e:
    print(e)

# Example 3
class AgeError(Exception):
    pass

age = 15
try:
    if age < 18:
        raise AgeError("Age must be 18 or above")
except AgeError as e:
    print(e)

# Example 4
class PasswordError(Exception):
    pass

password = "123"
try:
    if len(password) < 6:
        raise PasswordError("Password too short")
except PasswordError as e:
    print(e)

# Example 5
class BalanceError(Exception):
    pass

balance = 500
try:
    withdraw = 1000
    if withdraw > balance:
        raise BalanceError("Insufficient balance")
except BalanceError as e:
    print(e)
