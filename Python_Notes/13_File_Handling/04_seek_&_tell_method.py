# Seek and Tell Methods

# 1. seek() Method
'''It moves the file pointer to a specific position.'''

# Example
file = open("example.txt", "r")

file.seek(0)   # move to beginning
print(file.read())

file.close()

# Another example with position
file = open("example.txt", "r")

file.seek(6)
print(file.read())

file.close()

# 2. tell() Method
'''It returns the current position of the file pointer.'''

# Example
file = open("example.txt", "r")

print(file.tell())   # position before reading
file.read(5)
print(file.tell())   # position after reading

file.close()

