# Q: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors

brand = str(input("Enter the brand of the car: "))
model = str(input("Enter the model of car brand: "))
battery_size = str(input("Enter the size of the batter in KWh: "))
fuel_type = str(input("Enter the type of the fuel (e.g. petrol, diesel or CNG): "))

class Car:
    def __init__(self, brand, model, fuel_type):
        self.__brand = brand
        self.model = model
        self.fuel_type = fuel_type

    def get_brand(self):
        return self.__brand + " private"

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def get_fuel_type(self):
        return f"Fuel Type: {self.fuel_type}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size, fuel_type):
        super().__init__(brand, model, fuel_type)
        self.battery_size = battery_size

    def get_fuel_type(self):
        return f"Fuel Type: Electric Charge"

result = Car(brand, model, fuel_type)
print(result.full_name())
print(result.get_brand())
print(result.get_fuel_type())

EV_result = ElectricCar(brand, model, battery_size, fuel_type)
print(EV_result.battery_size)
print(EV_result.get_fuel_type())
