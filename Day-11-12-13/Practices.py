#while Loop

# 1. ATM Pin Validation
pin = ""
while pin != "1234":
    pin = input("Enter 4-digit PIN: ")

# 2. Wait for file to appear
import os
while not os.path.exists("data.txt"):
    print("Waiting for data file...")

# 3. Battery charging check
battery = 10
while battery < 100:
    print("Charging... Battery at", battery, "%")
    battery += 10

# 4. Alarm Clock Countdown
time_left = 5
while time_left > 0:
    print("Alarm ringing in", time_left, "seconds")
    time_left -= 1

# 5. Waiting for exam result
result = None
while result is None:
    result = input("Has the result been announced? (yes/no): ")
    if result.lower() != "yes":
        result = None

# 6. Stock price monitor
price = 100
while price < 110:
    print("Current stock price:", price)
    price += 1

# 7. Typing race
target = "python"
typed = ""
while typed != target:
    typed = input("Type the word 'python': ")

# 8. Repeat until odd number
num = 2
while num % 2 == 0:
    num = int(input("Enter an odd number: "))

# 9. Wait until login success
logged_in = False
while not logged_in:
    user = input("Username: ")
    pwd = input("Password: ")
    if user == "admin" and pwd == "123":
        print("Welcome!")
        logged_in = True

# 10. Download progress
progress = 0
while progress < 100:
    print(f"Downloading... {progress}%")
    progress += 20

# 11. Game life simulation
life = 3
while life > 0:
    print("You have", life, "lives")
    life -= 1

# 12. Water boiling simulation
temp = 90
while temp < 100:
    print("Heating... Current temp:", temp)
    temp += 2

# 13. Wait for internet connection
connected = False
while not connected:
    response = input("Is internet connected? (yes/no): ")
    if response.lower() == "yes":
        connected = True

# 14. Daily push-up counter
count = 0
while count < 20:
    print("Push-up:", count + 1)
    count += 1

# 15. Elevator floor movement
floor = 1
while floor <= 5:
    print("Reaching floor:", floor)
    floor += 1

# 16. Wait for approval
approval = "pending"
while approval != "approved":
    approval = input("Is your form approved? (approved/rejected): ")

# 17. Typing until correct length
text = ""
while len(text) < 5:
    text = input("Enter at least 5 characters: ")

# 18. Retry payment
status = "fail"
while status == "fail":
    status = input("Enter payment status (success/fail): ")

# 19. Loop until score is above 50
score = 0
while score < 50:
    score = int(input("Enter your score: "))

# 20. Wait until pizza is delivered
delivered = False
while not delivered:
    status = input("Is the pizza delivered? (yes/no): ")
    if status.lower() == "yes":
        delivered = True

# 21. Loop until name starts with 'A'
name = ""
while not name.startswith("A"):
    name = input("Enter name starting with A: ")

# 22. Repeat reading until satisfied
response = ""
while response != "done":
    response = input("Are you done reading? (done): ")

# 23. Cleaning task
dirty_dishes = 10
while dirty_dishes > 0:
    print("Cleaning dish:", dirty_dishes)
    dirty_dishes -= 1

# 24. Security check
access = "denied"
while access != "granted":
    access = input("Enter access code: ")

# 25. OTP verification
otp = ""
while otp != "5678":
    otp = input("Enter OTP: ")

# 26. Search until item found
found = False
attempts = 0
while not found:
    item = input("Search item (type 'phone' to stop): ")
    attempts += 1
    if item == "phone":
        found = True
print("Found after", attempts, "tries")

# 27. Retry quiz until correct answer
answer = ""
while answer.lower() != "paris":
    answer = input("Capital of France? ")

# 28. Login attempts max 3
tries = 0
while tries < 3:
    pwd = input("Enter password: ")
    if pwd == "admin":
        break
    tries += 1

# 29. Wait until printer is ready
printer = "offline"
while printer != "ready":
    printer = input("Is printer ready? (ready/offline): ")

# 30. Run until energy is depleted
energy = 10
while energy > 0:
    print("Running... Energy left:", energy)
    energy -= 2

#Simulated do-while Loop in Python(Executed at least once using while True: and break)

# 1. Ask age until valid
while True:
    age = int(input("Enter your age: "))
    if age > 0:
        break

# 2. Email validation
while True:
    email = input("Enter your email: ")
    if "@" in email and "." in email:
        print("Valid email")
        break

# 3. Ask for movie rating (1 to 5)
while True:
    rating = int(input("Rate the movie (1-5): "))
    if 1 <= rating <= 5:
        break

# 4. Accept terms and conditions
while True:
    agree = input("Do you accept terms? (yes/no): ").lower()
    if agree == "yes":
        print("Accepted")
        break

