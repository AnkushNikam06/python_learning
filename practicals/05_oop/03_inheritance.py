# Q: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size

brand = str(input("Enter the car brand: "))
model = str(input("Enter the model of car brand: "))
battery_size = int(input("Enter the size of the battery in KW: "))

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand , model)
        self.battery_size = battery_size

result = Car(brand, model)
EV_result = ElectricCar(brand, model, battery_size)
print(result.full_name())
print(EV_result.battery_size)
