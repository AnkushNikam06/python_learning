# Q: Add a method to the car class that displays the full name of the car (brand and model)

brand = str(input("Enter the brand of the car: "))
model = str(input("Enter the model of the car brand: "))

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

my_car = Car(brand, model)
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())
