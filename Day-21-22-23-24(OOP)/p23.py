"""
====================================================
Polymorphism
====================================================

Polymorphism -->
The word "Polymorphism" means "many forms."
In Python, polymorphism allows the same method,
operator, or function name to have different
behaviors depending on the object or context.

Why Use Polymorphism?
---------------------
1. Makes code flexible and dynamic.
2. Supports the concept of generalization.
3. Improves readability and reusability.
4. Helps in implementing real-world behavior
   (e.g., "speak()" method behaves differently
   for Dog, Cat, and Human).

Types of Polymorphism in Python
-------------------------------
1. Method Overriding → Child class redefines parent class method.
2. Method Overloading → Same method with different parameters
   (not directly supported, but can be achieved using default args or *args).
3. Operator Overloading → Same operator behaves differently for different objects.

Real-life Example Analysis:
---------------------------
Imagine a "Payment" system. The method "pay()" can behave differently:
- For CreditCard → pay() deducts from bank.
- For PayPal → pay() uses wallet.
- For Crypto → pay() uses blockchain.
This is polymorphism in action.
====================================================
"""

print("\n==============================")
print("  Basic 5 Polymorphism Examples")
print("==============================")

# Example 1: Function Polymorphism (built-in function 'len')
# Same function works with string, list, dictionary etc.
print("Length of string:", len("Shalini"))
print("Length of list:", len([10, 20, 30]))
print("Length of dictionary:", len({"a": 1, "b": 2}))


# Example 2: Method Overriding
# Same method name "sound()" behaves differently in child classes.
class Bird:
    def sound(self):
        print("Birds make sounds.")

class Sparrow(Bird):
    def sound(self):
        print("Sparrow chirps.")

class Parrot(Bird):
    def sound(self):
        print("Parrot talks.")

birds = [Sparrow(), Parrot()]
for b in birds:
    b.sound()


# Example 3: Operator Overloading
# '+' is redefined to add pages of two Book objects.
class Book:
    def __init__(self, pages):
        self.pages = pages
    def __add__(self, other):
        return self.pages + other.pages

b1 = Book(100)
b2 = Book(200)
print("Total Pages in 2 Books:", b1 + b2)


# Example 4: Method Overloading using default arguments
# Same function name 'add' works with 2 or 3 arguments.
def add(a, b=0, c=0):
    return a + b + c

print("Add 2 numbers:", add(5, 10))
print("Add 3 numbers:", add(5, 10, 20))


# Example 5: Polymorphism with different classes
# Same method name "area()" in different classes.
class Circle:
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r * self.r

class Square:
    def __init__(self, s): self.s = s
    def area(self): return self.s * self.s

shapes = [Circle(5), Square(4)]
for shape in shapes:
    print("Area:", shape.area())


print("\n==============================")
print("  5 Examples: Method Overriding")
print("==============================")

# 1. Animal sounds
class Animal:
    def speak(self): print("Animal speaks")
class Dog(Animal):
    def speak(self): print("Dog barks")
class Cat(Animal):
    def speak(self): print("Cat meows")

for a in [Dog(), Cat()]:
    a.speak()

# 2. Employee salary calculation
class Employee:
    def salary(self): print("Base salary")
class Manager(Employee):
    def salary(self): print("Manager salary + Bonus")
class Developer(Employee):
    def salary(self): print("Developer salary + Incentives")

for e in [Manager(), Developer()]:
    e.salary()

# 3. Vehicle speed
class Vehicle:
    def speed(self): print("Generic vehicle speed")
class Car(Vehicle):
    def speed(self): print("Car speed: 120 km/h")
class Bike(Vehicle):
    def speed(self): print("Bike speed: 80 km/h")

for v in [Car(), Bike()]:
    v.speed()

# 4. Payment modes
class Payment:
    def pay(self): print("Generic payment")
class CreditCard(Payment):
    def pay(self): print("Paid via Credit Card")
class PayPal(Payment):
    def pay(self): print("Paid via PayPal")

for p in [CreditCard(), PayPal()]:
    p.pay()

# 5. University roles
class Person:
    def role(self): print("General Person")
class Student(Person):
    def role(self): print("Student attends classes")
class Teacher(Person):
    def role(self): print("Teacher delivers lectures")

for person in [Student(), Teacher()]:
    person.role()


print("\n==============================")
print("  5 Examples: Method Overloading")
print("==============================")

# 1. Calculator (different number of inputs)
def multiply(a, b=1, c=1):
    return a * b * c
print("Multiply 2 nums:", multiply(2, 3))
print("Multiply 3 nums:", multiply(2, 3, 4))

# 2. Greeting function (default message)
def greet(name, msg="Hello"):
    print(f"{msg}, {name}!")
greet("Shalini")
greet("Shalini", "Good Morning")

# 3. Shopping discount (optional discount %)
def discount(price, percent=0):
    return price - (price * percent / 100)
print("Price after discount:", discount(1000))
print("Price after 20% discount:", discount(1000, 20))

