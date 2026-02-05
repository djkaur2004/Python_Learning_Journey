# Example 1
def greet():
    print("Hello, welcome to Python!")

greet()  # this is function calling
# Output : Hello, welcome to Python!

# Example 2: Greet user by taking input from the keyboard
def greet(name):
    print("Good day, "+ name)

name1 = input("Enter name : ") 
greet(name1)   

# Example 3: Adding two numbers (passing two parameters)
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8

# Example 4: Percentage of marks
def percent(marks):
    p = (sum(marks)/400)*100
    return p

marks1 = [45, 67, 89, 43]
percentage1 = percent(marks1)

marks2 = [56, 67, 78, 80]
percentage2 = percent(marks2)

print(percentage1)  # 61.0
print(percentage2)  # 70.25

# Example 5: Using a default parameter when no argument is passed in the function
def greet(name = "Stranger"):
    print("Good Day, "+name)

greet("John")  # Good Day, John
greet()        # Good Day, Stranger


