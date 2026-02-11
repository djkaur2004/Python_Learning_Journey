# Example 1
names = ["Alice", "Bob", "Charlie"]

for index, name in enumerate(names):
    print(index, name)
'''Output
0 Alice
1 Bob
2 Charlie
'''

# Example 2: Starting index from 1
names = ["Alice", "Bob", "Charlie"]

for index, name in enumerate(names, start=1):
    print(index, name)
'''Output
1 Alice
2 Bob
3 Charlie
'''

# Example 3: Using a String
word = "Python"

for index, letter in enumerate(word):
    print(index, letter)
'''Output
0 P
1 y
2 t
3 h
4 o
5 n
'''

# Example 4: Converting enumerate() to a list
numbers = [10, 20, 30]
print(list(enumerate(numbers)))  # [(0, 10), (1, 20), (2, 30)]
