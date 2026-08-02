#=======================
#   Classes and Objects
#=======================
 # Classes define object templates, and objects are individual instances.
 # Use classes to organize related data and behavior.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

# Create an object
person1 = Person("Prince", 31)
person1.greet()
print(person1)

# Inheritance example
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        print(f"Hello, I am {self.name}, my student ID is {self.student_id}.")

student = Student("Riya", 20, "S123")
student.greet()

# Class variable example
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
print("Number of Counter instances:", Counter.count)
