#=======================
#   Polymorphism
#=======================
 # Polymorphism means the same interface can have different implementations.
 # In Python, methods with the same name can behave differently for different object types.

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

shapes = [Square(4), Circle(3)]
for shape in shapes:
    print("Area:", shape.area())

# Polymorphism with a common function
def print_area(shape):
    print("Area:", shape.area())

print_area(Square(5))
print_area(Circle(2))
