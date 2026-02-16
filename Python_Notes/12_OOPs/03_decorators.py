# Decorators
'''A decorator in Python is a function that modifies or extends the behavior/functionality of another function without changing 
its actual code.

Instead of changing a function directly, you decorate it.
Original function → Decorator → Enhanced function'''

# Syntax
'''
@decorator_name
def function_name():
    pass

The @decorator_name is just a cleaner way of writing:
function_name = decorator_name(function_name)
'''

# Example 1: Adding a Message Before and After a Function Runs
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function runs.")
        func()
        print("Something is happening after the function runs.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Output
'''
Something is happening before the function runs.
Hello!
Something is happening after the function runs.
'''

# Example 2
def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Have a nice day\n")
    return mfx

@greet
def hello():
    print("Hello")

hello()

# Ouput
'''
Good Morning
Hello 
Have a nice day
'''

# Example 3
@greet
def greeting():
    print("Hey there how are you")

greeting()

# Output
'''
Good Morning
Hey there how are you
Have a nice day
'''

# Args and Kwargs in Python
# In order to use greet for add function with arguments we use *args and **kwargs
# Here *args is writing arguments as tuples and **kwargs is writing arguments as dictonary.

def greets(fxs):
    def mfxs(*args, **kwargs):
        print("Good Morning")
        fxs(*args, **kwargs)
        print("Thanks for using the function")
    return mfxs

@greets
def add(a, b):
    print(a + b)

add(4,5)

# Output
'''
Good Morning
9
Thanks for using the function
'''
