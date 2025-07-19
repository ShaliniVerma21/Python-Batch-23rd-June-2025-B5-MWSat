# ----------------------------------------Dictionary-----------------------------------
"""
What is a Dictionary in Python?

A dictionary is an unordered, mutable, and indexed collection of key-value pairs. 
Each key must be unique and immutable (like strings or numbers), while values can be of any data type.

Key Features:
- Unordered (until Python 3.6, ordered from Python 3.7+)
- Mutable (can be changed after creation)
- Indexed using unique keys
- Key-value pairs
- Fast lookup using keys

Real-Life Analogy: 
Think of a dictionary like a contact list in your phone:
- Name (key): "Rahul"
- Phone number (value): "9876543210"
"""

# ------------------------ Defining a Dictionary ------------------------

# Example 1: Empty dictionary
empty_dict = {}
print(empty_dict)  # Output: {}

# Example 2: Student details dictionary with string keys
student = {'name': 'Amit', 'age': 21, 'grade': 'A'}
print(student)

# Example 3: Country code mapping
country_code = {'India': 'IN', 'United States': 'US'}
print(country_code)

# Example 4: Product price list
products = {'Laptop': 55000, 'Mouse': 500}
print(products)

# Example 5: Book info
book = {'title': 'Atomic Habits', 'author': 'James Clear', 'pages': 320}
print(book)

# ------------------------ Creating a Dictionary (Different Methods) ------------------------

# Example 1: Using dict() with named parameters
employee = dict(name='John', salary=25000)
print(employee)

# Example 2: Creating from list of tuples (good for data from DB or CSV)
marks = dict([('Math', 90), ('Science', 95)])
print(marks)

# Example 3: Creating using zip() - useful when keys and values are in separate lists
keys = ['email', 'phone']
values = ['abc@gmail.com', '1234567890']
contact = dict(zip(keys, values))
print(contact)

# Example 4: Using dictionary comprehension – quick generation with logic
squares = {x: x*x for x in range(1, 4)}  # {1: 1, 2: 4, 3: 9}
print(squares)

# Example 5: Nested dictionary – useful for hierarchical or grouped data
company = {
    'HR': {'employees': 5, 'head': 'Asha'},
    'IT': {'employees': 10, 'head': 'Ravi'}
}
print(company)

# ------------------------ Accessing Dictionary Elements ------------------------

# Example 1: Access using key directly
student = {'name': 'Amit', 'age': 21}
print(student['name'])  # Output: Amit

# Example 2: Using get() method – safe way (won't raise error if key not found)
print(student.get('age'))     # Output: 21
print(student.get('grade'))   # Output: None (since not present)

# Example 3: Loop through dictionary keys
for key in student:
    print(key, '->', student[key])

# Example 4: Access keys and values using keys(), values(), items()
print(student.keys())     # dict_keys(['name', 'age'])
print(student.values())   # dict_values(['Amit', 21])
print(student.items())    # dict_items([('name', 'Amit'), ('age', 21)])

# Example 5: Check if key exists
if 'name' in student:
    print("Name exists")
else:
    print("Name does not exist")

# ------------------------ Dictionary Methods ------------------------

# Example 1: update() – to add or modify key-value pair
profile = {'name': 'Shalini'}
profile.update({'email': 'shalini@gmail.com'})  # Adds 'email' key
print(profile)

# Example 2: pop() – removes a specific key and returns its value
removed_item = profile.pop('email')  # Removes 'email' key
print("Removed:", removed_item)
print(profile)

# Example 3: items() – returns all key-value pairs as tuples
for key, value in profile.items():
    print(key, value)

# Example 4: setdefault() – adds key with default value if key is not present
profile.setdefault('location', 'India')  # Adds 'location' if missing
print(profile)

# Example 5: clear() – removes all items from the dictionary
profile.clear()
print(profile)  # Output: {}

# ------------------------ Additional Useful Operations ------------------------

# Example: Delete dictionary or a specific key
user = {'name': 'Jay', 'age': 22}
del user['age']  # Deletes 'age' key
print(user)

# Example: Copy dictionary (shallow copy)
original = {'a': 1, 'b': 2}
copied = original.copy()
print(copied)

# Example: Merge two dictionaries (Python 3.9+)
d1 = {'x': 10}
d2 = {'y': 20}
merged = d1 | d2
print(merged)

# Example: Length of dictionary
print("Number of keys:", len(merged))  # Output: 2


# ----------------------------------------------------------------------------
# Dictionary Operations – Add, Update, Delete, Traverse
# ----------------------------------------------------------------------------

# Let's define a dictionary of an online order
order = {
    'order_id': 'ORD123',
    'customer': 'Amit Sharma',
    'items': ['Laptop', 'Mouse'],
    'total_amount': 55500,
    'status': 'Processing'
}

# Add a new key-value pair
order['shipping'] = 'Free'
print("After Adding Shipping Info:", order)

# Update the value of an existing key
order['status'] = 'Shipped'
print("After Updating Status:", order)

# Delete a key-value pair using del
del order['shipping']
print("After Removing Shipping Info:", order)

# Use pop() to remove and return a key’s value
removed_item = order.pop('total_amount')
print("Removed Amount:", removed_item)
print("Order after pop():", order)

# Loop through keys and values
print("Order Details:")
for key, value in order.items():
    print(f"{key} : {value}")

# Check if a key exists
if 'items' in order:
    print("Items are present in the order.")

# Get list of all keys, values, and items
print("Keys:", list(order.keys()))
print("Values:", list(order.values()))
print("Key-Value Pairs:", list(order.items()))

# ----------------------------------------------------------------------------
# Real-World Data Analysis Example Using Dictionary
# ----------------------------------------------------------------------------

# Let's say we are analyzing sales data for 3 stores

sales_data = {
    'Store_A': {'Q1': 25000, 'Q2': 27000, 'Q3': 30000, 'Q4': 32000},
    'Store_B': {'Q1': 15000, 'Q2': 18000, 'Q3': 20000, 'Q4': 22000},
    'Store_C': {'Q1': 30000, 'Q2': 32000, 'Q3': 35000, 'Q4': 37000}
}

# Print total annual sales for each store
print("\nTotal Annual Sales per Store:")
for store, quarters in sales_data.items():
    total = sum(quarters.values())
    print(f"{store}: ₹{total}")

# Find which store performed best in Q4
q4_sales = {store: data['Q4'] for store, data in sales_data.items()}
best_store_q4 = max(q4_sales, key=q4_sales.get)
print(f"\n🏆 Best Store in Q4: {best_store_q4} with ₹{q4_sales[best_store_q4]}")

# Calculate average sales for each store
print("\nAverage Quarterly Sales:")
for store, quarters in sales_data.items():
    average = sum(quarters.values()) / len(quarters)
    print(f"{store}: ₹{round(average, 2)}")

# Combine sales of all stores for Q2
total_q2 = sum(store['Q2'] for store in sales_data.values())
print(f"\n📈 Combined Q2 Sales for All Stores: ₹{total_q2}")
