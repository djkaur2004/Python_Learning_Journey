# Name Mangling in Python
'''Name mangling is the process where Python automatically changes the name of a private variable (with double underscores __) 
to avoid accidental access or modification outside the class.

Python does this to make private variables harder to access, not completely impossible.'''

# Example
class BankAccount:
    def __init__(self):
        self.__balance = 1000   # private variable

account = BankAccount()

# Direct access ❌
# print(account.__balance)  → AttributeError

# Using name mangling ✅
print(account._BankAccount__balance)   # Output: 1000

# Why Python Uses Name Mangling
'''
✔ Prevents accidental override in subclasses
✔ Protects sensitive data
✔ Avoids name conflicts
'''
