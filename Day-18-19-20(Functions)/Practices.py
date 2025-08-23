#Section 1: Basics Defining Function

# 1. Function to print a greeting
def greet():
    print("Hello, welcome to Python!")
greet()

# 2. Function to print a user’s name
def print_name():
    print("My name is Shalini.")
print_name()

# 3. Function to add two numbers (fixed values)
def add_numbers():
    print(10 + 20)
add_numbers()

# 4. Function to multiply two numbers
def multiply():
    print(5 * 6)
multiply()

# 5. Function to print today’s motivational quote
def quote():
    print("Believe in yourself!")
quote()

# 6. Function to calculate area of rectangle
def rectangle_area():
    length = 5
    width = 3
    print("Area:", length * width)
rectangle_area()

# 7. Function to calculate area of square
def square_area():
    side = 4
    print("Square Area:", side * side)
square_area()

# 8. Function to check even or odd (fixed number)
def check_even():
    num = 10
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
check_even()

# 9. Function to display student details
def student_info():
    print("Name: Rahul, Roll: 101, Course: BBA")
student_info()

# 10. Function to print numbers from 1 to 5
def print_numbers():
    for i in range(1, 6):
        print(i)
print_numbers()

# 11. Function to print a fixed list
def show_list():
    fruits = ["apple", "banana", "cherry"]
    print(fruits)
show_list()

# 12. Function to print current marks
def marks():
    print("Math: 80, Science: 75, English: 85")
marks()

# 13. Function to display a message multiple times
def repeat_message():
    for i in range(3):
        print("Python is powerful!")
repeat_message()

# 14. Function to display prime check (hardcoded)
def check_prime():
    num = 7
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print("Not Prime")
                return
        print("Prime")
check_prime()

# 15. Function to display factorial (hardcoded)
def factorial():
    num = 5
    fact = 1
    for i in range(1, num+1):
        fact *= i
    print("Factorial:", fact)
factorial()

# 16. Function to display multiplication table
def table():
    num = 4
    for i in range(1, 11):
        print(num, "x", i, "=", num*i)
table()

# 17. Function to calculate simple interest
def simple_interest():
    p, r, t = 1000, 5, 2
    print("Simple Interest:", (p*r*t)/100)
simple_interest()

# 18. Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit():
    c = 37
    f = (c * 9/5) + 32
    print("Fahrenheit:", f)
celsius_to_fahrenheit()

# 19. Function to find maximum of three numbers
def max_three():
    a, b, c = 12, 45, 32
    print("Maximum:", max(a, b, c))
max_three()

# 20. Function to reverse a string
def reverse_string():
    text = "Python"
    print("Reversed:", text[::-1])
reverse_string()

# 21. Function to count vowels in a string
def count_vowels():
    text = "education"
    vowels = "aeiou"
    count = sum(1 for ch in text if ch in vowels)
    print("Vowels:", count)
count_vowels()

# 22. Function to display dictionary data
def show_dict():
    student = {"name": "Shalini", "age": 22, "course": "BBA"}
    print(student)
show_dict()

# 23. Function to sum elements in a list
def sum_list():
    numbers = [2, 4, 6, 8, 10]
    print("Sum:", sum(numbers))
sum_list()

# 24. Function to display Fibonacci series (first 5 terms)
def fibonacci():
    a, b = 0, 1
    for i in range(5):
        print(a, end=" ")
        a, b = b, a+b
fibonacci()

# 25. Function to check leap year
def leap_year():
    year = 2024
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")
leap_year()


#Section 2: Built-in functions & Types of Built-in functions

# 1. abs() → Absolute value
print("Absolute:", abs(-12))

# 2. all() → True if all items are true
print("All True:", all([True, 1, 5]))
print("All False:", all([True, 0, 5]))

# 3. any() → True if any item is true
print("Any True:", any([0, False, 5]))
print("Any False:", any([0, False, None]))

# 4. bin() → Binary representation
print("Binary of 10:", bin(10))

# 5. bool() → Convert to boolean
print("Bool of 0:", bool(0))
print("Bool of 7:", bool(7))

# 6. chr() → Character from ASCII value
print("Char for 65:", chr(65))

# 7. ord() → ASCII value of character
print("ASCII of 'A':", ord('A'))

