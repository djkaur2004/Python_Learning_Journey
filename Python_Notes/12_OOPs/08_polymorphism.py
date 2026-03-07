# Polymorphism
'''Polymorphism refers to the ability of a single method, function, or operator to behave differently depending on the object 
or data type.'''

# 1. Method Overriding
'''Method overriding happens when a child class provides its own implementation of a method that already exists in the 
parent class.'''

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

animals = [Dog(), Cat()]

for a in animals:
    a.speak()

'''Output
Dog barks
Cat meows
'''

'''1. All classes have the same method name speak()
2. But each class implements it differently'''

# 2. Method Overloading
'''Method overloading means multiple methods with the same name but different parameters.'''

class Calculator:

    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()

print(calc.add(5, 10))      # two numbers
print(calc.add(5, 10, 15))  # three numbers

'''Output
15
30
'''
# Same method works with different numbers of arguments.

# 3. Operator Overloading
'''Operator overloading means operators behave differently depending on the operands.'''

print(5 + 3)        # integer addition
print("Hello " + "World")   # string concatenation

'''Output
8 
Hello World
'''
# The same + operator performs different operations.
