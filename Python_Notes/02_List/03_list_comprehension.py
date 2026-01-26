# LIST COMPREHENSION
# A short and elegant way to create lists in Python using a single line of code.
# Instead of writing a for loop and appending items, you can generate lists directly.

lst = [i for i in range(4)]
print("\n",lst)  # [0,1,2,3]

lst1 = [i*i for i in range(10) if i%2==0]
print("\nList comprehension : ",lst1)  # [0, 4, 16, 36, 64]

# Example
# Square of numbers (without list comprehension)
print("Square of numbers without list comprehension")
squares = []
for i in range(5):
    squares.append(i*i)
print(squares)   

# Square of numbers (with list comprehension)
print("Square of numbers with list comprehension")
squares = [i*i for i in range(5)]
print(squares)   # [0, 1, 4, 9, 16]

# Why use list comprehension?
''' 
1. Shorter & cleaner code
2. More readable than for loops (if not overused)
3. Often faster
'''
