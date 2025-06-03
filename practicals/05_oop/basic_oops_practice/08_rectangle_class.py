# Create a Rectangle class:
# It should have attributes length and width.
# It should have a method area() that calculates and returns the area of the rectangle.
# Create a Rectangle object and calculate its area.

length = int(input("Enter the length of the Rectangle: "))
width = int(input("Enter the width of the Rectangle: "))

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return f"Area of Rectangle: {length * width}"
    
result = Rectangle(length, width)
print(result.area())
