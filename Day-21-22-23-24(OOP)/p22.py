"""
====================================================
Python OOP Concepts: Inheritance
====================================================

Inheritance -->
Inheritance allows one class (child/derived class) 
to acquire the properties and methods of another 
class (parent/base class).

It promotes code reusability and modular design.

Why Use Inheritance?
1. Avoids code duplication.
2. Promotes reusability and maintainability.
3. Helps in designing real-world models (e.g., Car inherits from Vehicle).

Types of Inheritance in Python
--------------------------------
1. Single Inheritance → One child inherits from one parent.
2. Multiple Inheritance → One child inherits from multiple parents.
3. Multilevel Inheritance → A chain of inheritance (Child → Parent → Grandparent).
4. Hierarchical Inheritance → Multiple children inherit from one parent.
5. Hybrid Inheritance → Combination of different inheritance types.

Python uses Method Resolution Order (MRO) to decide
which parent’s method to call in multiple inheritance.

Check MRO using: print(ClassName.mro())
====================================================
"""

# ==================================================
# 1. SINGLE INHERITANCE
# ==================================================
print("\n--- Single Inheritance Examples ---")

# Example 1: Animal → Dog
class Animal:
    # Parent method
    def speak(self):
        print("Animals can make sounds.")

class Dog(Animal):  # Dog inherits from Animal
    # Child method
    def bark(self):
        print("Dog barks: Woof! Woof!")

# Creating object of Dog
dog = Dog()
dog.speak()  # Inherited from Animal
dog.bark()   # Defined in Dog


# Example 2: Vehicle → Car
class Vehicle:
    def __init__(self, brand):
        self.brand = brand  # Parent class variable
    
    def move(self):
        print(f"{self.brand} Vehicle is moving.")

class Car(Vehicle):  # Car inherits from Vehicle
    def __init__(self, brand, model):
        super().__init__(brand)  # Call parent constructor
        self.model = model

    def info(self):
        print(f"Car Info: {self.brand} {self.model}")

car = Car("Toyota", "Camry")
car.move()  # Inherited from Vehicle
car.info()  # Child method


# Example 3: Person → Student
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")

class Student(Person):  # Student inherits from Person
    def study(self):
        print(f"{self.name} is studying.")

student = Student("Rahul")
student.introduce()  # Parent method
student.study()      # Child method


# Example 4: Device → Laptop
class Device:
    def __init__(self, name):
        self.name = name

    def power_on(self):
        print(f"{self.name} is now ON.")

class Laptop(Device):  # Laptop inherits from Device
    def code(self):
        print(f"{self.name} is used for coding.")

laptop = Laptop("Dell XPS")
laptop.power_on()  # Parent method
laptop.code()      # Child method


# Example 5: Employee → Manager
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def details(self):
        print(f"Employee: {self.name}, Salary: {self.salary}")

class Manager(Employee):  # Manager inherits from Employee
    def manage(self):
        print(f"Manager {self.name} is managing the team.")

mgr = Manager("Shalini", 90000)
mgr.details()  # Parent method
mgr.manage()   # Child method


# ==================================================
# 2. MULTIPLE INHERITANCE
# ==================================================
print("\n--- Multiple Inheritance Examples ---")

# Example 1: Father + Mother → Child
class Father:
    def skill(self):
        print("Father: Knows driving.")

class Mother:
    def talent(self):
        print("Mother: Knows cooking.")

class Child(Father, Mother):  # Inherits from both Father and Mother
    def hobby(self):
        print("Child: Loves painting.")

c = Child()
c.skill()   # From Father
c.talent()  # From Mother
c.hobby()   # From Child


# Example 2: Teacher + Coach → Student
class Teacher:
    def teach(self):
        print("Teacher is teaching.")

class Coach:
    def train(self):
        print("Coach is training sports.")

class Student(Teacher, Coach):  # Inherits from Teacher & Coach
    def perform(self):
        print("Student is performing well.")

s = Student()
s.teach()    # From Teacher
s.train()    # From Coach
s.perform()  # From Student


# Example 3: Engine + Body → Car
class Engine:
    def engine_type(self):
        print("Engine: V8 Petrol")

class Body:
    def design(self):
        print("Body: Sedan")

class SportsCar(Engine, Body):  # Inherits from Engine & Body
    def info(self):
        print("SportsCar is powerful and stylish.")

