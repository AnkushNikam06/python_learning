# Q: Create a Car class with attributes like brand and models. Then create an instance of this class
brand = str(input("Enter the car brand: "))
model = str(input("Enter the model of the car brand: "))

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car(brand, model)
print(my_car.brand)
print(my_car.model)