# 4. Travel booking (optional seats and destination)
def book_ticket(name, seats=1, destination="Delhi"):
    print(f"{name} booked {seats} seat(s) to {destination}")
book_ticket("Rahul")
book_ticket("Shalini", 2, "Mumbai")

# 5. Student grade (marks optional)
def grade(name, marks=None):
    if marks is None:
        print(f"{name}'s grade is pending")
    else:
        print(f"{name}'s grade is based on marks {marks}")
grade("Jay")
grade("Kavita", 85)


print("\n==============================")
print("  5 Examples: Operator Overloading")
print("==============================")


# 1. Complex numbers addition using '+'
class Complex:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    # Overloading '+'
    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)
    
    # Overloading 'print'
    def __str__(self):
        return f"{self.x}+{self.y}i"


c1, c2 = Complex(2, 3), Complex(1, 4)
print("1. Complex Sum:", c1 + c2)  # Uses __add__


# 2. Vector addition using '+'
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"


v1, v2 = Vector(2, 5), Vector(4, -1)
print("2. Vector Sum:", v1 + v2)


# 3. String repetition with '*'
class Repeat:
    def __init__(self, text):
        self.text = text
    
    # Overloading '*'
    def __mul__(self, n):
        return self.text * n


r = Repeat("Hi ")
print("3. Repeated String:", r * 3)


# 4. Comparing students by marks using '>'
class Student:
    def __init__(self, name, marks):
        self.name, self.marks = name, marks
    
    # Overloading '>' operator
    def __gt__(self, other):
        return self.marks > other.marks


s1, s2 = Student("A", 85), Student("B", 90)
print("4. Is Student A > Student B?", s1 > s2)


# 5. Custom length using len()
class Team:
    def __init__(self, members):
        self.members = members
    
    # Overloading len()
    def __len__(self):
        return len(self.members)


t = Team(["A", "B", "C"])
print("5. Team size:", len(t))


"""
====================================================
Encapsulation
====================================================

Encapsulation -->
Encapsulation is the process of wrapping data 
(variables) and methods (functions) into a single unit (class).

It restricts direct access to variables and 
prevents accidental modification, ensuring 
data security.

Access Specifiers in Python
---------------------------
1. Public Member → Accessible everywhere (default).
2. Protected Member (_variable) → Accessible inside class & subclasses.
3. Private Member (__variable) → Accessible only inside class.

Why Use Encapsulation?
----------------------
1. Data security and control.
2. Hides implementation details (abstraction support).
3. Increases modularity and maintainability.
4. Prevents unintended interference.

Real-life Example Analysis:
---------------------------
Think of a Bank Account:
- Balance should not be accessed directly.
- Only controlled actions like deposit() or withdraw() should modify it.
This is encapsulation in action.
====================================================
"""

# ==================================================
# 2. ENCAPSULATION
# ==================================================
print("\n--- Encapsulation Examples ---")

# Example 1: Public Members
# Real-life: Student name and age are public information.
class Student:
    def __init__(self, name, age):
        self.name = name        # Public
        self.age = age          # Public

    def display(self):
        print(f"Student: {self.name}, Age: {self.age}")

s = Student("Rahul", 21)
s.display()
print("Accessing Public Variable:", s.name)  # ✅ Allowed


# Example 2: Protected Members
# Real-life: Salary is sensitive but can be accessed by subclasses (e.g., Manager).
class Employee:
    def __init__(self, name, salary):
        self._name = name        # Protected
        self._salary = salary    # Protected

    def show(self):
        print(f"Employee: {self._name}, Salary: {self._salary}")

class Manager(Employee):
    def manage(self):
        print(f"Manager {self._name} manages with salary {self._salary}")

m = Manager("Shalini", 90000)
m.show()
m.manage()


# Example 3: Private Members
# Real-life: Bank balance should be strictly private.
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"{self.owner}'s Balance: {self.__balance}")

acc = BankAccount("Rahul", 5000)
acc.deposit(2000)
acc.show_balance()
# print(acc.__balance)  # ❌ Error: Cannot access private variable directly


# Example 4: Encapsulation with Getter/Setter
# Real-life: Product price can be updated only with conditions.
class Product:
    def __init__(self, price):
        self.__price = price

    # Getter
    def get_price(self):
        return self.__price

    # Setter
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid Price!")

p = Product(100)
print("Old Price:", p.get_price())
p.set_price(200)
print("Updated Price:", p.get_price())


# Example 5: Real-world ATM Example
# Encapsulation ensures that PIN and Balance cannot be accessed directly.
class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin          # Private
        self.__balance = balance  # Private

    def access(self, pin):
        if pin == self.__pin:
            print("Access Granted. Balance:", self.__balance)
        else:
            print("Access Denied. Wrong PIN.")

atm = ATM(1234, 10000)
atm.access(1234)   # ✅ Correct PIN
atm.access(1111)   # ❌ Wrong PIN
