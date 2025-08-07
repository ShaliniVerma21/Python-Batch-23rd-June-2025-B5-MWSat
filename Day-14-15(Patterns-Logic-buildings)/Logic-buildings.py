# Program 1: Check if a number is even or odd
num = 10
# Check if number is divisible by 2
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Program 2: Find the largest among three numbers
#This is an example of multiple assignment in Python.
a, b, c = 5, 10, 7
""" 
It assigns three variables a, b, and c in a single line, like this:
a = 5
b = 10
c = 7

Note- Python unpacks the tuple on the right-hand side (5, 10, 7) 
and assigns each value to the variable on the left in sequence.
"""
# Compare each variable to find the maximum
if a > b and a > c:
    print("a is largest")
elif b > c:
    print("b is largest")
else:
    print("c is largest")


# Program 3: Check if a year is a leap year

year = 2024  # You can change this value to test other years

# A year is a leap year if:
# 1. It is divisible by 4 AND not divisible by 100, OR
# 2. It is divisible by 400
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


# Program 4: Sum of digits of a number
# Initialize the number
num = 1234
# Initialize a variable to store the sum of digits
sum_digits = 0
# Loop runs as long as num is greater than 0
while num > 0:
    # Add the last digit of num to sum_digits
    sum_digits += num % 10
    # Remove the last digit from num
    num //= 10
# Print the final sum of digits
print("Sum of digits:", sum_digits)


# Program 5: Reverse a number
# Initialize the number to be reversed
num = 12345
# Initialize a variable to store the reversed number
rev = 0
# Loop until the number becomes 0
while num > 0:
    # Extract the last digit and add it to the reversed number
    rev = rev * 10 + num % 10
    # Remove the last digit from the number
    num //= 10
# Print the reversed number
print("Reversed number:", rev)

# Program 6: Check if a number is palindrome
# Initialize the number
num = 121
# Store the original number to compare later
temp = num
# Initialize variable to store the reversed number
rev = 0
# Reverse the number
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
# Check if the original and reversed numbers are equal
print("Palindrome" if num == rev else "Not Palindrome")

# Program 7: Fibonacci series up to n terms
# Number of terms to generate
n = 10
# First two terms of the series
a, b = 0, 1
# Loop to generate Fibonacci sequence
for _ in range(n):
    # Print current term
    print(a, end=' ')
    # Update values of a and b
    a, b = b, a + b

# Program 8: Factorial using loop
# Number for which to find factorial
num = 5
# Initialize factorial value
fact = 1
# Loop from 1 to num to calculate factorial
for i in range(1, num + 1):
    fact *= i
# Print the factorial result
print("Factorial:", fact)

# Program 9: Check if a number is prime
# Number to check
num = 29
# Prime check for numbers less than 2
if num < 2:
    print("Not Prime")
else:
    # Check divisibility from 2 to square root of num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        # No divisors found; it's a prime number
        print("Prime")

# Program 10: Print all prime numbers in range
# Loop through numbers from 10 to 49
for num in range(10, 50):
    # Check for prime
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        # Print the prime number
        print(num, end=' ')


# Program 11: Check if a string is palindrome
# Check if a string is the same when reversed
text = "madam"
# Compare original string with its reverse
if text == text[::-1]:
    print("Palindrome String")
else:
    print("Not Palindrome")

# Program 12: Count vowels and consonants in a string
# Count how many vowels and consonants in a string
text = "Hello World"
vowels = 'aeiouAEIOU'
v_count = c_count = 0
# Loop through each character in the string
for ch in text:
    if ch.isalpha():  # Check if it's a letter
        if ch in vowels:
            v_count += 1  # Count vowel
        else:
            c_count += 1  # Count consonant
print("Vowels:", v_count, "Consonants:", c_count)

# Program 13: Sum of first n natural numbers
# Calculate sum from 1 to n
n = 100
sum_n = 0
# Loop to add numbers from 1 to n
for i in range(1, n + 1):
    sum_n += i
print("Sum of natural numbers:", sum_n)

# Program 14: Multiplication table of a number
# Print table of a number (e.g., 7)
num = 7
# Loop through 1 to 10 to print the table
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Program 15: Factorial using recursion
# Recursively calculate factorial of a number
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

print("Factorial:", factorial(5))

# Program 16: GCD of two numbers
# Greatest Common Divisor using Euclidean algorithm
a, b = 36, 60
# Loop until remainder becomes 0
while b:
    a, b = b, a % b
# 'a' will hold the GCD
print("GCD is:", a)

# Program 17: LCM of two numbers
# Least Common Multiple using GCD
a, b = 12, 15
# Define function to compute GCD
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# LCM formula: (a * b) / GCD\lcm = a * b // gcd(a, b)
print("LCM is:", lcm)

# Program 18: Count digits in a number
# Count total digits in a number
num = 123456
count = 0
# Loop until num becomes 0
while num:
    num //= 10  # Remove last digit
    count += 1  # Increment count
print("Total digits:", count)

# Program 19: Print right triangle pattern
# Print right-angled triangle using stars
n = 5
# Loop through rows
for i in range(1, n + 1):
    print("*" * i)

# Program 20: Print inverted right triangle
# Print inverted triangle using stars
n = 5
# Loop from n down to 1
for i in range(n, 0, -1):
    print("*" * i)


