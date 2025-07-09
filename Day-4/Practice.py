# 4. Logical Operators (and, or, not)

# 1. Check if person is adult and has voter ID
age = 22
has_voter_id = True
if age >= 18 and has_voter_id:
    print("Eligible to vote")

# 2. Student eligible for scholarship
marks = 85
income = 20000
if marks > 80 and income < 25000:
    print("Scholarship Granted")

# 3. Login check using OR (either email or phone is needed)
has_email = False
has_phone = True
if has_email or has_phone:
    print("Can login")

# 4. Not operator usage
is_logged_in = False
if not is_logged_in:
    print("Please login first")

# 5. Check if it's weekend or holiday
is_weekend = True
is_holiday = False
if is_weekend or is_holiday:
    print("Take a rest day!")

# 6. Validate strong password
length = 12
has_special_char = True
if length >= 8 and has_special_char:
    print("Strong Password")

# 7. Check discount eligibility
is_prime = True
cart_value = 1200
if is_prime or cart_value > 1000:
    print("Discount Applied")

# 8. Bank loan eligibility
credit_score = 750
has_collateral = False
if credit_score > 700 and not has_collateral:
    print("Partial Loan Approved")

# 9. Check if mobile is connected
is_wifi = False
is_data = True
if is_wifi or is_data:
    print("Internet available")

# 10. Check exam pass
math = 65
english = 55
if math > 40 and english > 40:
    print("Passed")

# 11. Entry for senior citizen
age = 65
has_pass = False
if age > 60 and (has_pass or age > 70):
    print("Entry granted")

# 12. Check if form is incomplete
has_name = True
has_photo = False
if not has_name or not has_photo:
    print("Form is incomplete")

# 13. Check festival discount
is_festival = True
purchase_amount = 900
if is_festival and purchase_amount > 800:
    print("Festival Discount Applied")

# 14. Multiple login options
login_with_google = False
login_with_facebook = True
if login_with_google or login_with_facebook:
    print("User logged in")

# 15. Health check
is_fever = True
is_cough = False
if is_fever and not is_cough:
    print("Take paracetamol")

# 16. Night driving alert
is_night = True
has_headlights_on = False
if is_night and not has_headlights_on:
    print("Turn on headlights!")

# 17. Shopping site free delivery
total_cart = 1500
is_premium_member = False
if total_cart > 1000 or is_premium_member:
    print("Free delivery available")

# 18. Attendance check
is_present = False
is_on_leave = True
if not is_present and not is_on_leave:
    print("Marked absent")

# 19. Tourist permit
is_indian = True
has_visa = True
if is_indian or has_visa:
    print("Allowed")

# 20. School entry
has_id_card = True
is_in_uniform = False
if has_id_card and is_in_uniform:
    print("Entry allowed")

# 21. Discount offer
has_coupon = False
spent_above_500 = True
if has_coupon or spent_above_500:
    print("Discount available")

# 22. Insurance eligibility
age = 30
is_smoker = False
if age > 25 and not is_smoker:
    print("Eligible for insurance")

# 23. Ride eligibility
is_driver = True
has_license = True
if is_driver and has_license:
    print("Can ride")

# 24. Battery charging check
is_plugged = True
battery_percent = 45
if is_plugged and battery_percent < 100:
    print("Charging...")

# 25. Not operator for validation
logged_in = True
if not logged_in:
    print("Access denied")
else:
    print("Welcome user!")



#  5. Bitwise Operators (&, |, ^, ~, <<, >>)

# 1. Bitwise AND
print(12 & 5)  # 4

# 2. Bitwise OR
print(12 | 5)  # 13

# 3. Bitwise XOR
print(12 ^ 5)  # 9

# 4. Bitwise NOT
print(~5)  # -6

# 5. Left shift
print(5 << 2)  # 20

# 6. Right shift
print(20 >> 2)  # 5

# 7. Check even/odd using AND
num = 7
if num & 1:
    print("Odd")
else:
    print("Even")

