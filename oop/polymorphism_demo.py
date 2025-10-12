import math

# Base class for all shapes
class Shape:
    # Method meant to be overridden by subclasses
    def area(self):
        # Raises an error if a subclass doesn’t override this method
        raise NotImplementedError("Subclasses must override the area() method")


# Derived class representing a rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Override the area method for rectangles
    def area(self):
        return self.length * self.width


# Derived class representing a circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Override the area method for circles
    def area(self):
        return math.pi * (self.radius ** 2)
