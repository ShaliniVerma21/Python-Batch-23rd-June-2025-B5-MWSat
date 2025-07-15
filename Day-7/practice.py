#Section 1: Defining a Tuple 

# Tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')
print(vowels)

# Tuple of 5 odd numbers
odds = (1, 3, 5, 7, 9)
print(odds)

# Tuple with different currencies
currencies = ("USD", "INR", "EUR", "JPY")
print(currencies)

# Tuple of names
names = ("Amit", "Sara", "Zoya", "Rahul")
print(names)

# Tuple of booleans
flags = (True, False, True, False)
print(flags)

# Tuple from user input (age)
age = int(input("Enter your age: "))
user_info = ("User", age)
print(user_info)

# Tuple with square of numbers
squares = (1*1, 2*2, 3*3, 4*4)
print(squares)

# Tuple storing one value (with comma)
one_val = ("Data",)
print(one_val)

# Tuple of ASCII values
ascii_vals = (ord('A'), ord('B'), ord('C'))
print(ascii_vals)

# Tuple of mixed sports
sports = ("Cricket", "Chess", "Football", "Tennis")
print(sports)

# Tuple of planets
planets = ("Mercury", "Venus", "Earth", "Mars")
print(planets)

# Tuple with temperature readings
temps = (28.3, 32.0, 25.6, 30.1)
print(temps)

# Tuple with Python keywords
keywords = ("if", "else", "while", "for")
print(keywords)

# Tuple of even numbers
evens = tuple(range(2, 12, 2))
print(evens)

# Tuple from split string
sentence = "Python is fun"
words = tuple(sentence.split())
print(words)

# Tuple with formatted strings
version = (f"Python {3}.{10}",)
print(version)

# Tuple with mobile brands
brands = ("Samsung", "Apple", "OnePlus")
print(brands)

# Tuple with boolean conditions
results = (5 > 3, 2 == 4, not False)
print(results)

# Tuple of prime numbers
primes = (2, 3, 5, 7, 11)
print(primes)

# Tuple with currency conversion rates
rates = (83.25, 0.91, 110.0)
print(rates)

# Tuple from characters
chars = tuple("DATA")
print(chars)

# Tuple of city names
cities = ("Delhi", "Mumbai", "Chennai", "Kolkata")
print(cities)

# Tuple with age group brackets
age_groups = ("0-10", "11-18", "19-30", "31-50", "50+")
print(age_groups)

# Tuple of color shades
shades = ("Light Blue", "Dark Green", "Bright Red")
print(shades)

# Tuple with values from multiple input
name = input("Enter your name: ")
score = int(input("Enter your score: "))
result = (name, score)
print(result)


#Section 2: Creating a Tuple

# Tuple from list of subjects
subjects = ["Math", "English", "History"]
subject_tuple = tuple(subjects)
print(subject_tuple)

# Tuple from list of marks
marks_list = [80, 90, 88]
marks_tuple = tuple(marks_list)
print(marks_tuple)

# Tuple from input string
data = tuple(input("Enter 5 letters: "))
print(data)

# Tuple from zip of names and scores
names = ["Ali", "Tina"]
scores = [88, 95]
combined = tuple(zip(names, scores))
print(combined)

# Tuple from range of 1 to 5
r = tuple(range(1, 6))
print(r)

# Tuple from boolean results
values = [True, False, True]
bool_tuple = tuple(values)
print(bool_tuple)

# Tuple from float list
floats = [1.5, 2.8, 9.3]
float_tuple = tuple(floats)
print(float_tuple)

# Tuple using multiplication
multiply_result = tuple([i * 2 for i in range(3)])
print(multiply_result)

# Tuple from list of characters
char_list = list("HELLO")
char_tuple = tuple(char_list)
print(char_tuple)

# Tuple of coordinates
coordinates = (15.5, 25.7)
print(coordinates)

# Tuple from year-month-day
date = (2025, 7, 13)
print(date)

# Tuple using slicing
lst = [10, 20, 30, 40, 50]
tpl = tuple(lst[1:4])
print(tpl)