# 5. Confirm food order
while True:
    confirm = input("Confirm your order (yes): ")
    if confirm.lower() == "yes":
        print("Order placed")
        break

# 6. Ask name with at least 3 characters
while True:
    name = input("Enter your name: ")
    if len(name) >= 3:
        break

# 7. Select correct menu option
while True:
    option = input("1. Start Game\n2. Exit\nChoose: ")
    if option == "2":
        print("Exiting...")
        break

# 8. Ask for integer only
while True:
    try:
        num = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Invalid input")

# 9. Ask to retry file upload
while True:
    retry = input("Retry upload? (yes/no): ")
    if retry == "no":
        break

# 10. Payment confirmation
while True:
    paid = input("Payment successful? (yes): ")
    if paid == "yes":
        print("Transaction done")
        break

# 11. Enter password at least 6 chars
while True:
    pwd = input("Enter password: ")
    if len(pwd) >= 6:
        break

# 12. Enter OTP until 4 digits
while True:
    otp = input("Enter 4-digit OTP: ")
    if len(otp) == 4 and otp.isdigit():
        break

# 13. Exit simulation with keyword
while True:
    cmd = input("Type 'exit' to quit: ")
    if cmd == "exit":
        break

# 14. Ask for correct city
while True:
    city = input("Enter capital of India: ")
    if city.lower() == "delhi":
        break

# 15. Roll a dice until 6
import random
while True:
    roll = random.randint(1, 6)
    print("Rolled:", roll)
    if roll == 6:
        break

# 16. Simulate app loading
while True:
    print("Loading...")
    ready = input("Is app ready? (yes): ")
    if ready == "yes":
        break

# 17. Unlock with secret code
while True:
    code = input("Enter secret code: ")
    if code == "alpha123":
        print("Unlocked")
        break

# 18. Number must be positive
while True:
    num = float(input("Enter a positive number: "))
    if num > 0:
        break

# 19. Confirm profile details
while True:
    confirm = input("Are your details correct? (yes): ")
    if confirm == "yes":
        break

# 20. Ask for valid PIN (4 digits)
while True:
    pin = input("Enter 4-digit PIN: ")
    if len(pin) == 4 and pin.isdigit():
        break

# 21. Ask until fruit name is entered
while True:
    item = input("Enter any fruit name: ")
    if item.lower() in ["apple", "banana", "mango"]:
        break

# 22. Enter non-empty name
while True:
    name = input("Enter your full name: ")
    if name.strip() != "":
        break

# 23. Ask for confirmation to delete
while True:
    confirm = input("Confirm delete (Y/N): ")
    if confirm.upper() == "Y":
        break

# 24. Get feedback comment
while True:
    feedback = input("Give your feedback (min 10 chars): ")
    if len(feedback) >= 10:
        break

# 25. Loop until balance is enough
while True:
    balance = float(input("Enter account balance: "))
    if balance >= 500:
        print("Sufficient balance")
        break

# 26. Ask for email until Gmail
while True:
    email = input("Enter Gmail address: ")
    if "@gmail.com" in email:
        break

# 27. Quiz answer loop
while True:
    ans = input("Which language is this? (Python): ")
    if ans.lower() == "python":
        break

# 28. Resume or quit
while True:
    decision = input("Do you want to resume? (y/n): ")
    if decision.lower() == "n":
        break

# 29. Ask for yes/no with retry
while True:
    choice = input("Do you like this app? (yes/no): ")
    if choice in ["yes", "no"]:
        break

# 30. Order confirmation loop
while True:
    order = input("Confirm order (confirm/cancel): ")
    if order == "confirm":
        print("Order confirmed")
        break


# for Loop (Iterating with range, sequences, strings, simple automation, etc.)

# 1. Print days of the week
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for day in days:
    print("Day:", day)

# 2. Print characters in a password
password = "Secret123"
for ch in password:
    print("*", end="")

# 3. Countdown timer
for sec in range(10, 0, -1):
    print("Time left:", sec)

# 4. Print first 10 square numbers
for i in range(1, 11):
    print("Square of", i, "is", i ** 2)

# 5. Print top 5 movie names
movies = ["Inception", "Avatar", "Titanic", "Interstellar", "Joker"]
for m in movies:
    print("Movie:", m)

# 6. Loop over order IDs
order_ids = [101, 102, 103, 104]
for oid in order_ids:
    print("Processing order:", oid)

# 7. Loop to show employee salaries
salaries = [30000, 42000, 28000, 35000]
for s in salaries:
    print("Salary:", s)

# 8. Loop through class roll numbers
for roll in range(1, 6):
    print("Roll no:", roll)

# 9. Count total from transaction list
transactions = [100, -50, 200, -30]
total = 0
for t in transactions:
    total += t
print("Net amount:", total)

# 10. Loop through month numbers
for month in range(1, 13):
    print("Month:", month)

