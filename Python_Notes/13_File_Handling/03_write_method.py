# Write Method

# 1. write -> Writes data to a file
file = open("example.txt", "w")

file.write("Hello\n")
file.write("Python")

file.close()

# 2. writelines -> Write multiple lines (list)
file = open("example.txt", "w")

lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
file.writelines(lines)

file.close()
