# CONDITIONAL STATEMENTS
# 1. Conditional statements are used to make decisions in a program.
# 2. They allow the program to execute different code blocks depending on whether a condition is True or False.

# WHAT ARE IF-ELSE STATEMENTS
'''If–else statements are a type of conditional statement in Python.
They check a condition:
If the condition is True → if block runs
If the condition is False → else block runs '''

# SYNTAX
'''
if condition:
    # code runs if condition is True
else:
    # code runs if condition is False
'''

# 1. IF-ELSE STATEMENTS
a = 30
b = 50

if(a>b):
  print("a is the greatest number")
else:
  print("b is the greatest number")

# 2. IF-ELSE STATEMENTS WHERE COMPUTER TAKES INPUT FROM USER(KEYBOARD) USING INPUT() FUNCTION
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if(a>b):
  print("First number is the greatest")
else:
  print("Second number is the greatest")

# 3. IF-ELIF-ELSE LADDER IN PYTHON
a = input("Enter Marks : ")
a = int(a)

if(a<=39):
    print("Grade : F")
elif(a>=40 and a<=59):
    print("Grade : C")
elif(a>=60 and a<=79):
    print("Grade :B")
else:
    print("Grade : A")            

# 4. MULTIPLE IF STATEMENTS
b = 8 
if(b<3):
    print("The value of b is greater than 3")

if(b>13):
    print("The value of b is greater than 13")

if(b>7):
    print("The value of b is greater than 7")

if(b>17):
    print("The value of b is greater than 17")
else:
    print("The value of b is not greater than 17")            
'''NOTE: THE FIRST THREE IF STATEMENTS ARE INDEPENDENT AND THEY WILL PRINT INDIVIDUALLY BUT THE LAST 
IF STATEMENT IS WITH ELSE SO BOTH IF AND ELSE STATEMENT WILL BE CONSIDERED BEFORE RETURNING A VALUE.''' 

# 5. ELSE IS OPTIONAL
c = 7
if(c==7):
    print("YES")
elif(c>56):
    print("MAYBE")    

''' IMPORTANT NOTES :
1. THERE CAN BE ANY NUMBER OF ELIF STATEMENTS.
2. LAST ELSE IS EXECUTED ONLY IF ALL THE CONDITIONS INSIDE ELIF ARE FALSE.
3. ELSE IS OPTIONAL. PROGRAM WILL RUN EVEN IF WE DOESN'T USE ELSE STATEMENT.'''

# 6. NESTED IF STATEMENT
num = 18
if(num < 0):
    print("Number is negative")
elif(num > 0):
    if(num <= 10):
        print("Number is between 1-10")
    elif(num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")    

# SHORT HAND IF ELSE STATEMENTS
''' There is also a shorthand syntax for the if-else statement that can be used when the condition being
tested is simple and the code block to be executed are short. Eg:- '''
a = 330
b = 3303
print("A") if a>b else print("=") if a==b else print("B")

# Writing else with double quotes is important otherwise the code will show error
print(9) if a<b else ""
# OR
c = 9 if a>b else 0
print(c)