# Program 21: Check if a number is an Armstrong number
# 153 = 1³ + 5³ + 3³ = 153
num = 153
temp = num
power = len(str(num))
sum_of_powers = 0
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** power
    temp //= 10
print("Armstrong Number" if num == sum_of_powers else "Not Armstrong")


#Program 22: Print all Armstrong numbers in a range
# 153 = 1³ + 5³ + 3³ = 153
for num in range(100, 1000):
    temp = num
    power = len(str(num))
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10
    if total == num:
        print(num, end=' ')

#Program 23: Calculate power using loop (No **)
base = 2
exponent = 5
result = 1
for _ in range(exponent):
    result *= base
print("Power:", result)


#Program 24: Frequency of characters in a string
text = "interview"
freq = {}
for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(freq)


# Program 25: Check if a number is a Perfect number
# 6 = 1 + 2 + 3 = 6
# Perfect number = sum of its proper divisors (excluding itself)
num = 28
sum_factors = 0
for i in range(1, num):
    if num % i == 0:
        sum_factors += i
print("Perfect Number" if sum_factors == num else "Not Perfect")


# Program 26: Find all perfect numbers in a range
for num in range(1, 1000):
    sum_factors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_factors += i
    if sum_factors == num:
        print(num, end=' ')


#Program 27: Remove duplicates from a list
nums = [1, 2, 2, 3, 4, 4, 5]
unique = []
for n in nums:
    if n not in unique:
        unique.append(n)
print(unique)


# Program 28: Find second largest element in list
nums = [10, 20, 4, 45, 99]
first = second = float('-inf')
for num in nums:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num
print("Second Largest:", second)


# Program 29: Find common elements in two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]
common = []
for i in list1:
    if i in list2 and i not in common:
        common.append(i)
print("Common Elements:", common)


# Program 30: Count even and odd numbers in a list
nums = [1, 2, 3, 4, 5, 6]
even = odd = 0
for num in nums:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even, "Odd:", odd)


# Program 31: Find all prime numbers in a list
nums = [3, 4, 7, 9, 13, 17, 20]
for num in nums:
    if num < 2:
        continue
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        print(f"{num} is Prime")
        

#Program 32: Swap two variables without using a third variable
a, b = 10, 20
a, b = b, a
print("a =", a, "b =", b)


# Program 33: Find sum of elements in a list
nums = [1, 2, 3, 4, 5]
total = 0
for num in nums:
    total += num
print("Sum:", total)


#Program 34: Check if a number is positive, negative, or zero
num = -10
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Program 35: Print all factors of a number
num = 36
print(f"Factors of {num}:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=' ')


# Program 36: Check if a string is anagram of another
str1 = "listen"
str2 = "silent"
if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")


# Program 37: Reverse a string without using [::-1]
text = "hello"
rev = ''
for ch in text:
    rev = ch + rev
print("Reversed:", rev)


# Program 38: Find largest element in a list
nums = [5, 1, 9, 3, 7]
largest = nums[0]
for num in nums:
    if num > largest:
        largest = num
print("Largest:", largest)


# Program 39: Print numbers skipping multiples of 3 using continue
for i in range(1, 20):
    if i % 3 == 0:
        continue
    print(i, end=' ')


#Program 40: Find number of words in a sentence
sentence = "Python is an awesome language"
words = sentence.split()
print("Total words:", len(words))


#Program 41: Check if a number is a Perfect Square
# A number is a perfect square if its square root is an integer.

num = int(input("Enter a number: "))
sqrt = int(num ** 0.5)

if sqrt * sqrt == num:
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")


#Program 42: Check for Harshad Number
# A number is Harshad if it is divisible by the sum of its digits

num = int(input("Enter a number: "))
temp = num
sum_digits = 0

while temp > 0:
    sum_digits += temp % 10
    temp //= 10

if num % sum_digits == 0:
    print(f"{num} is a Harshad Number.")
else:
    print(f"{num} is not a Harshad Number.")


#Program 43: Replace all vowels in a string with '*'
# Using loops and conditional logic to modify a string

string = input("Enter a string: ")
vowels = 'aeiouAEIOU'
result = ""

for ch in string:
    if ch in vowels:
        result += '*'
    else:
        result += ch

print("Modified string:", result)


#Program 44:  Print diamond pattern using stars
# Nested loops and spacing logic

n = int(input("Enter number of rows: "))

# Upper half
for i in range(n):
    print(' '*(n-i-1) + '*'*(2*i+1))

# Lower half
for i in range(n-2, -1, -1):
    print(' '*(n-i-1) + '*'*(2*i+1))


#Program 45: Create a number pyramid pattern
# Number pattern using nested loops

rows = int(input("Enter number of rows: "))
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()


#Program 46: Sum of even and odd digits separately
# Separate sums using loops and conditions

num = int(input("Enter a number: "))
even_sum = 0
odd_sum = 0

while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit
    num //= 10

print("Sum of even digits:", even_sum)
print("Sum of odd digits:", odd_sum)


#Program 47: Check if a list is sorted
# Compare original list with sorted version

lst = list(map(int, input("Enter list elements: ").split()))

if lst == sorted(lst):
    print("List is sorted in ascending order.")
else:
    print("List is not sorted.")


#Program 48: Find all Armstrong numbers in a given range
# Armstrong number: sum of digits^number_of_digits = original number

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

for num in range(start, end+1):
    digits = list(map(int, str(num)))
    power = len(digits)
    if sum([d**power for d in digits]) == num:
        print(num, end=' ')


