#Created a class Car
class Car:
    # Class attribute shared by all objects
    wheels = 4

    def __init__(self, brand, year):
        # Created instance attributes
        self.brand = brand 
        self.year = year

    # Instance method info()
    def info(self):
        print(f"This car is a {self.brand} made in {self.year} with {self.wheels} wheels.")

# Created objects
# audi = Car("Audi", 2022)
# bmw = Car("BMW", 2021)

# Call info() method
# audi.info()
# bmw.info()

###############################

class Laptop: # Created a class Laptop
    os = "Linux" # Class attribute shared by all objects

    def __init__(self, brand, ram): # Created a constructor
        self.brand = brand
        self.ram = ram
    
    def specs(self): # Created a specs() method 
        print(f"Brand: {self.brand}, RAM: {self.ram}GB, OS: {self.os}")

# Created two objects
hp = Laptop("HP", 16)
lenovo = Laptop("Lenovo", 32)

Laptop.os = "Windows" # Changed the class attribute os for all objects to Windows

lenovo.os = "Linux" # Changed the instance attribute os for object lenovo

# for laptop in (hp, lenovo):
#     laptop.specs()

class Employee: # Created a class Employee
    def __init__(self, name, salary): # Created a constructor
        self.name = name
        self.salary = salary

    def info(self): # Created a method info()
        print(f"Employee: {self.name}, Salary: {self.salary}")

class Manager(Employee): # Created a class Manager
    def __init__(self, name, salary, department): # Created a constructor
        super().__init__(name, salary)
        self.department = department

    def info(self): # Created a method info()
        print(f"Manager: {self.name}, Department: {self.department}, Salary: {self.salary}")

employee = Employee("Paul", 50000)
manager = Manager("Pascal", 80000, "Engineering")

# for person in (employee, manager):
#     person.info()

# I created a class `Employee`, then created constructor and added instance attributes `name` and `salary`. 
# I created a class `Manager` that inherits from `Employee` and added instance attribute `department`. 
# Then I created two objects `employee` and `manager`. Finally, I called the `info()` method for both objects.

class Device: # Created a class Device
    def __init__(self, brand):
        self.brand = brand
        print("Device initialized")

class Computer(Device): # Created a subclass Computer that inherits from Device
    def __init__(self, brand, cpu):
        super().__init__(brand) # Called the constructor of the parent class
        self.cpu = cpu
        print("Computer initialized")

class Laptop(Computer): # Created a subclass Laptop that inherits from Computer
    def __init__(self, brand, cpu, ram):
        super().__init__(brand, cpu) # Called the constructor of the parent class C
        self.ram = ram
        print("Laptop initialized")

    def info(self):
        print(f"Brand: {self.brand}, CPU: {self.cpu}, RAM: {self.ram}")

# laptop = Laptop("Dell", "Intel Core i7", 16) # Created an object
# laptop.info() # Called the info() method


class Battery: # Created a class Battery
    def charge(self): # Created a method charge
        print("Battery charging...")

class Phone: # Created a class Phone
    def __init__(self, brand):
        self.brand = brand
        self.battery = Battery() # Created an instance of the Battery class

    def use_phone(self): # Created a method use_phone
        self.battery.charge()
        print(f"Using {self.brand} phone")

phone = Phone("Huawei")

# phone.use_phone()

# First, I created a class `Battery` and added a method `charge()`, then I created a class `Phone` and added an instance attribute `battery`.
# Finally, I created an object `phone` and called the `use_phone()` method.


class Appliance: # Created a class `Appliance`
    def __init__(self, brand):
        self.__brand = brand # Created a private attribute `__brand`

    def get_brand(self): # Created a method `get_brand()`
        
        return self.__brand
    
class PowerSupply:
    def turn_on(self): # Created a method `turn_on()`
        print("Power supply activated")

class WashingMachine(Appliance): # Created a subclass `WashingMachine` that inherits from `Appliance`
    def __init__(self, brand):
        super().__init__(brand) # Called the constructor of the parent class `Appliance`
        self.power_supply = PowerSupply() # Created an instance of the `PowerSupply` class

    def start(self): # Created a method `start()`
        self.power_supply.turn_on()
        print(f"Washing machine {self.get_brand()} is running")

washing_machine = WashingMachine("LG") # Created an object `washing_machine` and called the `start()` method
# washing_machine.start()

# First I created a class `Appliance` with a private attribute `__brand`and created a method `get_brand()`.
# Then I created a class `PowerSupply` with amethod `turn_on()`
# Next, I created a subclass `WashingMachine` that inherits from `Appliance`, 
# called the constructor of the parent class `Appliance`, and created an instance of the `PowerSupply` class
# Finally, I Created a method `start()` and Created an object `washing_machine` and called the `start()` method

import math
class Shape: # Created a class `Shape`
    def area(self): # Created a method `area()`
        print("Area not defined")

