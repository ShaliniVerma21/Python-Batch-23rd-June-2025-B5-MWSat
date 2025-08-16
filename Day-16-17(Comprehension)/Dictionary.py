""" 
1. Introduction to Dictionary Comprehension

A concise way to create dictionaries in a single line 
using `{key: value for ...}` syntax.

General Syntax:
{key_expr: value_expr for item in iterable if condition}

Advantages:

  * Short and readable
  * Often faster than loops
  * Easy to apply conditions

"""

#2. Basic Dictionary Comprehension
#Convert iterable data into a dictionary.

# 1. Squares of numbers 1–5
{n: n**2 for n in range(1, 6)}

# 2. Map words to their lengths
{word: len(word) for word in ["apple", "banana", "kiwi"]}

# 3. Index to letter mapping
{i: chr(65+i) for i in range(5)}

# 4. Even numbers and their cubes
{n: n**3 for n in range(2, 11, 2)}

# 5. Character frequency
{s: "vowel" for s in "aeiou"}

# 6. Mapping number to its square root
{n: round(n**0.5, 2) for n in range(1, 6)}

# 7. Convert list of tuples to dict
{k: v for k, v in [("a", 1), ("b", 2)]}

# 8. Reverse key-value in dictionary
{v: k for k, v in {"x": 1, "y": 2}.items()}

# 9. Number to binary mapping
{n: bin(n) for n in range(1, 6)}

# 10. Zip two lists into dict
{k: v for k, v in zip(["name", "age"], ["Alice", 25])}


#3. Conditional Dictionary Comprehension
#Add `if` to filter data.

# 1. Even numbers only
{n: n**2 for n in range(10) if n % 2 == 0}

# 2. Words longer than 4 letters
{w: len(w) for w in ["pen", "pencil", "marker"] if len(w) > 4}

# 3. Positive numbers only
{x: x**2 for x in [-2, -1, 0, 1, 2] if x > 0}

# 4. Vowels only from string
{c: ord(c) for c in "education" if c in "aeiou"}

# 5. Students with marks > 50
{s: m for s, m in {"A": 60, "B": 45, "C": 80}.items() if m > 50}

# 6. Filter dictionary by key
{k: v for k, v in {"x": 1, "y": 2, "z": 3}.items() if k != "y"}

# 7. Only odd squares
{n: n**2 for n in range(10) if n % 2 != 0}

# 8. Only fruits starting with 'a'
{f: len(f) for f in ["apple", "banana", "avocado"] if f.startswith("a")}

# 9. Filter by value type
{k: v for k, v in {"a": 1, "b": "two"}.items() if isinstance(v, int)}

# 10. Select multiples of 3
{n: n*2 for n in range(1, 11) if n % 3 == 0}


#4. Nested Dictionary Comprehension
#Create dictionaries inside dictionaries.

# 1. Multiplication table
{i: {j: i*j for j in range(1, 6)} for i in range(1, 6)}

# 2. Nested squares
{n: {p: p**2 for p in range(1, n+1)} for n in range(1, 4)}

# 3. Coordinates grid
{x: {y: (x, y) for y in range(3)} for x in range(3)}

# 4. Student subject marks
{student: {sub: 0 for sub in ["Math", "Science"]} for student in ["A", "B"]}

# 5. Year-month mapping
{year: {month: f"{month}-{year}" for month in range(1, 4)} for year in [2023, 2024]}

# 6. City-weather placeholder
{city: {day: "sunny" for day in ["Mon", "Tue"]} for city in ["Delhi", "Mumbai"]}

# 7. Language-character codes
{lang: {ch: ord(ch) for ch in "abc"} for lang in ["Python", "Java"]}

# 8. Multiples grouping
{n: {m: m*n for m in range(1, 4)} for n in range(1, 4)}

# 9. Dictionary of dictionaries from tuples
{k: {i: i*2 for i in v} for k, v in {"a": [1, 2], "b": [3, 4]}.items()}

# 10. Students and grades per subject
{s: {sub: "NA" for sub in ["Math", "English"]} for s in ["Tom", "Ana"]}


#5. Dictionary Comprehension with `if...else`
#Apply conditional expressions inside comprehension.

# 1. Even/Odd label
{n: "even" if n % 2 == 0 else "odd" for n in range(5)}

# 2. Pass/Fail
{s: "Pass" if m >= 50 else "Fail" for s, m in {"A": 40, "B": 60}.items()}

# 3. Positive/Negative
{x: "positive" if x > 0 else "negative" for x in [-1, 0, 2]}

# 4. Grade assign
{s: "A" if m >= 75 else "B" for s, m in {"John": 80, "Anna": 70}.items()}

# 5. Adult/Minor
{p: "Adult" if age >= 18 else "Minor" for p, age in {"Tom": 20, "Amy": 15}.items()}

# 6. Multiple of 3 or not
{n: "multiple" if n % 3 == 0 else "other" for n in range(1, 6)}

# 7. String case check
{w: "upper" if w.isupper() else "lower" for w in ["HI", "hello"]}

# 8. Long/Short word
{w: "Long" if len(w) > 4 else "Short" for w in ["apple", "bat"]}

# 9. Positive numbers else zero
{n: n if n > 0 else 0 for n in [-2, 3, 0]}

# 10. Even square else cube
{n: n**2 if n % 2 == 0 else n**3 for n in range(1, 6)}
