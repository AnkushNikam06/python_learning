# Create a Circle class:
# It should have an attribute radius.
# It should have methods to calculate the area() and circumference().
# Ensure that self is used correctly in the methods.
# Create a Circle object and test the area() and circumference() methods.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"Area of circle is: {math.pi * self.radius **2:.2f}"
    
    def circumference(self):
        return f"Circumference of circle is: {math.pi * self.radius *2:.2f}"
    
radius = int(input("Enter the radius of circle: "))
result = Circle(radius)
print(result.area())
print(result.circumference())
