#=======================
#   Inheritance
#=======================
 # Inheritance allows a class to reuse code from another class.
 # A child class inherits attributes and methods from a parent class.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + " makes a sound")

class Dog(Animal):
    def speak(self):
        print(self.name + " barks")

class Cat(Animal):
    def speak(self):
        print(self.name + " meows")

# Create objects from child classes
dog = Dog("Rex")
cat = Cat("Whiskers")

dog.speak()
cat.speak()

# Child class can extend the parent class
class Bird(Animal):
    def fly(self):
        print(self.name + " is flying")

bird = Bird("Tweety")
bird.speak()
bird.fly()
