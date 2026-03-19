# Read Method

# 1. read -> Reads the entire file
file = open("example.txt", "r")
print(file.read())
file.close()

#  2. readline -> Reads one line at a time
file = open("example.txt", "r")

print(file.readline())   # first line
print(file.readline())   # second line

file.close()

# 3. readlines -> Reads all lines and return a list
file = open("example.txt", "r")

lines = file.readlines()
print(lines)

file.close()
