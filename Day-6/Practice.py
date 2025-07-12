# 1.Defining a List – Real-World Examples

# 1. A list of employee names in a company
employees = ['Ankit', 'Priya', 'Karan', 'Neha']

# 2. Daily expenses in INR
expenses = [120, 85.5, 210, 64, 390.75]

# 3. Attendance record for a week (True = present, False = absent)
attendance = [True, True, False, True, False, True, True]

# 4. Cities with active service centers
cities = ['Mumbai', 'Delhi', 'Bengaluru', 'Chennai']

# 5. Product prices in a shopping cart
cart_prices = [299.99, 499.00, 1299.50, 99.99]

# 6. Product review ratings
ratings = [4, 5, 3, 4, 5, 2]

# 7. Daily to-do tasks
tasks = ['Email clients', 'Team meeting', 'Code review', 'Submit report']

# 8. University departments
departments = ['Computer Science', 'Biotech', 'Physics', 'Commerce']

# 9. Common website error codes
error_codes = [404, 500, 403, 401, 302]

# 10. Movie genres in a streaming app
genres = ['Action', 'Comedy', 'Drama', 'Thriller', 'Sci-Fi']

# 11. Stock symbols being tracked
stocks = ['TCS', 'INFY', 'RELIANCE', 'HDFCBANK']

# 12. Weekly temperature in Celsius
temperatures = [32.5, 34.0, 33.8, 31.2, 29.5, 30.0, 28.9]

# 13. Laptop RAM configurations
ram_sizes = [8, 16, 32, 64]

# 14. Internet usage in GB over a week
data_usage = [1.2, 0.8, 1.5, 2.0, 0.9, 1.0, 1.3]

# 15. Books available in a library
books = ['Python 101', 'Data Science Basics', 'AI for Everyone']

# 16. Blood groups in a classroom
blood_groups = ['A+', 'B-', 'O+', 'AB+']

# 17. Travel destinations planned
vacation_spots = ['Manali', 'Goa', 'Kerala', 'Jaipur']

# 18. Fees collected from students
fees = [15000, 16000, 15500, 16250, 14900]

# 19. Installed software on a computer
software = ['Chrome', 'VS Code', 'Excel', 'Slack']

# 20. Vehicle numbers parked in society
vehicle_numbers = ['MH12AB1234', 'MH14XY9876', 'MH01ZZ4567']

# 21. Patient admission status in a hospital
patient_status = [True, False, True, True, False]

# 22. Bank transaction types
transactions = ['Withdraw', 'Deposit', 'Transfer', 'Bill Payment']

# 23. Popular programming languages
languages = ['Python', 'JavaScript', 'C++', 'Java']

# 24. Appliance warranty durations in years
warranty_years = [2, 1, 3, 2, 1]

# 25. Favorite fruits
fruits = ['Mango', 'Apple', 'Grapes', 'Watermelon']


# 2. Creating a List – Real-World Examples

# 1. Create a list of exam scores using range()
scores = list(range(60, 101, 10))  # [60, 70, 80, 90, 100]

# 2. List of even numbers from 2 to 20
even_numbers = list(range(2, 21, 2))

# 3. User IDs assigned in a loop
user_ids = list(range(1001, 1006))

# 4. Repeated order status (e.g., 'Pending')
status = ['Pending'] * 4  # ['Pending', 'Pending', 'Pending', 'Pending']

# 5. List from a tuple of countries
countries = list(('India', 'USA', 'UK', 'Canada'))

# 6. Convert a string to list of characters
brand = list('Samsung')  # ['S', 'a', 'm', 's', 'u', 'n', 'g']

# 7. Items in a stationary bill
bill_items = ['Pen', 'Notebook', 'Stapler', 'Marker']

# 8. Create a list using list() constructor
available_colors = list(['Red', 'Blue', 'Black', 'White'])

# 9. Coupons repeated for multiple customers
coupons = ['SAVE10'] * 5

# 10. Create list from dictionary keys
student_dict = {'name': 'Arun', 'age': 22, 'grade': 'A'}
keys = list(student_dict.keys())

# 11. Convert tuple of float values into list
float_values = list((1.1, 2.2, 3.3, 4.4))

# 12. List of months in a semester
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

# 13. Boolean list for switch states
flags = list((True, False, True, False))

