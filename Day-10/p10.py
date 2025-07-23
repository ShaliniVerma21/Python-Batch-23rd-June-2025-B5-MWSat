#Control Structures

"""
Control Structure:
Control structures let you control the flow of execution in your programs.
They decide which block of code runs, depending on conditions.
As- If, if-else, elif, nested, etc.

Indentation
Python uses indentation (spaces or tabs) to define block-level structure 
instead of curly braces {} (like in C/C++/Java).

Convention: 4 spaces per indentation level.

Example:

if condition:
    # indented block runs if condition is True

"""

# 1. Simple if statement
"""
Definition: Executes a block of code only if the condition is true.

Syntax:
if condition:
    # statements

Purpose:
To perform an action when a condition is met.

"""

#Examples : 

# 1. Check temperature
temp = 32
if temp > 30:
    print("It's a hot day!")

# 2. Check bank balance
balance = 1000
if balance >= 500:
    print("Sufficient funds.")

# 3. Check driving age
age = 20
if age >= 18:
    print("You can drive.")

# 4. Door sensor
door_open = True
if door_open:
    print("Door is open.")

# 5. Rain check
is_raining = False
if not is_raining:
    print("You don't need an umbrella.")

# 6. Admin check
user_role = "admin"
if user_role == "admin":
    print("Access granted.")

# 7. High score
score = 95
if score > 90:
    print("You got a high score!")

# 8. Room temperature
room_temp = 25
if room_temp < 30:
    print("Room temperature is comfortable.")

# 9. Morning check
hour = 7
if hour < 12:
    print("Good morning!")

# 10. Stock price
stock_price = 120
if stock_price > 100:
    print("Stock price is above target.")



# 2. if-else Statement

"""
Definition:
Executes one block if condition is true, otherwise executes another block.

Syntax:
if condition:
    # true block
else:
    # false block

Purpose:
To handle two mutually exclusive outcomes.
"""

#Examples

# 1. Pass/fail
marks = 45
if marks >= 40:
    print("Pass")
else:
    print("Fail")

# 2. Login success
username = "user"
if username == "admin":
    print("Welcome, admin!")
else:
    print("Unknown user.")

# 3. Light switch
light_on = False
if light_on:
    print("Light is ON")
else:
    print("Light is OFF")

# 4. Attendance
present = True
if present:
    print("Marked present")
else:
    print("Absent")

# 5. Battery level
battery = 10
if battery < 20:
    print("Low battery warning")
else:
    print("Battery is OK")

# 6. Exam eligibility
attendance_percentage = 80
if attendance_percentage >= 75:
    print("Eligible for exam")
else:
    print("Not eligible for exam")

# 7. Payment status
payment_done = True
if payment_done:
    print("Payment Successful")
else:
    print("Payment Pending")

# 8. Seat availability
seats = 0
if seats > 0:
    print("Seats available")
else:
    print("Sold out")

# 9. Discount offer
purchase_amount = 300
if purchase_amount > 500:
    print("Discount applied")
else:
    print("No discount")

# 10. File existence
file_exists = False
if file_exists:
    print("File found")
else:
    print("File not found")



# 3. elif (Else if) Statement

"""
Definition:
Allows checking multiple conditions sequentially after an initial if.

Syntax:
if condition1:
    # block1
elif condition2:
    # block2
elif condition3:
    # block3
else:
    # default block

Purpose:
To handle multiple possible outcomes with clear priority.
"""

# Examples

# 1. Greeting based on time
time = 18
if time < 12:
    print("Good morning")
elif time < 17:
    print("Good afternoon")
else:
    print("Good evening")

# 2. Grade system
marks = 65
if marks >= 90:
    print("A Grade")
elif marks >= 75:
    print("B Grade")
elif marks >= 60:
    print("C Grade")
else:
    print("D Grade")

# 3. Weather message
temp = 5
if temp > 30:
    print("Hot")
elif temp > 20:
    print("Warm")
elif temp > 10:
    print("Cool")
else:
    print("Cold")

# 4. BMI category
bmi = 28
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

# 5. Membership level
points = 300
if points >= 1000:
    print("Platinum Member")
elif points >= 500:
    print("Gold Member")
else:
    print("Silver Member")

# 6. Traffic light
signal = "yellow"
if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Get ready")
else:
    print("Go")

# 7. Season finder
month = 4
if month in [12, 1, 2]:
    print("Winter")
elif month in [3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer")
else:
    print("Autumn")

# 8. Shipping cost
weight = 15
if weight <= 5:
    print("Low shipping cost")
elif weight <= 10:
    print("Medium shipping cost")
else:
    print("High shipping cost")

# 9. Exam result
percentage = 55
if percentage >= 85:
    print("Excellent")
elif percentage >= 60:
    print("Good")
elif percentage >= 40:
    print("Average")
else:
    print("Poor")

# 10. Internet speed
speed = 50
if speed >= 100:
    print("Ultra-fast internet")
elif speed >= 50:
    print("Fast internet")
else:
    print("Slow internet")



# 4. Nested if Statement

"""
Definition:
Placing an if statement inside another if block.

Syntax:
if outer_condition:
    if inner_condition:
        # nested block

Purpose:
To check multiple related conditions hierarchically.
"""

# Examples

# 1. Job eligibility
age = 25
degree = "Bachelor"
if age >= 18:
    if degree == "Bachelor":
        print("Eligible for job")

# 2. Purchase decision
price = 800
budget = 1000
if budget >= price:
    if price > 500:
        print("Purchase with discount")
    else:
        print("Purchase without discount")

# 3. Exam pass with grace
marks = 38
if marks < 40:
    if marks >= 35:
        print("Pass with grace marks")
    else:
        print("Fail")

# 4. File operations
file_open = True
file_type = "text"
if file_open:
    if file_type == "text":
        print("Read text file")
    else:
        print("Unsupported file type")

# 5. Security check
is_logged_in = True
is_admin = True
if is_logged_in:
    if is_admin:
        print("Admin panel access")
    else:
        print("User panel access")

# 6. Car start
key_in_ignition = True
fuel_available = True
if key_in_ignition:
    if fuel_available:
        print("Car started")
    else:
        print("Refuel needed")

# 7. Online class attendance
is_student_logged = True
class_active = True
if is_student_logged:
    if class_active:
        print("Attend class")
    else:
        print("Class not started yet")

# 8. ATM withdrawal
card_inserted = True
pin_correct = False
if card_inserted:
    if pin_correct:
        print("Withdrawal allowed")
    else:
        print("Incorrect PIN")

# 9. Game play
logged_in = True
has_subscription = False
if logged_in:
    if has_subscription:
        print("Play premium games")
    else:
        print("Play free games")

# 10. Voting eligibility
age = 20
citizen = True
if age >= 18:
    if citizen:
        print("Eligible to vote")
    else:
        print("Citizenship required")