# 11. Loop to simulate ATM cash withdrawal attempts
for attempt in range(1, 4):
    pin = input("Attempt " + str(attempt) + ": Enter PIN: ")
    if pin == "1234":
        print("Access granted")
        break

# 12. Print all vowels in a string
text = "application"
for letter in text:
    if letter in "aeiou":
        print("Vowel:", letter)

# 13. Loop over user emails
emails = ["a@gmail.com", "b@yahoo.com", "c@outlook.com"]
for e in emails:
    print("Email sent to:", e)

# 14. Print ASCII values of letters
for ch in "ABCD":
    print(f"{ch} = {ord(ch)}")

# 15. Loop through product ratings
ratings = [5, 4, 3, 5, 2]
for r in ratings:
    print("Rating:", "⭐" * r)

# 16. List all even numbers from 1 to 20
for i in range(2, 21, 2):
    print(i)

# 17. Print multiplication table of 7
for i in range(1, 11):
    print("7 x", i, "=", 7 * i)

# 18. Loop through top trending hashtags
hashtags = ["#AI", "#Python", "#Startup", "#Tech"]
for tag in hashtags:
    print("Trending:", tag)

# 19. Print list of years from 2000 to 2024
for year in range(2000, 2025):
    print(year)

# 20. Print total characters in each word
sentence = "Python is amazing"
for word in sentence.split():
    print(word, "has", len(word), "letters")

# 21. Simulate 3 train announcements
for i in range(3):
    print("Train arriving at platform", i + 1)

# 22. Show list of eligible students
marks = [76, 45, 88, 30, 92]
for m in marks:
    if m >= 50:
        print("Eligible:", m)

# 23. Show items in shopping cart
cart = ["Shoes", "Jeans", "T-shirt"]
for item in cart:
    print("Cart Item:", item)

# 24. Print menu with numbers
menu = ["Pizza", "Burger", "Pasta"]
for i in range(len(menu)):
    print(f"{i+1}. {menu[i]}")

# 25. List stock prices in rupees
prices = [123.5, 127.9, 129.3]
for p in prices:
    print("₹", p)

# 26. Print all digits in number
number = 4562
for digit in str(number):
    print(digit)

# 27. Count positive feedbacks
feedbacks = [1, 0, 1, 1, 0]
count = 0
for fb in feedbacks:
    if fb == 1:
        count += 1
print("Positive reviews:", count)

# 28. Alert user for unread notifications
unread = ["Msg1", "Msg2", "Msg3"]
for note in unread:
    print("New message:", note)

# 29. Print all prime numbers from 1 to 20
for num in range(2, 21):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print("Prime:", num)

# 30. Simulate loading progress
for percent in range(0, 101, 20):
    print(f"Loading... {percent}%")


#using for Loop over Collections (Lists, Tuples, Sets, Dicts, Strings)

# 1. Loop through student names
students = ["Anuj", "Meera", "Kabir"]
for name in students:
    print("Present:", name)

# 2. Loop through tuple of temperatures
temps = (30.5, 32.1, 29.0, 28.7)
for t in temps:
    print("Temp:", t)

# 3. Loop through a dictionary of book prices
books = {"Python": 450, "C++": 400, "Java": 500}
for book, price in books.items():
    print(f"{book} = ₹{price}")

# 4. Loop through shopping cart set
cart_items = {"shoes", "shirt", "jeans"}
for item in cart_items:
    print("Cart contains:", item)

# 5. Loop through characters of a password
password = "MySecret"
for ch in password:
    print("*", end="")

# 6. Loop through bank accounts with balances
accounts = {"A101": 5000, "A102": 12000, "A103": 8000}
for acc, bal in accounts.items():
    print(f"Account {acc} → Balance: ₹{bal}")

# 7. Loop through a list of website URLs
urls = ["google.com", "github.com", "linkedin.com"]
for site in urls:
    print("Opening:", site)

# 8. Loop through tuple of subject scores
scores = (88, 77, 92, 85)
for score in scores:
    print("Score:", score)

# 9. Loop through dict to show employee departments
departments = {"Ram": "HR", "Shyam": "IT", "Geeta": "Finance"}
for emp, dept in departments.items():
    print(emp, "→", dept)

# 10. Loop through string of phone number
phone = "9876543210"
for digit in phone:
    print(digit, end=" ")

# 11. Iterate over set of countries
countries = {"India", "USA", "Germany", "Canada"}
for country in countries:
    print("Visited:", country)

# 12. Loop over names and print in uppercase
names = ["ravi", "komal", "ishaan"]
for name in names:
    print(name.upper())

# 13. Loop over dictionary keys
flight_schedule = {"Indigo": "9:00 AM", "Air India": "12:30 PM"}
for airline in flight_schedule:
    print("Flight:", airline)

