# 1. DEFINING DICTIONARIES

""" 
A dictionary is a collection of key-value pairs. Each key is unique, and values can be of any type. 
Syntax:
dict_name = {key1: value1, key2: value2, ...}
"""

# 1. Empty dictionary
empty_dict = {}
print(empty_dict)

# 2. Simple dictionary
student = {'name': 'Anil', 'age': 21, 'grade': 'A'}
print(student)

# 3. Product dictionary
product = {'Laptop': 50000, 'Mouse': 700}
print(product)

# 4. Marks dictionary
marks = {'Math': 85, 'Science': 92}
print(marks)

# 5. Boolean values
status = {'loggedIn': True, 'verified': False}
print(status)

# 6. List as value
hobbies = {'Rahul': ['Reading', 'Gaming']}
print(hobbies)

# 7. Nested dictionary
employee = {'HR': {'count': 5}, 'IT': {'count': 10}}
print(employee)

# 8. Mix value types
data = {'name': 'Reena', 'score': 88, 'pass': True}
print(data)

# 9. Using int keys
room = {1: 'Occupied', 2: 'Vacant'}
print(room)

# 10. Duplicate keys (last one overrides)
test = {'a': 10, 'a': 20}
print(test)

# 11. Using tuple as key
location = {(10.5, 20.6): "Point A"}
print(location)

# 12. Mobile brand info
mobile = {'brand': 'Samsung', 'model': 'A52', 'price': 25000}
print(mobile)

# 13. Game info
game = {'name': 'Chess', 'players': 2}
print(game)

# 14. Using strings as keys
info = {'Name': 'Amit', 'City': 'Delhi'}
print(info)

# 15. Language usage
lang = {'Python': 'Web', 'C++': 'Game Dev'}
print(lang)

# 16. College details
college = {'name': 'ABC University', 'rank': 5}
print(college)

# 17. Car info
car = {'make': 'Honda', 'year': 2020}
print(car)

# 18. City population
population = {'Mumbai': 20000000, 'Pune': 7000000}
print(population)

# 19. Sports and coach
sports = {'Cricket': 'Ravi', 'Hockey': 'Surjit'}
print(sports)

# 20. Food calories
food = {'Apple': 95, 'Banana': 105}
print(food)

# 21. Student marksheet
marksheet = {'Roll': 101, 'Name': 'Meena', 'Marks': 85}
print(marksheet)

# 22. Devices and quantity
inventory = {'Laptop': 10, 'Monitor': 5}
print(inventory)

# 23. Profile with address
profile = {'name': 'Pooja', 'address': {'city': 'Indore', 'pincode': 452001}}
print(profile)

# 24. Social media stats
stats = {'likes': 230, 'shares': 45}
print(stats)

# 25. Festival dates
festivals = {'Holi': 'March', 'Diwali': 'November'}
print(festivals)


#2. CREATING DICTIONARIES
""" 
You can create dictionaries using different techniques like:

{} literal
dict() constructor
zip() function
Dictionary comprehension
Tuples/lists
"""

# 1. Using dict() constructor
user = dict(name='Anil', age=24)
print(user)

# 2. From list of tuples
employee = dict([('name', 'Rita'), ('age', 30)])
print(employee)

# 3. Using zip()
keys = ['Math', 'Science']
values = [95, 90]
result = dict(zip(keys, values))
print(result)

# 4. Comprehension - squares
squares = {x: x*x for x in range(1, 6)}
print(squares)

# 5. Nested using dict()
nested = dict(A=dict(x=1), B=dict(x=2))
print(nested)

# 6. From 2 lists
names = ['A', 'B', 'C']
scores = [80, 85, 90]
students = dict(zip(names, scores))
print(students)

# 7. Default value using comprehension
defaults = {k: 0 for k in ['a', 'b', 'c']}
print(defaults)

# 8. Characters count using comprehension
string = 'data'
count = {ch: string.count(ch) for ch in string}
print(count)

# 9. Using range keys
range_dict = {x: chr(65 + x) for x in range(5)}
print(range_dict)

# 10. Key from tuple list
tlist = [('x', 10), ('y', 20)]
t_dict = dict(tlist)
print(t_dict)

# 11. Boolean keys
b_dict = {True: "Yes", False: "No"}
print(b_dict)

# 12. Multiple ways combined
d = dict(zip(['a', 'b'], [1, 2]))
d.update({'c': 3})
print(d)

