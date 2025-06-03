# Create a Car class:
# It should have a class attribute wheels initialized to 4.
# It should have instance attributes make and model.
# Create two Car objects and print their make, model, and number of wheels.

# Modify the Car class:
# Add an instance attribute color.
# Add a method set_color(color) to change the color of a car object.
# Create a Car object, set its color, and then print the color.

make = str(input("Enter the make type of the car: "))
model = str(input("Enter the model of the car: "))
color = str(input("Enter the color of the car: "))

class Car:
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = None

    def set_color(self):
        self.color = color

    def car_details(self):
        return f"Car Name: {self.make} {self.model}, Number of wheels: {Car.wheels}"
    
    def car_color(self):
        return f"Color of the {model}: {color}"
    
result = Car(make, model, color)
print(result.car_details())
print(result.car_color())