# 14. Loop through letters of a username
username = "AlphaUser"
for ch in username:
    print(ch)

# 15. Loop through mobile app icons list
apps = ["Instagram", "YouTube", "Twitter"]
for app in apps:
    print("Opening app:", app)

# 16. Loop through set of unique customer IDs
customer_ids = {"C101", "C102", "C103"}
for cid in customer_ids:
    print("Customer ID:", cid)

# 17. Loop through dictionary of student marks
student_marks = {"Aman": 80, "Kriti": 95, "Tina": 89}
for student, mark in student_marks.items():
    print(f"{student} scored {mark}")

# 18. Loop over grocery list
groceries = ["milk", "eggs", "bread", "fruits"]
for item in groceries:
    print("Buy:", item)

# 19. Loop over tuple of login attempts
login_attempts = (1, 2, 3)
for attempt in login_attempts:
    print("Attempt", attempt)

# 20. Loop through dict with nested list
students = {"Ravi": [70, 80], "Kiran": [85, 90]}
for name, marks in students.items():
    print(name, "→", marks)

# 21. Loop over brand names in a set
brands = {"Nike", "Puma", "Adidas"}
for brand in brands:
    print("Brand:", brand)

# 22. Loop through characters and count vowels
text = "Application"
for ch in text:
    if ch.lower() in "aeiou":
        print("Vowel found:", ch)

# 23. Loop through employee dict and print initials
employees = {"Amit Kumar": "HR", "Sunita Jain": "Admin"}
for emp in employees:
    initials = ''.join([x[0] for x in emp.split()])
    print(initials)

# 24. Loop over data packages
data_plans = [1.5, 2, 3, 5]  # GB
for plan in data_plans:
    print(f"{plan}GB plan available")

# 25. Loop through string to count digits
data = "user123profile456"
for ch in data:
    if ch.isdigit():
        print("Digit:", ch)

# 26. Loop through tags in social media post
tags = ["#fitness", "#workout", "#goals"]
for tag in tags:
    print("Tag:", tag)

# 27. Loop through file extensions
extensions = [".jpg", ".png", ".pdf"]
for ext in extensions:
    print("Supported format:", ext)

# 28. Loop through subjects to mark attendance
subjects = ["Math", "Science", "English"]
for sub in subjects:
    print("Attendance marked for:", sub)

# 29. Loop through list of installed apps
installed_apps = ["Zoom", "Slack", "Notion"]
for app in installed_apps:
    print("Launching:", app)

# 30. Loop through a string and reverse it
name = "Shalini"
for ch in reversed(name):
    print(ch, end="")


# using Nested Loops in Python

# 1. Print 2D matrix
matrix = [[1, 2], [3, 4], [5, 6]]
for row in matrix:
    for col in row:
        print(col, end=' ')
    print()

# 2. Print multiplication table (1 to 5)
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i}×{j}={i*j}", end='\t')
    print()

# 3. Print star pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# 4. Print right-aligned triangle
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()

# 5. Compare elements of two lists
a = [10, 20, 30]
b = [15, 25, 35]
for i in a:
    for j in b:
        print(f"{i} vs {j}")

# 6. Print all possible coordinate pairs
for x in range(3):
    for y in range(3):
        print(f"({x},{y})", end=' ')
    print()

# 7. Print lowercase and uppercase combinations
for lower in ['a', 'b']:
    for upper in ['A', 'B']:
        print(lower + upper)

# 8. Employee-wise project-wise status
employees = ["Ravi", "Kiran"]
projects = ["ProjectA", "ProjectB"]
for emp in employees:
    for proj in projects:
        print(f"{emp} working on {proj}")

# 9. Print digital clock (hours:minutes)
for hour in range(1, 3):
    for minute in range(0, 60, 30):
        print(f"{hour}:{minute:02d}")

# 10. Find common elements between two lists
list1 = [1, 2, 3]
list2 = [2, 3, 4]
for i in list1:
    for j in list2:
        if i == j:
            print("Common:", i)

# 11. Generate combinations of toppings
pizzas = ["Veg", "Cheese"]
toppings = ["Mushroom", "Olives"]
for p in pizzas:
    for t in toppings:
        print(f"{p} + {t}")

# 12. Display month-wise day-wise schedule
months = ["Jan", "Feb"]
days = [1, 2]
for m in months:
    for d in days:
        print(f"Schedule: {m} {d}")

# 13. Print characters of multiple strings
words = ["Hi", "Go"]
for word in words:
    for ch in word:
        print(ch)

# 14. Student-wise subject-wise marks
students = ["Maya", "Kabir"]
subjects = ["Math", "Science"]
for s in students:
    for sub in subjects:
        print(f"{s} → {sub} marks recorded")

# 15. Nested list iteration
data = [[100, 200], [300, 400]]
for outer in data:
    for value in outer:
        print(value)

