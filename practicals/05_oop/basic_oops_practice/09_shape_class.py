# Create a Shape class:
# It should have a method area() that returns 0.
# Create a Rectangle class that inherits from Shape and overrides the area() method.
# Create a Circle class that inherits from Shape and overrides the area() method.
# Create objects of Rectangle and Circle and calculate their area.


import math
class Shape:
    def area(self):
        return 0
    
class Rectangle(Shape):
    def area(self):
        length = int(input("Enter the length of rectangle: "))
        width = int(input("Enter the width of the rectangle: "))
        return length*width
    
class Circle(Shape):
    def area(self):
        radius = int(input("Enter the radius of the circle: "))
        return math.pi*radius**2

rect = Rectangle()
circle = Circle()

print("Area of Rectangle:",rect.area())
print("Area of Circle:",circle.area())