# 14. Split a sentence into words (e.g., user input)
quote = 'Learn Code Repeat'
words = quote.split()  # ['Learn', 'Code', 'Repeat']

# 15. Convert string numbers to integers using map()
str_nums = ['1', '2', '3']
int_list = list(map(int, str_nums))

# 16. Convert a set to a list
unique_items = list({'Laptop', 'Tablet', 'Mobile'})

# 17. Generate list of squares using list comprehension
squares = [x*x for x in range(1, 6)]  # [1, 4, 9, 16, 25]

# 18. Laptop brands in stock
laptops = ['HP', 'Dell', 'Lenovo', 'Acer']

# 19. Duplicate a list using list()
backup_list = list(laptops)

# 20. List of bank branches
branches = ['Andheri', 'Borivali', 'Pune', 'Nashik']

# 21. Create a zipped list of names and scores
names_scores = list(zip(['Amit', 'Neha'], [85, 90]))  # [('Amit', 85), ('Neha', 90)]

# 22. List of stringified date numbers
dates = list(map(str, range(1, 6)))  # ['1', '2', '3', '4', '5']

# 23. Customer feedback entries
feedbacks = ['Good', 'Excellent', 'Poor', 'Average']

# 24. Order quantities for items
quantities = [2, 5, 1, 3, 4]

# 25. Create a city list from CSV-style input
city_line = 'Mumbai,Kolkata,Delhi,Chennai'
city_list = city_line.split(',')  # ['Mumbai', 'Kolkata', 'Delhi', 'Chennai']


# 3.Accessing List Elements – Real-World Examples

# 1. Access the first employee name
employees = ['Ankit', 'Priya', 'Karan']
print(employees[0])  # Ankit

# 2. Get last city from list using negative index
cities = ['Delhi', 'Mumbai', 'Pune', 'Chennai']
print(cities[-1])  # Chennai

# 3. Get top 3 expenses from a list
expenses = [200, 450, 120, 700, 330]
print(expenses[:3])  # [200, 450, 120]

# 4. Access middle name in a full name list
full_name = ['Shalini', 'Kumari', 'Verma']
print(full_name[1])  # Kumari

# 5. Access first 2 months from quarter list
q1_months = ['Jan', 'Feb', 'Mar']
print(q1_months[0:2])  # ['Jan', 'Feb']

# 6. Print all laptop brands except the first
brands = ['HP', 'Dell', 'Lenovo', 'Asus']
print(brands[1:])  # ['Dell', 'Lenovo', 'Asus']

# 7. Get last 2 subjects from course list
subjects = ['Math', 'English', 'Science', 'History']
print(subjects[-2:])  # ['Science', 'History']

# 8. Access second review comment
reviews = ['Good', 'Excellent', 'Fair']
print(reviews[1])  # Excellent

# 9. Get every second day from week list
week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
print(week[::2])  # ['Mon', 'Wed', 'Fri']

# 10. Access nested item - phone brand model
mobiles = [['Samsung', 'A23'], ['Apple', 'iPhone 13']]
print(mobiles[1][1])  # iPhone 13

# 11. Get first letter of first fruit
fruits = ['Banana', 'Mango', 'Apple']
print(fruits[0][0])  # B

# 12. Slice all but last item in book list
books = ['Python', 'Java', 'C++']
print(books[:-1])  # ['Python', 'Java']

# 13. Get middle 3 temperatures
temps = [30.1, 31.5, 32.0, 33.3, 34.1]
print(temps[1:4])  # [31.5, 32.0, 33.3]

# 14. Access first character of last name in the list
names = ['Rahul', 'Mona', 'Zara']
print(names[-1][0])  # Z

# 15. Get last 3 characters of a name
name = 'Shalini'
print(name[-3:])  # 'ini'

# 16. Access digits from a string ID in list
ids = ['AX123', 'BX456']
print(ids[0][2:])  # '123'

# 17. Slice list of years for last 2 entries
years = [2019, 2020, 2021, 2022]
print(years[-2:])  # [2021, 2022]

# 18. Get 4th day attendance status
attendance = [True, False, True, True, False]
print(attendance[3])  # True

# 19. Get item from a deep nested list (department → role)
company = [['HR', ['Manager', 'Executive']], ['IT', ['Developer']]]
print(company[0][1][0])  # Manager

