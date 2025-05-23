# Q: Add a static method to the Car class that returns a general description of a Car.

brand = str(input("Enter the brand of the Car: "))
model = str(input("Enter the model of Car brand: "))
battery_size = str(input("Enter the size of the battery in KWh: "))
fuel_type = str(input("Enter the fuel type for Car (e.g. petrol or diesel or CNG): "))

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

    @staticmethod
    def general_description():
        return f"These are the mechanical cars which requires {fuel_type}"

Result = Car(brand, model, fuel_type)
print(Result.full_name())
print(Result.get_fuel_type())
print(Result.general_description())


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size, fuel_type):
        super().__init__(brand, model, fuel_type)
        self.battery_size = battery_size

    def get_fuel_type(self):
        return f"Fuel Type: Electric Charge"

    @staticmethod
    def general_description():
        return f"These are the Electric Cars which requires Electric Charge"

EV_result = ElectricCar(brand, model, battery_size, fuel_type)
print("Battery_size: ", EV_result.battery_size)
print(EV_result.get_fuel_type())
print(EV_result.general_description())
