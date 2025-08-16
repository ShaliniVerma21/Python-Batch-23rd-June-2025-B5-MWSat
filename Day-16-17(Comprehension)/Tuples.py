# --------------------------------Tuple Comprehension in Python-------------------------

#1. What is Tuple Comprehension?

""" 
Tuple comprehension looks similar to list comprehension but instead of producing a list, 
it produces a tuple-like object called a generator.
Technically, Python does not directly support tuple comprehension 
— when you use parentheses `( )` with comprehension, 
Python creates a generator expression, not an actual tuple.

Example:
"""
t = (x**2 for x in range(5))
print(t)  # <generator object ...>


# If you really want a tuple, you must wrap the generator with the `tuple()` function:
t = tuple(x**2 for x in range(5))
print(t)  # (0, 1, 4, 9, 16)

""" 
Syntax --
tuple_variable = tuple(expression for item in iterable if condition)

expression→ operation or value to return.
item → variable representing each element from iterable.
iterable → sequence like list, range, string, etc.
condition (optional) → filter elements.

Advantages-->

1. Compact & readable code.
2. Memory efficient when used as a generator (lazy evaluation).
3. Easy transformation of sequences.

We’ll cover 4 sections:

1. Basic Tuple Comprehension (No Condition)
2. With Condition (Filtering)
3. With Functions
4. Nested Tuple Comprehension
"""


# Section 1 – Basic Tuple Comprehension (No condition, just transformation)

# Syntax
result = tuple(expression for item in iterable)

# 1. Squares of numbers
t1 = tuple(x**2 for x in range(5))

# 2. Double each number
t2 = tuple(x*2 for x in range(1,6))

# 3. Length of each word
words = ["apple", "banana", "kiwi"]
t3 = tuple(len(w) for w in words)

# 4. Convert string to tuple of characters
t4 = tuple(ch for ch in "python")

# 5. Cubes of numbers
t5 = tuple(x**3 for x in range(1,6))

# 6. ASCII values of characters
t6 = tuple(ord(c) for c in "abc")

# 7. First letter of each word
t7 = tuple(w[0] for w in ["sun", "moon", "star"])

# 8. Reverse each word
t8 = tuple(w[::-1] for w in ["cat", "dog", "owl"])

# 9. Numbers from 10 to 15
t9 = tuple(x for x in range(10,16))

# 10. Temperature conversion (C to F)
temps_c = [0, 20, 37, 100]
t10 = tuple((c*9/5)+32 for c in temps_c)


# Section 2 – Tuple Comprehension with Condition (Filtering elements)

# Syntax
result = tuple(expression for item in iterable if condition)

# 1. Even numbers
t1 = tuple(x for x in range(10) if x%2==0)

# 2. Odd numbers
t2 = tuple(x for x in range(10) if x%2!=0)
print(t2)

# 3. Words starting with 'a'
words = ["apple", "banana", "avocado", "grape"]
t3 = tuple(w for w in words if w.startswith("a"))

# 4. Numbers greater than 50
nums = [10, 60, 30, 80, 90]
t4 = tuple(x for x in nums if x > 50)

# 5. Multiples of 5
t5 = tuple(x for x in range(1,51) if x%5==0)

# 6. Positive numbers
nums = [-5, 3, 0, -1, 8]
t6 = tuple(x for x in nums if x > 0)

# 7. Names longer than 4 letters
names = ["Amy", "Jonathan", "Eva", "Michael"]
t7 = tuple(n for n in names if len(n) > 4)

# 8. Uppercase letters only
t8 = tuple(ch for ch in "PyThOn" if ch.isupper())

# 9. Numbers divisible by both 2 and 3
t9 = tuple(x for x in range(1,31) if x%2==0 and x%3==0)

# 10. Palindrome words
words = ["madam", "apple", "level", "world"]
t10 = tuple(w for w in words if w == w[::-1])

#Section 3 – Tuple Comprehension with Functions (Applying functions in comprehension)

# 1. Square root of numbers
import math
t1 = tuple(math.sqrt(x) for x in range(1,6))

# 2. Factorial of numbers
t2 = tuple(math.factorial(x) for x in range(1,6))

# 3. Absolute values
nums = [-5, 3, -10, 0]
t3 = tuple(abs(x) for x in nums)

# 4. String lengths using len()
words = ["apple", "banana", "kiwi"]
t4 = tuple(len(w) for w in words)

# 5. Lowercase conversion
t5 = tuple(s.lower() for s in ["PYTHON", "JAVA", "C++"])

# 6. Uppercase conversion
t6 = tuple(s.upper() for s in ["python", "java", "c++"])

# 7. First letter capitalized
t7 = tuple(s.capitalize() for s in ["apple", "banana", "kiwi"])

# 8. Round float numbers
nums = [3.1416, 2.7182, 1.6180]
t8 = tuple(round(x, 2) for x in nums)

# 9. Strip spaces from words
t9 = tuple(s.strip() for s in ["  apple ", " banana ", " kiwi "])

# 10. Count vowels in each word
def count_vowels(word):
    return sum(1 for ch in word.lower() if ch in "aeiou")

words = ["apple", "banana", "kiwi"]
t10 = tuple(count_vowels(w) for w in words)

#Section 4 – Nested Tuple Comprehension (Using two loops in comprehension)

# 1. Multiplication table pairs
t1 = tuple((x, y, x*y) for x in range(1,4) for y in range(1,4))

# 2. Cartesian product of two lists
colors = ["red", "blue"]
fruits = ["apple", "banana"]
t2 = tuple((c, f) for c in colors for f in fruits)

# 3. Pairs of even numbers
t3 = tuple((x, y) for x in range(2,5) for y in range(6,9))

# 4. Sum of pairs
t4 = tuple(x+y for x in [1,2] for y in [3,4])

# 5. Concatenate strings
t5 = tuple(a+b for a in ["A", "B"] for b in ["X", "Y"])

# 6. All coordinate pairs in a 2x2 grid
t6 = tuple((x, y) for x in range(2) for y in range(2))

# 7. Multiplication results in one tuple
t7 = tuple(x*y for x in range(1,4) for y in range(1,4))

# 8. Flatten a nested list
nested = [[1, 2], [3, 4]]
t8 = tuple(num for sublist in nested for num in sublist)

# 9. Combinations of digits and letters
t9 = tuple(str(x)+y for x in range(1,3) for y in ["A", "B"])

# 10. Pairs where sum is even
t10 = tuple((x, y) for x in range(3) for y in range(3) if (x+y)%2==0)
