class PlayerCharacter:
    memb = True
    def __init__(self, name='anonymous', age=0,  health=100, attack_power=1):#, health, attack_power):
        # if self.age > 17:
            self.name = name
            self.age = age
            self.health = health
            self.attack_power = attack_power
    def run(self):
        print(self.name)
        print('run')
        return self.name + str(self.attack_power)
    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2
     
# player1 = PlayerCharacter('bob', 20, 100, 10)
# print(player1.adding_things(1, 2))

class Item: # Created a class `Item`
    def __init__(self, title):
        self.__title = title # Created a private attribute `__title`

    def get_title(self): # Created a method `get_title()`
        return self.__title
    
    def info(self): # Created a method `info()`
        print(f"Title: {self.get_title()}")
    
class Book(Item): # Created a subclass `Book` that inherits from `Item`
    def __init__(self, title, author):
        super().__init__(title) # Called the constructor of the parent class `Item`
        self.author = author # Created an instance attribute `author`

    def info(self):
        print(f"Book: {self.get_title()}, Author: {self.author}")

class DVD(Item): # Created a subclass `DVD` that inherits from `Item`
    def __init__(self, title, duration):
        super().__init__(title) # Called the constructor of the parent class `Item`
        self.duration = duration # Created an instance attribute `duration`

    def info(self):
        print(f"Title: {self.get_title()}, Duration: {self.duration}")
class Library: # Created a class `Library`
    def __init__(self):
        self.list_of_items = []
    
    def add_item(self, item):
        self.list_of_items.append(item)

    def show_items(self):
        for item in self.list_of_items:
            item.info()

library = Library() # Created an object `library`
library.add_item(Book("Harry Potter", "J.K. Rowling"))
library.add_item(DVD("Avatar", 2.5))
library.show_items()


