# While Loop
# 1. A while loop runs as long as a condition is True.
# 2. The condition is checked before each iteration.

# SYNTAX
'''
while condition:
    # code block
'''
# Example 1
i = 1  # initialization
while i <= 5:  # condition
    print(i)  # 1 2 3 4 5 (this prints vertically)
    i += 1  # iteration

# Example 2
i = 0
while i<5:
    print("YES " + str(i)) # YES 0, YES 1 and so on prints 5 times (vertically)
    i = i + 1

'''Here, i = i+1 is the iteration used. If we do not use iteration and left it at i=0 which is intializtion step then
loop becomes an infinite loop and it prints "YES" without stoping.'''

# Example 3
i = 1 
while i<=50:
    print(i)  # numbers print from 1 to 50
    i = i + 1

# Example 4
i = 0
while i<5:
    print("HELLO")  # here HELLO prints 5 times from index 0 to index 4 (as i<5 so fifth index is not considered)
    i = i + 1

# Example 5
# Program to print content of a list using while loop
fruits = ['Apples', 'Mangoes', 'Kiwi', 'Orange', 'Watermelon']
i = 0
while i<len(fruits):
    print(fruits[i])
    i = i + 1    
# Output of the above code is 
# Apples
# Mangoes
# Kiwi
# Orange
# Watermelon
