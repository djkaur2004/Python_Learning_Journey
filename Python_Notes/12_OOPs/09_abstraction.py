# What is Abstraction?
'''Abstraction is the OOP concept of hiding internal implementation details and showing only the essential features of an object.

👉 In simple words:
Users know what a system does, but they don’t need to know how it works internally.

Example:
When you drive a car, you use the steering wheel and pedals, but you don't need to know the internal engine mechanism.
'''

# Example of Abstraction
'''In Python, abstraction is implemented using the abc (Abstract Base Class) module.'''

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(3.14 * self.radius * self.radius)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)

c = Circle(5)
c.area()        # Output: 78.5

r = Rectangle(4,6)
r.area()        # Output: 24

# Explanation
'''
1. Shape is an abstract class
2. area() is an abstract method
3. Child classes must implement the area() method
4. Users only call area() without knowing the internal calculation.
'''