sc = SportsCar()
sc.engine_type()  # From Engine
sc.design()       # From Body
sc.info()         # From SportsCar


# Example 4: Keyboard + Screen → Laptop
class Keyboard:
    def input_device(self):
        print("Keyboard: Used for typing.")

class Screen:
    def display(self):
        print("Screen: Displays visuals.")

class Laptop(Keyboard, Screen):  # Inherits from Keyboard & Screen
    def work(self):
        print("Laptop: Combination of input and output devices.")

lap = Laptop()
lap.input_device()  # From Keyboard
lap.display()       # From Screen
lap.work()          # From Laptop


# Example 5: Musician + Writer → Artist
class Musician:
    def play_music(self):
        print("Musician plays guitar.")

class Writer:
    def write(self):
        print("Writer writes poetry.")

class Artist(Musician, Writer):  # Inherits from Musician & Writer
    def show(self):
        print("Artist shows creativity.")

a = Artist()
a.play_music()  # From Musician
a.write()       # From Writer
a.show()        # From Artist


# ==================================================
# 3. MULTILEVEL INHERITANCE
# ==================================================
print("\n--- Multilevel Inheritance Examples ---")

# Example 1: Grandparent → Parent → Child
class Grandparent:
    def legacy(self):
        print("Grandparent: Passes traditions.")

class Parent(Grandparent):  # Parent inherits from Grandparent
    def responsibility(self):
        print("Parent: Takes care of children.")

class Child(Parent):  # Child inherits from Parent (chain)
    def learn(self):
        print("Child: Learns from elders.")

c = Child()
c.legacy()        # From Grandparent
c.responsibility()  # From Parent
c.learn()         # From Child


# Example 2: Vehicle → Car → ElectricCar
class Vehicle:
    def move(self):
        print("Vehicle is moving.")

class Car(Vehicle):
    def fuel(self):
        print("Car uses petrol or diesel.")

class ElectricCar(Car):  # Extends Car
    def charge(self):
        print("ElectricCar charges with electricity.")

ec = ElectricCar()
ec.move()   # From Vehicle
ec.fuel()   # From Car
ec.charge() # From ElectricCar


# Example 3: Animal → Mammal → Human
class Animal:
    def breathe(self):
        print("Animal breathes.")

class Mammal(Animal):
    def warm_blooded(self):
        print("Mammals are warm-blooded.")

class Human(Mammal):  # Extends Mammal
    def think(self):
        print("Humans can think logically.")

h = Human()
h.breathe()        # From Animal
h.warm_blooded()   # From Mammal
h.think()          # From Human


# Example 4: Company → Department → Employee
class Company:
    def info(self):
        print("This is a Company.")

class Department(Company):
    def dept_info(self):
        print("This is the IT Department.")

class Employee(Department):  # Extends Department
    def emp_info(self):
        print("This is an Employee in IT Department.")

emp = Employee()
emp.info()      # From Company
emp.dept_info() # From Department
emp.emp_info()  # From Employee


# Example 5: Device → Computer → Laptop
class Device:
    def power(self):
        print("Device is powered.")

class Computer(Device):
    def compute(self):
        print("Computer performs computation.")

class Laptop(Computer):  # Extends Computer
    def portable(self):
        print("Laptop is portable.")

lap = Laptop()
lap.power()    # From Device
lap.compute()  # From Computer
lap.portable() # From Laptop


# ==================================================
# 4. HIERARCHICAL INHERITANCE
# ==================================================
print("\n--- Hierarchical Inheritance Examples ---")

# Example 1: Parent → Child1, Child2
class Parent:
    def guide(self):
        print("Parent guides children.")

class Child1(Parent):  # Inherits from Parent
    def play(self):
        print("Child1 is playing.")

class Child2(Parent):  # Inherits from Parent
    def study(self):
        print("Child2 is studying.")

c1 = Child1()
c2 = Child2()
c1.guide()  # From Parent
c2.guide()  # From Parent
c1.play()   # From Child1
c2.study()  # From Child2


# Example 2: Vehicle → Car, Bike
class Vehicle:
    def fuel(self):
        print("Vehicle needs fuel.")

class Car(Vehicle):  # Inherits Vehicle
    def four_wheels(self):
        print("Car has four wheels.")

class Bike(Vehicle):  # Inherits Vehicle
    def two_wheels(self):
        print("Bike has two wheels.")

