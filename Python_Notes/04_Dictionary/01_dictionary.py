# WHAT IS A DICTIONARY
''' A dictionary is an mutable, unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.'''
# Dictionary is a Mapped Data

# Creating a Dictionary
myDict = {
    "fast" : "furious",
    "eat" : "vegetables",
    "list" : [1,23,3],
    "anotherdict" : {'knock knock' : 'who is there'}
}
print(myDict)  # {'fast': 'furious', 'eat': 'vegetables', 'list': [1, 23, 3], 'anotherdict': {'knock knock': 'who is there'}}

# Printing value for the given key
print(myDict['fast'])  # furious
print(myDict['eat'])  # vegetables

# Adding a new key:value pair in dictionary
myDict['list'] = ['4,77,89']
print(myDict['list'])  # ['4,77,89']
# dictionary is mutable that means we can change it accordingly.

# Updated dictionary
print(myDict)  # {'fast': 'furious', 'eat': 'vegetables', 'list': ['4,77,89'], 'anotherdict': {'knock knock': 'who is there'}}

# we can print another dictionary in a dictionary and its elements.
print(myDict['anotherdict'])  # {'knock knock': 'who is there'}
print(myDict['anotherdict']['knock knock'])  # who is there

# NOTE : KEY IN A DICTIONARY CANNOT BE REPEATED OTHERWISE THE COMPILER MAY THINK THERE IS CHANGE IN THE VALUE SO IT WILL GET CONFUSED AND GIVES A ERROR IN THE CODE WRITTEN.

# dictionary does not allow duplicate values
dict_2 = {'name':'David','age':'30','country':'India','name':'David','age':'30','country':'India'}
print(dict_2)  # {'name': 'David', 'age': '30', 'country': 'India'}

'''Advantages of dictionary
1. Fast Looksup:- Keys are hashed, making key-based access very efficient.
2. Flexibility:- Keys can be immutable data types, and values can be in any Python object.'''
