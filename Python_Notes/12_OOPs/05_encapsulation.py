# 1. Public Members
'''Public variables and methods can be accessed from anywhere — inside the class, outside the class, and in subclasses.

When to use:
When data is safe to be accessed or modified freely.'''

# 2. Protected Members
'''Protected members are intended to be accessed only within the class and its subclasses.

Written with a single underscore _
(Still accessible outside, but considered internal by convention)

When to use
When data should not be accessed directly outside the class but can be used by subclasses.'''

# 3. Private Members
'''Private members are meant to be accessed only within the class.
Python uses name mangling to make them harder to access.

Written with double underscore __'''

# Example
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public variable
        self._salary = salary   # Protected variable
        self.__ssn = ssn        # Private variable

    def show_details(self):
        print("Name:", self.name)
        print("Salary:", self._salary)
        print("SSN:", self.__ssn)


class Manager(Employee):
    def access_protected(self):
        print("Accessing protected salary:", self._salary)


emp = Employee("Luna", 50000, "123-45-6789")

# Public → accessible
print(emp.name)          # Output: Luna

# Protected → accessible but not recommended
print(emp._salary)       # Output: 50000

# Private → not accessible directly (will cause error)
# print(emp.__ssn)       # ❌ AttributeError

emp.show_details()
# Output:
# Name: Luna
# Salary: 50000
# SSN: 123-45-6789

mgr = Manager("Amanda", 80000, "987-65-4321")
mgr.access_protected()
# Output:
# Accessing protected salary: 80000