# 8. divmod() → Quotient & Remainder
q, r = divmod(10, 3)
print("Quotient:", q, "Remainder:", r)

# 9. enumerate() → Index with values
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)

# 10. eval() → Evaluate string as expression
x = eval("10 + 5 * 2")
print("Eval Result:", x)

# 11. float() → Convert to float
print("Float:", float(7))

# 12. int() → Convert to integer
print("Int:", int(7.89))

# 13. len() → Length of list/string
print("Length:", len("Python"))

# 14. list() → Convert to list
print("List from string:", list("HELLO"))

# 15. max() → Maximum value
print("Max:", max(2, 7, 1, 9))

# 16. min() → Minimum value
print("Min:", min(2, 7, 1, 9))

# 17. pow() → Power calculation
print("2^5:", pow(2, 5))

# 18. range() → Sequence generator
for i in range(3):
    print("Range value:", i)

# 19. reversed() → Reverse sequence
nums = [1, 2, 3, 4]
print("Reversed List:", list(reversed(nums)))

# 20. round() → Round number
print("Round(7.567, 2):", round(7.567, 2))

# 21. set() → Create set
print("Set:", set([1, 2, 2, 3, 4]))

# 22. sorted() → Sort values
print("Sorted:", sorted([5, 2, 9, 1]))

# 23. sum() → Sum of values
print("Sum:", sum([1, 2, 3, 4, 5]))

# 24. type() → Check type
print("Type of 'Hello':", type("Hello"))

# 25. zip() → Combine iterables
names = ["Amit", "Neha", "Raj"]
scores = [90, 85, 88]
zipped = zip(names, scores)
print("Zipped:", list(zipped))


#Section 3: User Defined Functions 

# 1. Function to greet user
def greet(name):
    print("Hello", name, "Welcome to Python!")
greet("Shalini")

# 2. Function to add two numbers
def add(a, b):
    return a + b
print("Sum:", add(5, 3))

# 3. Function to calculate area of circle
def area_circle(radius):
    return 3.14 * radius * radius
print("Circle Area:", area_circle(7))

# 4. Function to calculate factorial
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
print("Factorial of 5:", factorial(5))

# 5. Function to check prime number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print("Is 17 Prime?", is_prime(17))

# 6. Function to check even/odd
def even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"
print("10 is:", even_odd(10))

# 7. Function to calculate simple interest
def simple_interest(p, r, t):
    return (p * r * t) / 100
print("SI:", simple_interest(1000, 5, 2))

# 8. Function to reverse a string
def reverse_string(text):
    return text[::-1]
print("Reverse:", reverse_string("Python"))

# 9. Function to count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in text if ch in vowels)
print("Vowels in Education:", count_vowels("Education"))

# 10. Function to calculate average
def average(numbers):
    return sum(numbers) / len(numbers)
print("Average:", average([10, 20, 30]))

# 11. Function to check palindrome
def is_palindrome(word):
    return word == word[::-1]
print("madam Palindrome?", is_palindrome("madam"))

# 12. Function to get maximum from list
def list_max(lst):
    return max(lst)
print("Max:", list_max([5, 2, 8, 1]))

# 13. Function to calculate BMI
def bmi(weight, height):
    return weight / (height ** 2)
print("BMI:", bmi(65, 1.65))

# 14. Function to generate Fibonacci sequence
def fibonacci(n):
    seq = []
    a, b = 0, 1
    for i in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq
print("Fibonacci:", fibonacci(7))

# 15. Function to calculate compound interest
def compound_interest(p, r, t):
    return p * (1 + r/100)**t - p
print("CI:", compound_interest(1000, 5, 2))

# 16. Function to convert Celsius to Fahrenheit
def c_to_f(c):
    return (c * 9/5) + 32
print("37°C =", c_to_f(37), "F")

# 17. Function to convert Fahrenheit to Celsius
def f_to_c(f):
    return (f - 32) * 5/9
print("98.6°F =", f_to_c(98.6), "C")

# 18. Function to count words in a sentence
def word_count(sentence):
    return len(sentence.split())
print("Word Count:", word_count("Python is powerful"))

# 19. Function to find square of a number
def square(n):
    return n * n
print("Square of 9:", square(9))

# 20. Function to calculate power
def power(base, exp):
    return base ** exp
print("2^5 =", power(2, 5))