class Circle(Shape): # Created a subclass `Circle` that inherits from `Shape`
    def __init__(self, radius):
        self.radius = radius

    def area(self): # Created a method `area()`
        print(f"Area of circle with radius {self.radius} is {math.pi * self.radius **2:.2f}")

class Rectangle(Shape): # Created a subclass `Rectangle` that inherits from `Shape`
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self): # Created a method `area()`
        print(f"Area of rectangle with width {self.width} and height {self.height} is {self.width * self.height:.2f}")

area = Shape() # Created an object `area` and called the `area()` method
circle = Circle(5) # Created an object `circle` and called the `area()` method
rectangle = Rectangle(5, 8) # Created an object `rectangle` and called the `area()` method

# for shape in (area,circle, rectangle): # Created a for loop to iterate through the list
#     shape.area()

# First, I created a class `Shape` with a method `area()`. 
# Then I created a subclass `Circle` that inherits from `Shape` and added an instance attribute `radius`.
# Finally, I created a subclass `Rectangle` that inherits from `Shape` and added instance attributes `width` and `height`.

class Item: # Created a class `Item`
    def __init__(self, title):
        self.__title = title # Created a private attribute `__title`

    def get_title(self): # Created a method `get_title()`
        return self.__title
    
    def info(self):  # Created a method `info()`
        print(f"Title: {self.get_title()}")

class Book(Item): # Created a subclass `Book` that inherits from `Item`
    def __init__(self, title, author):
        super().__init__(title) # Called the constructor of the parent class `Item`
        self.author = author
    
    def info(self): # Created a method `info()`
        print(f"Book: {self.get_title()} | Author: {self.author}")

class DVD(Item): # Created a subclass `DVD` that inherits from `Item`
    def __init__(self, title, duration):
        super().__init__(title) # Called the constructor of the parent class `Item`
        self.duration = duration

    def info(self): # Created a method `info()`
        print(f"DVD: {self.get_title()} | Duration: {self.duration} min")

class Library: # Created a class `Library`
    def __init__(self):
        self.items = [] # Created an instance attribute `items`
    
    def add_item(self, item): # Created a method `add_item()`
        try:
            self.items.append(item) # Added the item to the list `items`
        except:
            print("Error: Only Item subclasses can be added.")
    
    def show_items(self): # Created a method `show_items()`
        try:
            for item in self.items:
                item.info() # Called the `info()` method of each item in the list `items'
        except:
            print("Library is empty.")

# library = Library() # Created an object `library` and called the `add_item()` method
# library.add_item(Book("Ананасная вода для прекрасной дамы", "Виктор Пелевин"))
# library.add_item(DVD("The Lord of the Rings", 178))
# library.show_items()



# First, I created a class `Item` and addeda private attribute `__title`. Then I created a method `get_title()` and a method `info()`
# Second, I created a subclasses `Book` and `DVD` that inherits from `Item` and called the constructor of the parent class `Item`. Then I created a method `info()` for each subclass.
# Third, I created a class `Library`, and created an instance attribute `items`
# Then I created a method `add_item()` and added the item to the list `items`. Then I created a method `show_items()`
# Finally, I created an object `library` and called the `add_item()` method and the `show_items()` method


class Counter:
    """Tracks the number of instances created and assigns each a unique ID.

    Each instance receives an `id` equal to the total number of instances
    created so far. The class attribute `total_created` is shared across
    all instances and increments automatically on instantiation.
    """
    total_created = 0

    def __init__(self):
        Counter.total_created += 1
        self.id = Counter.total_created

c1 = Counter()
c2 = Counter()
c3 = Counter()

# print(c1.id, c2.id, c3.id)


# print(Counter.__doc__)

class Config:
    '''
    '''
    debug = False

    def enable_debug(self):
        self.debug = True

# config1 = Config()
# config1.enable_debug()
# print(config1.debug)
# config2 = Config()
# print(config2.debug)

'''
Write a function inspect_attributes(obj, attr_name) that returns a tuple:
(found_in_instance: bool, found_in_class: bool)

It should check whether attr_name exists in obj.__dict__ and in obj.__class__.__dict__ (only the direct class, not parents).

Acceptance Criteria:

Do not use hasattr() or getattr()—inspect __dict__ directly.
Return (True, False) if only in instance, (False, True) if only in class, etc.
Submit your function.
'''
def inspect_attributes(obj, attr_name):
    found_in_instance = attr_name in obj.__dict__
    found_in_class = attr_name in obj.__class__.__dict__
    return (found_in_instance, found_in_class)

# obj = Config()
# print(inspect_attributes(obj, "debug"))

class Product:
    tax_rate = 0.2

    def __init__(self, name, price):
        if isinstance(name, str) and isinstance(price, (float)):
            self.name = name
            self.price = price
        else:
            raise TypeError("Name and price must be strings and floats")
        
    def get_total(self):
        return self.price * (1 + self.tax_rate)
    

product1 = Product("Laptop", 1000.0)
product2 = Product("Phone", 500.0)
# print(product1.get_total())
# print(product2.get_total())