# 16. Count matching characters between two strings
s1 = "abc"
s2 = "bcd"
for i in s1:
    for j in s2:
        if i == j:
            print(f"Common char: {i}")

# 17. Room-wise guest names
rooms = {"Room1": ["Anu", "Meena"], "Room2": ["Kabir"]}
for room, guests in rooms.items():
    for guest in guests:
        print(room, "→", guest)

# 18. Nested loop with break
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print(i, j)

# 19. Print pairings of students
students = ["A", "B", "C"]
for i in students:
    for j in students:
        if i != j:
            print(i, "with", j)

# 20. Count vowel pairs
vowels = "aeiou"
for v1 in vowels:
    for v2 in vowels:
        print(v1 + v2)

# 21. Print all 2-letter codes from alphabets
alphabets = ['A', 'B', 'C']
for a in alphabets:
    for b in alphabets:
        print(a + b)

# 22. Tabular data (rows & columns)
for row in range(3):
    for col in range(4):
        print(f"{row},{col}", end="  ")
    print()

# 23. Combine two arrays to form tuples
a = [1, 2]
b = ['x', 'y']
for i in a:
    for j in b:
        print((i, j))

# 24. Loop through list of dictionaries
users = [{"name": "Anu"}, {"name": "Kabir"}]
for user in users:
    for key in user:
        print(key, "→", user[key])

# 25. Comparing each student with others
students = ["Riya", "Mehul", "Tina"]
for s1 in students:
    for s2 in students:
        if s1 != s2:
            print(f"{s1} compared with {s2}")

# 26. Time slots for interview schedule
hours = [9, 10]
minutes = [0, 30]
for h in hours:
    for m in minutes:
        print(f"Time slot: {h}:{m:02d}")

# 27. Multiplication of 2x3 matrix with scalar
matrix = [[1, 2, 3], [4, 5, 6]]
scalar = 2
for row in matrix:
    for i in range(len(row)):
        row[i] *= scalar
print(matrix)

# 28. Pattern of alphabets
for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end="")
    print()

# 29. Print upper triangle matrix form
n = 3
for i in range(n):
    for j in range(n):
        if j >= i:
            print("1", end=" ")
        else:
            print(" ", end=" ")
    print()

# 30. Check which subjects are taught by which teachers
teachers = {"Ms.A": ["Math", "Science"], "Mr.B": ["English"]}
for t, subs in teachers.items():
    for sub in subs:
        print(f"{t} teaches {sub}")


#  Using break Statement in Python

# 1. Stop when PIN is correct
for i in range(3):
    pin = input("Enter PIN: ")
    if pin == "1234":
        print("Access granted.")
        break
    else:
        print("Wrong PIN.")

# 2. Find first even number
nums = [1, 3, 5, 8, 9]
for n in nums:
    if n % 2 == 0:
        print("First even:", n)
        break

# 3. Stop countdown when user cancels
for i in range(10, 0, -1):
    cancel = input("Type 'stop' to cancel countdown or press Enter to continue: ")
    if cancel == "stop":
        print("Countdown stopped.")
        break
    print("Time left:", i)

# 4. Break on duplicate name
names = ["Alice", "Bob", "Charlie", "Bob", "Eve"]
seen = set()
for n in names:
    if n in seen:
        print("Duplicate name found:", n)
        break
    seen.add(n)

# 5. ATM pin entry
for _ in range(3):
    pin = input("Enter your PIN: ")
    if pin == "7890":
        print("Transaction allowed.")
        break
    else:
        print("Try again.")

# 6. Stop loop if item is out of stock
items = ["Soap", "Shampoo", "Toothpaste", "OutOfStock", "Lotion"]
for item in items:
    if item == "OutOfStock":
        print("Item out of stock! Stopping...")
        break
    print("Packing:", item)

# 7. Find a student with score above 90
scores = [70, 85, 92, 88]
for s in scores:
    if s > 90:
        print("Topper found:", s)
        break

# 8. Stop searching product after 5 attempts
for i in range(1, 6):
    found = input(f"Search attempt {i}: Did you find the product? (yes/no): ")
    if found.lower() == "yes":
        print("Product found.")
        break

# 9. Exit when first negative value found
nums = [5, 8, 10, -3, 6]
for n in nums:
    if n < 0:
        print("Negative value:", n)
        break

# 10. Stop loop if username already exists
usernames = ["rahul", "kavita", "mahi", "rahul"]
unique = set()
for name in usernames:
    if name in unique:
        print("Username already exists:", name)
        break
    unique.add(name)

# 11. Stop checking files once virus found
files = ["doc1", "doc2", "virus", "doc4"]
for f in files:
    if f == "virus":
        print("Infected file found!")
        break
    print("Safe file:", f)