# 8. Swap using XOR
a, b = 5, 7
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)

# 9. Set specific bit
n = 4
n = n | (1 << 1)
print(n)

# 10. Clear specific bit
n = 7
n = n & ~(1 << 1)
print(n)

# 11. Toggle specific bit
n = 5
n = n ^ (1 << 1)
print(n)

# 12. Multiply by 2 using <<
print(10 << 1)  # 20

# 13. Divide by 2 using >>
print(10 >> 1)  # 5

# 14. Bit masking
n = 13  # 1101
mask = 1 << 2
if n & mask:
    print("Bit 2 is set")

# 15. Check if power of 2
num = 16
if num & (num - 1) == 0:
    print("Power of 2")

# 16. Convert decimal to binary
print(bin(10))  # 0b1010

# 17. Count number of 1s in binary
print(bin(15).count('1'))  # 4

# 18. Invert all bits
n = 0b1010
print(bin(~n))

# 19. Set all bits to 1 in 8-bit
print(bin((1 << 8) - 1))  # 0b11111111

# 20. Bitwise AND with mask
value = 13
mask = 0b111
print(value & mask)

# 21. Store multiple flags
read = 0b001
write = 0b010
execute = 0b100
perm = read | write
print(perm & execute)  # 0

# 22. Toggle bit in status flag
status = 0b1011
toggle_bit = 0b0100
status = status ^ toggle_bit
print(bin(status))

# 23. Turn off rightmost 1-bit
x = 12
print(x & (x - 1))

# 24. Turn on rightmost 0-bit
x = 10
print(x | (x + 1))

# 25. Get rightmost 1-bit only
x = 10
print(x & -x)



# 6. Membership Operators (in, not in)

# 1. Check if item exists in list
fruits = ['apple', 'banana']
if 'banana' in fruits:
    print("Found banana")

# 2. Check if char in string
word = "Python"
if 'y' in word:
    print("Yes")

# 3. Check if value not in set
roll_numbers = {101, 102, 103}
if 105 not in roll_numbers:
    print("Absent")

# 4. Keyword in sentence
sentence = "Python is awesome"
if "awesome" in sentence:
    print("Compliment found")

# 5. Check file extension
filename = "report.pdf"
if ".pdf" in filename:
    print("PDF File")

# 6. Check domain
email = "user@gmail.com"
if "@gmail.com" in email:
    print("Gmail user")

# 7. Character in password
password = "myp@ss123"
if '@' in password:
    print("Valid special character")

# 8. Membership in dict keys
student = {'name': 'Raj', 'age': 21}
if 'name' in student:
    print("Name exists")

# 9. Membership in values
if 21 in student.values():
    print("Age exists")

# 10. Membership in tuple
colors = ('red', 'green', 'blue')
if 'blue' in colors:
    print("Color matched")

# 11. Check in list of dicts
users = [{'id': 1}, {'id': 2}]
if {'id': 2} in users:
    print("User found")

# 12. Find substring
msg = "Welcome to Python batch"
if "Python" in msg:
    print("Batch verified")

# 13. Word not in paragraph
para = "Learning Python with real examples"
if "Java" not in para:
    print("Java is missing")

# 14. Tag check in HTML
html = "<h1>Hello</h1>"
if "<h1>" in html:
    print("Title tag found")

# 15. Find item in cart
cart = ["pen", "pencil", "eraser"]
if "pencil" in cart:
    print("In cart")

# 16. Role check
roles = ['admin', 'editor']
if 'viewer' not in roles:
    print("Access denied")

# 17. Skill set match
skills = ['Python', 'SQL']
if 'Excel' in skills:
    print("Has Excel skill")
else:
    print("Excel missing")

# 18. Search query in title
title = "Data Science Workshop"
query = "Science"
if query in title:
    print("Match found")

# 19. Ingredient in recipe
ingredients = ["milk", "sugar", "tea"]
if "tea" in ingredients:
    print("Make chai")

