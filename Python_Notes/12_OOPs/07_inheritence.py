# What is Inheritence
'''Inheritance is an OOP concept where a child class (subclass) can acquire the properties and methods of a parent class (superclass).'''

# Syntax
'''
class BaseClass:                   # Parent Class
    Body of base class
class DerivedClass(BaseClass):     # Child Class
    Body of derived class
'''

# Types of Inheritence

# 1. Single Inheritence
'''Single inheritence is a type of inheritence where a class inherits properties and behaviors from a single parent.'''
class Animal:    # Parent Class/ Base Class
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):   # Dog inherits from Animal    # Child Class/ Derived Class
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()   # Animal makes a sound
d.bark()    # Dog barks

# 2. Multiple Inheritence
'''It is a type of inheritence where one child class inherits from more than one parent class.'''
class Father:
    def skills(self):
        print("Gardening")

class Mother:
    def talent(self):
        print("Painting")

class Child(Father, Mother):
    pass

c = Child()
c.skills()    # Gardening, inherited from Father class
c.talent()    # Painting, inherited from Mother class

# 3. Multilevel Inheritence
'''It is a type of inheritence where a class inherits from a child class, forming a chain.'''
class Grandparent:
    def house(self):
        print("Grandparent's house")

class Parent(Grandparent):
    def car(self):
        print("Parent's car")

class Child(Parent):
    def bike(self):
        print("Child's bike")

c = Child()
c.house()    # Grandparent's house, inherited from Grandparent class
c.car()      # Parent's car, inherited from Parent class
c.bike()     # Child's bike

# 4. Hierarchical Inheritance
'''It is a type of inheritence where multiple child classes inherit from the same parent class.'''
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Cat(Animal):
    def meow(self):
        print("Meowing")

d = Dog()
c = Cat()

d.eat()    # Eating
c.eat()    # Eating
# here both Dog and Cat class inherited same Animal class and its properties and methods.

# Hybrid Inheritence
''' It is a combination of two or more inheritence types'''
class A:
    def method_a(self):
        print("Class A")

class B(A):
    def method_b(self):
        print("Class B")

class C(A):
    def method_c(self):
        print("Class C")

class D(B, C):
    def method_d(self):
        print("Class D")

obj = D()
obj.method_a()    # Class A
obj.method_b()    # Class B
obj.method_c()    # Class C
obj.method_d()    # Class D
'''
here in the above more than one inheritence type is used:
1. Hierarchical Inheritance (A → B and A → C)
2. Multiple Inheritance (B + C → D)
'''
