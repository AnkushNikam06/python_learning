# Q: Modify the car class to encapsulate the brand attribute making it private and provide a getter method for it

brand = str(input("Enter the brand name: "))
model = str(input("Enter the model of the car brand: "))
battery_size = str(input("Enter the battery capacity required in KW: "))

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " private"

    def full_name(self):
        return f"{self.__brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

result = Car(brand, model)
EV_result = ElectricCar(brand, model, battery_size)
print(result.get_brand())
print(result.full_name())
print(EV_result.battery_size)
