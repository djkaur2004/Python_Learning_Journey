# Instance Variable
'''An instance variable is a variable that belongs to a specific object of a class.
It is defined inside the constructor (__init__) using self, and each object has its own separate copy of it.

In simple words:
It stores data that is unique for every object.

Example: name, age, marks, salary
'''

# Class Variable
'''A class variable is a variable that belongs to the class itself rather than any single object.
It is defined directly inside the class (outside methods), and all objects share the same copy of it.

In simple words:
It stores data that is common for all objects.

Example: company name, school name, interest rate
'''

class Student:
    school = "ABC School"     # class variable

    def __init__(self, name, marks):
        self.name = name      # instance variable
        self.marks = marks    # instance variable

s1 = Student("Aman", 90)
s2 = Student("Riya", 85)

print(s1.name)      # Aman
print(s2.name)      # Riya

print(s1.school)    # ABC School
print(s2.school)    # ABC School

'''
1. name and marks are different for each object
2. school is the same for all objects.
'''
