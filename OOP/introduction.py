class Car: # I created a class car
    def __init__(self, brand, model, year): #I created a constructor
        self.brand = brand #I created attributes brand, model and year
        self.model = model
        self.year = year

    def start(self): # I created a method start
        print(f"{self.brand} {self.model} is starting...")

audi = Car("Audi", "A4", 2022) # I created an object
aito = Car("Aito", "M7", 2025) 

# print(audi.start()) # I called the method start
# print(aito.start())

class Laptop: # I created a class laptop
    
    category = "Electronics" # I created a class attribute

    def __init__(self, brand, model, price): # I created a constructor
        self.brand = brand # I created attributes brand, model and price
        self.model = model
        self.price = price

    def info(self): # I created a method info
        print(f"{self.brand} {self.model} costs {self.price}$ and belongs to {self.category}.")

laptop1 = Laptop("Asus", "ROG", 1500) # I created an object
laptop2 = Laptop("Macbook", "Pro", 2000)

Laptop.category = "Computers" # I changed the class attribute

# laptop1.info() # I called the method info
# laptop2.info()

class Student: # I created a class Student
    def __init__(self, name, grade): # I created a constructor
        self.__name = name # I created the attributes name and grade
        self.__grade = grade

    def set_grade(self, new_grade): # I created a method set_grade
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
    
    def get_info(self): # I created a method get_info
        print(f"Student {self.__name} has grade {self.__grade}.")

# I created two objects
student1 = Student("John", 85)
student2 = Student("Jim", 90)

# print(student1.get_info())

# print("Values before change:")
# student1.get_info()
# student2.get_info()

# # I called the method set_grade and changed the grade of the student
# student1.set_grade(89)
# student2.set_grade(101) # I entered an invalid grade

# print("\nValues after change:")
# student1.get_info()
# student2.get_info()

# Created a class Vehicle
class Vehicle:
    # Created a constructor
    def __init__(self, brand, year): 
        # Created the attributes brand and year
        self.brand = brand
        self.year = year
    
    # Created a method display_info
    def display_info(self):
        print(f"{self.brand} vehicle from {self.year}.")

# Created a class ElectricCar that inherits from the Vehicle class
class ElectricCar(Vehicle):
    # Created a constructor
    def __init__(self, brand, year, battery_capacity):
        super().__init__(brand, year) # Called the constructor of the parent class
        self.battery_capacity = battery_capacity

    # Created a method display_info that overrides the display_info method in the Vehicle class
    def display_info(self):
        print(f"{self.brand} electric car from {self.year} with {self.battery_capacity} kWh battery.")

tesla = ElectricCar('Tesla', 2022, 75) # Created an ElectricCar object 
# tesla.display_info() # Called the display_info method

# Created a class Shape
class Shape:
    # Created a method area
    def area(self):
        print("Area not defined")

# Created a class Circle that inherits from the Shape class
class Circle(Shape):
    # Created a constructor
    def __init__(self, radius):
        self.radius = radius
    
    # Created the area() method
    def area(self):
        import math # Imported the math module
        print(f"Area of circle with radius {self.radius} is {math.pi * self.radius ** 2:.2f}")

# Created a class Rectangle that inherits from the Shape class
class Rectangle(Shape):
    # Created a constructor
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Created the area() method
    def area(self):
        print(f"Area of rectangle with width {self.width} and hight {self.height} is {self.width * self.height:.2f}")


circle = Circle(5) # Created a Circle object
rectangle = Rectangle(5, 8.4) # Created a Rectangle object
lst = [circle, rectangle] # Created a list

# Called the area() method
for shape in lst: 
    shape.area()