# 20. Extract domain from an email list
emails = ['alpha@gmail.com', 'beta@yahoo.com']
print(emails[1].split('@')[1])  # yahoo.com

# 21. Get alternate feedbacks
feedbacks = ['Nice', 'Poor', 'Great', 'Bad']
print(feedbacks[::2])  # ['Nice', 'Great']

# 22. Reverse the list of cities
cities = ['Delhi', 'Mumbai', 'Kolkata']
print(cities[::-1])  # ['Kolkata', 'Mumbai', 'Delhi']

# 23. Split brand string into characters using list
brands = ['Nike']
print(list(brands[0]))  # ['N', 'i', 'k', 'e']

# 24. Print initials from list of names
names = ['Ravi', 'Neha', 'Jay']
print([n[0] for n in names])  # ['R', 'N', 'J']

# 25. Access marks of second student (2nd subject)
marks = [[80, 75], [90, 88], [78, 84]]
print(marks[1][1])  # 88


# 4.List Methods

# 1. Add new order to the list
orders = ['Order1', 'Order2']
orders.append('Order3')  # ['Order1', 'Order2', 'Order3']

# 2. Insert a task at the top of the to-do list
tasks = ['Code', 'Test']
tasks.insert(0, 'Login')  # ['Login', 'Code', 'Test']

# 3. Remove an item from shopping list
shopping = ['Milk', 'Eggs', 'Bread']
shopping.remove('Eggs')  # ['Milk', 'Bread']

# 4. Remove last notification
notifications = ['Email', 'SMS', 'Push']
notifications.pop()  # ['Email', 'SMS']

# 5. Combine two teams
team_a = ['Alice', 'Bob']
team_b = ['Charlie', 'David']
team_a.extend(team_b)  # ['Alice', 'Bob', 'Charlie', 'David']

# 6. Add new movie to watchlist
watchlist = ['Inception', 'Titanic']
watchlist.append('Interstellar')

# 7. Insert emergency contact first
contacts = ['Friend', 'Family']
contacts.insert(0, 'Doctor')

# 8. Remove discontinued course
courses = ['Python', 'Java', 'Ruby']
courses.remove('Ruby')

# 9. Remove item by index from cart
cart = ['Laptop', 'Mouse', 'Keyboard']
cart.pop(1)  # ['Laptop', 'Keyboard']

# 10. Merge morning and evening schedules
morning = ['Jog', 'Shower']
evening = ['Read', 'Dinner']
morning.extend(evening)

# 11. Add today’s expense
expenses = [120, 200]
expenses.append(300)

# 12. Insert newly joined employee
employees = ['Ankit', 'Rahul']
employees.insert(1, 'Neha')

# 13. Remove failed login entry
logins = ['user1', 'user2', 'user3']
logins.remove('user2')

# 14. Remove last product from deals
deals = ['Shoes', 'Watch', 'Bag']
deals.pop()

# 15. Add new books to shelf
shelf = ['Book1', 'Book2']
shelf.extend(['Book3', 'Book4'])

# 16. Add new chat message
chat = ['Hi', 'Hello']
chat.append('How are you?')

# 17. Insert top priority project
projects = ['App', 'Website']
projects.insert(0, 'Migration')

# 18. Remove out-of-stock product
products = ['Pen', 'Pencil', 'Eraser']
products.remove('Eraser')

# 19. Remove third table from list
tables = ['Wood', 'Glass', 'Metal']
tables.pop(2)

# 20. Add students to attendance
students = ['Amit', 'Rita']
students.extend(['Sahil', 'Anu'])

# 21. Add recent video to history
videos = ['Intro', 'Lesson1']
videos.append('Lesson2')

# 22. Insert password request at beginning
requests = ['Reset Email', 'OTP']
requests.insert(0, 'Forgot Password')

# 23. Remove old notification
alerts = ['Low Battery', 'Update', 'Reminder']
alerts.remove('Update')

# 24. Remove last search history
history = ['Google', 'YouTube', 'ChatGPT']
history.pop()

# 25. Merge two order lists
branch1_orders = ['Pizza', 'Burger']
branch2_orders = ['Pasta', 'Coke']
branch1_orders.extend(branch2_orders)


# 5. List Functions – Real-World Examples

