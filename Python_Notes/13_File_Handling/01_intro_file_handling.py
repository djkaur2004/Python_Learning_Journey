# What is File Handling?
'''File handling in Python is the process of creating, reading, writing, and manipulating files stored on your system.

👉 In simple words:
It allows your program to store data permanently instead of keeping it only in memory.'''

# Basic Steps in File Handling
'''
1. Open a file
2. Perform operation (read/write)
3. Close the file
'''

# Example
# Writing to a file
file = open("example.txt", "w")  # here a file will be created as we are using write
file.write("Hello World\n")
file.write("Learning File Handling")
file.close()

# Reading from a file
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