# 12. Stop login attempts on success
attempts = 0
while attempts < 5:
    user = input("Enter username: ")
    if user == "admin":
        print("Login successful.")
        break
    print("Incorrect username.")
    attempts += 1

# 13. Stop loop on empty string
while True:
    word = input("Enter a word (or press Enter to stop): ")
    if word == "":
        print("Stopped input.")
        break
    print("You entered:", word)

# 14. Stop when battery low
battery_levels = [100, 80, 60, 30, 10, 5]
for level in battery_levels:
    print("Battery:", level, "%")
    if level <= 10:
        print("Battery low! Stopping tasks.")
        break

# 15. Search for a keyword in paragraph
paragraph = ["This is a book.", "This is a pen.", "Keyword found here.", "Another line"]
for line in paragraph:
    if "Keyword" in line:
        print("Found:", line)
        break

# 16. Exit when secret word is guessed
secret = "apple"
while True:
    guess = input("Guess the word: ")
    if guess == secret:
        print("Correct guess!")
        break

# 17. Break on invalid input
inputs = ["10", "25", "abc", "40"]
for i in inputs:
    if not i.isdigit():
        print("Invalid input:", i)
        break
    print("Valid:", i)

# 18. Exit when target reached
targets = [2, 4, 8, 16]
for t in targets:
    print("Checking:", t)
    if t == 8:
        print("Target found!")
        break

# 19. Check if number is prime (use break if divisible)
num = 29
for i in range(2, num):
    if num % i == 0:
        print("Not prime")
        break
else:
    print("Prime")

# 20. Stop processing faulty transaction
transactions = [100, 200, -999, 300]
for t in transactions:
    if t < 0:
        print("Invalid transaction:", t)
        break
    print("Processed:", t)

# 21. End loop if customer cancels
customers = ["Amit", "Neha", "Cancel", "Priya"]
for c in customers:
    if c == "Cancel":
        print("Customer cancelled the order.")
        break
    print("Processing:", c)

# 22. Stop robot if obstacle detected
for step in range(1, 10):
    obstacle = input("Obstacle at step " + str(step) + "? (yes/no): ")
    if obstacle == "yes":
        print("Stopping robot!")
        break

# 23. Stop email sending on error
emails = ["sent", "sent", "error", "sent"]
for status in emails:
    if status == "error":
        print("Email sending failed.")
        break

# 24. Stop OTP verification on success
for _ in range(5):
    otp = input("Enter OTP: ")
    if otp == "123456":
        print("Verified.")
        break
    else:
        print("Incorrect OTP")

# 25. Break on high temperature
temps = [98, 99.5, 101, 97]
for temp in temps:
    if temp > 100:
        print("Fever detected:", temp)
        break

# 26. Break when parking is full
parking = [True, True, False, True]
for slot in parking:
    if not slot:
        print("Parking full.")
        break

# 27. Break when passcode is matched
codes = [4321, 9999, 1234]
for c in codes:
    if c == 1234:
        print("Passcode matched.")
        break

# 28. Stop train simulation on signal
signals = ["green", "green", "red", "green"]
for s in signals:
    print("Signal:", s)
    if s == "red":
        print("Train stopped.")
        break

# 29. Stop machine on critical error
statuses = ["running", "running", "critical", "running"]
for s in statuses:
    if s == "critical":
        print("Error! Stop machine.")
        break

# 30. Stop app install on fail
apps = ["Installed", "Installed", "Failed", "Installed"]
for a in apps:
    if a == "Failed":
        print("Installation failed. Stopping process.")
        break
    print("Installed:", a)


# 7. continue Statement

# 1. Skip even numbers
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"Odd Number: {i}")

# 2. Skip blank names
names = ["John", "", "Alice", " "]
for name in names:
    if name.strip() == "":
        continue
    print(f"Valid Name: {name}")

# 3. Skip out-of-stock items
items = [{"name": "Milk", "stock": 0}, {"name": "Eggs", "stock": 12}]
for item in items:
    if item["stock"] == 0:
        continue
    print(f"{item['name']} is available")

# 4. Skip zero salary employees
salaries = [25000, 0, 40000, 5000]
for salary in salaries:
    if salary == 0:
        continue
    print(f"Salary Processed: ₹{salary}")

# 5. Skip cancelled orders
orders = ["Order1", "Cancelled", "Order2"]
for order in orders:
    if order == "Cancelled":
        continue
    print(f"Processing {order}")

# 6. Skip failed students
marks = {"Ajay": 75, "Sunita": 30, "Ravi": 90}
for name, mark in marks.items():
    if mark < 40:
        continue
    print(f"{name} passed with {mark} marks")

# 7. Skip non-txt files
files = ["report.docx", "summary.txt", "data.csv", "notes.txt"]
for file in files:
    if not file.endswith(".txt"):
        continue
    print(f"Text File: {file}")

