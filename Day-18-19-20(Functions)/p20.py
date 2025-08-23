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

# 11. Global list modification
items = [1, 2, 3]
def append_item():
    global items
    items.append(4)
append_item()
print("Items =", items)

# 12. Local variable disappears after function ends
def temp_var():
    msg = "Temporary"
    print("Inside:", msg)
temp_var()
# print(msg)  # ERROR: msg is not defined

# 13. Global counter using function calls
counter = 0
def increase():
    global counter
    counter += 1
for i in range(5):
    increase()
print("Counter =", counter)

# 14. Function returning global + local
num = 50
def combine():
    local_num = 25
    return num + local_num
print("Combined:", combine())

# 15. Nested functions with variable scope
z = 100
def outer():
    y = 50
    def inner():
        x = 25
        print("Inner x:", x, "Outer y:", y, "Global z:", z)
    inner()
outer()


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

# 2. Lambda to square a number
square = lambda x: x ** 2
print(square(7))

# 3. Lambda with no arguments
hello = lambda : "Hello World"
print(hello())

# 4. Lambda with default argument
power = lambda x, y=2: x ** y
print(power(5))

# 5. Lambda with map() to double numbers
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x*2, nums))
print(doubled)

# 6. Lambda with filter() to find evens
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# 7. Lambda with reduce() to find product
from functools import reduce
product = reduce(lambda x, y: x*y, nums)
print(product)

# 8. Lambda to reverse string
rev = lambda s: s[::-1]
print(rev("Python"))

# 9. Lambda to check even/odd
check = lambda x: "Even" if x%2==0 else "Odd"
print(check(11))

# 10. Sorting with lambda by length
words = ["apple", "kiwi", "banana", "grape"]
sorted_words = sorted(words, key=lambda w: len(w))
print(sorted_words)

# 11. Sorting tuples with lambda by second value
pairs = [(1,5), (3,2), (4,8)]
pairs.sort(key=lambda x: x[1])
print(pairs)

# 12. Nested lambda
mul_add = lambda a, b: (lambda c: a*b + c)
print(mul_add(2, 3)(4))

# 13. Lambda with multiple conditions
grade = lambda marks: "Pass" if marks >= 40 else "Fail"
print(grade(35))

# 14. Lambda with map() for uppercase
words = ["dog", "cat", "parrot"]
caps = list(map(lambda w: w.upper(), words))
print(caps)

# 15. Lambda in dictionary for quick functions
funcs = {
    "add": lambda x, y: x + y,
    "mul": lambda x, y: x * y
}
print(funcs["add"](10, 20))
print(funcs["mul"](5, 6))


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