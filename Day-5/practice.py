#1. Defining Strings

# Example 1: Product name
product_name = "iPhone 15 Pro"

# Example 2: Email address
email = "contact@example.com"

# Example 3: Website URL
website = "https://www.python.org"

# Example 4: Error message
error_msg = "File not found."

# Example 5: Success message
success_msg = "Data saved successfully."

# Example 6: Book title
book = 'To Kill a Mockingbird'

# Example 7: Movie title
movie = "The Shawshank Redemption"

# Example 8: Password (don't do this in real code!)
password = "mySecret123"

# Example 9: Car model
car = "Tesla Model Y"

# Example 10: Country name
country = "Japan"

# Example 11: Favorite quote
quote = 'The only limit to our realization of tomorrow is our doubts of today.'

# Example 12: Social media handle
handle = "@python_coder"

# Example 13: Department name
department = "Human Resources"

# Example 14: Street address
address = "221B Baker Street"

# Example 15: Song title
song = "Bohemian Rhapsody"

# Example 16: City name
city = "San Francisco"

# Example 17: Username
username = "coolguy99"

# Example 18: Payment method
payment = "Credit Card"

# Example 19: WiFi network name
wifi = "Home_Network_5G"

# Example 20: Task description
task = "Finish the Python project."

# Example 21: Travel destination
destination = "Paris"

# Example 22: Event name
event = "Summer Music Festival"

# Example 23: Currency code
currency = "USD"

# Example 24: Customer review
review = "Great product, fast delivery!"

# Example 25: Recipe name
recipe = "Classic Pancakes"


#2. Accessing Elements of Strings

title = "Artificial Intelligence"

# Example 1: Get first character
print(title[0])  # A

# Example 2: Get second character
print(title[1])  # r

# Example 3: Get last character
print(title[-1])  # e