# 13. Using dict with keyword args
profile = dict(name='Aarti', country='India')
print(profile)

# 14. Initializing with None
blank = dict.fromkeys(['x', 'y', 'z'])
print(blank)

# 15. From user input
data = dict([('name', input("Enter name: ")), ('city', input("Enter city: "))])
print(data)

# 16. Using map
keys = ['p', 'q']
values = list(map(int, ['10', '20']))
m_dict = dict(zip(keys, values))
print(m_dict)

# 17. String to dictionary using split
info = 'name:Raj,age:25'
data = dict(item.split(':') for item in info.split(','))
print(data)

# 18. ASCII mapping
ascii_dict = {chr(i): i for i in range(65, 71)}
print(ascii_dict)

# 19. Word length mapping
words = ['apple', 'banana']
length_dict = {w: len(w) for w in words}
print(length_dict)

# 20. Mapping even numbers
evens = {x: 'even' for x in range(10) if x % 2 == 0}
print(evens)

# 21. Creating a timetable
timetable = dict(zip(['Monday', 'Tuesday'], ['Math', 'Science']))
print(timetable)

# 22. Using tuple unpack
pairs = [(1, 'one'), (2, 'two')]
pair_dict = dict(pairs)
print(pair_dict)

# 23. Integer keys and string values
num_map = {i: str(i) for i in range(5)}
print(num_map)

# 24. Course & instructor
course = dict(Python='Shalini', SQL='Rahul')
print(course)

# 25. Custom mapping
data = dict(((x, x*10) for x in range(1, 6)))
print(data)


#3. ACCESSING & MODIFYING DICTIONARIES
""" 
You can access and update dictionary values using:

Brackets []
.get() method
.update(), .setdefault()
.pop(), .clear()
Looping through .items(), .keys(), .values()
"""

# 1. Access using key
person = {'name': 'Ajay'}
print(person['name'])

# 2. Use get() safely
print(person.get('age', 'Not found'))

# 3. Modify existing key
person['name'] = 'Vijay'
print(person)

# 4. Add new key
person['age'] = 30
print(person)

# 5. Using update()
person.update({'city': 'Delhi'})
print(person)

# 6. setdefault() if not exists
person.setdefault('state', 'Delhi')
print(person)

# 7. Remove key using pop()
removed = person.pop('state')
print("Removed:", removed)

# 8. Loop through items
for k, v in person.items():
    print(k, v)

# 9. Check key presence
if 'city' in person:
    print("City exists")

# 10. Access all keys
print(person.keys())

# 11. Access all values
print(person.values())

# 12. Use popitem()
last_item = person.popitem()
print("Popped:", last_item)

# 13. Use clear()
person.clear()
print(person)

# 14. Merge dictionaries
a = {'x': 1}
b = {'y': 2}
a.update(b)
print(a)

# 15. Access nested key
company = {'IT': {'emp': 10}}
print(company['IT']['emp'])

# 16. Modify nested value
company['IT']['emp'] = 20
print(company)

# 17. Convert keys to list
print(list(company.keys()))

# 18. Count values > 90
marks = {'A': 91, 'B': 89, 'C': 95}
count = sum(1 for m in marks.values() if m > 90)
print("Count > 90:", count)

# 19. Use dictionary in if-else
user = {'role': 'admin'}
if user.get('role') == 'admin':
    print("Access granted")

# 20. Copy dictionary
copied = user.copy()
print(copied)

# 21. Check value in dictionary
if 'admin' in user.values():
    print("Role is admin")

# 22. Combine using dict unpacking
merged = {**a, **b}
print(merged)

# 23. Update using loop
for k in marks:
    marks[k] += 5
print(marks)

# 24. Delete key
del marks['B']
print(marks)

# 25. Dictionary as function input
def greet(info):
    return f"Hi {info['name']}!"
print(greet({'name': 'Shalini'}))


# 4. Dictionary Methods

# 1. get(): Safe access
employee = {"name": "Meena", "department": "HR"}
print(employee.get("name"))  # Meena
print(employee.get("salary", "Not Disclosed"))  # Not Disclosed

# 2. keys(): List of all keys
car = {"brand": "BMW", "color": "Black"}
print(car.keys())  # dict_keys(['brand', 'color'])

# 3. values(): List of all values
print(car.values())  # dict_values(['BMW', 'Black'])

# 4. items(): List of (key, value) pairs
print(car.items())  # dict_items([('brand', 'BMW'), ('color', 'Black')])

