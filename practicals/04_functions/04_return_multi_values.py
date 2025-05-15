# Q: Create a function that returns both the area and circumference of a circle given its radius
import math

radius = int(input("Enter the radius of the circle: "))

def circle_stats(radius):
    area = radius ** 2 * math.pi
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = circle_stats(radius)
print("Area: ", round(a,2), "Circumference: ", round(c,2))

# print(circle_stats(radius))
