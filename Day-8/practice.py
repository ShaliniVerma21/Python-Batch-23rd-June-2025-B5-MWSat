#1. Defining a Set

# 1. Store unique fruits
fruits = {"apple", "banana", "cherry"}

# 2. Unique phone brands
phones = {"Samsung", "Apple", "OnePlus"}

# 3. Unique years
years = {2020, 2021, 2022}

# 4. Days of week
days = {"Mon", "Tue", "Wed", "Thu", "Fri"}

# 5. Unique exam scores
scores = {85, 92, 75, 85, 92}

# 6. Set with mixed data
data = {101, "User", 3.5}

# 7. Defining empty set
empty = set()

# 8. Set of student roll numbers
rolls = {101, 102, 103, 101}

# 9. Book titles
books = {"Python Basics", "ML Guide", "Data Science"}

# 10. Set of pin codes
pins = {110001, 560001, 400001}

# 11. Unique car colors
colors = {"red", "blue", "white", "red"}

# 12. Items in a to-do list
tasks = {"Email client", "Meeting", "Code Review"}

# 13. Favorite subjects
subjects = {"Math", "English", "Science"}

# 14. Class sections
sections = {"A", "B", "C"}

# 15. Web technologies
tech = {"HTML", "CSS", "JavaScript"}

# 16. Items in cart
cart = {"Shirt", "Jeans", "Socks"}

# 17. Branches in a company
branches = {"Sales", "HR", "Tech", "Tech"}

# 18. Unique temperature readings
temps = {98.6, 100.1, 99.5}

# 19. Set of cities visited
cities = {"Delhi", "Mumbai", "Chennai"}

# 20. Set of unique IDs
ids = {1010, 1020, 1030}

# 21. Movie genres
genres = {"Action", "Drama", "Comedy"}

# 22. Traffic light colors
signals = {"Red", "Yellow", "Green"}

# 23. Olympic sports
sports = {"Swimming", "Running", "Shooting"}

# 24. Airline names
airlines = {"Indigo", "Air India", "Vistara"}

# 25. Set of error codes
errors = {"404", "403", "500"}


# 2. Creating a Set Dynamically 

# 1. From list
emails = list(set(["a@gmail.com", "b@gmail.com", "a@gmail.com"]))

# 2. From user input
names = set(input("Enter names: ").split())

# 3. From range
nums = set(range(1, 11))

# 4. From string
letters = set("hello")

# 5. From tuple
marks = set((85, 90, 85))

# 6. Using loop
even = set()
for i in range(10):
    if i % 2 == 0:
        even.add(i)

# 7. From dictionary keys
student = {"name": "Ram", "age": 20}
keys = set(student.keys())

# 8. From dictionary values
values = set(student.values())

# 9. Set from file lines
# file_lines = set(open("data.txt").readlines())  # (if file used)

# 10. From function return
def get_departments():
    return ["HR", "IT", "Finance", "HR"]
unique_dept = set(get_departments())

# 11. Removing duplicates from input
numbers = set(map(int, input("Enter numbers: ").split()))

# 12. Set from random numbers
import random
rand_set = set(random.sample(range(1, 100), 5))

# 13. Split CSV string
csv = "apple,banana,apple"
fruit_set = set(csv.split(","))

# 14. Emails from logs
logs = ["user1", "user2", "user1"]
unique_users = set(logs)

# 15. Set of vowels in sentence
sentence = "Python is awesome"
vowels = set(filter(lambda x: x in 'aeiouAEIOU', sentence))

# 16. Set of prices from list of dicts
items = [{"price": 10}, {"price": 20}, {"price": 10}]
prices = set(i["price"] for i in items)

# 17. Set from nested list
nested = [[1, 2], [2, 3]]
flat_set = set([x for lst in nested for x in lst])

# 18. Unique product names
products = set(["Pen", "Pencil", "Pen", "Eraser"])

# 19. Set of hostnames
hosts = set(["server1", "server2", "server1"])

# 20. Cleaned phone numbers
numbers = set(["+91-9999", "+91-8888", "+91-9999"])

# 21. Unique hashtags
hashtags = set(["#fun", "#work", "#fun"])

# 22. Unique file extensions
files = ["a.py", "b.txt", "c.py"]
exts = set([f.split('.')[-1] for f in files])

