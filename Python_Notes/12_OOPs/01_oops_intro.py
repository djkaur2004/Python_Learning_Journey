# What is Object Oriented Programming?
'''Object-Oriented Programming is a programming paradigm that organizes code into classes and objects, combining data and methods 
together to improve modularity and reusability.'''

# Basic Idea 
'''In real life:
A Car has:
Data → color, model, speed
Behavior → drive(), brake()

In OOP:
Data → Attributes
Behavior → Methods
Blueprint → Class
Real thing → Object'''

# What is a Class?
'''A class is a blueprint/template for creating objects. Eg:'''
class Car:
    def __init__(self, color, model):
        self.color = color    # instance variable
        self.model = model

    def drive(self):
        print("The car is moving")

# What is an Object?
'''An object is an instance of a class used to access the properties of the class.'''
car1 = Car("Red", "Tesla")
car2 = Car("Blue", "BMW")

print(car1.color)  # Red
car1.drive()       # The car is moving

# Self Parameter
''' Self parameter is a refernce to the current instance of the class, and is used to access variables that belongs to the class.'''

# Another Example
class Person:
    name = "John"    # class variable
    occupation = "Web Developer"
    networth = 1000000
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
b = Person()
c = Person()

a.name = "Jason"
a.occupation = "Architect"

b.name = "June"
b.occupation = "Fashion Designer"

a.info()  # Jason is a Architect
b.info()  # June is a Fashion Designer
c.info()  # John is a Web Developer
