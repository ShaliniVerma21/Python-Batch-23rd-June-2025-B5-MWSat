# 1. Introduction to Set Comprehension

""" 
A set comprehension is a concise way to create a Python `set` in a single line, 
using a syntax similar to list comprehensions but with curly braces `{}`.

Purpose:

  --> Remove duplicates automatically (because sets store only unique elements).
  --> Write cleaner and shorter code.
  --> Apply transformations or filters in a single step.

Syntax:
{expression for item in iterable if condition}

Parts:

1. expression → what value you want to include in the set.
2. iterable → sequence or collection to loop through.
3. condition (optional) → filters items.

"""

#2. Basic Set Comprehension
# Creates a set by iterating over an iterable and applying an expression. Removes duplicates automatically.

# 1: Square numbers from 1 to 5
squares = {x**2 for x in range(1, 6)}

# 2: Uppercase letters from a word
letters = {ch.upper() for ch in "hello"}

# 3: First letters of given words
first_letters = {word[0] for word in ["apple", "banana", "cherry", "apricot"]}

# 4: Even numbers from a list
evens = {x for x in [1, 2, 2, 3, 4, 4, 6] if x % 2 == 0}

# 5: Length of words
lengths = {len(word) for word in ["cat", "elephant", "dog", "ant"]}

# 6: Absolute values
abs_values = {abs(x) for x in [-1, -2, 3, -4, 3]}

# 7: Remove whitespace from string
chars = {ch for ch in "hello world" if ch != " "}

# 8: Multiples of 3
multiples_3 = {x for x in range(1, 20) if x % 3 == 0}

# 9: Vowels in a sentence
vowels = {ch for ch in "Python Programming" if ch.lower() in "aeiou"}

# 10: Reverse words in a list
reverse_words = {word[::-1] for word in ["apple", "banana", "cat"]}


#3. Set Comprehension with Condition (Adds an `if` clause to filter elements.)

# 1: Odd numbers from 1 to 10
odds = {x for x in range(1, 11) if x % 2 != 0}

# 2: Names starting with 'A'
names_a = {name for name in ["Alice", "Bob", "Andrew", "Charlie"] if name.startswith("A")}

# 3: Numbers greater than 50
greater_50 = {x for x in [12, 55, 78, 30, 99] if x > 50}

# 4: Words longer than 4 characters
long_words = {word for word in ["cat", "elephant", "dog", "mouse"] if len(word) > 4}

# 5: Positive numbers
positives = {x for x in [-2, 3, -5, 6, 0, 8] if x > 0}

# 6: Consonants only
consonants = {ch for ch in "Hello World" if ch.lower() not in "aeiou "}

# 7: Numbers divisible by both 2 and 3
div_2_3 = {x for x in range(1, 30) if x % 2 == 0 and x % 3 == 0}

# 8: Non-empty strings
non_empty = {word for word in ["", "apple", "", "banana"] if word}

# 9: Prices greater than 100
expensive = {price for price in [50, 120, 300, 80] if price > 100}

# 10: Only lowercase letters from a string
lowercase_letters = {ch for ch in "Python3.8" if ch.islower()}


#4. Nested Set Comprehension
#You can use nested loops inside set comprehensions, similar to nested `for` loops.

# 1: All products of two lists
products = {x*y for x in [1, 2, 3] for y in [4, 5]}

# 2: Pairs of letters
pairs = {a+b for a in "ab" for b in "12"}

# 3: Multiplication table (values only)
table = {i*j for i in range(1, 4) for j in range(1, 4)}

# 4: Sum of two ranges
sum_pairs = {x+y for x in range(3) for y in range(3)}

# 5: Unique character pairs from two strings
char_pairs = {a+b for a in "hi" for b in "ok"}

# 6: All coordinates in a 2x2 grid
coordinates = {(x, y) for x in range(2) for y in range(2)}

# 7: Concatenate names and titles
full_names = {title + name for title in ["Mr.", "Ms."] for name in ["John", "Emma"]}

# 8: Common multiples of 2 and 5
common_mult = {x*y for x in [2, 4] for y in [5, 10]}

# 9: Word pairs from two lists
word_pairs = {w1 + " " + w2 for w1 in ["red", "blue"] for w2 in ["car", "bike"]}

# 10: Cross product of sets
cross_product = {m+n for m in {"A", "B"} for n in {"1", "2"}}

#5. Set Comprehension with Functions
#Functions can be used inside the expression for cleaner or more complex logic.

# 1: Square numbers using pow()
squares = {pow(x, 2) for x in range(1, 6)}

# 2: Convert to uppercase using str.upper()
upper_words = {word.upper() for word in ["apple", "banana", "cherry"]}

# 3: Length of each string using len()
word_lengths = {len(w) for w in ["a", "abc", "hello"]}

# 4: Absolute values using abs()
abs_vals = {abs(x) for x in [-3, -1, 2, 4, -4]}

# 5: Round float numbers using round()
rounded = {round(num) for num in [1.1, 2.5, 3.8]}

# 6: Remove spaces using str.strip()
cleaned = {name.strip() for name in [" John ", "  Alice", "Bob "]}

# 7: Reverse strings using slicing
reversed_words = {w[::-1] for w in ["abc", "xyz", "hello"]}

# 8: Extract domain from emails
domains = {email.split("@")[1] for email in ["a@gmail.com", "b@yahoo.com"]}

# 9: Factorials using math.factorial()
import math
factorials = {math.factorial(n) for n in range(1, 6)}

# 10: Lowercase letters from string
lowercase = {ch.lower() for ch in "PYTHON"}