# 23. Unique tweet authors
tweets = [{"author": "A"}, {"author": "B"}, {"author": "A"}]
authors = set([t["author"] for t in tweets])

# 24. Converting set from another set
x = set([1, 2, 3])
y = set(x)

# 25. Input numbers as tuple -> convert to set
tup = tuple(map(int, input("Enter tuple: ").split()))
tup_set = set(tup)


#  3. Set Operations:

# A. Union
a = {"Delhi", "Mumbai"}
b = {"Mumbai", "Kolkata"}
print(a | b)


# B. Intersection
x = {"python", "java", "c++"}
y = {"java", "go"}
print(x & y)


# C.Difference
paid_users = {"Alice", "Bob", "Charlie"}
free_users = {"Charlie", "David"}
print(paid_users - free_users)


# D.Symmetric Difference
a = {1, 2, 3}
b = {3, 4, 5}
print(a ^ b)


# E. Membership Test
colors = {"red", "green", "blue"}
print("green" in colors)
print("yellow" not in colors)


# 4. Set Methods 

items = {"pen", "pencil"}

# 1. add()
items.add("eraser")

# 2. remove()
items.remove("pen")

# 3. discard()
items.discard("marker")

# 4. pop()
items.pop()

# 5. clear()
items.clear()

# More:
# 6. copy()
new_items = items.copy()

# 7. update()
items.update(["scale", "sharpener"])

# 8. intersection_update()
a = {1, 2, 3}
b = {2, 3, 4}
a.intersection_update(b)

# 9. difference_update()
x = {1, 2, 3, 4}
y = {2, 4}
x.difference_update(y)

# 10. symmetric_difference_update()
p = {1, 2, 3}
q = {3, 4}
p.symmetric_difference_update(q)

# 11. add() – Add a new fruit to the basket
fruits = {"apple", "banana"}
fruits.add("mango")
print(fruits)

# 12. remove() – Remove a subject from enrolled list
subjects = {"math", "english", "science"}
subjects.remove("math")
print(subjects)

# 13. discard() – Try discarding a non-existent element (no error)
languages = {"Python", "Java"}
languages.discard("C++")  # No error
print(languages)

# 14. pop() – Remove a random hobby
hobbies = {"singing", "dancing", "painting"}
hobbies.pop()
print(hobbies)

# 15. clear() – Clear all participants from a set
participants = {"Amit", "Pooja", "Karan"}
participants.clear()
print(participants)

# 16. copy() – Duplicate set of available seats
seats = {"A1", "A2", "A3"}
backup_seats = seats.copy()
print(backup_seats)

# 17. update() – Add new cities to a travel list
cities = {"Delhi", "Mumbai"}
cities.update(["Chennai", "Kolkata"])
print(cities)

# 18. intersection_update() – Common skills between two job profiles
profile1 = {"Python", "SQL", "Git"}
profile2 = {"SQL", "Java", "Python"}
profile1.intersection_update(profile2)
print(profile1)

# 19. difference_update() – Skills unique to employee1
employee1 = {"C", "Python", "ML"}
employee2 = {"ML", "Java"}
employee1.difference_update(employee2)
print(employee1)

# 20. symmetric_difference_update() – Unmatched hashtags between two posts
post1 = {"#fun", "#sun", "#beach"}
post2 = {"#sun", "#travel"}
post1.symmetric_difference_update(post2)
print(post1)

# 21. add() – Add a new holiday to the list
holidays = {"Diwali", "Holi"}
holidays.add("Christmas")
print(holidays)

# 22. remove() – Remove a team member
team = {"Ravi", "Simran", "Neha"}
team.remove("Simran")
print(team)

# 23. discard() – Discard a canceled feature
features = {"Login", "Signup", "Dark Mode"}
features.discard("Payments")  # No error if not found
print(features)

# 24. update() – Add additional tools for a designer
tools = {"Photoshop", "Illustrator"}
tools.update(["Figma", "Canva"])
print(tools)

# 25. intersection_update() – Courses common to two platforms
platform1 = {"Python", "DSA", "Java"}
platform2 = {"Python", "ML", "Java"}
platform1.intersection_update(platform2)
print(platform1)


# ---------------------------------------------------
# 5. Real-World Data Analysis using Python Sets
# ---------------------------------------------------

"""
Real-life scenarios where Python sets are helpful:

- set(): Removes duplicates efficiently
- list: For data storage
- tuple: For storing fixed, unchangeable values
- input/print: For user interaction
- Logical Operators: For filtering, comparing, merging

Below are practical examples using sets.
"""

