# 1. DEFINING DICTIONARIES

""" 
A dictionary is a collection of key-value pairs. Each key is unique, and values can be of any type. 
Syntax:
dict_name = {key1: value1, key2: value2, ...}
"""


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