c = Car()
b = Bike()
c.fuel()         # From Vehicle
b.fuel()         # From Vehicle
c.four_wheels()  # From Car
b.two_wheels()   # From Bike


# Example 3: Animal → Dog, Cat
class Animal:
    def eat(self):
        print("Animals eat food.")

class Dog(Animal):
    def bark(self):
        print("Dog barks.")

class Cat(Animal):
    def meow(self):
        print("Cat meows.")

d = Dog()
cat = Cat()
d.eat()   # From Animal
cat.eat() # From Animal
d.bark()  # From Dog
cat.meow()# From Cat


# Example 4: Device → Mobile, Laptop
class Device:
    def power_on(self):
        print("Device is powered on.")

class Mobile(Device):
    def call(self):
        print("Mobile can make calls.")

class Laptop(Device):
    def code(self):
        print("Laptop can be used for coding.")

m = Mobile()
l = Laptop()
m.power_on()  # From Device
l.power_on()  # From Device
m.call()      # From Mobile
l.code()      # From Laptop


# Example 5: Shape → Circle, Square
class Shape:
    def draw(self):
        print("Drawing a shape.")

class Circle(Shape):
    def area(self, r):
        print("Area of Circle:", 3.14 * r * r)

class Square(Shape):
    def area(self, s):
        print("Area of Square:", s * s)

circle = Circle()
square = Square()
circle.draw()   # From Shape
square.draw()   # From Shape
circle.area(5)  # From Circle
square.area(4)  # From Square


# ==================================================
# 5. HYBRID INHERITANCE
# ==================================================
print("\n--- Hybrid Inheritance Examples ---")

# Example 1: Multiple + Hierarchical
class A:
    def featureA(self):
        print("Feature A")

class B(A):  # B inherits from A
    def featureB(self):
        print("Feature B")

class C(A):  # C inherits from A
    def featureC(self):
        print("Feature C")

class D(B, C):   # Hybrid: Multiple + Hierarchical
    def featureD(self):
        print("Feature D")

d = D()
d.featureA()  # From A
d.featureB()  # From B
d.featureC()  # From C
d.featureD()  # From D


# Example 2: Device → Mobile & Computer → SmartPhone
class Device:
    def power(self):
        print("Device has power.")

class Mobile(Device):
    def call(self):
        print("Mobile can make calls.")

class Computer(Device):
    def compute(self):
        print("Computer can compute.")

class SmartPhone(Mobile, Computer):  # Combines Mobile + Computer
    def feature(self):
        print("SmartPhone combines both features.")

sp = SmartPhone()
sp.power()    # From Device
sp.call()     # From Mobile
sp.compute()  # From Computer
sp.feature()  # From SmartPhone


# Example 3: Person → Employee + Student → Intern
class Person:
    def info(self):
        print("This is a person.")

class Employee(Person):
    def job(self):
        print("Employee has a job.")

class Student(Person):
    def study(self):
        print("Student is studying.")

class Intern(Employee, Student):  # Combines Employee + Student
    def work(self):
        print("Intern works and studies.")

intern = Intern()
intern.info()   # From Person
intern.job()    # From Employee
intern.study()  # From Student
intern.work()   # From Intern


# Example 4: Animal → Mammal + Bird → Bat
class Animal:
    def breathe(self):
        print("Animal breathes.")

class Mammal(Animal):
    def milk(self):
        print("Mammal gives milk.")

class Bird(Animal):
    def fly(self):
        print("Bird can fly.")

class Bat(Mammal, Bird):  # Bat combines Mammal + Bird
    def nature(self):
        print("Bat is a mammal that can fly.")

bat = Bat()
bat.breathe()  # From Animal
bat.milk()     # From Mammal
bat.fly()      # From Bird
bat.nature()   # From Bat


# Example 5: Vehicle → Car + Bike → HybridVehicle
class Vehicle:
    def move(self):
        print("Vehicle can move.")

class Car(Vehicle):
    def four_wheels(self):
        print("Car has four wheels.")

class Bike(Vehicle):
    def two_wheels(self):
        print("Bike has two wheels.")

class HybridVehicle(Car, Bike):  # Combines Car + Bike
    def hybrid(self):
        print("Hybrid Vehicle combines Car and Bike.")

hv = HybridVehicle()
hv.move()        # From Vehicle
hv.four_wheels() # From Car
hv.two_wheels()  # From Bike
hv.hybrid()      # From HybridVehicle
