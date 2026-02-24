# What is Inheritence
'''Inheritance is an OOP concept where a child class (subclass) can acquire the properties and methods of a parent class (superclass).'''

# Example
class Animal:    # Parent Class/ Base Class
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):   # Dog inherits from Animal    # Child Class/ Derived Class
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()   # inherited method
d.bark()

# Output
'''
Animal makes a sound
Dog barks'''

# Types of Inheritence
