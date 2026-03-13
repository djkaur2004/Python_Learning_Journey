# Magic Methods/Dunders
'''Magic methods, also called dunder methods (double underscore methods), are special methods in Python that start and end with 
double underscores.

Example:
__init__
__str__
__len__
__add__

1. They are powerful tools that allow you to customize the behaviour of your classes.
2. These methods allow Python objects to interact with built-in functions and operators.
3. They are used to implement special methods such as addition, subtraction and comparison operators, as well as some more 
advanced techniques like descriptors and properties.'''

# Example
class Employee:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i
    # If we use len() directly the program will show error
  
    def __str__(self):
        return f"The name of the employee is {self.name}"  # str method is always returned

e = Employee("Fauna")
print(e)
print(len(e))

# Output
'''
The name of the employee is Fauna
5
'''