# 21. Function to display multiplication table
def multiplication_table(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num*i)
multiplication_table(6)

# 22. Function to calculate grade
def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"
print("Grade:", grade(82))

# 23. Function to check leap year
def leap_year(year):
    return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)
print("2024 Leap?", leap_year(2024))

# 24. Function to remove duplicates from list
def remove_duplicates(lst):
    return list(set(lst))
print("Unique:", remove_duplicates([1, 2, 2, 3, 3, 4]))

# 25. Function to calculate perimeter of rectangle
def perimeter_rectangle(l, w):
    return 2 * (l + w)
print("Perimeter:", perimeter_rectangle(5, 3))


#Section 4: Function Call & Return Statement

# 1. Function returning sum of 2 numbers
def add(a, b):
    return a + b
result = add(5, 7)
print("Sum:", result)

# 2. Function returning multiple values
def operations(a, b):
    return a+b, a-b, a*b, a/b
s, d, m, q = operations(10, 5)
print("Results:", s, d, m, q)

# 3. Function returning square of a number
def square(n):
    return n**2
print("Square:", square(8))

# 4. Function to check pass/fail
def check_pass(marks):
    return "Pass" if marks >= 40 else "Fail"
print("Result:", check_pass(35))

# 5. Function returning factorial
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
print("Factorial:", factorial(6))

# 6. Function returning maximum from list
def list_max(lst):
    return max(lst)
print("Max:", list_max([10, 25, 3]))

# 7. Function returning min from list
def list_min(lst):
    return min(lst)
print("Min:", list_min([10, 25, 3]))

# 8. Function returning average
def average(lst):
    return sum(lst) / len(lst)
print("Average:", average([10, 20, 30, 40]))

# 9. Function returning reversed string
def reverse_text(text):
    return text[::-1]
print("Reverse:", reverse_text("Python"))

# 10. Function returning grade
def grade(marks):
    if marks >= 90: return "A"
    elif marks >= 75: return "B"
    elif marks >= 50: return "C"
    else: return "Fail"
print("Grade:", grade(88))

# 11. Function returning length of string
def length(text):
    return len(text)
print("Length:", length("Shalini"))

# 12. Function returning tuple of squares
def squares(n):
    return tuple(i**2 for i in range(1, n+1))
print("Squares:", squares(5))

# 13. Function returning dictionary of squares
def dict_squares(n):
    return {i: i**2 for i in range(1, n+1)}
print("Dict Squares:", dict_squares(4))

# 14. Function returning whether number is prime
def is_prime(n):
    if n < 2: return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print("17 Prime?", is_prime(17))

# 15. Function returning Celsius to Fahrenheit
def c_to_f(c):
    return (c*9/5)+32
print("37°C =", c_to_f(37), "F")

# 16. Function returning list of even numbers
def even_list(n):
    return [i for i in range(n+1) if i % 2 == 0]
print("Evens:", even_list(10))

# 17. Function returning list of odd numbers
def odd_list(n):
    return [i for i in range(n+1) if i % 2 != 0]
print("Odds:", odd_list(10))

# 18. Function returning word count
def word_count(sentence):
    return len(sentence.split())
print("Words:", word_count("Python is very powerful"))

# 19. Function returning vowels count
def count_vowels(text):
    return sum(1 for ch in text if ch.lower() in "aeiou")
print("Vowels:", count_vowels("Education"))

# 20. Function returning leap year check
def leap_year(year):
    return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)
print("2024 Leap?", leap_year(2024))

# 21. Function returning perimeter of square
def perimeter_square(side):
    return 4 * side
print("Perimeter:", perimeter_square(5))

# 22. Function returning SI
def simple_interest(p, r, t):
    return (p*r*t)/100
print("SI:", simple_interest(2000, 5, 2))

# 23. Function returning CI
def compound_interest(p, r, t):
    return p*((1+r/100)**t)-p
print("CI:", compound_interest(2000, 5, 2))

# 24. Function returning multiplication table
def table(n):
    return [n*i for i in range(1, 11)]
print("Table of 7:", table(7))

# 25. Function calling another function
def outer_function(x, y):
    def inner_function(a, b):
        return a+b
    return inner_function(x, y) * 2
print("Result:", outer_function(5, 3))


#Section 5: Local and Global Variables