# 5. update(): Merge dictionaries
settings = {"theme": "dark"}
new_settings = {"volume": 70}
settings.update(new_settings)
print(settings)  # {'theme': 'dark', 'volume': 70}

# 6. pop(): Remove key and return value
order = {"item": "Laptop", "price": 80000}
print(order.pop("price"))  # 80000

# 7. popitem(): Removes last item
fridge = {"milk": 2, "eggs": 12}
print(fridge.popitem())  # ('eggs', 12)

# 8. clear(): Empty dictionary
temp = {"data": 123}
temp.clear()
print(temp)  # {}

# 9. copy(): Create a copy
record = {"student": "Kavya"}
backup = record.copy()
print(backup)  # {'student': 'Kavya'}

# 10. setdefault(): Add key if missing
user = {"name": "Arjun"}
user.setdefault("email", "arjun@example.com")
print(user)  # {'name': 'Arjun', 'email': 'arjun@example.com'}

# 11. fromkeys(): Create dictionary from list
cities = ["Delhi", "Mumbai", "Kolkata"]
temperature = dict.fromkeys(cities, "Unknown")
print(temperature)

# 12. Check if dictionary is empty
d = {}
print("Empty" if not d else "Not Empty")

# 13. Count word frequency
text = "apple banana apple mango"
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)  # {'apple': 2, 'banana': 1, 'mango': 1}

# 14. Merge student scores
scores1 = {"John": 90}
scores2 = {"Emma": 85}
scores1.update(scores2)
print(scores1)

# 15. Check value exists
students = {"Raj": "A", "Amit": "B"}
print("A" in students.values())  # True

# 16. Remove item if exists
if "Amit" in students:
    students.pop("Amit")
print(students)

# 17. Using items() in loop
for key, val in students.items():
    print(key, val)

# 18. keys() in loop
for k in students.keys():
    print(k)

# 19. values() in loop
for v in students.values():
    print(v)

# 20. Dictionary length
print(len(students))  # 1

# 21. Rename a key
info = {"username": "admin"}
info["user"] = info.pop("username")
print(info)

# 22. Dictionary as default config
default_config = dict.fromkeys(["font", "theme", "lang"], "default")
print(default_config)

# 23. Dictionary for status mapping
status_code = {200: "OK", 404: "Not Found"}
print(status_code.get(404))  # Not Found

# 24. Remove item with default message
print(order.pop("discount", "No discount applied"))

# 25. Counting vowels in a string
vowels = "aeiou"
sample = "education"
count = {}
for char in sample:
    if char in vowels:
        count[char] = count.get(char, 0) + 1
print(count)  # {'e': 1, 'u': 1, 'a': 1, 'i': 1, 'o': 1}


# 5. Dictionary Operations

# 1. Iterate over dictionary
user = {"id": 101, "name": "Ankit"}
for key in user:
    print(f"{key} => {user[key]}")

# 2. Check if key exists
print("name" in user)  # True

# 3. Loop and build new dictionary
marks = {"Ajay": 50, "Vijay": 80}
grade = {}
for name, score in marks.items():
    grade[name] = "Pass" if score >= 60 else "Fail"
print(grade)

# 4. Add key-value dynamically
user["email"] = "ankit@example.com"
print(user)

# 5. Remove key safely
user.pop("email", None)

# 6. Compare two dictionaries
a = {"x": 1, "y": 2}
b = {"y": 2, "x": 1}
print(a == b)  # True

# 7. Reverse key-value pairs
data = {"red": 1, "blue": 2}
reversed_data = {v: k for k, v in data.items()}
print(reversed_data)

# 8. Use dictionary with list
orders = {"id": 101, "items": ["pen", "pencil"]}
print(orders["items"][0])  # pen

# 9. Count elements from list
students = ["A", "B", "A", "C"]
counts = {}
for s in students:
    counts[s] = counts.get(s, 0) + 1
print(counts)

# 10. Nested dictionaries for product
product = {
    "id": 1,
    "details": {
        "name": "Shoes",
        "price": 999
    }
}
print(product["details"]["name"])

# 11. Filter keys with condition
filtered = {k: v for k, v in marks.items() if v > 60}
print(filtered)

# 12. Add values from two dicts
math = {"A": 50, "B": 40}
science = {"A": 30, "B": 60}
total = {k: math[k] + science.get(k, 0) for k in math}
print(total)