# a = product1.get_total()
# Product.tax_rate = 0.3

# print(product1.get_total(), a, sep="\n")

class Car: 
    wheels = 4

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def info(self):
        print(f"{self.brand} car has {self.wheels} wheels and color {self.color}")

# toyota = Car("Toyota", "red")
# bmw = Car("BMW", "black")
# toyota.info()
# bmw.info()

# Car.wheels = 6
# toyota.info()
# bmw.info()

# toyota.wheels = 8
# toyota.info()
# bmw.info()

class Device:
    """Parent class for all device."""
    category = "Electronics"

class Phone(Device):
    """Subclass of Device."""
    category = "Mobile"

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f"{self.brand} {self.model} belongs to category {self.category}")

# phone1 = Phone("Apple", "iPhone 16")
# print(phone1.__dict__)
# phone1 = Phone("Apple", "iPhone 16")
# phone2 = Phone("Samsung", "S24")

# print(f"Device.category: {Device.category}")
# print(f"Phone.category: {Phone.category}")
# phone1.info()
# phone2.info()

# Device.category = "Tech"

# print(f"Device.category: {Device.category}")
# print(f"Phone.category: {Phone.category}")


# phone1.info()
# phone2.info()

class Account:
    status = "active"

    def __init__(self, owner):
        self.owner = owner
    
a1 = Account("Tom")
a2 = Account("Eva")

# print("Step 1: Initial state")
# print(f"a1.status: {a1.status}")
# print(f"a2.status: {a2.status}")
# print(f"a1.__dict__: {a1.__dict__}")
# print(f"Account.__dict__['status']: {Account.__dict__['status']}")
# print()

# a1.status = "frozen"
# print("Step 2: After a1.status = 'frozen'")
# print(f"a1.status: {a1.status}")
# print(f"a2.status: {a2.status}")
# print(f"a1.__dict__: {a1.__dict__}")
# print()``


# del a1.status
# print("Step 3: After del a1.status")
# print(f"a1.status: {a1.status}")
# print(f"a1.__dict__: {a1.__dict__}")

class Library:
    books = []

    def add_book(self, title):
        self.title = title
        print(f"{self.title} added to personal record")

    
    @classmethod
    def add_shared_book(cls, title):
        cls.books.append(title)
        print(f"{title} added to shared library")

    @staticmethod
    def info():
        print("Library stores books in shared and personal records")

# Library.info()
# l1 = Library()
# l2 = Library()
# l1.add_shared_book("1984")
# l2.add_shared_book("Brave New World")

# print(Library.books)


# l1.add_book("Dune")

# print(l1.__dict__)
# print(l2.__dict__)


class Counter:
    '''Counter class with shared count and configurable step'''
    count = 0
    step = 1

    def __init__(self):
        '''Initialize counter and increment the shared count by step.'''
        Counter.count += Counter.step

    @classmethod
    def reset(cls):
        cls.count = 0

    @classmethod
    def set_step(cls, step):
        cls.step = step

# c1 = Counter()
# c2 = Counter()

# print(Counter.count) 
# Counter.set_step(3)

# c3 = Counter()
# print(Counter.count) 

# # Shadow with c1.count = 999; change Counter.count = 100; show c1.count, c2.count, c3.count, and Counter.count.

# c1.count = 999
# Counter.count = 100
# print(f'Shadow with c1.count = 999; change Counter.count = 100; show c1.count, c2.count, c3.count, and Counter.count.', end='\n\t')
# print(c1.count, c2.count, c3.count, Counter.count, sep="\n\t")
# print("Shadow with c1.count = 999; change Counter.count = 100; show c1.count, c2.count, c3.count, and Counter.count.")
# Counter.reset()
# print(Counter.count, c1.count, c2.count, c3.count, sep="\n")
# print("Call Counter.reset(); show Counter.count and that c1.count (shadowed) is unchanged unless you delete it.")
# del c1.count
# print(c1.count)

class CartBad:
    items = []

    def add_item(self, item):
        self.items.append(item)

class CartGood:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

cart_bad1 = CartBad()
cart_bad2 = CartBad()
cart_bad1.add_item("Apple")
cart_bad2.add_item("Banana")

print(f"\ncart_bad1.items: {cart_bad1.items}")
print(f"cart_bad2.items: {cart_bad2.items}")

cart_good1 = CartGood()
cart_good2 = CartGood()
cart_good1.add_item("Apple")
cart_good2.add_item("Banana")
print(f"\ncart_good1.items: {cart_good1.items}")
print(f"cart_good2.items: {cart_good2.items}")

class CartFixed:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)


cart_fixed1 = CartFixed()
cart_fixed2 = CartFixed()

cart_fixed1.add_item("Orange")
cart_fixed2.add_item("Grape")
print(f"\ncart_fixed1.items: {cart_fixed1.items}")
print(f"cart_fixed2.items: {cart_fixed2.items}")