# 1. Count total number of students
students = ['Amit', 'Neha', 'Ravi', 'Kavita']
print(len(students))  # 4

# 2. Find maximum sales in a week
sales = [1200, 2200, 1800, 1500]
print(max(sales))  # 2200

# 3. Get the lowest temperature of the day
temperatures = [32.1, 30.5, 29.8, 33.2]
print(min(temperatures))  # 29.8

# 4. Find total marks in 5 subjects
marks = [88, 75, 92, 67, 81]
print(sum(marks))  # 403

# 5. Sort product prices in ascending order
prices = [1500, 299, 450, 1999]
print(sorted(prices))  # [299, 450, 1500, 1999]

# 6. Length of feedback comments received
feedbacks = ['Good', 'Excellent', 'Poor', 'Average']
print(len(feedbacks))  # 4

# 7. Find longest comment (based on length)
comments = ['Nice', 'Very helpful', 'Great course']
print(max(comments, key=len))  # 'Very helpful'

# 8. Find shortest name
names = ['Shalini', 'Jay', 'Mahi', 'Kavita']
print(min(names, key=len))  # 'Jay'

# 9. Total quantity of items in cart
quantities = [2, 1, 3, 5]
print(sum(quantities))  # 11

# 10. Sort names alphabetically
team = ['Vikas', 'Aman', 'Reena', 'Zoya']
print(sorted(team))  # ['Aman', 'Reena', 'Vikas', 'Zoya']

# 11. Count how many tasks are scheduled
tasks = ['Login Page', 'Signup API', 'Database Setup']
print(len(tasks))  # 3

# 12. Find maximum rating given by users
ratings = [3.5, 4.8, 2.0, 4.9]
print(max(ratings))  # 4.9

# 13. Minimum delivery time from options
times = [45, 30, 55, 40]
print(min(times))  # 30

# 14. Total hours spent on projects
hours = [2.5, 4.0, 3.0, 5.0]
print(sum(hours))  # 14.5

# 15. Sort meeting durations
durations = [60, 45, 30, 90]
print(sorted(durations))  # [30, 45, 60, 90]

# 16. Count total messages in inbox
inbox = ['Welcome', 'Offer', 'Reminder']
print(len(inbox))  # 3

# 17. Get subject with smallest name
subjects = ['Math', 'History', 'AI', 'Python']
print(min(subjects, key=len))  # 'AI'

# 18. Get highest donation received
donations = [5000, 10000, 7500, 6200]
print(max(donations))  # 10000

# 19. Sort employee names by alphabetical order
employees = ['Shreya', 'Anuj', 'Bhavna', 'Chetan']
print(sorted(employees))  # ['Anuj', 'Bhavna', 'Chetan', 'Shreya']

# 20. Sum of shopping bill amounts
bills = [220.5, 530.0, 119.9]
print(sum(bills))  # 870.4

# 21. Total classes attended in a week
attendance = [1, 1, 0, 1, 1]
print(sum(attendance))  # 4

# 22. Highest discount percentage available
discounts = [10, 20, 15, 25, 5]
print(max(discounts))  # 25

# 23. Sort list of dates (strings)
dates = ['2024-07-01', '2024-06-29', '2024-07-05']
print(sorted(dates))  # Sorted by string order

# 24. Get total visitors per day for 3 days
visitors = [200, 150, 180]
print(sum(visitors))  # 530

# 25. Find max/min of numeric IDs
user_ids = [1012, 1005, 1098, 1030]
print(max(user_ids), min(user_ids))  # 1098 1005


# 6. Sorting Lists – Real-World Examples 

# 1. Sort student marks in ascending order
marks = [76, 89, 45, 92, 55]
marks.sort()
print(marks)  # [45, 55, 76, 89, 92]

# 2. Sort product prices in descending order
prices = [199, 349, 129, 599]
prices.sort(reverse=True)
print(prices)  # [599, 349, 199, 129]

# 3. Sort names alphabetically
names = ['Ravi', 'Ankit', 'Neha', 'Bina']
names.sort()
print(names)  # ['Ankit', 'Bina', 'Neha', 'Ravi']

# 4. Sort cities in reverse alphabetical order
cities = ['Delhi', 'Mumbai', 'Kolkata']
cities.sort(reverse=True)
print(cities)  # ['Mumbai', 'Kolkata', 'Delhi']

