# Exception Handling
''' What is Exception Handling?
1. Exception handling is a mechanism used to handle runtime errors (exceptions) so that the program does not crash and continues to run smoothly.
2. Exception handling allows a program to deal with errors gracefully instead of stopping abruptly.
'''

# What is an Exception?
'''An exception is an error that occurs during program execution.
Common examples:
1. Dividing by zero
2. Accessing an invalid index
3. Using a variable before defining it
4. Opening a file that doesn’t exist
'''

# Example
'''
x = 10
y = 0
print(x / y)
-> here program crashes with: ZeroDivisionError
'''

# Basic Syntax
'''
try:
    # code that may cause an exception
except:
    # code that runs if exception occurs
'''

# Why do we need exception handling?
'''
1. Prevent program crash
2. Handle unexpected user input
3. Improve user experience
4. Debug errors easily
5. Write robust and professional code
'''