# 1. Remove duplicate emails (Marketing Campaign)
# Example: A company has email signups from multiple platforms. Duplicates need to be removed before sending newsletters.
emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com"]
unique_emails = set(emails)
print("Unique Emails:", unique_emails)

# 2. Compare listed vs sold products (E-commerce Inventory)
# Example: Identify unsold products at the end of the day.
listed = {"Shoes", "Bag", "Watch", "Perfume"}
sold = {"Bag", "Watch"}
unsold = listed - sold
print("Unsold Products:", unsold)

# 3. Attendance system in a Classroom
# Example: Calculate which students are absent.
present = {"Ram", "Shyam", "Kavita"}
total = {"Ram", "Shyam", "Kavita", "Mohan"}
absent = total - present
print("Absent Students:", absent)

# 4. Unique tags entered by a blog writer (SEO Tags)
# Example: Ensure no repeated tags are added for better search ranking.
tags = set(input("Enter SEO tags separated by space: ").split())
print("Unique Tags:", tags)

# 5. Students in both sports and debate (Activity Analysis)
# Example: Identify multitaskers who participate in both activities.
sports = {"Anil", "Sunil", "Meena"}
debate = {"Meena", "Ravi"}
both = sports & debate
print("In Both Sports and Debate:", both)

# 6. IP Log Filter – Remove Duplicate Access (Server Logs)
ip_logs = ["192.168.0.1", "192.168.0.2", "192.168.0.1"]
unique_ips = set(ip_logs)
print("Unique Visitors:", unique_ips)

# 7. Price Comparison – Common Offers (Shopping App)
amazon = {"TV", "Laptop", "Fan"}
flipkart = {"Fan", "Laptop", "AC"}
common_offers = amazon & flipkart
print("Common Products on Both Sites:", common_offers)

# 8. Merging Contacts from 2 Devices (Phone Sync)
device1 = {"Amit", "Ravi", "Neha"}
device2 = {"Neha", "Simran", "Raj"}
all_contacts = device1 | device2
print("Merged Contacts:", all_contacts)

# 9. Duplicate Names in School Registration (Admin Panel)
registration = ["Aarav", "Riya", "Aarav", "Rohan"]
unique_names = set(registration)
print("Unique Registrations:", unique_names)

# 10. Match Attendees with Registrants (Event Check-In)
registered = {"Ravi", "Anjali", "Sohan"}
checked_in = {"Sohan", "Ravi"}
not_arrived = registered - checked_in
print("Not Yet Arrived Attendees:", not_arrived)

# 11. Missing Records – HR Data Sync
old_records = {"E001", "E002", "E003", "E004"}
new_records = {"E001", "E003"}
missing = old_records - new_records
print("Missing Employee IDs:", missing)

# 12. Keyword Matching in Job Descriptions (Job Portal)
job_keywords = {"Python", "SQL", "Machine Learning", "AI"}
candidate_skills = {"Python", "HTML", "CSS"}
matched = job_keywords & candidate_skills
print("Matched Skills:", matched)

# 13. Find Common Friends on Two Social Networks
facebook = {"Meena", "Rahul", "Sneha"}
linkedin = {"Sneha", "Ravi", "Meena"}
common_friends = facebook & linkedin
print("Common Friends:", common_friends)

# 14. Online Course Enrollments – Unique Students
course_A = {"Amit", "Shreya", "Neha"}
course_B = {"Neha", "Ravi", "Pooja"}
all_students = course_A | course_B
print("Total Unique Enrolled Students:", all_students)

# 15. Remove Suspended IDs from Main List
all_ids = {"ID01", "ID02", "ID03", "ID04"}
suspended = {"ID02", "ID04"}
valid_ids = all_ids - suspended
print("Valid User IDs:", valid_ids)

# 16. Detect Email ID Conflicts Between Departments
hr_emails = {"hr@company.com", "recruit@company.com"}
admin_emails = {"admin@company.com", "hr@company.com"}
conflicts = hr_emails & admin_emails
print("Email Conflicts:", conflicts)

# 17. Matching Discount Codes Used on Two Platforms
app_codes = {"NEW50", "SAVE20", "DIWALI100"}
website_codes = {"SAVE20", "HOLI30", "NEW50"}
reused_codes = app_codes & website_codes
print("Discount Codes Used on Both:", reused_codes)