# 1. Local variable example
def local_example():
    x = 10
    print("Inside function:", x)
local_example()

# 2. Global variable example
x = 20
def global_example():
    print("Using global:", x)
global_example()

# 3. Local overrides global inside function
x = 50
def override_example():
    x = 100
    print("Inside function:", x)
override_example()
print("Outside function:", x)

# 4. Using 'global' keyword to modify variable
y = 10
def modify_global():
    global y
    y = y + 5
    print("Inside function:", y)
modify_global()
print("Outside function:", y)

# 5. Local variable destroyed after function ends
def temp_variable():
    a = 7
    print("Inside function:", a)
temp_variable()
# print(a)  # This will give error if uncommented

# 6. Same variable name: local vs global
z = 30
def show_var():
    z = 99
    print("Local z:", z)
show_var()
print("Global z:", z)

# 7. Nested function accessing outer local variable
def outer():
    msg = "Hello"
    def inner():
        print("Inner sees:", msg)
    inner()
outer()

# 8. Using nonlocal inside nested functions
def outer_func():
    count = 0
    def inner_func():
        nonlocal count
        count += 1
        print("Count:", count)
    inner_func()
outer_func()

# 9. Global variable across multiple functions
score = 0
def increase():
    global score
    score += 10
def decrease():
    global score
    score -= 5
increase()
decrease()
print("Final Score:", score)

# 10. Function accessing global list
items = [1, 2, 3]
def append_item():
    items.append(4)
append_item()
print("Updated List:", items)

# 11. Local variable shadowing global
val = 100
def shadow():
    val = 200
    print("Local val:", val)
shadow()
print("Global val:", val)

# 12. Global dictionary modification
student = {"name": "Amit", "age": 20}
def update_age():
    student["age"] = 21
update_age()
print("Updated Student:", student)

# 13. Counter using global variable
counter = 0
def increment():
    global counter
    counter += 1
increment()
increment()
print("Counter:", counter)

# 14. Global string modification
message = "Good"
def change_message():
    global message
    message = "Better"
change_message()
print("Message:", message)

# 15. Local variables independent in different calls
def counter_local():
    count = 0
    count += 1
    print("Local count:", count)
counter_local()
counter_local()

# 16. Function returning local variable
def create_value():
    val = 42
    return val
print("Returned Value:", create_value())

# 17. Function using global constant
PI = 3.14
def area_circle(r):
    return PI * r * r
print("Circle Area:", area_circle(5))

# 18. Access global tuple
nums = (1, 2, 3)
def show_tuple():
    print("Tuple:", nums)
show_tuple()

# 19. Global set modification
data = {1, 2, 3}
def add_set():
    data.add(4)
add_set()
print("Set:", data)

# 20. Using global inside recursion
total = 0
def add_numbers(n):
    global total
    if n > 0:
        total += n
        add_numbers(n-1)
add_numbers(5)
print("Total:", total)

# 21. Demonstrating variable scope difference
x = "global"
def func():
    x = "local"
    print("Inside:", x)
func()
print("Outside:", x)

# 22. Local variable used only inside function
def only_local():
    name = "Shalini"
    print("Inside function:", name)
only_local()

# 23. Global variable used in multiple functions
points = 50
def gain():
    global points
    points += 20
def lose():
    global points
    points -= 10
gain()
lose()
print("Points:", points)

# 24. Local and global with same name
a = 5
def show_a():
    a = 15
    print("Local a:", a)
show_a()
print("Global a:", a)

# 25. Modify global list inside function
marks = [70, 80, 90]
def add_mark(m):
    marks.append(m)
add_mark(85)
print("Marks:", marks)


#Section 6: Lambda Function (map, filter, reduce)

from functools import reduce

# 1. Simple lambda to add two numbers
add = lambda a, b: a + b
print("Sum:", add(5, 7))

# 2. Square of a number
square = lambda x: x**2
print("Square:", square(6))

# 3. Check even/odd
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print("8 is:", is_even(8))

# 4. Find maximum of two numbers
maximum = lambda a, b: a if a > b else b
print("Max:", maximum(10, 15))

# 5. Convert Celsius to Fahrenheit
c_to_f = lambda c: (c*9/5) + 32
print("37°C =", c_to_f(37))

# 6. Lambda inside map → square list
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print("Squares:", squares)