# 13. Merge and handle duplicates
d1 = {"A": 100}
d2 = {"A": 50, "B": 70}
for k, v in d2.items():
    d1[k] = d1.get(k, 0) + v
print(d1)

# 14. Check if two dicts share keys
print(bool(set(d1.keys()) & set(science.keys())))  # True

# 15. Remove duplicates by value
unique_vals = {}
for k, v in {"x": 1, "y": 2, "z": 1}.items():
    if v not in unique_vals.values():
        unique_vals[k] = v
print(unique_vals)

# 16. Dictionary with list values
grades = {"A": [80, 85], "B": [70, 75]}
grades["A"].append(90)
print(grades)

# 17. Flatten nested dictionary
flat = {}
for k, v in product.items():
    if isinstance(v, dict):
        for sub_k, sub_v in v.items():
            flat[f"{k}_{sub_k}"] = sub_v
    else:
        flat[k] = v
print(flat)

# 18. Sort dictionary by value
sorted_scores = dict(sorted(marks.items(), key=lambda item: item[1], reverse=True))
print(sorted_scores)

# 19. Replace key in dictionary
d = {"old": 1}
d["new"] = d.pop("old")
print(d)

# 20. Dictionary comprehension for square
squares = {x: x*x for x in range(1, 6)}
print(squares)

# 21. Convert two lists to dict
keys = ["id", "name"]
vals = [201, "Asha"]
combined = dict(zip(keys, vals))
print(combined)

# 22. Unique character counter
word = "hello"
char_count = {c: word.count(c) for c in set(word)}
print(char_count)

# 23. Track login status
users = {"admin": True, "guest": False}
for u, s in users.items():
    print(f"{u} is {'online' if s else 'offline'}")

# 24. Group items by category
items = [("Fruit", "Apple"), ("Fruit", "Banana"), ("Veg", "Spinach")]
grouped = {}
for category, name in items:
    grouped.setdefault(category, []).append(name)
print(grouped)

# 25. Track inventory count
inventory = {"pen": 5, "book": 2}
sold = {"pen": 1, "book": 1}
for item in sold:
    inventory[item] -= sold[item]
print(inventory)


# 6. Real-World Data Analysis Example Using Dictionary 

# 1. Student marks and percentage
marks = {"Amit": [70, 80, 90], "Rahul": [60, 50, 65]}
percentage = {k: sum(v)/len(v) for k, v in marks.items()}
print(percentage)

# 2. E-commerce sales
sales = {"Shoes": 500, "Watch": 300, "Bags": 150}
total_sales = sum(sales.values())
print("Total Sales:", total_sales)

# 3. Employee database
employees = {
    101: {"name": "John", "dept": "HR"},
    102: {"name": "Sara", "dept": "IT"}
}
print(employees[102]["name"])

# 4. Bank account balance tracking
accounts = {"Ravi": 5000, "Asha": 3000}
accounts["Ravi"] += 2000
print(accounts)

# 5. Stock market holdings
portfolio = {"TCS": 10, "Infosys": 5}
price = {"TCS": 3500, "Infosys": 1400}
value = sum(portfolio[stock] * price[stock] for stock in portfolio)
print("Portfolio Value:", value)

# 6. Grocery bill
items = {"milk": 2, "bread": 1}
rates = {"milk": 30, "bread": 25}
total = sum(items[i] * rates[i] for i in items)
print("Total:", total)

# 7. Weather report
temp = {"Monday": 35, "Tuesday": 38, "Wednesday": 36}
avg_temp = sum(temp.values()) / len(temp)
print("Average Temp:", avg_temp)

# 8. School attendance
attendance = {"Grade 1": 25, "Grade 2": 20}
total_students = sum(attendance.values())
print("Total Students:", total_students)

# 9. Festival budget planner
budget = {"decor": 1000, "food": 2500, "gifts": 2000}
if sum(budget.values()) <= 6000:
    print("Under Budget")
else:
    print("Over Budget")

# 10. Hotel room bookings
rooms = {"101": "booked", "102": "empty", "103": "booked"}
available = [k for k, v in rooms.items() if v == "empty"]
print("Available Rooms:", available)

# 11. Patient medicine tracker
patients = {"Kiran": ["Paracetamol", "Zinc"], "Ravi": ["Vitamin C"]}
print(patients["Kiran"])

