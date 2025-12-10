from abc import ABC, abstractmethod

# Parent class with abstraction
class Shape(ABC):
    def describe(self):
        # Regular method
        return "I am a geometric shape."

    @abstractmethod
    def area(selfself):
        # Abstract method to be implemented with child classes
        pass


# Child class implementing abstract method
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Use both parent and child methods
rect = Rectangle(5, 3)
print(rect.describe())      # Parent's regular method
print(rect.area())          # Child's implementation of abstract method
