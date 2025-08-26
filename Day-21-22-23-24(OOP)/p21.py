""" 
What is Object Oriented Programming?

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects, which represent real-world entities.
Each object contains:

--> Properties (Data/Variables) → describe the object.
--> Behaviors (Methods/Functions) → actions the object can perform.

Note- OOP allows modularity, reusability, scalability, and cleaner project structures. 
It is heavily used in software development, data analysis, machine learning, and web applications.

4 pillars of oops :

1.Inheritance — Build on existing classes
2.Polymorphism — Same method name, different behaviors
3.Abstraction — Hide internals, show an interface
4.Data Encapsulation — Protect and validate data


Class :
A class is a blueprint/template used to create objects. It defines properties (attributes) and behaviors (methods).

Example : Person, Employee, Bank, etc

Important Points:
1. Defined using the class keyword.
2. Attributes → variables inside a class.
3. Methods → functions inside a class.
4. A class itself does not hold data → objects store actual values.

Syntax : 
class ClassName:
    # code


Object :
An object is an instance of a class. Each object has its own state (attributes) and behavior (methods).

Example : Dog, Chair, laptop etc

Important Points:
1. Created from a class.
2. Each object has its own copy of attributes.
3. Multiple objects can be created from one class.

Syntax : 
object_name = ClassName(arguments)


constructors : 
A constructor (__init__) is a special function that is automatically called when a new object is created.

Important Points:
1. Always named __init__.
2. Used to initialize attributes.
3. Runs only once when the object is created.

Syntax:
class ClassName:
    def __init__(self, arg1, arg2):
        self.attr1 = arg1
        self.attr2 = arg2

What is self in Constructor?

--> self is a reference to the current object.
--> It allows you to access variables & methods inside the class.
--> Every instance (object) passes itself as the first argument automatically.

 Example: (Here, self.brand & self.color are different for each object.)
 
 class Car:
    def __init__(self, brand, color):
        self.brand = brand     # self.brand belongs to the current object
        self.color = color

c1 = Car("BMW", "Black")
c2 = Car("Audi", "Red")

print(c1.brand, c1.color)   # BMW Black
print(c2.brand, c2.color)   # Audi Red


Functions/Methods : 
Methods are functions inside a class that define the behavior of objects.

Example: start(), run(), post()

Important Points:
1. Always have self as the first parameter → refers to the current object.
2. Can modify attributes of the object.
3. Types: Instance methods, Class methods, Static methods.

Syntax : 
class ClassName:
    def method_name(self, args):
        # code


Instead of writing code in a linear way, OOP allows us to structure programs like the real world:

1. Car → has properties like color, model, speed and behaviors like start(), stop(), accelerate().
2. Student → has properties like name, age, marks and behaviors like study(), give_exam().
3. Bank Account → has properties like account_number, balance and behaviors like deposit(), withdraw(), check_balance().
4. Employee → has properties like name, position, salary and behaviors like work(), get_salary(), promote().
5. Book → has properties like title, author, available_status and behaviors like borrow(), return_book().

""" 
# Real-world Examples using classes, objects, constructor & functions

# ============================
# Real-world Examples in Python
# Classes, Objects, Constructors, Variables & Functions
# ============================

# 1) Car Example
class Car:
    def __init__(self, color, model, speed, fuel, owner):
        self.color = color
        self.model = model
        self.speed = speed
        self.fuel = fuel
        self.owner = owner

    def start(self):
        print(f"{self.model} owned by {self.owner} started")

    def accelerate(self):
        self.speed += 10
        print(f"{self.model} speed increased to {self.speed} km/h")


car1 = Car("Red", "Honda Civic", 60, "Petrol", "Alice")
car2 = Car("Blue", "Toyota Corolla", 50, "Diesel", "Bob")
car1.start()
car1.accelerate()
car2.start()
car2.accelerate()


# 2) Student Example
class Student:
    def __init__(self, name, age, marks, course, roll_no):
        self.name = name
        self.age = age
        self.marks = marks
        self.course = course
        self.roll_no = roll_no

    def study(self):
        print(f"{self.name} is studying {self.course}")

    def give_exam(self):
        print(f"{self.name} scored {self.marks} marks in the exam")