# 18. Data Merge – Sales from Two Quarters
q1_sales = {"P1", "P2", "P3"}
q2_sales = {"P3", "P4", "P5"}
total_products = q1_sales | q2_sales
print("Total Products Sold:", total_products)

# 19. Remove Outdated SKUs (Inventory Cleanup)
available = {"SKU1", "SKU2", "SKU3", "SKU4"}
obsolete = {"SKU2", "SKU4"}
updated_inventory = available - obsolete
print("Updated Inventory:", updated_inventory)

# 20. Filter Common Authors in Two Journals
journal1_authors = {"Dr. A", "Dr. B", "Dr. C"}
journal2_authors = {"Dr. C", "Dr. D"}
common_authors = journal1_authors & journal2_authors
print("Authors in Both Journals:", common_authors)

# 21. Identify Duplicate Items in Cart (E-commerce)
cart = ["Shoe", "Shoe", "Bag", "Belt"]
unique_cart = set(cart)
print("Cart Without Duplicates:", unique_cart)

# 22. Filter Students Who Submitted Multiple Projects
project1 = {"Riya", "Ankit", "Varun"}
project2 = {"Varun", "Riya", "Divya"}
multi_submitters = project1 & project2
print("Students Submitted Multiple Projects:", multi_submitters)

# 23. Skill Gap Analysis (Training Needs)
required_skills = {"Python", "Excel", "PowerBI"}
employee_skills = {"Excel", "Python"}
gaps = required_skills - employee_skills
print("Training Required For:", gaps)

# 24. Find People Who Didn't Vote (Survey System)
total_people = {"A", "B", "C", "D"}
voted = {"A", "D"}
not_voted = total_people - voted
print("People Who Didn't Vote:", not_voted)

# 25. Compare Uploaded vs Approved Documents
uploaded = {"Doc1", "Doc2", "Doc3"}
approved = {"Doc1", "Doc3"}
pending_approval = uploaded - approved
print("Pending Documents for Approval:", pending_approval)

# --------------------------------------------
# SCENARIO:
# You are managing enrollments for two online courses: "Python Basics" and "Data Analysis".
# You want to:
# - Remove duplicate entries
# - Compare students across courses
# - Filter students who enrolled in at least one course
# - Find students who missed both
# - Merge all enrolled student lists
# - Validate if all students submitted an assignment
# --------------------------------------------

# Step 1: Store course data (with duplicates)
python_course = ["Amit", "Rina", "Zoya", "Amit", "Farhan"]
data_analysis_course = ["Farhan", "Rina", "Raj", "Raj", "Kabir"]

# Remove duplicates using set()
unique_python = set(python_course)
unique_data_analysis = set(data_analysis_course)

# Step 2: Show unique students in both courses
print("Unique Python Course Enrollees:", unique_python)
print("Unique Data Analysis Course Enrollees:", unique_data_analysis)

# Step 3: Students enrolled in both courses (intersection)
common_students = unique_python & unique_data_analysis
print("Students in both courses:", common_students)

# Step 4: Students in Python but not in Data Analysis (difference)
only_python = unique_python - unique_data_analysis
print("Students only in Python course:", only_python)

# Step 5: Students in Data Analysis but not in Python (difference)
only_data = unique_data_analysis - unique_python
print("Students only in Data Analysis course:", only_data)

# Step 6: Students enrolled in either course (union)
all_enrolled = unique_python | unique_data_analysis
print("All enrolled students (merged list):", all_enrolled)

# Step 7: Students who enrolled in exactly one course (symmetric difference)
one_course_only = unique_python ^ unique_data_analysis
print("Students in exactly one course:", one_course_only)

# Step 8: Validate if all students submitted the assignment
submitted = {"Amit", "Rina", "Zoya", "Farhan", "Raj"}  # Tuple could be used here if fixed
missing_submission = all_enrolled - submitted
print("Students who didn’t submit assignments:", missing_submission)

# Step 9: Total registered students (provided by admin)
total_registered = {"Amit", "Rina", "Zoya", "Farhan", "Raj", "Kabir", "Maya", "Tara"}

# Step 10: Who didn’t enroll in any course?
not_enrolled = total_registered - all_enrolled
print("Registered but not enrolled in any course:", not_enrolled)