# Example 4: Middle character
print(title[len(title)//2])  # i

# Example 5: First word using slicing
print(title[0:10])  # Artificial

# Example 6: Second word using slicing
print(title[11:])  # Intelligence

# Example 7: Every second letter
print(title[::2])  # AtfclIelgne

# Example 8: Reversed string
print(title[::-1])  # ecnegilletnI laicifitrA

# Example 9: Third from end
print(title[-3])  # c

# Example 10: Characters from index 5 to 9
print(title[5:10])  # cial

# Example 11: First three letters
print(title[:3])  # Art

# Example 12: From 5th character to end
print(title[5:])  # cial Intelligence

# Example 13: Characters excluding first and last
print(title[1:-1])  # rtificial Intelligenc

# Example 14: Every third character
print(title[::3])  # Aftclte

# Example 15: All except last two characters
print(title[:-2])  # Artificial Intelligenc

# Example 16: Last five characters
print(title[-5:])  # gence

# Example 17: First half of string
print(title[:len(title)//2])  # Artificia

# Example 18: Second half of string
print(title[len(title)//2:])  # l Intelligence

# Example 19: From index 2 to 7
print(title[2:8])  # tifici

# Example 20: Negative slicing from -10 to -1
print(title[-10:-1])  # telligenc

# Example 21: Index 8 character
print(title[8])  # l

# Example 22: Index -8 character
print(title[-8])  # t

# Example 23: Single character slice
print(title[4:5])  # f

# Example 24: Slice with step -2 reversed
print(title[::-2])  # egeletIciAr

# Example 25: Slice with step 1 (copy entire string)
print(title[::1])  # Artificial Intelligence


#3. String Methods

info = "   python is Amazing!   "

# Example 1: Remove whitespace
print(info.strip())

# Example 2: Convert to uppercase
print(info.upper())

# Example 3: Convert to lowercase
print(info.lower())

# Example 4: Swap case
print(info.swapcase())

# Example 5: Title case
print(info.title())

# Example 6: Check starts with "python"
print(info.strip().startswith("python"))

# Example 7: Check ends with "Amazing!"
print(info.strip().endswith("Amazing!"))

# Example 8: Count occurrences of 'a'
print(info.lower().count('a'))

# Example 9: Find first index of 'i'
print(info.find('i'))

# Example 10: Find last index of 'i'
print(info.rfind('i'))

# Example 11: Replace word
print(info.replace("Amazing", "Powerful"))

# Example 12: Split into words
print(info.strip().split())

# Example 13: Join words with hyphen
words = ['Data', 'Science', 'Rocks']
print('-'.join(words))

# Example 14: Center the string
print(info.strip().center(30, '*'))

# Example 15: Left justify
print(info.strip().ljust(30, '-'))

# Example 16: Right justify
print(info.strip().rjust(30, '-'))

# Example 17: Check isdigit
print("12345".isdigit())

# Example 18: Check isalpha
print("Python".isalpha())

# Example 19: Check islower
print("hello".islower())

# Example 20: Check isupper
print("HELLO".isupper())

# Example 21: Expand tabs
print("A\tB\tC".expandtabs(4))

# Example 22: Partition string
print(info.strip().partition('is'))

# Example 23: Zero-fill numbers
print("42".zfill(5))  # 00042

# Example 24: Encode string
print(info.encode())

# Example 25: Check if string is printable
print("Hello\nWorld".isprintable())  # False because of newline


#4. Type-Casting

# Example 1: Integer to string
num = 42
print(str(num))

# Example 2: Float to string
flt = 3.14
print(str(flt))

# Example 3: Boolean to string
flag = True
print(str(flag))

# Example 4: List to string (via join)
lst = ['apple', 'banana']
print(', '.join(lst))

# Example 5: String number to int
print(int("250"))

# Example 6: String number to float
print(float("99.99"))

# Example 7: Float to int (truncates decimal)
print(int(12.75))

# Example 8: Int to float
print(float(8))

# Example 9: Int to complex
print(complex(5))

# Example 10: Float to complex
print(complex(0, 5.5))

# Example 11: Boolean to int
print(int(True))  # 1

# Example 12: Boolean to float
print(float(False))  # 0.0

# Example 13: String to list of characters
print(list("Code"))

# Example 14: String to tuple of characters
print(tuple("Code"))

# Example 15: List of tuples to dict
pairs = [('a', 1), ('b', 2)]
print(dict(pairs))

# Example 16: Set to list
print(list({1, 2, 3}))

# Example 17: List to set (remove duplicates)
print(set([1, 1, 2, 3]))

# Example 18: Number to binary
print(bin(7))

# Example 19: Number to octal
print(oct(7))

# Example 20: Number to hexadecimal
print(hex(255))

# Example 21: Char to ASCII value
print(ord('A'))

# Example 22: ASCII value to char
print(chr(66))

# Example 23: Float string to decimal precision
print(round(float("123.4567"), 2))

# Example 24: List of strings to list of integers
nums = ["1", "2", "3"]
print([int(n) for n in nums])

# Example 25: String 'True' to boolean manually
print(True if "True" == "True" else False)


#5. Input and Output

# Example 1: Ask user's name
name = input("Enter your name: ")

# Example 2: Greet the user
print("Hello,", name)

# Example 3: Ask age and print it
age = input("How old are you? ")
print("You are", age, "years old.")

# Example 4: Ask favorite color
color = input("What is your favorite color? ")
print("Nice choice:", color)

# Example 5: Ask city and confirm
city = input("Which city do you live in? ")
print("You live in", city)

# Example 6: Ask for feedback
feedback = input("Please share your feedback: ")
print("Thanks for your feedback:", feedback)

# Example 7: Ask product rating
rating = input("Rate the product (1-5): ")
print("Your rating is", rating)

# Example 8: Ask favorite programming language
language = input("Favorite programming language: ")
print(language, "is awesome!")

# Example 9: Ask for email
email = input("Enter your email: ")
print("Your email is", email)

# Example 10: Ask if they like pizza
pizza = input("Do you like pizza? (yes/no): ")
print("You answered:", pizza)

# Example 11: Ask mobile number
mobile = input("Enter your mobile number: ")
print("Your number is", mobile)

# Example 12: Ask favorite sport
sport = input("Favorite sport: ")
print(sport, "is exciting!")

# Example 13: Ask dream job
job = input("What's your dream job? ")
print("Dream job:", job)

# Example 14: Ask weekend plans
plans = input("Weekend plans? ")
print("Sounds fun:", plans)

# Example 15: Ask birthday month
month = input("Your birth month: ")
print("You were born in", month)

# Example 16: Ask how many siblings
siblings = input("How many siblings do you have? ")
print("Siblings:", siblings)

# Example 17: Ask favorite movie genre
genre = input("Favorite movie genre: ")
print("You like", genre, "movies.")

# Example 18: Ask country of travel
travel = input("Where would you like to travel? ")
print("Dream destination:", travel)

# Example 19: Ask favorite food
food = input("Favorite food: ")
print("Yum! I like", food, "too!")

# Example 20: Ask for pet’s name
pet = input("Do you have a pet? What's its name? ")
print("Pet's name:", pet)

# Example 21: Ask for favorite season
season = input("Favorite season (spring/summer/fall/winter): ")
print("You love", season)

# Example 22: Ask for lucky number
lucky = input("What is your lucky number? ")
print("Lucky number is", lucky)

# Example 23: Ask for hobbies
hobbies = input("What are your hobbies? ")
print("Great hobbies:", hobbies)

# Example 24: Ask favorite superhero
hero = input("Favorite superhero: ")
print(hero, "is legendary!")

# Example 25: Ask for favorite app
app = input("Which app do you use the most? ")
print("You love using", app)



#6.String Formatting

# Example 1: Using f-string for greeting
name = "Alice"
print(f"Hello, {name}!")

# Example 2: Using format() with multiple variables
age = 30
city = "Paris"
print("I am {} and I live in {}.".format(age, city))

# Example 3: Formatting numbers with two decimal places
price = 19.99
print(f"Price: ${price:.2f}")

# Example 4: Using % operator with strings
language = "Python"
print("I love %s programming!" % language)

# Example 5: Zero-padding number
order = 7
print(f"Order number: {order:03}")

# Example 6: Align text to right
text = "Welcome"
print(f"{text:>20}")

# Example 7: Align text to left
print(f"{text:<20}END")

# Example 8: Center text
print(f"{text:^20}")

# Example 9: Escaping curly braces
print(f"{{ This is inside curly braces }}")

# Example 10: Named placeholders
print("My name is {name} and I am {age} years old.".format(name="Bob", age=28))

# Example 11: Formatting percentage
percent = 0.876
print(f"Success rate: {percent:.2%}")

# Example 12: Binary format
num = 5
print(f"Binary of {num}: {num:b}")

# Example 13: Hexadecimal format
print(f"Hexadecimal: {255:x}")

# Example 14: Octal format
print(f"Octal: {255:o}")

# Example 15: Exponential notation
big_num = 1234567
print(f"Scientific: {big_num:e}")

# Example 16: Truncate long text
long_text = "This is a long sentence."
print(f"{long_text:.10}")

# Example 17: Currency formatting
amount = 45.678
print(f"Amount: ${amount:.2f}")

# Example 18: Positional placeholders
print("{0} {1} {0}".format("abra", "cadabra"))

# Example 19: Complex sentence
user = "Eve"
points = 950
print(f"User {user} has {points} points!")

# Example 20: Format with thousands separator
num = 123456789
print(f"Population: {num:,}")

# Example 21: Multiple f-strings in one line
temp, humidity = 28, 70
print(f"Temp: {temp}°C, Humidity: {humidity}%")

# Example 22: Print boolean value
is_active = True
print(f"Active: {is_active}")

# Example 23: Format to include quotes
word = "amazing"
print(f'This is an "{word}" example.')

# Example 24: Reorder placeholders
print("{2}, {0}, {1}".format("A", "B", "C"))

# Example 25: Chained f-string
subtotal = 100
tax = 0.15
print(f"Total: ${subtotal + subtotal * tax:.2f}")


#7. Print function

# Example 1: Basic print
print("Welcome to Python!")

# Example 2: Print two strings
print("Hello", "World")

# Example 3: Print multiple variables
x, y = 5, 10
print("x =", x, "y =", y)

# Example 4: Use custom separator
print("apple", "banana", "cherry", sep=", ")

# Example 5: Print without newline
print("Hello", end=" ")
print("World!")

# Example 6: Multiline print
print("Line1\nLine2\nLine3")

# Example 7: Print list directly
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Example 8: Print dictionary
student = {"name": "John", "age": 20}
print(student)

# Example 9: Print with tabs
print("A\tB\tC")

# Example 10: Escape double quotes
print("He said, \"Python is great!\"")

# Example 11: Escape single quotes
print('It\'s a beautiful day.')

# Example 12: Unicode character
print("Smile: \u263A")

# Example 13: Print emoji
print("Python 🐍 is fun!")

# Example 14: Print stars pattern
print("*" * 10)

# Example 15: Combine text and math
a, b = 4, 3
print(f"{a} + {b} = {a + b}")

# Example 16: Print boolean value
status = True
print("Status:", status)

# Example 17: Print float with precision
pi = 3.14159
print("Pi rounded:", round(pi, 2))

# Example 18: Nested print inside f-string
print(f"Sum: {print(1+1)}")  # prints 2 first

# Example 19: Raw string to ignore escape
print(r"C:\Users\Name")

# Example 20: Print empty line
print()

# Example 21: Print with formatting
name = "Alice"
print(f"Name: {name:>10}")

# Example 22: Print multiple types
print("Number:", 42, "Float:", 3.14, "String:", "text")

# Example 23: Print from loop
for i in range(3):
    print("Loop:", i)

# Example 24: Print separator line
print("-" * 40)

# Example 25: Print large numbers with commas
big_num = 1000000
print(f"Big number: {big_num:,}")
