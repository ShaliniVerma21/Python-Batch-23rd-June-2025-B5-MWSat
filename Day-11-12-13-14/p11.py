#------------------------------ Loops Statements -----------------------------------

# Loops are used to execute a block of code repeatedly for a specified number of times.

num1=1
num2=2
num3=3
num4=4
num5=5
# Using for loop to print numbers from 1 to 5
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
# Using for loop to print numbers from 1 to 5
for i in range(1,6):
    print(i)

""" 
1. while Loop --> The while loop continues executing a block as long as the condition is True.

Syntax :

while condition:
    # block of code

"""

# Examples:

# Example 1: Print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1

# Example 2: Print even numbers less than 10
num = 2
while num < 10:
    print(num)
    num += 2

# Example 3: Sum of numbers till 100
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
    print("Total:", total)

# Example 4: Countdown timer
count = 5
while count > 0:
    print(count)
    count -= 1

# Example 5: Validating user input
user_input = ""
while user_input != "yes":
    user_input = input("Type 'yes' to continue: ")


""" 
2. Simulated do-while Loop (Python doesn't have built-in do-while)

A do-while loop executes the block at least once and then checks the condition.
If the condition is False, it stops the loop.

Syntax :  Simulated using while True and break
"""

#Examples:

# Example 1: Print number once, then check
i = 1
while True:
    print(i)
    if i >= 5:
        break
    i += 1

# Example 2: User password input validation
while True:
    password = input("Enter password: ")
    if password == "admin":
        print("Access granted")
        break

# Example 3: Menu simulation
while True:
    print("1. Start\n2. Exit")
    choice = input("Enter choice: ")
    if choice == "2":
        break

# Example 4: Sum input until 0
while True:
    num = int(input("Enter number (0 to stop): "))
    if num == 0:
        break

# Example 5: Print even numbers till 10
i = 0
while True:
    i += 2
    print(i)
    if i >= 10:
        break

"""
3. for Loop --> A for loop is used to iterate over a sequence (like list, tuple, string, range).

Syntax:
for variable in sequence:
    # block
    
"""

#Examples:
# Example 1: Print numbers 1 to 5
for i in range(1, 6):
    print(i)

# Example 2: Print characters in a string
for char in "Python":
    print(char)

# Example 3: Sum of numbers using for loop
total = 0
for i in range(101):
    total += i
print("Sum:", total)

# Example 4: Print table of 3
for i in range(1, 11):
    print("3 x", i, "=", 3 * i)

# Example 5: Countdown from 5
for i in range(5, 0, -1):
    print(i)


""" 
 4. for Loop when iterating over collections.
"""

# Example 1: List items
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example 2: Dictionary keys and values
person = {"name": "John", "age": 25}
for key, value in person.items():
    print(key, ":", value)

# Example 3: Set elements
colors = {"red", "blue", "green"}
for color in colors:
    print(color)

# Example 4: Tuple iteration
nums = (10, 20, 30)
for num in nums:
    print(num)

# Example 5: Iterating over string
for ch in "HELLO":
    print(ch)

""" 
 5. Nested Loops

A loop inside another loop. Useful for grids, patterns, matrices, etc.

"""

# Example 1: Print matrix
for i in range(3):
    for j in range(3):
        print(i, j)
    print()  # Empty line for better readability

# Example 2: Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="\t")
    print()

# Example 3: Star pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Example 4: Number grid
for i in range(1, 4):
    for j in range(1, 4):
        print(j, end=" ")
    print()

# Example 5: Nested list processing
matrix = [[1,2], [3,4], [5,6]]
for row in matrix:
    for val in row:
        print(val)


""" 
6. break Statement

break is used to exit the loop prematurely.
"""

# Example 1: Stop loop at 5
for i in range(10):
    if i == 5:
        break
    print(i)

# Example 2: While loop break
i = 1
while True:
    if i > 3:
        break
    print(i)
    i += 1

# Example 3: Loop user input until 'exit'
while True:
    cmd = input("Type 'exit' to stop: ")
    if cmd == "exit":
        break

# Example 4: Stop on negative number
nums = [1, 2, 3, -1, 4]
for n in nums:
    if n < 0:
        break
    print(n)

# Example 5: Break in nested loop
for i in range(3):
    for j in range(3):
        if j == 2:
            break
        print(i, j)

""" 
 7. continue Statement

continue skips the current loop iteration and moves to the next one.
"""

# Example 1: Skip even numbers
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i)

# Example 2: Skip specific item
names = ["John", "", "Mike"]
for name in names:
    if name == "":
        continue
    print(name)

# Example 3: Skip on condition
for i in range(1, 6):
    if i == 3:
        continue
    print("Number:", i)

# Example 4: Skip zero division
nums = [1, 0, 2]
for n in nums:
    if n == 0:
        continue
    print(10 / n)

# Example 5: Continue in while loop
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

""" 
8. else with Loops

else in loop runs only if the loop completes normally (no break).
"""

# Example 1: Simple for-else
for i in range(5):
    print(i)
else:
    print("Loop completed")

# Example 2: Break prevents else
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Will not print")

# Example 3: While-else
x = 0
while x < 3:
    print(x)
    x += 1
else:
    print("While finished")

# Example 4: Search success check
for item in [1, 2, 3]:
    if item == 4:
        print("Found")
        break
else:
    print("Not Found")

# Example 5: No break, so else runs
for i in [10, 20, 30]:
    print(i)
else:
    print("Loop done")

""" 
 9. Infinite Loop

A loop that never ends unless broken manually.
"""

# Example 1: Basic infinite loop
while True:
    print("Running...")
    break

# Example 2: Menu system
while True:
    print("1. Show\n2. Exit")
    if input("Choice: ") == "2":
        break

# Example 3: Server ping simulation
while True:
    print("Pinging server...")
    break  # Simulate stop

# Example 4: Countdown until stop
while True:
    stop = input("Stop? (yes): ")
    if stop == "yes":
        break

# Example 5: Retry until correct
while True:
    code = input("Enter code: ")
    if code == "1234":
        print("Correct")
        break

""" 
10. List/Dict Comprehensions (Loop Shortcuts)

Comprehensions offer a short syntax for loops inside lists, sets, and dicts.
"""

# Example 1: Squares list
squares = [x**2 for x in range(5)]
print(squares)

# Example 2: Even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# Example 3: Dictionary comprehension
sqr_dict = {x: x**2 for x in range(3)}
print(sqr_dict)

# Example 4: String to char list
chars = [ch for ch in "Data"]
print(chars)

# Example 5: Filter names
names = ["Ram", "Raj", "Rani"]
r_names = [name for name in names if name.startswith("R")]
print(r_names)
