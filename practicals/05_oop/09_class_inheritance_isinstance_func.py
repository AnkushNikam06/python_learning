# Q: Demonstrate the use of isinstance() to check if EV_result is an instance of Car and ElectricCar.

brand = str(input("Enter the brand of the Car: "))
model = str(input("Enter the model of the Car brand: "))
battery_size = str(input("Enter the size of the battery in KWh: "))
fuel_type = str(input("Enter the type of the fuel: "))

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        self.fuel_type = fuel_type

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def get_fuel_type(self):
        return f"Fuel Type: {self.fuel_type}"

    def get_brand(self):
        return self.__brand + " private"

    @staticmethod
    def general_description():
        return f"This is the mechanical car requires {fuel_type}"

print("******")
result = Car(brand, model)
print("Carname:",result.full_name())
print(result.get_fuel_type())
print("Description:",result.general_description())

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size, fuel_type):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def get_fuel_type(self):
        return f"Fuel Type: Electric Charge"

    @staticmethod
    def general_description():
        return f"If you choose Electric Car then it will require Electric Charge"

    @property
    def model(self):
        return self.__model

print("******")
EV_result = ElectricCar(brand, model, battery_size, fuel_type)
# print("Battery Size:",EV_result.battery_size)
# print("Description:",EV_result.general_description())
print("Result is instance of Car? = ",isinstance(result, Car))
print("Result is instance of ElectricCar? = ",isinstance(result, ElectricCar))

print("EV_Result is instance of Car? = ",isinstance(EV_result, Car))
print("EV_Result is instance of ElectricCar? = ", isinstance(EV_result, ElectricCar))
