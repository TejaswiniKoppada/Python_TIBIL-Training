# 4. Implement abstraction using ABC module

from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # abstract method — must be implemented in subclasses


# Derived class 1
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Derived class 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# --- Main Program ---
rect = Rectangle(5, 3)
circle = Circle(4)

print("Area of Rectangle:", rect.area())
print("Area of Circle:", circle.area())


#
# from abc import ABC, abstractmethod
# class vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
# class car(vehicle):
#     def start(selfself):
#         print("Hello self")
# v=car()
# v.start()