# Tuple using input converted list
items = input("Enter 3 items comma-separated: ").split(',')
items_tpl = tuple(items)
print(items_tpl)

# Tuple from square roots
import math
roots = tuple([math.sqrt(x) for x in [4, 9, 16]])
print(roots)

# Tuple from binary string
binary = tuple(bin(x) for x in range(4))
print(binary)

# Tuple of salaries
salaries = tuple([20000, 30000, 25000])
print(salaries)

# Tuple of email domains
emails = ["abc@gmail.com", "xyz@yahoo.com"]
domains = tuple([email.split('@')[1] for email in emails])
print(domains)

# Tuple of reversed list
rev_list = [1, 2, 3][::-1]
rev_tuple = tuple(rev_list)
print(rev_tuple)

# Tuple from nested list
nested = [[1, 2], [3, 4]]
nested_tpl = tuple([tuple(i) for i in nested])
print(nested_tpl)

# Tuple of month abbreviations
months = tuple("Jan Feb Mar Apr".split())
print(months)

# Tuple of boolean from conditions
nums = [5, 10, 15]
conditions = tuple(n > 10 for n in nums)
print(conditions)

# Tuple from dictionary keys
d = {"a": 1, "b": 2}
keys_tuple = tuple(d.keys())
print(keys_tuple)

# Tuple from dictionary values
values_tuple = tuple(d.values())
print(values_tuple)

# Tuple from string formatting
name = "Shalini"
tpl = (f"Welcome {name}",)
print(tpl)

# Tuple from user-defined list of hobbies
hobbies = input("Enter hobbies: ").split()
print(tuple(hobbies))


#Section 3: Accessing Tuple 