# 20. Filter empty strings
words = ["alpha", "", "beta"]
filtered = [w for w in words if w != '']
print(filtered)

# 21. Check file path
path = "C:/Users/Admin/Desktop"
if "Desktop" in path:
    print("Inside desktop")

# 22. URL check
url = "https://youtube.com"
if "youtube" in url:
    print("Video site")

# 23. Membership in range
if 5 in range(1, 10):
    print("Within range")

# 24. Find duplicate
nums = [1, 2, 3, 4, 2]
if nums.count(2) > 1:
    print("Duplicate found")

# 25. Validate token
token = "abc123"
valid_tokens = ['xyz456', 'abc123']
if token in valid_tokens:
    print("Token accepted")



# 7. Identity Operators (is, is not)

# 1. Check same object
x = [1, 2]
y = x
if x is y:
    print("Same object")

# 2. Check different object
a = [3, 4]
b = [3, 4]
if a is not b:
    print("Different object")

# 3. Check None
result = None
if result is None:
    print("Result not available")

# 4. Compare strings
name1 = "Shalini"
name2 = "Shalini"
if name1 is name2:
    print("Same string objects")

# 5. Check boolean identity
status = True
if status is True:
    print("Active")

# 6. Compare memory references
a = 1000
b = 1000
print(a is b)  # False in some cases due to memory

# 7. Tuple identity
t1 = (1, 2)
t2 = (1, 2)
print(t1 is t2)  # True in some versions

# 8. Float identity
f1 = 2.5
f2 = 2.5
print(f1 is f2)

# 9. Integer cache check
x = 10
y = 10
print(x is y)  # True for small integers

# 10. Not identical list
a = [1]
b = [1]
print(a is not b)

# 11. Object None check
obj = None
if obj is None:
    print("Object not created")

# 12. Flag toggle
flag = True
if flag is not False:
    print("Valid flag")

# 13. Check instance id
data = {}
if id(data) is not None:
    print("ID exists")

# 14. Object comparison
class A:
    pass

a = A()
b = A()
print(a is b)  # False

# 15. Check if two sets are same
set1 = {1, 2}
set2 = {1, 2}
print(set1 is set2)

# 16. String intern check
a = "hello"
b = "hello"
print(a is b)  # True due to interning

# 17. Validate None
name = None
if name is None:
    print("No name found")

# 18. Different type object
x = 10
y = '10'
print(x is y)

# 19. Nested object identity
l1 = [1, [2, 3]]
l2 = l1
print(l1[1] is l2[1])  # True

# 20. Check reused variable
x = 100
y = x
print(x is y)

# 21. Dict identity
d1 = {"a": 1}
d2 = d1
print(d1 is d2)

# 22. Temporary object
print([] is [])

# 23. Check is not for deletion
item = None
if item is not None:
    print("Still exists")

# 24. Validate empty string identity
s = ""
if s is not None:
    print("Not null")

# 25. Check same function reference
def fun(): pass
a = fun
print(a is fun)



# Escape Sequence

# 1. Newline
print("Hello\nWorld")

# 2. Tab
print("Name:\tShalini")

# 3. Double quote
print("She said, \"I love Python\"")

# 4. Single quote
print('It\'s a sunny day')

# 5. Backslash
print("C:\\Users\\Shalini")

# 6. Bell sound
print("\a")

# 7. Carriage return
print("123456\rAB")

# 8. Unicode char
print("\u2764")  # Heart symbol

# 9. Vertical tab
print("Hello\vWorld")

# 10. Form feed
print("Line1\fLine2")

# 11. Hex character
print("\x41")  # A

# 12. Triple quote with escape
print("""This is line one\nThis is line two""")

# 13. Multiline string
print("Line1\nLine2\nLine3")

# 14. File path
print("D:\\Data\\file.txt")

# 15. Quotes inside string
print("He said, \"Let's learn Python\"")

# 16. Emoji using Unicode
print("Smile: \U0001F604")

