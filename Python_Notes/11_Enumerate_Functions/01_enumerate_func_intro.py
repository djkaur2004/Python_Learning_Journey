# Enumerate Functions
''' The enumerate function is a built-in function in python that allows you to loop over a sequence(such as list, tuple, or string)
and get the index and value at the same time.'''

# Why do we need enumerate()?
# Code without using enumerate()
fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):
    print(i, fruits[i])

# Using enumerate()
fruits = ["apple", "banana", "cherry"]

for index, value in enumerate(fruits):
    print(index, value)
# here the code is more readable and cleaner