# Access middle item
colors = ("Red", "Green", "Blue", "Yellow", "Pink")
print(colors[len(colors)//2])  # Output: Blue

# Access first and last character from tuple of strings
chars = ("alpha", "beta", "gamma")
print(chars[0][0], chars[-1][-1])

# Access full name from tuple
person = ("Shalini", "Verma")
print("Full Name:", person[0] + " " + person[1])

# Get domain from email tuple
email_info = ("abc@gmail.com",)
print(email_info[0].split('@')[1])

# Iterate using while loop
nums = (10, 20, 30)
i = 0
while i < len(nums):
    print(nums[i])
    i += 1

# Slice last 3 elements
months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun")
print(months[-3:])

# Reverse access using negative index
alphabets = ("A", "B", "C", "D")
print(alphabets[-2])

# Use slicing to get every second item
data = ("a", "b", "c", "d", "e", "f")
print(data[::2])

# Combine access and format
info = ("Shalini", "Trainer", "Python")
print(f"{info[0]} is a {info[1]} expert in {info[2]}.")

# Access nested tuple
college = ("Delhi University", ("BBA", "BCA"))
print(college[1][1])  # Output: BCA

# Access date from timestamp tuple
timestamp = ("13", "July", "2025", "15:00")
print("Date:", timestamp[0], timestamp[1], timestamp[2])

# Print initials from name tuple
name = ("Rahul", "Dev", "Verma")
initials = name[0][0] + name[1][0] + name[2][0]
print(initials)

# Access part of address tuple
address = ("123 Street", "New Delhi", "110001")
print("City:", address[1])

# Access last element
info = ("item1", "item2", "item3")
print(info[-1])

# Check if item exists and access
products = ("Laptop", "Tablet", "Phone")
if "Tablet" in products:
    print("Tablet found at index:", products.index("Tablet"))

# Use tuple in decision making
login_status = (True,)
if login_status[0]:
    print("Login Successful!")

# Use for loop with index
names = ("Amit", "Pooja", "Kabir")
for i in range(len(names)):
    print(f"{i+1}. {names[i]}")

# Concatenate and access
x = ("Hello",)
y = ("World",)
z = x + y
print(z[1])

# Unpack and print one value
record = ("XYZ", 101, "Intern")
_, emp_id, _ = record
print("ID:", emp_id)

# Count specific character from tuple of strings
words = ("apple", "banana", "cherry")
count = sum(w.count('a') for w in words)
print("Count of 'a':", count)

# Access through function
def show_employee(emp):
    print(f"Emp Name: {emp[0]} | Dept: {emp[1]}")

show_employee(("Shalini", "IT"))

# Tuple from multiple slicing patterns
s = ("one", "two", "three", "four", "five")
print(s[1:4])
print(s[:-2])
print(s[::3])

# Tuple with days and access weekends
days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
weekend = days[-2:]
print("Weekend Days:", weekend)

# Dynamic indexing
i = int(input("Enter index 0-3: "))
data = ("India", "USA", "UK", "Canada")
if 0 <= i < len(data):
    print("You selected:", data[i])
else:
    print("Invalid Index")

# Tuple with real-world use (latitude, longitude)
location = (28.6139, 77.2090)
print(f"Latitude: {location[0]}, Longitude: {location[1]}")


#SECTION 4: Tuple Operations

# 1. Tuple Concatenation
t1 = ("Pen", "Pencil")
t2 = ("Eraser",)
stationery = t1 + t2
print(stationery)

# 2. Tuple Repetition
greet = ("Hi",)
print(greet * 3)  # Output: ('Hi', 'Hi', 'Hi')

# 3. Membership Test
skills = ("Python", "SQL", "Excel")
print("SQL" in skills)  # Output: True

# 4. Count Occurrence
nums = (1, 2, 2, 3, 4, 2)
print(nums.count(2))  # Output: 3

# 5. Index of Element
animals = ("cat", "dog", "cow", "dog")
print(animals.index("dog"))  # Output: 1

# 6. Convert List to Tuple
items = ["apple", "banana", "kiwi"]
print(tuple(items))

# 7. Tuple Unpacking
product = ("Laptop", 55000, "Electronics")
name, price, category = product
print(f"{name} costs Rs.{price} in {category} category")

# 8. Nested Tuple Access
employees = (("Rahul", "HR"), ("Shalini", "IT"))
print(employees[0][1])  # Output: HR

# 9. Iterate with index
fruits = ("Mango", "Guava", "Grapes")
for i in range(len(fruits)):
    print(f"Fruit-{i+1}: {fruits[i]}")

# 10. Use len() on tuple
colors = ("Red", "Blue", "Green")
print("Length:", len(colors))

# 11. Combine tuples with numbers
t1 = (1, 2)
t2 = (3, 4)
result = tuple(x + y for x, y in zip(t1, t2))
print(result)

# 12. Get all even numbers from tuple
numbers = (1, 2, 3, 4, 5, 6)
evens = tuple(i for i in numbers if i % 2 == 0)
print(evens)

# 13. Convert String to Tuple
msg = "HELLO"
print(tuple(msg))  # ('H', 'E', 'L', 'L', 'O')

# 14. Remove duplicates using set and convert back to tuple
data = (1, 2, 2, 3, 3, 3)
unique = tuple(set(data))
print(unique)

# 15. Sorting a tuple (convert to list first)
unsorted = (5, 2, 4, 1)
sorted_tuple = tuple(sorted(unsorted))
print(sorted_tuple)

# 16. Reverse a tuple
sample = ("a", "b", "c")
print(sample[::-1])

# 17. Convert tuple to string
words = ("Hello", "World")
sentence = " ".join(words)
print(sentence)

# 18. Compare two tuples
a = (1, 2)
b = (1, 3)
print(a < b)  # Output: True

# 19. Tuple in dictionary key
t = (101, "John")
emp_dict = {t: "Sales"}
print(emp_dict[(101, "John")])

# 20. Slice tuple
nums = (10, 20, 30, 40, 50)
print(nums[1:4])

# 21. Tuple with float conversion
str_nums = ("1.2", "3.4", "5.6")
float_nums = tuple(map(float, str_nums))
print(float_nums)

# 22. Zipping two tuples
names = ("Amit", "Neha")
grades = ("A", "B")
print(tuple(zip(names, grades)))

# 23. Flatten nested tuple
nested = ((1, 2), (3, 4))
flat = tuple(i for pair in nested for i in pair)
print(flat)

# 24. Tuple from multiple ranges
combined = tuple(range(1, 4)) + tuple(range(7, 10))
print(combined)

# 25. Using max() and min()
values = (9, 1, 5, 3)
print("Max:", max(values))
print("Min:", min(values))


#SECTION 5: Immutability

# 1. Trying to modify tuple element
person = ("Amit", 30)
# person[1] = 25  # ❌ Raises TypeError

# 2. Using try-except to show immutability
try:
    person[0] = "Rahul"
except TypeError as e:
    print("Error:", e)

# 3. Appending to tuple is not allowed
t = (1, 2, 3)
# t.append(4)  # ❌ AttributeError

# 4. Deleting tuple element not allowed
# del t[0]  # ❌ TypeError

# 5. Using replace-like behavior (create new tuple)
person = ("John", 25)
person = (person[0], 26)
print(person)

# 6. Tuples inside list can be changed by replacing tuple
data = [("Alice", 1), ("Bob", 2)]
data[0] = ("Alice", 3)
print(data)

# 7. Elements can't be popped
# t.pop()  # ❌ AttributeError

# 8. You can slice but not modify
t = (1, 2, 3)
print(t[:2])  # Output: (1, 2)

# 9. Concatenation creates a new tuple
t1 = (1, 2)
t2 = (3,)
t1 = t1 + t2
print(t1)

# 10. Tuples are hashable
coordinates = (10, 20)
print(hash(coordinates))

# 11. Use tuple in sets
unique = {(1, 2), (3, 4)}
print((1, 2) in unique)

# 12. Tuple values fixed in functions
def show(emp):
    # emp[0] = "Test" ❌ Not allowed
    print(emp)

# 13. Protect values using tuples
API_KEYS = ("key123", "key456")
print(API_KEYS)

# 14. Tuple inside list - modify list not tuple
students = [("Ravi", "BCA")]
students[0] = ("Ravi", "MCA")
print(students)

# 15. Strings are immutable like tuples
msg = "hello"
try:
    msg[0] = "H"
except TypeError:
    print("Immutable!")

# 16. Tuple with mutable elements (not safe)
t = ([1, 2], [3, 4])
t[0][0] = 100  # Changes the list inside
print(t)

# 17. Immutable record storage
record = ("ID001", "Shalini", "Trainer")
print(record)

# 18. Attempting to add element
# record += ("New",)  # New tuple created

# 19. Use tuple in caching/frozen state
cached_data = ("User123", "Page5")
print("Cached:", cached_data)

# 20. Tuple in function default argument
def greet(info=("Guest",)):
    print(f"Hello, {info[0]}!")

greet()

# 21. Replacing tuple requires reassignment
address = ("Delhi", "India")
address = ("Mumbai", "India")
print(address)

# 22. Check immutability of data
data = (10, 20)
print("Immutable:", isinstance(data, tuple))

# 23. ID card info (fixed data)
id_card = ("Shalini", "BBA", "Maharishi")
print(id_card)

# 24. Immutable timestamps
timestamp = (2025, 7, 13, 16, 30)
print(timestamp)

# 25. Tuple values in loops can't change
status = ("Active", "Blocked")
for s in status:
    print(s.upper())


#SECTION 6: List vs Tuple Use Cases

# 1. List for shopping items (can add/remove)
shopping = ["milk", "bread"]
shopping.append("butter")
print(shopping)

# 2. Tuple for fixed days of week
days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
print(days)

# 3. List for student marks
marks = [88, 76, 92]
marks[1] = 85
print(marks)

# 4. Tuple for immutable student ID
student_id = ("ID123",)
print(student_id)

# 5. List for employee records (update allowed)
emp = ["Amit", "HR"]
emp[1] = "IT"
print(emp)

# 6. Tuple for fixed config values
config = ("v1.2", "release", True)
print(config)

# 7. List supports sort()
cities = ["Mumbai", "Delhi", "Agra"]
cities.sort()
print(cities)

# 8. Tuples can't be sorted directly
nums = (3, 1, 2)
print(sorted(nums))

# 9. Use list for dynamic inputs
user_inputs = []
for _ in range(3):
    user_inputs.append(input("Enter value: "))
print(user_inputs)

# 10. Use tuple for country codes
codes = ("IN", "US", "UK")
print(codes)

# 11. Convert list to tuple for security
temp = ["Admin", "1234"]
secure = tuple(temp)
print(secure)

# 12. Append/remove with list
tasks = ["Email", "Call"]
tasks.remove("Call")
print(tasks)

# 13. Tuple as dictionary key
login = {("user1", "admin"): True}
print(login[("user1", "admin")])

# 14. List is better for data manipulation
data = [1, 2, 3]
data[0] += 5
print(data)

# 15. Tuple for fixed coordinate points
coord = (23.56, 77.89)
print(coord)

# 16. List inside tuple: careful!
data = ([1, 2],)
data[0].append(3)
print(data)

# 17. Use list for inventory
inventory = ["pen", "eraser"]
inventory.extend(["marker"])
print(inventory)

# 18. Tuple for fixed language codes
langs = ("EN", "HI", "FR")
print(langs)

# 19. List for grades (frequently updated)
grades = ["A", "B", "C"]
grades[2] = "A"
print(grades)

# 20. Tuple in logging
log_entry = ("Login", "12:45PM")
print(log_entry)

# 21. Store customer info in list (editable)
customer = ["Name", "Age", "City"]
customer[2] = "Delhi"
print(customer)

# 22. Use tuple for months
months = ("Jan", "Feb", "Mar")
print(months)

# 23. Update preferences in list
prefs = ["Dark", "English"]
prefs[0] = "Light"
print(prefs)

# 24. Tuple for license types
licenses = ("MIT", "Apache", "GPL")
print(licenses)

# 25. List to hold dynamic records
records = []
records.append(("User1", 100))
print(records)


#SECTION 7: Tuple Operations 

#(Tuple Concatenation, Repetition, Membership, Indexing, Counting)

# 1. Concatenate employee designations
des1 = ("Manager", "Clerk")
des2 = ("HR", "Trainer")
all_roles = des1 + des2
print(all_roles)

# 2. Repeat week pattern
week = ("Mon", "Tue")
print(week * 2)  # Output: ('Mon', 'Tue', 'Mon', 'Tue')

# 3. Check if "Python" skill exists in tuple
skills = ("Excel", "SQL", "Python", "Power BI")
print("Python" in skills)

# 4. Count how many times "apple" appears in orders
orders = ("apple", "banana", "apple", "mango", "apple")
print("Apple Count:", orders.count("apple"))

# 5. Find index of "mango"
fruits = ("grape", "banana", "mango", "kiwi")
print(fruits.index("mango"))


#(Tuple Conversion & Type Casting)

# 6. Convert a list of numbers into a tuple
lst = [100, 200, 300]
print("Converted Tuple:", tuple(lst))

# 7. Convert tuple to string (for message display)
words = ("Welcome", "to", "Python", "World")
message = " ".join(words)
print("Message:", message)

# 8. Convert a string of characters to tuple
code = "DATA123"
code_tuple = tuple(code)
print(code_tuple)

# 9. Tuple from multiple inputs
name = input("Enter your name: ")
city = input("Enter your city: ")
info = (name, city)
print("User Info Tuple:", info)

# 10. Convert a range of even numbers into a tuple
evens = tuple(range(2, 11, 2))
print(evens)


#(Tuple Unpacking, Slicing, and Indexing)
# 11. Unpack a tuple of course info
course = ("BBA", "3 Years", "Full-Time")
name, duration, type_ = course
print(f"{name} - {duration} - {type_}")

# 12. Slice tuple to get last two months
months = ("Jan", "Feb", "Mar", "Apr", "May")
print("Last 2 Months:", months[-2:])

# 13. Get initials from tuple of names
names = ("Shalini", "Verma")
initials = names[0][0] + names[1][0]
print("Initials:", initials)

# 14. Print alternate items from tuple
colors = ("Red", "Green", "Blue", "Yellow", "Pink")
print("Alternate Colors:", colors[::2])

# 15. Access nested values
records = (("John", 25), ("Meena", 30))
print("Second Person's Age:", records[1][1])


#(Tuple with Loops, Conditionals, and Functions)
# 16. Print all square numbers from a tuple
nums = (1, 2, 3, 4, 5)
for n in nums:
    print(f"Square of {n} is {n*n}")

# 17. Display subjects that start with 'P'
subjects = ("Physics", "Chemistry", "Python", "Math")
for sub in subjects:
    if sub.startswith("P"):
        print(sub)

# 18. Filter and store only strings from a mixed tuple
mixed = ("data", 25, "python", 30.5, True)
only_str = tuple(i for i in mixed if isinstance(i, str))
print("Only Strings:", only_str)

# 19. Create tuple of pass/fail status
marks = (78, 45, 60, 32, 90)
status = tuple("Pass" if m >= 50 else "Fail" for m in marks)
print("Result Status:", status)

# 20. Function to calculate total and average of numbers in a tuple
def analyze(tup):
    total = sum(tup)
    avg = total / len(tup)
    print("Total:", total)
    print("Average:", round(avg, 2))

analyze((80, 75, 90, 85))


#( Tuple with Zip, Enumerate, and Other Utilities)

# 21. Zip two tuples into (name, age) pairs
names = ("Amit", "Neha", "Rahul")
ages = (21, 22, 23)
combined = tuple(zip(names, ages))
print(combined)

# 22. Enumerate tuple values
languages = ("Python", "Java", "C++")
for i, lang in enumerate(languages, 1):
    print(f"{i}. {lang}")

# 23. Check if all numbers are even in a tuple
numbers = (2, 4, 6, 8)
print("All Even:", all(n % 2 == 0 for n in numbers))

# 24. Find max and min values from a tuple
prices = (100, 250, 190, 300)
print("Max:", max(prices), "| Min:", min(prices))

# 25. Reverse and display a tuple
places = ("Delhi", "Mumbai", "Chennai")
print("Reversed:", places[::-1])


#Mini-Task

# Student Result System (Tuple-Based)
students = (
    ("Shalini", [80, 90, 85]),
    ("Ravi", [60, 75, 70]),
    ("Neha", [95, 85, 88])
)

for name, marks in students:
    avg = sum(marks) / len(marks)
    print(f"{name} - Average: {avg} - {'Pass' if avg >= 75 else 'Fail'}")


#Real-World Mini Tasks Using Tuples

# Task 1: Top Performer Analysis
students = (("Anu", 88), ("Mohan", 76), ("Riya", 93), ("Kunal", 89))
# Find topper
top_score = 0
topper = ""
for name, score in students:
    if score > top_score:
        top_score = score
        topper = name
print("Topper:", topper, "| Marks:", top_score)

# Task 2: Product Price Calculator
products = (("Pen", 10), ("Pencil", 5), ("Notebook", 40))
total = sum(p[1] for p in products)
print("Total Price:", total)

# Task 3: Login Validation System
credentials = (("admin", "1234"), ("user1", "abcd"))
uname = input("Enter username: ")
pwd = input("Enter password: ")
if (uname, pwd) in credentials:
    print("Login Successful!")
else:
    print("Access Denied.")

# Task 4: Weather Stats
weather = (("Delhi", 38), ("Mumbai", 32), ("Kolkata", 35))
for city, temp in weather:
    if temp > 35:
        print(f"{city} is very hot today.")

# Task 5: City Lookup with Coordinates
locations = (("Delhi", 28.6, 77.2), ("Mumbai", 19.0, 72.8))
city = input("Enter city name: ")
found = False
for name, lat, lon in locations:
    if name.lower() == city.lower():
        print(f"{name}: Latitude {lat}, Longitude {lon}")
        found = True
if not found:
    print("City not found.")
