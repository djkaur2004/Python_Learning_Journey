# Super Keyword
'''super() is a built-in Python function used to call methods or constructors of the parent class from the child class.

👉 In simple words:
It allows a child class to access functionality of its parent class without rewriting the code.'''

# Why super() is Used
'''
✔ To reuse parent class code
✔ To avoid repeating code
✔ To access parent constructor (__init__)
✔ To maintain proper inheritance behavior (especially in multiple inheritance)
'''

# Example 1: Calling Parent Constructor
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)   # calling parent constructor
        self.roll_no = roll_no

s = Student("John", 101)

print(s.name)      # Output: John
print(s.roll_no)   # Output: 101

# Explanation
'''
1. Student inherits from Person
2. super().__init__(name) calls the parent class constructor
3. This initializes the name variable from the parent class.

Without super(), we would have to manually call the parent class.
'''

# Example 2: Calling Parent Method
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        super().speak()      # calling parent method
        print("Dog barks")

d = Dog()
d.speak()

# Output
'''
Animal makes a sound
Dog barks
'''

# Explanation
'''
1. super().speak() calls the parent method.
2. Then the child method adds its own behavior.
'''