# 12. City population growth
pop_2020 = {"Delhi": 2, "Mumbai": 3}
pop_2024 = {"Delhi": 2.4, "Mumbai": 3.5}
growth = {k: pop_2024[k] - pop_2020[k] for k in pop_2020}
print(growth)

# 13. Online course ratings
courses = {"Python": 4.5, "Java": 4.2}
print("Top Rated:", max(courses, key=courses.get))

# 14. Budget vs Expense
budget = {"Food": 2000, "Rent": 8000}
expense = {"Food": 2500, "Rent": 7500}
status = {k: "Over" if expense[k] > budget[k] else "Under" for k in budget}
print(status)

# 15. Word count in feedback
feedback = "great course great content"
words = feedback.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print(freq)

# 16. Employee shift tracking
shift = {"Mon": ["John"], "Tue": ["Sara"]}
shift["Wed"] = ["Amit"]
print(shift)

# 17. Analyze exam results
results = {"John": {"Math": 80, "Eng": 70}}
average = {k: sum(v.values()) / len(v) for k, v in results.items()}
print(average)

# 18. Orders by user
orders = [("Ravi", 1), ("Ravi", 2), ("Meena", 1)]
summary = {}
for user, qty in orders:
    summary[user] = summary.get(user, 0) + qty
print(summary)

# 19. Survey results (likes per option)
survey = ["A", "B", "A", "C", "B"]
count = {}
for opt in survey:
    count[opt] = count.get(opt, 0) + 1
print(count)

# 20. Rental car record
cars = {"MH01": {"name": "Ford", "days": 3}, "MH02": {"name": "Toyota", "days": 5}}
for plate, details in cars.items():
    print(plate, details["name"])

# 21. Voting results
votes = ["Rahul", "Rahul", "Priya"]
vote_count = {}
for v in votes:
    vote_count[v] = vote_count.get(v, 0) + 1
print(vote_count)

# 22. Hostel room allocation
hostel = {"A101": "Ankit", "A102": "Priya"}
print("A102" in hostel)

# 23. Book catalog by genre
catalog = {
    "Fiction": ["Book1", "Book2"],
    "Non-Fiction": ["Book3"]
}
print(catalog["Fiction"])

# 24. Transport cost calculator
trips = {"auto": 50, "bus": 20, "train": 100}
print("Total:", sum(trips.values()))

# 25. Subscription renewal tracker
subscriptions = {"Netflix": "2025-01-01", "Spotify": "2024-12-31"}
print(subscriptions.get("Spotify"))

""" 
Scenario: Analyzing Sales Data of a Retail Store

Goal: Analyze product sales, quantities, and revenue using dictionary operations.
"""

#Step 1: Define Product Data

# Dictionary storing product data
sales_data = {
    'Laptop': {'price': 55000, 'units_sold': 8},
    'Mouse': {'price': 500, 'units_sold': 45},
    'Keyboard': {'price': 1000, 'units_sold': 30},
    'Monitor': {'price': 12000, 'units_sold': 10},
    'USB Drive': {'price': 800, 'units_sold': 60}
}

# Step 2: Total Revenue Generated

total_revenue = 0

for product, info in sales_data.items():
    revenue = info['price'] * info['units_sold']
    total_revenue += revenue
    print(f"{product} -> Revenue: ₹{revenue}")

print(f"\nTotal Revenue: ₹{total_revenue}")


#Step 3: Find Top-Selling Product

top_product = ''
max_units = 0

for product, info in sales_data.items():
    if info['units_sold'] > max_units:
        max_units = info['units_sold']
        top_product = product

print(f"\nTop-Selling Product: {top_product} ({max_units} units sold)")


# Step 4: Add New Product Stock

# Adding a new product dynamically
sales_data['Webcam'] = {'price': 2500, 'units_sold': 12}
print("\nNew Product Added: Webcam")


# Step 5: Apply Discount on Low-Selling Products

# Apply 10% discount if units_sold < 20
for product in sales_data:
    if sales_data[product]['units_sold'] < 20:
        old_price = sales_data[product]['price']
        sales_data[product]['price'] = int(old_price * 0.9)  # Apply 10% discount
        print(f"Discount applied to {product}: Old ₹{old_price} -> New ₹{sales_data[product]['price']}")

# Step 6: Report Summary

print("\n--- Final Product Summary ---")
for product, info in sales_data.items():
    print(f"{product} - Price: ₹{info['price']}, Units Sold: {info['units_sold']}")