# 8. Skip students with 0 assignments
assignments = {"Neha": 3, "Karan": 0, "Isha": 2}
for student, count in assignments.items():
    if count == 0:
        continue
    print(f"{student} submitted {count} assignments")

# 9. Skip negative balances
balances = [1500, -200, 800, -50, 1200]
for balance in balances:
    if balance < 0:
        continue
    print(f"Valid balance: ₹{balance}")

# 10. Skip unverified users
users = [{"name": "Raj", "verified": True}, {"name": "Simran", "verified": False}]
for user in users:
    if not user["verified"]:
        continue
    print(f"Welcome, {user['name']}")

# 11. Skip even-indexed characters
text = "ContinueExample"
for i in range(len(text)):
    if i % 2 == 0:
        continue
    print(text[i], end=" ")

# 12. Skip temperatures below freezing
temps = [25, -3, 14, -10, 30]
for t in temps:
    if t < 0:
        continue
    print(f"Safe Temperature: {t}°C")

# 13. Skip empty lines in a file
lines = ["Data line 1", "", "Data line 2", " "]
for line in lines:
    if line.strip() == "":
        continue
    print(f"Line: {line}")

# 14. Skip weekends
days = ["Mon", "Tue", "Sat", "Sun", "Wed"]
for day in days:
    if day in ["Sat", "Sun"]:
        continue
    print(f"Working day: {day}")

# 15. Skip small expenses
expenses = [1200, 50, 7000, 30, 500]
for amount in expenses:
    if amount < 100:
        continue
    print(f"Recorded expense: ₹{amount}")

# 16. Skip invalid ages
ages = [25, -1, 30, 0, 45]
for age in ages:
    if age <= 0:
        continue
    print(f"Valid Age: {age}")

# 17. Skip duplicate names
names = ["Alice", "Bob", "Alice", "John"]
seen = set()
for name in names:
    if name in seen:
        continue
    seen.add(name)
    print(f"Unique name: {name}")

# 18. Skip uncompleted tasks
tasks = [{"title": "Task1", "done": True}, {"title": "Task2", "done": False}]
for task in tasks:
    if not task["done"]:
        continue
    print(f"Completed: {task['title']}")

# 19. Skip underage voters
ages = [15, 18, 21, 12]
for age in ages:
    if age < 18:
        continue
    print(f"Eligible voter age: {age}")

# 20. Skip invalid email addresses
emails = ["user@example.com", "invalid@", "@domain.com", "valid@mail.com"]
for email in emails:
    if "@" not in email or email.startswith("@"):
        continue
    print(f"Valid email: {email}")

# 21. Skip products with no price
products = [{"name": "Pen", "price": 10}, {"name": "Notebook", "price": 0}]
for p in products:
    if p["price"] <= 0:
        continue
    print(f"Available product: {p['name']}")

# 22. Skip files starting with temp
files = ["temp1.tmp", "main.py", "temp2.log", "script.py"]
for f in files:
    if f.startswith("temp"):
        continue
    print(f"Loaded file: {f}")

# 23. Skip values greater than 100
values = [45, 102, 99, 120]
for v in values:
    if v > 100:
        continue
    print(f"Accepted value: {v}")

# 24. Skip fruits that start with "B"
fruits = ["Apple", "Banana", "Cherry", "Blueberry"]
for fruit in fruits:
    if fruit.startswith("B"):
        continue
    print(f"Eating: {fruit}")

# 25. Skip odd numbers in range
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(f"Even Number: {i}")

# 26. Skip already vaccinated people
people = [{"name": "Kiran", "vaccinated": True}, {"name": "Anu", "vaccinated": False}]
for p in people:
    if p["vaccinated"]:
        continue
    print(f"{p['name']} needs vaccination")

# 27. Skip tasks with no deadline
tasks = [{"name": "Build App", "deadline": None}, {"name": "Deploy App", "deadline": "2025-08-01"}]
for t in tasks:
    if t["deadline"] is None:
        continue
    print(f"Task with deadline: {t['name']}")

# 28. Skip scores below 50
scores = [45, 60, 30, 80]
for score in scores:
    if score < 50:
        continue
    print(f"Passed with score: {score}")

# 29. Skip lower case vowels
word = "DataAnalytics"
for ch in word:
    if ch in "aeiou":
        continue
    print(ch, end=" ")

# 30. Skip sites with no HTTPS
urls = ["http://abc.com", "https://secure.com", "http://xyz.com"]
for url in urls:
    if not url.startswith("https://"):
        continue
    print(f"Secure Site: {url}")


#8. else with Loops

# Example 1: Simple for-else
for i in range(3):
    print("Running loop:", i)
else:
    print("Loop finished successfully\n")

