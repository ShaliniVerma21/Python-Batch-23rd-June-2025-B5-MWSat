
# 4. User-defined Functions

"""
--> User-defined functions (custom created by programmers)

a. Functions that are created by the programmer using the def keyword.
b. Useful when we want to perform a task repeatedly with our own logic.

Structure: definition → calling → execution

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

# 9. Function with loop (Factorial)
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


""" 
5. Function Call and Return Statement

- To use a function, we call it using its name followed by parentheses.
- The return keyword sends a value back to the caller.


A function can:

- Return nothing (default → None).
- Return a single value.
- Return multiple values (as tuple).

Difference between print() and return:

- print() → Displays output on screen.
- return → Sends value back to program for further use.

"""
# 1. Function call
def hello():
    print("Hello World")
hello()

# 2. Function with return
def square(n):
    return n * n
print("Square of 5:", square(5))

# 3. Function with multiple returns
def calc(a, b):
    return a+b, a-b
res = calc(10, 3)
print("Results:", res)

# 4. Function with return vs print
def show1():
    print("Inside show1")
def show2():
    return "Inside show2"
show1()
print(show2())

# 5. Return used in calculation
def double(x):
    return x*2
print("Double of 8:", double(8))

# 6. Return None explicitly
def test():
    return None
print(test())

# 7. Early return
def divide(a, b):
    if b == 0:
        return "Division by Zero not allowed"
    return a/b
print(divide(10, 0))
print(divide(10, 2))

# 8. Function inside another function call
def increment(x):
    return x+1
print("Result:", increment(square(4)))

# 9. Returning string
def greet(name):
    return f"Hello {name}"
print(greet("Python"))

# 10. Function with multiple values unpacked
def stats(lst):
    return max(lst), min(lst), sum(lst)
high, low, total = stats([10, 20, 30, 40])
print("High:", high, "Low:", low, "Sum:", total)


""" 
6. Functions with and without Parameters

There are 4 categories:

- Without parameters & without return
- With parameters & without return
- Without parameters & with return
- With parameters & with return
"""

# 1. Without parameters & without return
def greet():
    print("Good Morning!")
greet()

# 2. With parameters & without return
def welcome(name):
    print("Hello", name)
welcome("Ravi")

# 3. Without parameters & with return
def get_pi():
    return 3.14159
print(get_pi())

# 4. With parameters & with return
def add(a, b):
    return a+b
print("Sum:", add(5, 7))

# 5. Function with default parameter
def message(msg="Hi"):
    return msg
print(message())
print(message("Hello World"))

# 6. Function with multiple return values
def operations(a, b):
    return a+b, a-b, a*b
print(operations(8, 2))

# 7. Function returning list
def squares(n):
    return [i*i for i in range(1, n+1)]
print(squares(5))

# 8. Function with string input
def reverse(s):
    return s[::-1]
print(reverse("Python"))

# 9. Function with no argument but user input
def user_input():
    n = int(input("Enter number: "))
    return n*2
print("Double:", user_input())

# 10. Function with multiple args
def average(*args):
    return sum(args) / len(args)
print("Average:", average(10, 20, 30, 40))


""" 
7. Local and Global Variables

- Local Variable: Declared inside a function → accessible only inside it.
- Global Variable: Declared outside functions → accessible everywhere.
- global keyword allows modification of global variables inside a function.
"""

# 1. Global variable
x = 10
def show():
    print("x =", x)
show()

# 2. Local variable
def local_demo():
    y = 5
    print("Local y =", y)
local_demo()

# 3. Same name global & local
x = 100
def test():
    x = 50
    print("Local x =", x)
test()
print("Global x =", x)

# 4. Access global inside function
count = 0
def increment():
    global count
    count += 1
print("Before:", count)
increment()
print("After:", count)

# 5. Function modifying global
g = "Python"
def change():
    global g
    g = "Java"
change()
print("Now g =", g)

# 6. Local variable shadowing
a = 10
def shadow():
    a = 20
    print("Inside:", a)
shadow()
print("Outside:", a)

# 7. Return local variable
def calc():
    num = 42
    return num
print(calc())

# 8. Using global inside loop
total = 0
def add_items(lst):
    global total
    for i in lst:
        total += i
add_items([1,2,3])
print("Total =", total)

# 9. Function with both global & local
m = 5
def fun():
    n = 10
    print("Global m:", m, "Local n:", n)
fun()

# 10. No global modification
x = 10
def no_change():
    print("Inside:", x)
no_change()
print("Outside:", x)


"""
8. Lambda (Anonymous Functions)

