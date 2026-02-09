# Example 1
# Handling Division by Zero
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

# Example 2
# Handling Mulitple Exceptions
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print(x / y)

except ZeroDivisionError:
    print("Division by zero is not allowed")

except ValueError:
    print("Please enter valid integers")  # eg: if user entered floating-point number instead of an integer

# Example 3
# else block -> Runs only if no exception occurs
try:
    num = int(input("Enter a number: "))
    print(100 / num)

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Calculation successful")

# Example 4
# finally block -> Runs always, whether exception occurs or not
try:
    f = open("data.txt", "r")
    print(f.read())

except FileNotFoundError:
    print("File not found")

finally:
    print("Program execution completed")

# Example 5
a = input("Enter any number : ")
print(f"Multiplication table of {a} is : ")

try:
    for i in range(1,11):
       print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)

print("Some important lines of code")
print("End of loop")

# Example 6
try:
    num = int(input("\nEnter an integer : "))
except ValueError:
    print("Number entered is not an integer.")