# Example 2: Check if number is prime
num = 7
for i in range(2, num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime Number\n")

# Example 3: Search item in list
items = ["pen", "book", "scale"]
for item in items:
    if item == "eraser":
        print("Eraser found")
        break
else:
    print("Eraser not found\n")

# Example 4: While-else loop
i = 0
while i < 3:
    print("i =", i)
    i += 1
else:
    print("While loop completed\n")

# Example 5: Loop with break and else
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed without break\n")

# Example 6: Password attempts
passwords = ["pass1", "pass2", "admin"]
for pwd in passwords:
    if pwd == "admin":
        print("Access Granted")
        break
else:
    print("Access Denied\n")

# Example 7: Check if string has digits
s = "Hello123"
for ch in s:
    if ch.isdigit():
        print("Contains Digit")
        break
else:
    print("No Digits Found\n")

# Example 8: Check if all even
nums = [2, 4, 6, 8]
for n in nums:
    if n % 2 != 0:
        print("Found odd number")
        break
else:
    print("All are even\n")

# Example 9: While-else without break
n = 1
while n <= 3:
    print("Count", n)
    n += 1
else:
    print("No interruption\n")

# Example 10: Check if username is taken
usernames = ["john", "alex", "maya"]
for name in usernames:
    if name == "maya":
        print("Username already taken")
        break
else:
    print("Username available\n")

# Example 11: Find multiple of 5
data = [3, 8, 10, 14]
for val in data:
    if val % 5 == 0:
        print("Found a multiple of 5")
        break
else:
    print("No multiple of 5 found\n")

# Example 12: Empty list check
numbers = []
for n in numbers:
    print(n)
else:
    print("List is empty\n")

# Example 13: All positive check
values = [1, 3, 7]
for v in values:
    if v < 0:
        break
else:
    print("All numbers are positive\n")

# Example 14: For-else with dictionary
info = {"a": 1, "b": 2}
for key in info:
    if key == "c":
        print("Found")
        break
else:
    print("Key not found\n")

# Example 15: Password length check
passwords = ["123", "admin12", "longpass"]
for pwd in passwords:
    if len(pwd) > 6:
        print("Strong password found")
        break
else:
    print("All passwords are weak\n")

# Example 16: While-else with break
x = 1
while x <= 5:
    if x == 3:
        break
    print(x)
    x += 1
else:
    print("Completed\n")

# Example 17: Validate score
scores = [55, 89, 60]
for s in scores:
    if s < 40:
        print("Fail detected")
        break
else:
    print("All passed\n")

# Example 18: Detect vowel in word
word = "sky"
for ch in word:
    if ch in "aeiou":
        print("Vowel found")
        break
else:
    print("No vowels\n")

# Example 19: For-else with input
inputs = ["a", "b", "c"]
for val in inputs:
    if val == "x":
        print("Found x")
        break
else:
    print("x not found\n")

# Example 20: Check for duplicates
ids = [101, 102, 103, 101]
for i in range(len(ids)):
    if ids[i] in ids[i+1:]:
        print("Duplicate found")
        break
else:
    print("No duplicates\n")

# Example 21: Check if student absent
students = ["Ajay", "Neha", "Ravi"]
for s in students:
    if s == "Deepa":
        print("Deepa present")
        break
else:
    print("Deepa absent\n")

# Example 22: Search city in list
cities = ["Delhi", "Mumbai", "Lucknow"]
for c in cities:
    if c == "Pune":
        print("City found")
        break
else:
    print("City not found\n")

# Example 23: All items in stock
inventory = [5, 10, 8, 0]
for item in inventory:
    if item == 0:
        print("Out of stock item found")
        break
else:
    print("All items available\n")

# Example 24: All items below limit
weights = [45, 50, 55]
for w in weights:
    if w > 60:
        print("Overweight item")
        break
else:
    print("All within limit\n")

# Example 25: While-else no break
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Normal exit\n")

# Example 26: All passwords are different
passwords = ["123", "abc", "xyz"]
for p in range(len(passwords)):
    if passwords[p] in passwords[p+1:]:
        print("Duplicate password")
        break
else:
    print("All passwords are unique\n")

# Example 27: Detect uppercase
text = "hello"
for ch in text:
    if ch.isupper():
        print("Uppercase found")
        break
else:
    print("All lowercase\n")

# Example 28: Check if divisible by 7
nums = [5, 14, 21, 10]
for n in nums:
    if n % 7 == 0:
        print("Divisible by 7")
        break
else:
    print("No divisible number\n")

# Example 29: While-else to count down
n = 3
while n > 0:
    print("Counting down:", n)
    n -= 1
else:
    print("Countdown complete\n")

# Example 30: Detect lowercase vowel in sentence
sentence = "WELCOME"
for ch in sentence:
    if ch in "aeiou":
        print("Lowercase vowel found")
        break
else:
    print("No lowercase vowels\n")