# 5. Sort feedback ratings (float values)
ratings = [3.4, 4.7, 2.1, 5.0]
ratings.sort()
print(ratings)  # [2.1, 3.4, 4.7, 5.0]

# 6. Sort by name length using key
names = ['Jay', 'Shalini', 'Amit']
names.sort(key=len)
print(names)  # ['Jay', 'Amit', 'Shalini']

# 7. Sort names ignoring case
mixed_case = ['banana', 'Apple', 'cherry']
sorted_names = sorted(mixed_case, key=str.lower)
print(sorted_names)  # ['Apple', 'banana', 'cherry']

# 8. Sort mobile brands alphabetically
brands = ['Samsung', 'Xiaomi', 'Apple', 'Realme']
print(sorted(brands))  # ['Apple', 'Realme', 'Samsung', 'Xiaomi']

# 9. Sort file sizes from smallest to largest
sizes = [420, 120, 580, 310]
sizes.sort()
print(sizes)  # [120, 310, 420, 580]

# 10. Sort age list in descending order
ages = [23, 34, 19, 45]
ages.sort(reverse=True)
print(ages)  # [45, 34, 23, 19]

# 11. Sort dates as strings (ISO format)
dates = ['2024-07-02', '2024-06-30', '2024-07-01']
print(sorted(dates))  # ['2024-06-30', '2024-07-01', '2024-07-02']

# 12. Sort stock prices
stocks = [102.5, 98.3, 110.1, 105.0]
print(sorted(stocks))  # [98.3, 102.5, 105.0, 110.1]

# 13. Sort project names alphabetically
projects = ['AI Model', 'Website', 'Mobile App']
print(sorted(projects))  # ['AI Model', 'Mobile App', 'Website']

# 14. Sort a copy of marks list without changing original
marks = [88, 92, 70, 95]
sorted_marks = sorted(marks)
print(sorted_marks)  # [70, 88, 92, 95]

# 15. Sort list of word lengths
words = ['apple', 'is', 'beautiful']
print(sorted(words, key=len))  # ['is', 'apple', 'beautiful']

# 16. Sort products by character count
products = ['Chair', 'Notebook', 'Pen']
products.sort(key=len)
print(products)  # ['Pen', 'Chair', 'Notebook']

# 17. Sort names and store in a new list
students = ['Meena', 'Zoya', 'Ansh']
sorted_students = sorted(students)
print(sorted_students)

# 18. Sort scores with duplicates
scores = [85, 92, 85, 75, 92]
scores.sort()
print(scores)  # [75, 85, 85, 92, 92]

# 19. Sort price list using sorted() without modifying original
prices = [999, 299, 499]
new_prices = sorted(prices)
print(new_prices)  # [299, 499, 999]

# 20. Sort days of week by custom order
days = ['Mon', 'Wed', 'Tue', 'Thu']
order = ['Mon', 'Tue', 'Wed', 'Thu']
days.sort(key=lambda x: order.index(x))
print(days)  # ['Mon', 'Tue', 'Wed', 'Thu']

# 21. Sort strings by last character
names = ['Neha', 'Ravi', 'Ajay']
names.sort(key=lambda x: x[-1])
print(names)  # ['Neha', 'Ajay', 'Ravi']

# 22. Sort nested list by first element
nested = [[2, 'Two'], [1, 'One'], [3, 'Three']]
nested.sort(key=lambda x: x[0])
print(nested)  # [[1, 'One'], [2, 'Two'], [3, 'Three']]

# 23. Sort employee names by second character
names = ['Amit', 'Ravi', 'Neha']
names.sort(key=lambda x: x[1])
print(names)  # ['Neha', 'Ravi', 'Amit']

# 24. Sort real estate prices from low to high
prices = [5500000, 3200000, 4200000]
prices.sort()
print(prices)

# 25. Sort words in a sentence
sentence = 'data analytics makes business better'
words = sentence.split()
print(sorted(words))  # ['analytics', 'better', 'business', 'data', 'makes']


# 50 Real-World Miscellaneous Examples (list, string, operators, input/output)

# 1. Create a to-do list
todo = ['Wake up', 'Exercise', 'Study']
print(todo)

# 2. Add a task
todo.append('Sleep')
print(todo)

# 3. Remove completed task
todo.remove('Exercise')
print(todo)

