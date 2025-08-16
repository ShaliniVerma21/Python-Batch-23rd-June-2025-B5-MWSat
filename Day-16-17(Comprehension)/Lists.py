
#---------------------------List Comprehension in Python---------------------------

#1. Introduction

""" 
A list comprehension is a concise way to create lists in Python using a 
single line of code.

Syntax:
  [expression for item in iterable if condition]

Benefits:

  1. Shorter and cleaner code.
  2. Faster than using loops (in most cases).
  3. More Pythonic (recommended style).
"""

#SECTION 1 — Basic List Comprehension (No Condition)
#Directly apply an operation or transformation on each element of an iterable.

#Syntax:
  #[expression for item in iterable]
  
# 1. Square numbers from 0 to 9
squares = [x**2 for x in range(10)]

# 2. Convert strings to uppercase
words = ["python", "java", "c++"]
upper_words = [w.upper() for w in words]

# 3. Get lengths of each word
lengths = [len(w) for w in words]

# 4. Multiply each number by 10
nums = [1, 2, 3]
times_10 = [n*10 for n in nums]

# 5. Convert list of numbers to strings
num_str = [str(n) for n in [10, 20, 30]]

# 6. Add 5 to each number
plus_5 = [n+5 for n in range(5)]

# 7. Cube of each number
cubes = [n**3 for n in range(1,6)]

# 8. Double characters in a string
doubled = [ch*2 for ch in "hello"]

# 9. First letter of each name
names = ["Alice", "Bob", "Charlie"]
first_letters = [name[0] for name in names]

# 10. Reverse each word
reversed_words = [w[::-1] for w in ["apple", "banana", "cherry"]]


#SECTION 2 — List Comprehension with Condition (If)

#Filter elements while building the list.

#Syntax:
  #[expression for item in iterable if condition]
  
# 1. Even numbers from 0 to 20
evens = [n for n in range(21) if n%2 == 0]

# 2. Odd numbers from 1 to 20
odds = [n for n in range(21) if n%2 != 0]

# 3. Numbers greater than 5
greater_than_5 = [n for n in range(10) if n > 5]

# 4. Words starting with 'p'
words = ["python", "java", "perl", "c"]
starts_with_p = [w for w in words if w.startswith('p')]

# 5. Words longer than 4 letters
long_words = [w for w in words if len(w) > 4]

# 6. Positive numbers only
nums = [-3, -1, 0, 2, 4]
positive_nums = [n for n in nums if n > 0]

# 7. Strings containing 'a'
contains_a = [w for w in ["cat", "dog", "apple"] if 'a' in w]

# 8. Numbers divisible by both 2 and 3
divisible = [n for n in range(30) if n%2==0 and n%3==0]

# 9. Skip empty strings
names = ["John", "", "Sam", ""]
non_empty = [n for n in names if n]

# 10. Words not equal to "java"
not_java = [w for w in words if w != "java"]


#SECTION 3 — List Comprehension with If-Else (Conditional Expressions)
# Apply a transformation depending on a condition.

#Syntax:
  #[true_expr if condition else false_expr for item in iterable]
  
# 1. Label numbers as Even or Odd
labels = ["Even" if n%2==0 else "Odd" for n in range(10)]

# 2. Replace negatives with 0
nums = [-5, 3, -1, 7]
no_negatives = [n if n > 0 else 0 for n in nums]

# 3. Pass/Fail based on marks
marks = [45, 80, 30, 95]
result = ["Pass" if m>=40 else "Fail" for m in marks]

# 4. Convert numbers to strings if > 10
nums = [5, 12, 7]
converted = [str(n) if n > 10 else n for n in nums]

# 5. Grade students
scores = [90, 70, 40, 20]
grades = ["A" if s>=80 else "B" if s>=50 else "C" for s in scores]

# 6. Replace even numbers with double, odd numbers unchanged
nums = [1,2,3,4]
modified = [n*2 if n%2==0 else n for n in nums]

# 7. Uppercase short words, lowercase long words
words = ["hi", "HELLO", "bye", "GoodMorning"]
case_change = [w.upper() if len(w)<=3 else w.lower() for w in words]

# 8. Tag positive/negative numbers
nums = [-3, -1, 0, 2, 4]
tagged = ["Positive" if n>0 else "Negative" if n<0 else "Zero" for n in nums]

# 9. Replace vowels with '*'
chars = ['a', 'b', 'e', 'f']
vowel_replace = ['*' if c in 'aeiou' else c for c in chars]

# 10. Append suffix '_ok' if string length < 5
words = ["cat", "python", "dog"]
with_suffix = [w+"_ok" if len(w)<5 else w for w in words]


#SECTION 4 — Nested List Comprehensions
# Used for two or more loops inside a comprehension.

#Syntax:
  #[expression for item1 in iterable1 for item2 in iterable2]

# 1. Cartesian product of two lists
product = [(x, y) for x in [1,2,3] for y in ['a', 'b']]

# 2. Flatten a 2D list
matrix = [[1,2,3], [4,5], [6,7]]
flat = [num for row in matrix for num in row]

# 3. All pairs (i,j) where i<j
pairs = [(i,j) for i in range(3) for j in range(3) if i<j]

# 4. Multiplication table (1 to 3)
table = [f"{i}x{j}={i*j}" for i in range(1,4) for j in range(1,4)]

# 5. Combine adjectives with nouns
adjectives = ["red", "big"]
nouns = ["apple", "car"]
combinations = [a + " " + n for a in adjectives for n in nouns]

# 6. All possible coordinates
coords = [(x,y,z) for x in range(2) for y in range(2) for z in range(2)]

# 7. Extract diagonal elements from matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
diag = [matrix[i][i] for i in range(len(matrix))]

# 8. Reverse each word in sentences
sentences = [["hello", "world"], ["python", "rocks"]]
reversed_words = [word[::-1] for sentence in sentences for word in sentence]

# 9. Get even numbers from multiple lists
lists = [[1,2,3],[4,5,6],[7,8,9]]
evens = [n for sublist in lists for n in sublist if n%2==0]

# 10. Combine letters from two words
letters = [a+b for a in "ab" for b in "12"]


#SECTION 5 — Using Functions inside List Comprehensions
#You can call functions directly inside the comprehension.

# 1. Square using pow()
squares = [pow(n, 2) for n in range(5)]

# 2. Strip spaces from strings
words = [" apple ", " banana ", " cherry "]
cleaned = [w.strip() for w in words]

# 3. Get absolute values
nums = [-5, -1, 0, 3]
abs_values = [abs(n) for n in nums]

# 4. Convert to title case
names = ["john doe", "jane smith"]
titles = [n.title() for n in names]

# 5. Length of each sentence
sentences = ["Hello world", "Python is fun"]
lengths = [len(s) for s in sentences]

# 6. Find factorial of numbers
import math
facts = [math.factorial(n) for n in range(6)]

# 7. Convert float to int
floats = [2.5, 3.7, 8.1]
ints = [int(f) for f in floats]

# 8. Count vowels in words
count_vowels = [sum(1 for ch in w if ch in 'aeiou') for w in ["apple", "banana"]]

# 9. Check palindrome
palindrome_check = [w == w[::-1] for w in ["madam", "cat", "racecar"]]

# 10. Round off numbers
rounded = [round(n, 1) for n in [1.234, 5.678, 9.876]]