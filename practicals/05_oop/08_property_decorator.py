# Q: Use a property decorator in the Car class to make the model attribute read-only

brand = str(input("Enter the car brand: "))
model = str(input("Enter the model of the car brand: "))
battery_size = str(input("Enter the size of battery in KWh: "))
fuel_type = str(input("Enter the type of fuel to be used: "))

class Car:
    def __init__(self, brand, model):
        self.__brand    = brand
        self.__model    = model
        self.fuel_type  = fuel_type

    def get_brand(self):
        return self.__brand + "private"

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def get_fuel_type(self):
        return f"Fuel Type: {self.fuel_type}"

    @staticmethod
    def general_description():
        return f"This is the mechanical car which requires {fuel_type}"

    @property
    def model(self):
        return self.__model

print("**********")
Result = Car(brand, model)
print("Car Brand and Name:", Result.full_name())
print(Result.get_fuel_type())
print(Result.general_description())

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def get_fuel_type(self):
        return f"Fuel Type: Electric Charge"

    @staticmethod
    def general_description():
        return f"If you select Electric model, it will require Electric Charge to run."

print("********")
print("Optional Information: ")
EV_result = ElectricCar(brand, model, battery_size)
print("Battery size of the car:",EV_result.battery_size, "KWh")
print(EV_result.general_description())