# 4. Count tasks
print(len(todo))

# 5. Sort tasks
print(sorted(todo))

# 6. Merge grocery and snacks
groceries = ['Rice', 'Oil']
snacks = ['Chips', 'Cookies']
groceries.extend(snacks)
print(groceries)

# 7. Nested list: timetable
timetable = [['Math', '9AM'], ['Science', '10AM']]
print(timetable[0][0])

# 8. Items in cart
cart = ['Shirt', 'Pants', 'Shoes']
print(len(cart))

# 9. Reverse cities
cities = ['Mumbai', 'Delhi', 'Chennai']
cities.reverse()
print(cities)

# 10. Slice top 2 marks
marks = [85, 92, 78, 88]
print(marks[:2])

# 11. Uppercase
name = 'shalini'
print(name.upper())

# 12. Count vowels
sentence = 'Data is powerful'
print(sum(1 for ch in sentence if ch.lower() in 'aeiou'))

# 13. Replace word
quote = 'Data is boring'
print(quote.replace('boring', 'fun'))

# 14. Find word
text = 'Python is easy'
print('Python' in text)

# 15. Join characters
chars = ['P', 'y', 't', 'h', 'o', 'n']
print(''.join(chars))

# 16. Split sentence
sentence = 'Learn Python Now'
print(sentence.split())

# 17. Remove whitespace
raw = '  Hello  '
print(raw.strip())

# 18. Is digit?
s = '123'
print(s.isdigit())

# 19. Capitalize
sentence = 'hello world'
print(sentence.capitalize())

# 20. String slicing
word = 'Analytics'
print(word[1:5])

# 21. Add numbers
a, b = 10, 20
print(a + b)

# 22. Price comparison
price1, price2 = 150, 200
print(price1 < price2)

# 23. Login check
user, pwd = True, True
print(user and pwd)

# 24. Membership test
colors = ['red', 'blue', 'green']
print('blue' in colors)

# 25. Identity check
x = [1, 2, 3]
y = x
print(x is y)

# 26. Even check
num = 12
print(num % 2 == 0)

# 27. Not operator
logged_in = False
print(not logged_in)

# 28. Bitwise OR
print(4 | 1)

# 29. Compound assignment
x = 5
x += 3
print(x)

# 30. String comparison
print('apple' < 'banana')

# 31. User name input
# name = input("Enter name: ")
# print("Hello", name)

# 32. Add two inputs
# x = int(input("Enter 1st: "))
# y = int(input("Enter 2nd: "))
# print("Sum:", x + y)

# 33. Formatted message
user = "Shalini"
age = 28
print(f"{user} is {age} years old")

# 34. Favorite food input
# food = input("Favorite food? ")
# print("You love", food)

# 35. Convert to float
# temp = float(input("Enter temperature: "))
# print("You entered:", temp)

# 36. Print list line-by-line
shopping = ['Milk', 'Eggs', 'Bread']
for item in shopping:
    print(item)

# 37. Age check
# age = int(input("Enter age: "))
# print("Adult" if age >= 18 else "Minor")

# 38. Format float
price = 45.6789
print("Price: {:.2f}".format(price))

# 39. Print stars
stars = 5
print("*" * stars)

# 40. List from input
# data = input("Enter CSV: ")
# print(data.split(","))

# 41. Initials
names = ['Shalini', 'Sharad', 'Sudhakar']
print([n[0] for n in names])

# 42. List of squares
nums = [1, 2, 3, 4]
print([n**2 for n in nums])

# 43. Filter evens
nums = [1, 2, 3, 4, 5]
print([n for n in nums if n % 2 == 0])

# 44. Reverse string
text = 'Python'
print(text[::-1])

# 45. Pair names with scores
names = ['Amit', 'Rita']
scores = [80, 90]
print(list(zip(names, scores)))

# 46. Check if all tasks done
status = [True, True, True]
print(all(status))

# 47. Max salary
salaries = [32000, 54000, 42000]
print(max(salaries))

# 48. Average marks
marks = [85, 90, 80]
print(sum(marks) / len(marks))

# 49. Uppercase fruits
fruits = ['apple', 'banana']
print([f.upper() for f in fruits])

# 50. Multiply each number
nums = [2, 3, 4]
print([n * 2 for n in nums])
