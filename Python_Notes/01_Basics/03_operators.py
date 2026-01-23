# Operators are special symbols used to perform operations on variables or values.

# Types of Operators
# 1. Arithmetic Operator
num_1 = 20
num_2 = 10

# addition
sum = num_1 + num_2
print('sum = ',sum)

# difference
diff = num_1 - num_2
print("difference = ",diff)

# multiplication
pro = num_1 * num_2
print("product = ",pro)

# division
quo = num_1/num_2
print("quotient = ",quo)

# exponent
exp = num_1**num_2
print("exponent = ",exp)

# modulus
mod = num_1 % num_2
print("modulus = ",mod)

# 2. Assignment Operator
a = 5
a += 5
print(a)

b = 5
b -= 2
print(b)

# 3. Comparison Operator
a = 5
b = 10
# Gives answer in True or False
print(a == b)    # equal to
print(a != b)    # not equal to
print(a > b)     # greater than 
print(a < b)     # less than
print(a <= b)    # less than equal to
print(a >= b)    # greater than equal to 

# 4. Logical Operators
a = 10

# and -> Returns True if only both conditions are True
print(a > 5 and a < 20)   # True

# or -> Returns True if atleast one condition is True
print(a < 5 or a == 10)   # True

# not -> Reverses the result (True becomes False, and vice versa)
x = True
print(not x)   # False

# 5. Identity Operator
x = 5
y = 5

# is 
print(x is y)  # True

# is not 
print(x is not y)  # False

# 6. Membership Operator
a = 5
b = 10
c = [1,2,3,4,5]

# in
print(a in c)  # True
print(b in c)  # False

# not in
print(a not in c)  # False
print(b not in c)  # True