s1 = Student("Ravi", 20, 88, "BBA", 101)
s2 = Student("Sneha", 21, 92, "BCA", 102)
s1.study()
s1.give_exam()
s2.study()
s2.give_exam()


# 3) Bank Account Example
class BankAccount:
    def __init__(self, acc_num, balance, holder, branch, bank_name):
        self.acc_num = acc_num
        self.balance = balance
        self.holder = holder
        self.branch = branch
        self.bank_name = bank_name

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.holder} deposited {amount}. Balance = {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.holder} withdrew {amount}. Balance = {self.balance}")
        else:
            print("Insufficient funds")


acc1 = BankAccount(1001, 5000, "Rohit", "Delhi", "SBI")
acc2 = BankAccount(1002, 8000, "Anita", "Mumbai", "HDFC")
acc1.deposit(2000)
acc1.withdraw(1000)
acc2.deposit(3000)
acc2.withdraw(9000)


# 4) Employee Example
class Employee:
    def __init__(self, name, position, salary, emp_id, department):
        self.name = name
        self.position = position
        self.salary = salary
        self.emp_id = emp_id
        self.department = department

    def work(self):
        print(f"{self.name} is working in {self.department} department")

    def promote(self, amount):
        self.salary += amount
        print(f"{self.name} promoted! New salary: {self.salary}")


e1 = Employee("Vikram", "Manager", 50000, 201, "HR")
e2 = Employee("Kiran", "Developer", 40000, 202, "IT")
e1.work()
e1.promote(5000)
e2.work()
e2.promote(8000)


# 5) Book Example
class Book:
    def __init__(self, title, author, genre, year, pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.pages = pages
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"{self.title} borrowed")
        else:
            print(f"{self.title} is not available")

    def return_book(self):
        self.available = True
        print(f"{self.title} returned")


b1 = Book("Python Basics", "Guido", "Education", 2020, 350)
b2 = Book("AI Future", "John", "Technology", 2022, 280)
b1.borrow()
b1.return_book()
b2.borrow()
b2.return_book()


""" 
Types of Constructors in Python : 
Unlike Java/C++, Python officially supports only one constructor (__init__), but we can categorize them as:

1. Default Constructor
No parameters (except self).
Initializes with fixed/default values.

Example : 
"""
class Student:
    def __init__(self):  # default constructor
        self.name = "Unknown"
        self.age = 18

s1 = Student()
print(s1.name, s1.age)   # Output: Unknown 18


""" 
2. Parameterized Constructor
Takes arguments to initialize attributes dynamically.

Example: 
"""
class Student:
    def __init__(self, name, age):  # parameterized constructor
        self.name = name
        self.age = age

s1 = Student("Amit", 20)
print(s1.name, s1.age)   # Output: Amit 20

""" 
3. Copy Constructor (Not built-in, but created manually)
Used to create a new object as a copy of another object.
Python doesn’t have an inbuilt copy constructor like C++, but we can implement it ourselves.

Example : 
"""
class Student:
    def __init__(self, name, age):  
        self.name = name
        self.age = age

    # copy constructor
    @classmethod
    def copy(cls, obj):
        return cls(obj.name, obj.age)

s1 = Student("Riya", 21)
s2 = Student.copy(s1)   # making a copy of s1
print(s2.name, s2.age)  # Output: Riya 21


