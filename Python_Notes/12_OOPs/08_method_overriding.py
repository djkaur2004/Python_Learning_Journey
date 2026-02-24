# Method Overriding
'''Method overriding happens when a child class provides its own implementation of a method that already exists in the parent class.'''

# Example
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):   # overriding parent method
        print("Dog barks")

a = Animal()
d = Dog()

a.speak()   # Animal makes a sound
d.speak()   # Dog barks