# 7. Lambda inside map → convert to uppercase
words = ["python", "java", "c++"]
upper = list(map(lambda w: w.upper(), words))
print("Uppercase:", upper)

# 8. Lambda inside map → double numbers
double = list(map(lambda x: x*2, [5, 10, 15]))
print("Doubled:", double)

# 9. Lambda with filter → even numbers
even = list(filter(lambda x: x % 2 == 0, range(1, 11)))
print("Even Numbers:", even)

# 10. Lambda with filter → odd numbers
odd = list(filter(lambda x: x % 2 != 0, range(1, 11)))
print("Odd Numbers:", odd)

# 11. Lambda with filter → words starting with 'p'
words = ["python", "java", "php", "ruby"]
p_words = list(filter(lambda w: w.startswith('p'), words))
print("P words:", p_words)

# 12. Lambda with filter → numbers > 50
nums = [10, 55, 32, 70, 80, 25]
above_50 = list(filter(lambda x: x > 50, nums))
print(">50:", above_50)

# 13. Lambda with reduce → sum of list
nums = [1, 2, 3, 4, 5]
sum_all = reduce(lambda a, b: a+b, nums)
print("Sum:", sum_all)

# 14. Lambda with reduce → product of list
product = reduce(lambda a, b: a*b, [2, 3, 4])
print("Product:", product)

# 15. Lambda with reduce → maximum in list
max_num = reduce(lambda a, b: a if a > b else b, [5, 9, 2, 11, 3])
print("Max:", max_num)

# 16. Sort list by length using lambda
words = ["apple", "banana", "kiwi"]
words.sort(key=lambda w: len(w))
print("Sorted by length:", words)

# 17. Sort list of tuples by second element
pairs = [(1, 5), (2, 1), (3, 4)]
pairs.sort(key=lambda x: x[1])
print("Sorted tuples:", pairs)

# 18. Lambda to calculate cube
cube = lambda x: x**3
print("Cube:", cube(4))

# 19. Map with lambda → Fahrenheit to Celsius
temps_f = [32, 68, 104]
temps_c = list(map(lambda f: (f-32)*5/9, temps_f))
print("Celsius:", temps_c)

# 20. Filter with lambda → strings with length > 4
words = ["pen", "pencil", "book", "eraser"]
long_words = list(filter(lambda w: len(w) > 4, words))
print("Long Words:", long_words)

# 21. Reduce with lambda → concatenate strings
names = ["Shalini", "Verma", "Python"]
full_name = reduce(lambda a, b: a + " " + b, names)
print("Concatenated:", full_name)

# 22. Lambda with map → square root approximation
import math
nums = [4, 9, 16]
roots = list(map(lambda x: round(math.sqrt(x), 2), nums))
print("Roots:", roots)

# 23. Nested lambda → addition then square
nested = (lambda a, b: (a+b)**2)(3, 4)
print("Nested Result:", nested)

# 24. Conditional lambda → grade system
grade = lambda m: "A" if m>=90 else "B" if m>=75 else "C" if m>=50 else "Fail"
print("Marks 82 Grade:", grade(82))

# 25. Using map, filter, reduce together
nums = [1, 2, 3, 4, 5, 6]
# Double even numbers, then sum them
result = reduce(lambda a,b: a+b, map(lambda x: x*2, filter(lambda x: x%2==0, nums)))
print("Sum of doubled evens:", result)


#Section 7: Recursion

# Program 1: Factorial of a number
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))


# Program 2: Sum of first n natural numbers
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print("Sum of first 10 numbers:", sum_n(10))

# Program 3: Power of a number (x^n)
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

print("2^5 =", power(2, 5))

# Program 4: Fibonacci series
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("First 7 Fibonacci numbers:", [fibonacci(i) for i in range(7)])

# Program 5: Reverse a string
def reverse_string(s):
    if len(s) == 0:
        return ""
    return reverse_string(s[1:]) + s[0]

print("Reverse:", reverse_string("Python"))

# Program 6: Greatest Common Divisor (GCD)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print("GCD of 48 and 18:", gcd(48, 18))

# Program 7: Decimal to Binary
def to_binary(n):
    if n == 0:
        return ""
    return to_binary(n // 2) + str(n % 2)

print("Binary of 13:", to_binary(13))

# Program 8: Length of a string
def str_length(s):
    if s == "":
        return 0
    return 1 + str_length(s[1:])

print("Length:", str_length("recursion"))

# Program 9: Check Palindrome
def is_palindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])