# 6) Laptop Example
class Laptop:
    def __init__(self, brand, ram, storage, os, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.os = os
        self.price = price

    def upgrade_ram(self, extra):
        self.ram += extra
        print(f"{self.brand} RAM upgraded to {self.ram}GB")

    def show_specs(self):
        print(f"{self.brand} Laptop → RAM: {self.ram}GB, Storage: {self.storage}GB, OS: {self.os}, Price: ₹{self.price}")


lap1 = Laptop("Dell", 8, 512, "Windows 11", 55000)
lap2 = Laptop("Apple", 16, 1024, "macOS", 120000)
lap1.show_specs()
lap1.upgrade_ram(4)
lap2.show_specs()
lap2.upgrade_ram(8)


# 7) Teacher Example
class Teacher:
    def __init__(self, name, subject, exp, emp_id, salary):
        self.name = name
        self.subject = subject
        self.exp = exp
        self.emp_id = emp_id
        self.salary = salary

    def teach(self):
        print(f"{self.name} is teaching {self.subject}")

    def increment_salary(self, amount):
        self.salary += amount
        print(f"{self.name}'s new salary is ₹{self.salary}")


t1 = Teacher("Meena", "Maths", 10, 301, 40000)
t2 = Teacher("Rajesh", "English", 8, 302, 35000)
t1.teach()
t1.increment_salary(5000)
t2.teach()
t2.increment_salary(7000)


# 8) Dog Example
class Dog:
    def __init__(self, name, breed, age, color, owner):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
        self.owner = owner

    def bark(self):
        print(f"{self.name} ({self.breed}) says Woof!")

    def show_info(self):
        print(f"Dog: {self.name}, Breed: {self.breed}, Age: {self.age}, Color: {self.color}, Owner: {self.owner}")


d1 = Dog("Tommy", "Labrador", 3, "Golden", "Amit")
d2 = Dog("Sheru", "German Shepherd", 4, "Black", "Priya")
d1.bark()
d1.show_info()
d2.bark()
d2.show_info()


# 9) Restaurant Example
class Restaurant:
    def __init__(self, name, location, rating, cuisine, owner):
        self.name = name
        self.location = location
        self.rating = rating
        self.cuisine = cuisine
        self.owner = owner
        self.menu = {}

    def add_item(self, item, price):
        self.menu[item] = price
        print(f"{item} added to {self.name} menu")

    def show_menu(self):
        print(f"{self.name} ({self.cuisine}) Menu: {self.menu}")


r1 = Restaurant("Foodies Hub", "Delhi", 4.5, "Indian", "Sunita")
r2 = Restaurant("Pizza World", "Mumbai", 4.2, "Italian", "Rakesh")
r1.add_item("Paneer Tikka", 250)
r1.show_menu()
r2.add_item("Margherita Pizza", 300)
r2.show_menu()


# 10) Shopping Cart Example
class ShoppingCart:
    def __init__(self, user, date, store, cart_id, location):
        self.user = user
        self.date = date
        self.store = store
        self.cart_id = cart_id
        self.location = location
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item} added to cart {self.cart_id}")

    def show_cart(self):
        print(f"Cart {self.cart_id} ({self.user}) Items: {self.items}")


c1 = ShoppingCart("Anil", "2025-08-26", "Amazon", 101, "Delhi")
c2 = ShoppingCart("Sonia", "2025-08-26", "Flipkart", 102, "Mumbai")
c1.add_item("Laptop")
c1.show_cart()
c2.add_item("Shoes")
c2.show_cart()


# 11) Phone Example
class Phone:
    def __init__(self, brand, number, model, os, price):
        self.brand = brand
        self.number = number
        self.model = model
        self.os = os
        self.price = price

    def call(self, other_number):
        print(f"{self.brand} {self.model} calling {other_number} from {self.number}")

    def show_info(self):
        print(f"Phone: {self.brand} {self.model}, OS: {self.os}, Price: ₹{self.price}")


p1 = Phone("Samsung", "9876543210", "Galaxy S22", "Android", 60000)
p2 = Phone("Apple", "9123456780", "iPhone 14", "iOS", 120000)
p1.show_info()
p1.call("9988776655")
p2.show_info()
p2.call("8877665544")


# 12) School Example
class School:
    def __init__(self, name, location, board, principal, established_year):
        self.name = name
        self.location = location
        self.board = board
        self.principal = principal
        self.established_year = established_year
        self.students = []

    def add_student(self, student_name):
        self.students.append(student_name)
        print(f"{student_name} admitted to {self.name}")

    def show_students(self):
        print(f"Students in {self.name}: {self.students}")


