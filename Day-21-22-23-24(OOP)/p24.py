"""
====================================================
Abstraction
====================================================
What is Abstraction?
----------------------------------------------------
- Abstraction means hiding the internal implementation details**
  and showing only the necessary features to the user.  

- In Python, abstraction is mainly achieved using:
  1. Abstract Classes
  2. Abstract Methods
  (via the `abc` module → Abstract Base Class).  

👉 Real-Life Example:  
When you drive a car, you only use the **steering, brake, accelerator**.  
You don’t need to know how the engine, fuel injection, or gears work internally.  
That’s abstraction in action.  

----------------------------------------------------
Why use Abstraction?
----------------------------------------------------
1. Code Security → Hides complex code and exposes only essential parts.  
2. Reusability → Provides a base structure that can be reused by multiple classes.  
3. Flexibility → Different child classes can have their own versions 
   of the same method (supports polymorphism).  
4. Blueprint Creation → Abstract classes act as a design template for other classes.  
5. Simplifies Development → Developers can focus on “what to do” 
   rather than “how it’s done.”  

----------------------------------------------------
How to Achieve Abstraction in Python?
----------------------------------------------------
1. Import `ABC` and `abstractmethod` from `abc` module.  
2. Define an abstract class that contains one or more abstract methods.  
3. Any class inheriting the abstract class must provide implementation
   for all abstract methods.  
4. If a child class does not implement the abstract method(s),
   it cannot be instantiated.  

----------------------------------------------------
Key Points to Remember:
----------------------------------------------------
- Abstract class cannot be instantiated directly.  
- Abstract methods act like "rules" → child classes must override them.  
- You can have normal methods + abstract methods inside the same abstract class.  
- Helps in achieving real-world modeling (e.g., Vehicle → Car, Bike).  

"""
#Example: Abstraction in Python

# ====================================================
# Example 1: Banking System
# ====================================================
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    @abstractmethod
    def withdraw(self, amount):
        pass

# Savings Account (child class)
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.holder} withdrew {amount}. Remaining balance: {self.balance}")
        else:
            print("Insufficient balance!")

# Current Account (child class)
class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        # Allows overdraft up to -5000
        if self.balance - amount >= -5000:
            self.balance -= amount
            print(f"{self.holder} withdrew {amount}. Remaining balance: {self.balance}")
        else:
            print("Overdraft limit exceeded!")

acc1 = SavingsAccount("Shalini", 10000)
acc2 = CurrentAccount("Rahul", 2000)

acc1.withdraw(3000)
acc2.withdraw(6000)


# ====================================================
# Example 2: Payment Gateway
# ====================================================
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

class PayPal(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")

class Crypto(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Cryptocurrency.")

p1 = CreditCard()
p2 = PayPal()
p3 = Crypto()

p1.pay(1200)
p2.pay(500)
p3.pay(2500)


# ====================================================
# Example 3: Employee Management
# ====================================================
class Employee(ABC):
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    @abstractmethod
    def calculate_salary(self):
        pass

class Manager(Employee):
    def calculate_salary(self):
        return self.base_salary + 5000  # Bonus

class Developer(Employee):
    def calculate_salary(self):
        return self.base_salary + 2000  # Incentive

m = Manager("Kavita", 40000)
d = Developer("Jay", 30000)

print(f"{m.name}'s Salary: {m.calculate_salary()}")
print(f"{d.name}'s Salary: {d.calculate_salary()}")


# ====================================================
# Example 4: Device Abstraction
# ====================================================
class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class Laptop(Device):
    def turn_on(self):
        print("Laptop is booting up with Windows 11.")

class Smartphone(Device):
    def turn_on(self):
        print("Smartphone is starting with Android 14.")

devices = [Laptop(), Smartphone()]
for d in devices:
    d.turn_on()


# ====================================================
# Example 5: Shape Area Calculation
# ====================================================
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length, self.width = length, width
    def area(self):
        return self.length * self.width

s1 = Circle(7)
s2 = Rectangle(10, 5)

print("Circle Area:", s1.area())
print("Rectangle Area:", s2.area())


""" 
====================================================
Constructor Chaining
====================================================
What is Constructor Chaining?

Constructor chaining means when a child class constructor calls the parent class constructor 
automatically using super().
This ensures the parent class is initialized first before the child adds its own features.

👉 Example in real life:
When you create a Student object (child), 
first the Person details (parent) are set up, then Student-specific details.
"""
#Example: Constructor Chaining in Python
class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor called.")

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)   # Calls Person constructor
        self.student_id = student_id
        print("Student constructor called.")

# Object Creation
s1 = Student("Shalini", "S101")


""" 
====================================================
Mini Project: Bank Account System
====================================================
Demonstrates: Class + Object + Constructors + Functions + logics(control structure, loops) 
+ list + set + tuples + dictionary + Encapsulation + Inheritance + Polymorphism + Abstraction 
"""

from abc import ABC, abstractmethod

# ====================================================
# Abstract Class: Account
# ====================================================
class Account(ABC):
    def __init__(self, account_number, holder_name, balance=0):
        # Encapsulation: Using protected members
        self._account_number = account_number
        self._holder_name = holder_name
        self._balance = balance
        print(f"Account {self._account_number} for {self._holder_name} created.")

    # Abstract methods
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    # Method to show account details
    def show_details(self):
        print(f"Account Number: {self._account_number}, Holder: {self._holder_name}, Balance: {self._balance}")

# ====================================================
# Savings Account
# ====================================================
class SavingsAccount(Account):
    interest_rate = 0.04  # Class variable (4% interest)

    def __init__(self, account_number, holder_name, balance=0):
        super().__init__(account_number, holder_name, balance)  # Constructor chaining
        print("Savings Account initialized.")

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount}. New Balance: {self._balance}")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. Balance left: {self._balance}")
        else:
            print("Insufficient balance!")

    # Polymorphism: same method name, behaves differently
    def calculate_interest(self):
        interest = self._balance * SavingsAccount.interest_rate
        print(f"Interest for {self._holder_name}: {interest}")
        return interest

