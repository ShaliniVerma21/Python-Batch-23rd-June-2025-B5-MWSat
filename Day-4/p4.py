

# ==================================
# 4. LOGICAL OPERATORS
# and, or, not

age = 20
has_id = True
print(age >= 18 and has_id)  # True

username = "admin"
password = "123"
print(username == "admin" or password == "admin")  # True

is_busy = False
print(not is_busy)  # True

grade = 'A'
attendance = 90
print(grade == 'A' and attendance > 85)  # True

income = 30000
credit_score = 750
print(income > 25000 and credit_score >= 700)  # True

height = 150
age = 12
print(height >= 140 and age >= 10)  # True

total_amount = 400
coupon = True
print(total_amount > 500 or coupon)  # True

msg = ""
print(not msg)  # True if empty string

print(age >= 18 and has_id)  # Driving license

is_weekend = True
is_holiday = False
print(is_weekend or is_holiday)  # Day off?

# ==================================
# 5. BITWISE OPERATORS
# &, |, ^, ~, <<, >>

"""
Get Binary Number -

-------512, 256, 128, 64, 32, 16, 8, 4, 2,1

Binary of 5 is - 0101
Binary of 3 is - 0011

"""

a = 5  # 0101
b = 3  # 0011

print(a & b)  # AND: 1
print(a | b)  # OR: 7
print(a ^ b)  # XOR: 6
print(~a)     # NOT: -6
print(a << 1)  # Left shift: 10
print(a >> 1)  # Right shift: 2

read = 4
write = 2
execute = 1
user = read | write  # 6 (Read + Write)

x = 7  # 0111
mask = ~1
print(x & mask)  # Turn off last bit: 6

num = 4
print(num & 1 == 0)  # Even check: True

# Efficient Calculations (Swapping Without Temp Variable)
x = 10
y = 20
x = x ^ y
y = x ^ y
x = x ^ y

"""
Flags and Permissions (Access Control Systems)
Imagine managing user permissions like:

Read = 1
Write = 2
Execute = 4

"""

#Example: Assign and check user access
# User has Read + Execute
user_permission = 1 | 4  # 5

# Check if user has Write access
has_write = user_permission & 2
print("Write access?", bool(has_write))  # False

# Add Write access
user_permission |= 2  # Now permission becomes 7
print("Updated permission:", user_permission)  # 7


# ==================================
# 6. MEMBERSHIP OPERATORS
# in, not in

fruits = ["apple", "banana", "mango"]
print("banana" in fruits)     # True
print("grapes" not in fruits)  # True

email = "shalini@example.com"
print("@" in email)  # Valid email check

text = "Python is powerful"
print("Python" in text)  # True

usernames = ["admin", "test"]
print("admin" in usernames)

print("a" in "data")

permissions = "rw"
print("r" in permissions and "w" in permissions)

banned = ["abc", "xyz"]
print("user1" not in banned)

courses = ["Python", "Java"]
print("Python" in courses)

coupon_codes = ["SAVE50", "NEW100"]
print("SAVE50" in coupon_codes)

# ==================================
# 7. IDENTITY OPERATORS
# is, is not

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)        # True (same object)
print(a is not c)    # True (different object)
x = None
print(x is None)     # True

print(id(a) == id(b))  # Same memory

x = 100
y = 100
print(x is y)  # True (Python caches small ints)

a.append(4)
print(b)  # [1, 2, 3, 4]

s1 = "hello"
s2 = "hello"
print(s1 is s2)  # True

print(id(c))  # Different ID than 'a' and 'b'

b = [5, 6]
print(a is b)  # False

print(a == c)  # True (values same)
print(a is c)  # False (objects different)


#  5. Escape Sequence – Handling special characters
"""
Escape sequences are special characters preceded by a backslash (\) used to represent 
things that are difficult to type directly in a string, like new lines, tabs, quotes, or 
Unicode characters.
"""
# 1. New line – splits output into two lines
print("Hello\nWorld")

# 2. Tab space – creates horizontal spacing
print("Name:\tShalini")

# 3. Double quote inside string
print("She said, \"I love Python\"")

# 4. Single quote inside string
print('It\'s a sunny day')

# 5. Backslash in file path
print("C:\\Users\\Shalini\\Documents")

# 6. Bell sound (beep) – may not work in all terminals
print("Alert\a")

# 7. Carriage return – replaces beginning of string
print("Start\rEnd")  # Output: "Endrt"

# 8. Unicode character – red heart
print("I ❤️ Python \u2764")

# 9. Octal values – prints "Hello"
print("\110\145\154\154\157")  # Octal codes for H, e, l, l, o

# 10. Null character – invisible
print("End\0Start")

# 11. Backspace – deletes previous character
print("Hello\bWorld")  # Removes 'o'

# 12. Vertical tab – not widely used, acts like new line
print("Python\vRocks")

# 13. Form feed – new page in printers (not visible on screen)
print("Hello\fWorld")

# 14. Quote in quote
print("He said, \"Don't worry.\"")

# 15. File path example
print("D:\\NewFolder\\script.py")

# 16. Emoji using Unicode
print("Smile: \U0001F604")  # 😄

# 17. Hexadecimal – \x48 = H
print("\x48\x45\x4C\x4C\x4F")  # HELLO

# 18. Multiline string with escape characters
print("Line1\nLine2\nLine3")

# 19. Escape both quotes
print("\"Quote\" and \'Single quote\' inside")

# 20. Escape in JSON-like string
print("{\"name\": \"Shalini\", \"age\": 25}")

# 21. Text formatting
print("Column1\tColumn2\tColumn3")

# 22. Escaping backslashes in URLs
print("URL: https:\\\\www.example.com")

# 23. Double quotes in double quotes
print("This is a \"quoted\" word.")

# 24. Single quotes in single quotes
print('It\'s working fine.')

# 25. Clear screen (not an escape, but for terminal control)
print("\033c")  # ANSI escape code for clearing screen (if terminal supports)