sch1 = School("Green Valley School", "Delhi", "CBSE", "Mr. Sharma", 1995)
sch2 = School("Sunrise Academy", "Mumbai", "ICSE", "Mrs. Mehta", 2005)
sch1.add_student("Ravi")
sch1.show_students()
sch2.add_student("Sneha")
sch2.show_students()


# 13) Movie Example
class Movie:
    def __init__(self, title, duration, genre, director, release_year):
        self.title = title
        self.duration = duration
        self.genre = genre
        self.director = director
        self.release_year = release_year

    def play(self):
        print(f"Playing movie: {self.title} ({self.duration} mins)")

    def show_info(self):
        print(f"{self.title} | Genre: {self.genre}, Director: {self.director}, Year: {self.release_year}")


m1 = Movie("Inception", 148, "Sci-Fi", "Christopher Nolan", 2010)
m2 = Movie("3 Idiots", 170, "Comedy-Drama", "Rajkumar Hirani", 2009)
m1.show_info()
m1.play()
m2.show_info()
m2.play()


# 14) Hospital Example
class Hospital:
    def __init__(self, name, location, type, capacity, established):
        self.name = name
        self.location = location
        self.type = type
        self.capacity = capacity
        self.established = established
        self.patients = []

    def admit_patient(self, patient):
        if len(self.patients) < self.capacity:
            self.patients.append(patient)
            print(f"{patient} admitted to {self.name}")
        else:
            print("No beds available")

    def show_patients(self):
        print(f"Patients in {self.name}: {self.patients}")


h1 = Hospital("City Hospital", "Delhi", "Multi-specialty", 2, 1990)
h2 = Hospital("Apollo", "Mumbai", "Private", 3, 2001)
h1.admit_patient("Ramesh")
h1.show_patients()
h2.admit_patient("Sita")
h2.show_patients()


# 15) Train Example
class Train:
    def __init__(self, train_no, name, source, destination, seats):
        self.train_no = train_no
        self.name = name
        self.source = source
        self.destination = destination
        self.seats = seats

    def book_ticket(self):
        if self.seats > 0:
            self.seats -= 1
            print(f"Ticket booked on {self.name}. Remaining seats: {self.seats}")
        else:
            print("No seats available")

    def show_info(self):
        print(f"Train {self.train_no} - {self.name} from {self.source} to {self.destination}")


tr1 = Train(10101, "Rajdhani Express", "Delhi", "Mumbai", 2)
tr2 = Train(10102, "Shatabdi Express", "Delhi", "Chandigarh", 1)
tr1.show_info()
tr1.book_ticket()
tr2.show_info()
tr2.book_ticket()


# 16) University class example
class University:
    def __init__(self, name, location, students):
        self.name = name
        self.location = location
        self.students = students
    
    def enroll_student(self, number):
        self.students += number
        print(f"{number} students enrolled. Total now: {self.students}")
    
    def conduct_exam(self):
        print(f"{self.name} is conducting semester exams for {self.students} students.")

# Creating objects
uni1 = University("Harvard University", "USA", 20000)
uni2 = University("Oxford University", "UK", 25000)

# Execution
print("---- University Details ----")
print(uni1.name, "-", uni1.location)
uni1.enroll_student(500)
uni1.conduct_exam()

print(uni2.name, "-", uni2.location)
uni2.enroll_student(1000)
uni2.conduct_exam()


# 17) Hospital
class Hospital:
    def __init__(self, patient_name, age, disease):
        self.patient_name = patient_name
        self.age = age
        self.disease = disease
    
    def admit(self):
        return f"Patient {self.patient_name} (Age: {self.age}) admitted with {self.disease}."
    
    def discharge(self):
        return f"Patient {self.patient_name} discharged after treatment."

# Objects
p1 = Hospital("Ramesh", 45, "Fever")
p2 = Hospital("Geeta", 30, "Fracture")

# Execution
print(p1.admit())
print(p2.admit())
print(p1.discharge())