# 17. Nested quote
print('It\'s called a \"bug\"')

# 18. Real path with escapes
path = "C:\\newfolder\\images"
print(path)

# 19. Password masked
print("Password:\t********")

# 20. Escape ending
print("Hello\\")  # Ends with backslash

# 21. Quote string manually
quote = "\"Success is a journey\""
print(quote)

# 22. Escaping URL
print("https:\/\/www.example.com")

# 23. Escape name
print("Shalini\nVerma")

# 24. Print bullet points
print("\u2022 Learn Python\n\u2022 Practice Daily")

# 25. Combine escapes
print("Name:\tShalini\nAge:\t27")


#------------------------------------ Swapping -----------------------------------

#1. Using a Temporary Variable

# Swapping using a third (temporary) variable
a = 10
b = 20

print("Before Swapping:")
print("a =", a, ", b =", b)

# Step 1: Store value of a in temp
temp = a

# Step 2: Assign value of b to a
a = b

# Step 3: Assign temp (original a) to b
b = temp

print("After Swapping using Temp Variable:")
print("a =", a, ", b =", b)


#2. Without Using a Temporary Variable (Using Arithmetic Operators)

# Swapping using addition and subtraction
a = 30
b = 40

print("Before Swapping:")
print("a =", a, ", b =", b)

# Step 1: Add both numbers and store in a
a = a + b  # a = 70

# Step 2: Subtract b from new a to get original a
b = a - b  # b = 30

# Step 3: Subtract new b from new a to get original b
a = a - b  # a = 40

print("After Swapping using Arithmetic:")
print("a =", a, ", b =", b)


# 3.Using Bitwise XOR Operator

# Swapping using bitwise XOR (works only for integers)
a = 70
b = 80

print("Before Swapping:")
print("a =", a, ", b =", b)

# Step 1: XOR a and b, store in a
a = a ^ b

# Step 2: XOR new a with b to get original a, store in b
b = a ^ b

# Step 3: XOR new a with new b to get original b, store in a
a = a ^ b

print("After Swapping using XOR:")
print("a =", a, ", b =", b)

#--------------------------------------------------------------------------------------------------
#10 real-world Python problems that are commonly used in interviews and based on basic concepts
#--------------------------------------------------------------------------------------------------

#1. Sum of Two Numbers
# Problem: Take two numbers from the user and print their sum.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)


# 2. Area of a Circle
# Problem: Calculate the area of a circle given its radius.
radius = float(input("Enter radius of circle: "))
area = 3.1416 * radius * radius
print("Area of Circle =", area)


#3. Swap Two Numbers
# Problem: Swap two variables and print the result.
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
a, b = b, a
print("After Swapping: a =", a, "b =", b)


# 4. Check Even or Odd
# Problem: Check if a number is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


#5. Simple Interest Calculator
# Problem: Calculate simple interest.
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))
si = (p * r * t) / 100
print("Simple Interest =", si)


#6. Celsius to Fahrenheit Conversion
# Problem: Convert temperature from Celsius to Fahrenheit.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)


#7. Find the Largest of Two Numbers
# Problem: Find the maximum of two numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest is", a)
else:
    print("Largest is", b)


#8. Calculate Total and Average Marks
# Problem: Calculate total and average of marks in 5 subjects.
m1 = int(input("Enter marks in Subject 1: "))
m2 = int(input("Enter marks in Subject 2: "))
m3 = int(input("Enter marks in Subject 3: "))
m4 = int(input("Enter marks in Subject 4: "))
m5 = int(input("Enter marks in Subject 5: "))
total = m1 + m2 + m3 + m4 + m5
average = total / 5
print("Total Marks =", total)
print("Average Marks =", average)


# 9. Calculate the Square and Cube of a Number
# Problem: Find square and cube of a number.
num = int(input("Enter a number: "))
print("Square =", num ** 2)
print("Cube =", num ** 3)


# 10. Check Whether Year is Leap Year or Not
# Problem: Check whether a year is a leap year.
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

