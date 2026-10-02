                                    # Inheritance

                                # Simple Inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def show(self):
#         print(f"my name is {self.name}")

# class Human(Animal):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#     def show(self):
#         super().show()
#         print(f"my age is {self.age}")
    

# obj1 = Animal("Dog")
# obj2 = Human("Nitish", 22)

# for i in obj1, obj2:
#     i.show()

                                # Multiple Inheritance
# class Camera:
#     def takePhoto(self):
#         print(f"Photo taken Sucessfully \N{CAMERA}")

# class Phone:
#     def callSomeone(self):
#         print(f"Calling Someone \N{MOBILE PHONE}")

# class SmartPhone(Camera, Phone):
#     pass

# iPhone_17 = SmartPhone()
# iPhone_17.takePhoto()
# iPhone_17.callSomeone()

                                # Multi-Level Inheritance
# Grandparent -> Parent -> Child (a chain)
print("----- Multi-Level Inheritance -----")

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        print(f"{self.brand} vehicle started \N{KEY}")

class Car(Vehicle):
    def __init__(self, brand, seats):
        super().__init__(brand)
        self.seats = seats
    def drive(self):
        print(f"Driving {self.brand} car with {self.seats} seats \N{AUTOMOBILE}")

class ElectricCar(Car):
    def __init__(self, brand, seats, battery):
        super().__init__(brand, seats)
        self.battery = battery
    def charge(self):
        print(f"Charging {self.battery} kWh battery \N{ELECTRIC PLUG}")

tesla = ElectricCar("Tesla", 5, 75)
tesla.start()     # from Vehicle (grandparent)
tesla.drive()     # from Car (parent)
tesla.charge()    # its own method

# MRO = Method Resolution Order, the order Python searches for a method
print(ElectricCar.__mro__)

                                # Hierarchical Inheritance
# One parent -> many children
print("\n----- Hierarchical Inheritance -----")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def details(self):
        print(f"{self.name} earns {self.salary}")

class Manager(Employee):
    def conductMeeting(self):
        print(f"{self.name} is conducting a meeting")

class Developer(Employee):
    def writeCode(self):
        print(f"{self.name} is writing code \N{PERSONAL COMPUTER}")

m = Manager("Rahul", 90000)
d = Developer("Nitish", 80000)
m.details()
m.conductMeeting()
d.details()
d.writeCode()


                                    # Encapsulation
# Wrapping data + methods together and controlling access to the data
#   name    -> public    (use anywhere)
#   _name   -> protected (convention only: "please don't touch from outside")
#   __name  -> private   (Python renames it to _ClassName__name)
print("\n----- Encapsulation -----")

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner            # public
        self._bank = "SBI"            # protected
        self.__balance = balance      # private

    # getter
    def getBalance(self):
        return self.__balance

    # setters with validation, this is the real benefit of encapsulation
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive \N{WARNING SIGN}")
            return
        self.__balance += amount
        print(f"Deposited {amount}, new balance is {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance \N{CROSS MARK}")
            return
        self.__balance -= amount
        print(f"Withdrew {amount}, new balance is {self.__balance}")

acc = BankAccount("Nitish", 1000)
acc.deposit(500)
acc.withdraw(5000)
acc.deposit(-100)
print("Balance:", acc.getBalance())

# print(acc.__balance)              # AttributeError, it's private
print(acc._BankAccount__balance)    # name mangling: still reachable, but never do this

                                # @property (the Pythonic getter/setter)
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks            # this goes through the setter below

    @property
    def marks(self):                  # getter, use as s.marks (no brackets)
        return self.__marks

    @marks.setter
    def marks(self, value):           # setter, runs on s.marks = value
        if not 0 <= value <= 100:
            raise ValueError("Marks must be between 0 and 100")
        self.__marks = value

s = Student("Nitish", 85)
print(s.marks)
s.marks = 95
print(s.marks)
# s.marks = 150                     # ValueError


                                    # Abstraction
# Show WHAT an object does, hide HOW it does it.
# An abstract class can't be created directly; it forces children to
# implement its abstract methods (like pure virtual functions in C++).
print("\n----- Abstraction -----")

from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def pay(self):
        pass

    # normal method, children get it for free
    def receipt(self):
        print(f"Receipt: paid {self.amount} \N{WHITE HEAVY CHECK MARK}")

class UPI(Payment):
    def pay(self):
        print(f"Paying {self.amount} using UPI \N{MOBILE PHONE}")

class Card(Payment):
    def pay(self):
        print(f"Paying {self.amount} using Card \N{CREDIT CARD}")

# p = Payment(100)                  # TypeError: can't instantiate abstract class

u = UPI(250)
u.pay()
u.receipt()

c = Card(1200)
c.pay()
c.receipt()


                                    # Polymorphism
# Same name, different behaviour ("many forms")
print("\n----- Polymorphism -----")

                                # 1. Method Overriding
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b
    def area(self):
        return self.l * self.b

# same call shape.area(), different result for each object
for shape in [Circle(2), Rectangle(3, 4)]:
    print(f"{type(shape).__name__} area = {shape.area()}")

                                # 2. Duck Typing
# "If it walks like a duck and quacks like a duck, it's a duck"
# No common parent needed, Python only checks that the method exists.
class Dog:
    def speak(self):
        print("Woof \N{DOG FACE}")

class Cat:
    def speak(self):
        print("Meow \N{CAT FACE}")

for animal in [Dog(), Cat()]:
    animal.speak()

                                # 3. Operator Overloading
# Teach +, ==, print() etc. how to work with your own class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):         # p1 + p2
        return Point(self.x + other.x, self.y + other.y)
    def __eq__(self, other):          # p1 == p2
        return self.x == other.x and self.y == other.y
    def __str__(self):                # print(p)
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)
print(p1 == Point(1, 2))

                                # 4. Method Overloading
# Python has NO real method overloading like C++.
# If you write two methods with the same name, the last one wins.
# Use default arguments (or *args) instead:
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))
print(calc.add(2, 3, 4))

# Built-in polymorphism: the same len() works on different types
print(len("Nitish"), len([1, 2, 3]), len({"a": 1}))