print("Palindrome?", is_palindrome("madam"))

# Program 10: Sum of digits
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

print("Sum of digits of 1234:", sum_digits(1234))

# Program 11: Find maximum in list
def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    return max(lst[0], find_max(lst[1:]))

print("Max:", find_max([10, 45, 32, 67, 23]))

# Program 12: Sum of list elements
def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

print("Sum:", sum_list([1, 2, 3, 4, 5]))

# Program 13: Count occurrences of an element
def count_occ(lst, x):
    if not lst:
        return 0
    return (lst[0] == x) + count_occ(lst[1:], x)

print("Occurrences of 3:", count_occ([1, 3, 2, 3, 4, 3], 3))

# Program 14: Flatten nested list
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result

print("Flatten:", flatten([1, [2, [3, 4], 5], 6]))

# Program 15: Product of list elements
def product_list(lst):
    if not lst:
        return 1
    return lst[0] * product_list(lst[1:])

print("Product:", product_list([2, 3, 4]))

# Program 16: Print numbers 1 to n
def print_1_to_n(n):
    if n > 0:
        print_1_to_n(n - 1)
        print(n, end=" ")

print_1_to_n(5)

# Program 17: Print numbers n to 1
def print_n_to_1(n):
    if n > 0:
        print(n, end=" ")
        print_n_to_1(n - 1)

print_n_to_1(5)

# Program 18: Tower of Hanoi
def hanoi(n, source, target, aux):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, aux, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, aux, target, source)

hanoi(3, "A", "C", "B")

# Program 19: Find nth triangular number
def triangular(n):
    if n == 0:
        return 0
    return n + triangular(n - 1)

print("10th triangular number:", triangular(10))

# Program 20: Count vowels in a string
def count_vowels(s):
    if not s:
        return 0
    return (s[0].lower() in "aeiou") + count_vowels(s[1:])

print("Vowels:", count_vowels("recursion"))

