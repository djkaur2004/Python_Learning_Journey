# with statement
'''with statement automatically closes the file i.e. it is not necessary to do it manually using close().'''

with open("example.txt", "r") as file:
    content = file.read()
    print(content)
