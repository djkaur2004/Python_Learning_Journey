# CONSTRUCTORS
''' A constructor is a special method in a class that runs automatically when an object is created.
Syntax:-

def __init__(self):
    // initialization
    
init is one of the reserved functions in Python. In Object Oriented Programming, it is known as a constructor. We 
can also create constructor by defining the function name with same class name. 
Syntax:-

class ABC:
    def ABC(self):
        // initialization
        
In Python, __init__ is an instance method that initializes a newly created onjects. It takes the object as its
first argument (self) followed by additional arguments.
.'''

# DEFAULT CONSTRUCTOR
'''Default constructor is a constructor that does not take any extra parameters (except self). '''
# Example 1
class Example:
    def __init__(self):
        print("Constructor is called")   # anything in init will print whenever function is called 

a = Example()  # Constructor is called

# Example 2
class Car:
    def __init__(self):
        self.color = "Red"
        self.brand = "Tesla"

    def display(self):
        print(f"{self.color} {self.brand}")

car1 = Car()
car1.display()  # Red Tesla

# PARAMETERIZED CONSTRUCTOR
'''When the constructor accepts arguments along with self, it is known as parameterized constructor.
These arguments can be used inside the class to assign the values to the data members. '''
class Occupation:
    def __init__(self,name,occ):
        print("What is your Occupation?")
        self.name = name
        self.occ = occ
    
    def info(self):
        print(f"{self.name} is a {self.occ}")
    
b = Occupation("Debbie", "Fashion Designer")
c = Occupation("Sam", "Tennis Player")

b.info()
c.info()
# Output
'''
What is your Occupation?
What is your Occupation?
Debbie is a Fashion Designer
Sam is a Tennis Player

here 2 objects are created so constructor will be called 2 times and then next arguments will be called
'''