# Program 21: Reverse a number
def reverse_num(n, rev=0):
    if n == 0:
        return rev
    return reverse_num(n // 10, rev * 10 + n % 10)

print("Reverse of 1234:", reverse_num(1234))

# Program 22: Count consonants in a string
def count_consonants(s):
    if not s:
        return 0
    return (s[0].lower() not in "aeiou" and s[0].isalpha()) + count_consonants(s[1:])

print("Consonants:", count_consonants("python"))

# Program 23: Multiplication using recursion
def multiply(a, b):
    if b == 0:
        return 0
    return a + multiply(a, b - 1)

print("6*4 =", multiply(6, 4))

# Program 24: Binary Search using recursion
def binary_search(lst, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return binary_search(lst, target, low, mid - 1)
    else:
        return binary_search(lst, target, mid + 1, high)

arr = [1, 3, 5, 7, 9]
print("Index of 7:", binary_search(arr, 7, 0, len(arr) - 1))

# Program 25: Generate permutations of a string
def permute(s, answer=""):
    if len(s) == 0:
        print(answer, end="  ")
    else:
        for i in range(len(s)):
            ch = s[i]
            left = s[:i]
            right = s[i+1:]
            permute(left + right, answer + ch)

print("Permutations of 'abc':")
permute("abc")


#Section 8: Mixed programs covering normal functions, default arguments, lambda, recursion etc

# 1. Normal + Default Argument Function
def greet(name="Guest"):
    return f"Hello, {name}!"
print(greet())
print(greet("Shalini"))

# 2. Function + Lambda
square = lambda x: x**2
print("Square of 7:", square(7))

# 3. Recursion + Normal Function
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)
print("Factorial:", factorial(5))

# 4. Function + Multiple Default Arguments
def bill(item, qty=1, price=50):
    return f"Total = {qty*price} for {item}"
print(bill("Book", 3, 100))
print(bill("Pen"))

# 5. Function + Lambda (even check)
is_even = lambda x: x % 2 == 0
print("Is 6 even?", is_even(6))

# 6. Function calling Function
def add(x, y): return x+y
def multiply(x, y): return x*y
def calc(x, y):
    return add(x, y), multiply(x, y)
print(calc(4, 5))

# 7. Recursion + Lambda-like style
fib = lambda n: n if n<=1 else fib(n-1)+fib(n-2)
print("Fibonacci 6:", fib(6))

# 8. Function + Default & Keyword Arguments
def intro(name, age=18, city="Delhi"):
    return f"{name}, Age {age}, City {city}"
print(intro("Rahul", city="Mumbai"))

# 9. Function + List Comprehension
def squares(n):
    return [x**2 for x in range(1, n+1)]
print(squares(5))

# 10. Function + Map + Lambda
nums = [1, 2, 3, 4]
print(list(map(lambda x: x*10, nums)))

# 11. Function + Filter + Lambda
nums = [5, 12, 17, 24]
print(list(filter(lambda x: x%2==0, nums)))

# 12. Function + Reduce + Lambda
from functools import reduce
nums = [1,2,3,4]
print(reduce(lambda x,y: x+y, nums))

# 13. Recursion + Default Argument
def power(base, exp=2):
    return 1 if exp==0 else base*power(base, exp-1)
print("2^5:", power(2, 5))

# 14. Normal + Recursion Mix
def sum_digits(num):
    if num==0: return 0
    return num%10 + sum_digits(num//10)
print("Sum of digits:", sum_digits(456))

# 15. Default + Variable Length Arguments
def student(name, *subjects, city="Delhi"):
    return f"{name} studies {subjects} in {city}"
print(student("Aman", "Math", "Science"))

# 16. Function + Lambda in Same Code
def multiply(a, b): return a*b
product = lambda a,b: a*b
print(multiply(4, 3), product(4, 3))

# 17. Function Returning Function
def outer():
    def inner():
        return "Hello from Inner"
    return inner
msg = outer()
print(msg())

# 18. Recursive + Lambda
fact = lambda n: 1 if n==0 else n*fact(n-1)
print("Factorial(6):", fact(6))

# 19. Normal + Recursion for Palindrome
def is_palindrome(s):
    if len(s)<=1: return True
    return s[0]==s[-1] and is_palindrome(s[1:-1])
print("madam palindrome?", is_palindrome("madam"))

# 20. Function + Dictionary Default Args
def employee(name, role="Staff", salary=30000):
    return {"name":name, "role":role, "salary":salary}
print(employee("Ravi", "Manager", 60000))

# 21. Function with Conditional Return
def grade(marks):
    return "Pass" if marks>=40 else "Fail"
print("Grade:", grade(55))

# 22. Normal + Lambda Sorting
students = [("Ravi", 21), ("Anu", 19), ("Kiran", 25)]
students.sort(key=lambda x: x[1])
print(students)

# 23. Recursive Reverse String
def reverse(s):
    return s if len(s)<=1 else reverse(s[1:]) + s[0]
print(reverse("Python"))

# 24. Function + Map/Filter in One
nums = [1,2,3,4,5,6]
evens_squared = list(map(lambda x: x**2, filter(lambda x: x%2==0, nums)))
print(evens_squared)

# 25. Function + Recursion + Default Argument
def gcd(a, b):
    return a if b==0 else gcd(b, a%b)
print("GCD of 48 and 18:", gcd(48, 18))


#Section 9: Real Data Analysis Examples(including data types, operators, loops, control structures, list, set, dict, tuples, functions)

# 1. Count frequency of words in a text
text = "data science with python is fun and python is powerful"
word_freq = {}
for word in text.split():
    word_freq[word] = word_freq.get(word, 0) + 1
print("Word Frequency:", word_freq)


# 2. Find max, min, and average salary from a dataset
salaries = [45000, 56000, 60000, 72000, 50000, 90000]
print("Max Salary:", max(salaries))
print("Min Salary:", min(salaries))
print("Average Salary:", sum(salaries) / len(salaries))


# 3. Count even and odd numbers in a dataset
data = [23, 44, 12, 67, 90, 55, 32]
even = len([x for x in data if x % 2 == 0])
odd = len([x for x in data if x % 2 != 0])
print("Even:", even, "Odd:", odd)


# 4. Convert Celsius temperatures to Fahrenheit
temps_c = [0, 20, 30, 40]
temps_f = [round((9/5)*c + 32, 2) for c in temps_c]
print("Converted Temps:", temps_f)


# 5. Remove duplicates from dataset
dataset = [1, 2, 2, 3, 4, 4, 5, 6]
unique_data = list(set(dataset))
print("Unique Values:", unique_data)


# 6. Merge two datasets
sales_2023 = {"Jan": 200, "Feb": 300, "Mar": 250}
sales_2024 = {"Apr": 400, "May": 500}
sales_2023.update(sales_2024)
print("Merged Sales:", sales_2023)


# 7. Find most frequent number
nums = [1, 3, 3, 2, 2, 2, 5, 5]
most_freq = max(set(nums), key=nums.count)
print("Most Frequent:", most_freq)


# 8. Sort dataset by values (dictionary)
students = {"Ravi": 85, "Anita": 92, "Sunil": 78, "Meera": 95}
sorted_data = dict(sorted(students.items(), key=lambda x: x[1], reverse=True))
print("Sorted by Marks:", sorted_data)


# 9. Analyze sentence length in words
sentences = ["Python is fun", "Data science is amazing", "I love coding"]
lengths = [len(s.split()) for s in sentences]
print("Sentence Word Counts:", lengths)


# 10. Filter dataset: numbers > 50
dataset = [10, 45, 60, 72, 20, 90]
filtered = [x for x in dataset if x > 50]
print("Numbers > 50:", filtered)


# 11. Find students who passed
marks = {"Aman": 40, "Rita": 75, "Raj": 30, "Sita": 65}
passed = [name for name, score in marks.items() if score >= 40]
print("Passed Students:", passed)


# 12. Count vowels in a dataset of names
names = ["Ravi", "Anita", "Sunil", "Meera"]
vowel_count = {name: sum(ch in 'aeiouAEIOU' for ch in name) for name in names}
print("Vowel Counts:", vowel_count)


# 13. Create a summary of numeric dataset
data = [12, 34, 56, 78, 90]
summary = {
    "max": max(data),
    "min": min(data),
    "mean": sum(data)/len(data),
    "count": len(data)
}
print("Summary:", summary)


# 14. Count frequency of characters in a string
s = "machinelearning"
char_freq = {ch: s.count(ch) for ch in set(s)}
print("Character Frequency:", char_freq)


# 15. Find intersection of two datasets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Intersection:", a.intersection(b))


# 16. Find top 3 scores
scores = [78, 89, 95, 67, 85, 99, 90]
top3 = sorted(scores, reverse=True)[:3]
print("Top 3 Scores:", top3)


# 17. Calculate student grades
students = {"Ravi": 85, "Anita": 92, "Sunil": 78, "Meera": 65}
grades = {name: ("A" if score >= 85 else "B" if score >= 70 else "C") 
          for name, score in students.items()}
print("Grades:", grades)


# 18. Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
print("Flattened List:", flat)


# 19. Find common letters in two names
name1, name2 = "Shalini", "Sharad"
common = set(name1) & set(name2)
print("Common Letters:", common)


# 20. Create dictionary from two lists
keys = ["id", "name", "age"]
values = [101, "Ravi", 22]
person = dict(zip(keys, values))
print("Person Dict:", person)


# 21. Identify prime numbers from dataset
nums = [11, 15, 17, 20, 23, 29]
prime = []
for n in nums:
    if all(n % i != 0 for i in range(2, int(n**0.5)+1)):
        prime.append(n)
print("Prime Numbers:", prime)


# 22. Count words starting with each letter
words = ["apple", "banana", "apricot", "blueberry", "cherry"]
freq = {}
for w in words:
    freq[w[0]] = freq.get(w[0], 0) + 1
print("Word Initial Counts:", freq)


# 23. Group numbers by even/odd
nums = [10, 15, 22, 33, 42, 55]
groups = {"even": [], "odd": []}
for n in nums:
    groups["even" if n % 2 == 0 else "odd"].append(n)
print("Grouped:", groups)


# 24. Reverse key-value pairs in dictionary
data = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in data.items()}
print("Reversed Dict:", reversed_dict)


# 25. Create dataset of word lengths
sentence = "Python makes data analysis easier"
length_data = {word: len(word) for word in sentence.split()}
print("Word Lengths:", length_data)


#Section 10: 1 Complete & detailed Real  Situation based Data Analysis Example(including data types, operators, loops, control structures, list, set, dict, tuples, functions) 