- A lambda function in Python is a small, anonymous function (a function without a name).
- It is mainly used for short, simple operations where defining a full function with def would be unnecessary.

Syntax : 
lambda arguments: expression

- lambda → keyword to define
- arguments → inputs to the function
- expression → single statement that returns a value

"""

#Example:
square = lambda x: x * x
print(square(5))   # Output: 25

"""
Usage of Lambda with Functions

- map() – Applies a function to each element of a sequence.
- filter() – Filters elements based on a condition.
- reduce() – Reduces a sequence to a single value (requires functools).
"""

# 1. Lambda to add two numbers
add = lambda a, b: a + b
print(add(5, 3))

# 2. Lambda to find square of a number
square = lambda x: x ** 2
print(square(7))

# 3. Lambda with map() to double list values
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)

# 4. Lambda with map() to convert list of strings to uppercase
words = ["apple", "banana", "cherry"]
upper_words = list(map(lambda w: w.upper(), words))
print(upper_words)

# 5. Lambda with filter() to get even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# 6. Lambda with filter() to get words starting with 'a'
a_words = list(filter(lambda w: w.startswith('a'), words))
print(a_words)

# 7. Lambda with reduce() to calculate sum
from functools import reduce
total = reduce(lambda x, y: x + y, nums)
print(total)

# 8. Lambda with reduce() to find maximum
maximum = reduce(lambda a, b: a if a > b else b, nums)
print(maximum)

# 9. Sorting using lambda by string length
sorted_words = sorted(words, key=lambda w: len(w))
print(sorted_words)

# 10. Nested lambda
mul_add = lambda x, y: (lambda z: x * y + z)
print(mul_add(2, 3)(4))   # (2*3)+4=10


"""
9. Recursion

What is Recursion?

Recursion is when a function calls itself to solve a problem.
It breaks a problem into smaller sub-problems until reaching a base condition.

Structure of a Recursive Function--
def func():
    if base_condition:
        return result
    else:
        return func(modified_input)

"""

# 1. Factorial using recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))   # 120

# 2. Fibonacci sequence using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(i) for i in range(7)])

# 3. Sum of digits using recursion
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

print(sum_digits(1234))  # 10

# 4. Power using recursion (x^y)
def power(x, y):
    if y == 0:
        return 1
    return x * power(x, y-1)

print(power(2, 5))  # 32

# 5. Reverse a string using recursion
def reverse_str(s):
    if len(s) == 0:
        return s
    return reverse_str(s[1:]) + s[0]

print(reverse_str("hello"))

# 6. Greatest Common Divisor (GCD)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))  # 6

# 7. Count digits using recursion
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

print(count_digits(12345))  # 5

# 8. Check palindrome string
def is_palindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])

print(is_palindrome("madam"))

# 9. Print numbers from 1 to N
def print_nums(n):
    if n > 0:
        print_nums(n-1)
        print(n, end=" ")

print_nums(5)

# 10. Binary search using recursion
def binary_search(arr, low, high, x):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid-1, x)
        else:
            return binary_search(arr, mid+1, high, x)
    return -1

arr = [1, 2, 3, 4, 5, 6, 7]
print(binary_search(arr, 0, len(arr)-1, 4))  # 3


"""
10. Examples & Practice Programs

Mixed programs covering normal functions, default arguments, lambda, recursion:
"""

# 1. Function to add two numbers
def add(a, b):
    return a + b
print(add(10, 20))

# 2. Function to check even/odd
def even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"
print(even_odd(7))

# 3. Function with default arguments
def greet(name="Guest"):
    return f"Hello, {name}!"
print(greet())
print(greet("Shalini"))

# 4. Function returning multiple values
def calc(a, b):
    return a+b, a-b, a*b
print(calc(10, 5))

# 5. Lambda function with map()
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x*x, nums))
print(squares)

# 6. Lambda with filter()
odds = list(filter(lambda x: x % 2 != 0, nums))
print(odds)

# 7. Lambda with reduce()
from functools import reduce
product = reduce(lambda x, y: x * y, nums)
print(product)

# 8. Recursive factorial
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)
print(factorial(6))

# 9. Recursive Fibonacci
def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)
print([fib(i) for i in range(6)])

# 10. Function to check prime number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print(is_prime(29))