# 18) Library
class Library:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return f"'{self.title}' by {self.author} has been borrowed."
        else:
            return f"'{self.title}' is already borrowed."
    
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return f"'{self.title}' has been returned."
        else:
            return f"'{self.title}' was not borrowed."

# Objects
book1 = Library("The Alchemist", "Paulo Coelho")
book2 = Library("Wings of Fire", "A.P.J. Abdul Kalam")

# Execution
print(book1.borrow())
print(book2.borrow())
print(book1.borrow())
print(book1.return_book())


# 19) GymMember Example

class GymMember:
    # Constructor
    def __init__(self, name, age, membership_type):
        self.name = name
        self.age = age
        self.membership_type = membership_type
        self.attendance = 0

    # Method 1: Check-in
    def check_in(self):
        self.attendance += 1
        print(f"{self.name} checked in. Total visits: {self.attendance}")

    # Method 2: Workout
    def workout(self, exercise):
        print(f"{self.name} is doing {exercise} workout.")

    # Method 3: Show Progress
    def show_progress(self):
        print(f"{self.name} ({self.membership_type}) - Total Visits: {self.attendance}")


# ---- Objects & Execution ----
member1 = GymMember("Ravi", 25, "Gold")
member2 = GymMember("Priya", 30, "Platinum")

# Actions
member1.check_in()
member1.workout("Cardio")
member1.show_progress()

print("-----")

member2.check_in()
member2.check_in()
member2.workout("Strength Training")
member2.show_progress()





"""
Purpose of Learning Oops Concepts in Python?

1) Reusability — Write once, reuse many times
Why it matters: Cut duplication; share the same class across scripts/projects.
Example: A Logger class can be used in different projects to record logs.

2) Modularity — Break work into small pieces
Why it matters: Each class handles one responsibility → easier testing and teamwork.
Example: In data pipelines → Extractor, Transformer, and Loader classes.

3) Maintainability — Easy to change or fix
Why it matters: Find bugs faster; update a single class instead of scattered code.
If rules change, you only update the related class, not the whole project.
Example: In an Invoice class, if tax policy changes, edit only one method.

4) Scalability — Grow to large systems naturally
Why it matters: New features fit by adding new classes/subclasses, not rewriting.
Example: Adding new Payment methods (UPI, Card) without touching existing ones.

5) Real-world Mapping — Model natural entities
Why it matters: Code mirrors the domain (User, Order, Product), reducing confusion.
Classes represent real-world things → easier to understand.
Example: Product, User, and Cart in an e-commerce system.

6) Data Encapsulation — Protect and validate data
Why it matters: Prevent invalid state; expose only safe operations.
Keeps data safe from invalid access.
Example: A BankAccount hides balance and allows changes only through deposit() and withdraw()

7) Inheritance — Build on existing classes
Why it matters: Share common behavior; specialize as needed.
Child classes reuse code from parent classes.
Example: Dog and Cat can inherit from an Animal class.

8) Polymorphism — Same method name, different behaviors
Why it matters: Write generic code that works with many types.
Different classes can use the same method but behave differently.
Example: predict() works differently for LinearModel and TreeModel.

9) Abstraction — Hide internals, show an interface
Why it matters: Users focus on what it does, not how it does.
User only sees what the method does, not how it works inside.
Example: read() method in CSVSource or APISource → both just return data.

10) Code Reuse Across Projects — Ship faster consistently
Why it matters: Package your classes; import anywhere.
Classes can be stored in a library and reused in new projects.
Example: A shared EmailValidator class can be used in signup, login, or newsletter apps.


Real life Examples of OOps in Data Analysis & Developement?

1. Pandas DataFrame → class for tabular data.
2. NumPy and array → object for multi-dimensional arrays.
3. Matplotlib Figure/Axes → classes for plots.
4. Sklearn Models → objects like LinearRegression(), uniform methods.
5. Banking → Account, Transaction, Ledger classes.
6. E-commerce → Product, Order, Cart, Payment.
7. Hospital → Patient, Doctor, Appointment.
8. Transport → Bus, Route, Ticket.
9. Chat → User, Message, Channel.
10. Blog → Post, Comment, Author.

"""