# ====================================================
# Current Account
# ====================================================
class CurrentAccount(Account):
    overdraft_limit = 5000  # Class variable

    def __init__(self, account_number, holder_name, balance=0):
        super().__init__(account_number, holder_name, balance)
        print("Current Account initialized.")

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount}. New Balance: {self._balance}")

    def withdraw(self, amount):
        if self._balance - amount >= -CurrentAccount.overdraft_limit:
            self._balance -= amount
            print(f"Withdrew {amount}. Balance left: {self._balance}")
        else:
            print("Overdraft limit reached!")

# ====================================================
# Fixed Deposit Account
# ====================================================
class FixedDepositAccount(Account):
    def __init__(self, account_number, holder_name, balance, tenure):
        super().__init__(account_number, holder_name, balance)
        self.tenure = tenure  # Tenure in years
        print(f"Fixed Deposit Account for {self._holder_name}, Tenure: {self.tenure} years.")

    def deposit(self, amount):
        self._balance += amount
        print(f"Added to Fixed Deposit: {amount}. Total: {self._balance}")

    def withdraw(self, amount):
        print("Withdrawals not allowed before maturity!")

    # Polymorphism: Overriding interest calculation
    def calculate_interest(self):
        interest = self._balance * 0.07 * self.tenure  # 7% per annum
        print(f"FD Interest for {self._holder_name}: {interest}")
        return interest

# ====================================================
# Bank Management
# ====================================================
class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []  # List to store accounts

    # Add account to bank
    def add_account(self, account):
        self.accounts.append(account)
        print(f"Account {account._account_number} added to {self.name} bank.")

    # Show all accounts
    def show_all_accounts(self):
        for acc in self.accounts:
            acc.show_details()

    # Total balance in bank
    def total_balance(self):
        total = sum(acc._balance for acc in self.accounts)
        print(f"Total balance in {self.name}: {total}")
        return total

# ====================================================
# --- Testing the Project ---
# ====================================================
print("\n--- Bank System Demo ---")
bank = Bank("Alpha Bank")

# Creating accounts
s1 = SavingsAccount("SA101", "Shalini", 5000)
c1 = CurrentAccount("CA202", "Rahul", 2000)
fd1 = FixedDepositAccount("FD303", "Kavita", 10000, 5)

# Add accounts to bank
bank.add_account(s1)
bank.add_account(c1)
bank.add_account(fd1)

# Operations
s1.deposit(2000)
s1.withdraw(1000)
s1.calculate_interest()

c1.deposit(1500)
c1.withdraw(6000)

fd1.deposit(5000)
fd1.calculate_interest()
fd1.withdraw(1000)

# Bank overview
print("\n--- All Bank Accounts ---")
bank.show_all_accounts()
bank.total_balance()

# ====================================================
# Example: Using List, Tuple, Set, Dictionary
# ====================================================
# List of account holders
account_holders = [acc._holder_name for acc in bank.accounts]
print("Account Holders List:", account_holders)

# Tuple of balances
balances = tuple(acc._balance for acc in bank.accounts)
print("Balances Tuple:", balances)

# Set of unique account types
account_types = {type(acc).__name__ for acc in bank.accounts}
print("Account Types Set:", account_types)

# Dictionary: Account number -> Holder Name
account_dict = {acc._account_number: acc._holder_name for acc in bank.accounts}
print("Accounts Dictionary:", account_dict)
