# Q: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance

brand = str(input("Enter the brand of the Car: "))
model = str(input("Enter the model of Car brand: "))
battery_size = str(input("Enter the size of the battery: "))
fuel_type = str(input("Enter the fuel type: "))

class Car:
    def __init__(self, brand, model, fuel_type):
        self.__brand = brand
        self.__model = model
        self.fuel_type = fuel_type

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def get_fuel_type(self):
        return f"Fuel Type: {self.fuel_type}"

    @staticmethod
    def general_description():
        return f"This is the mechanical car requires {fuel_type}"

    @property
    def model(self):
        return self.__model

print("*********")
result = Car(brand, model, fuel_type)
print("Car Name:",result.full_name())
print(result.get_fuel_type())
print("Description:",result.general_description())


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size, fuel_type):
        super().__init__(brand, model, fuel_type)
        self.battery_size = battery_size

    def get_fuel_type(self):
        return f"If you choose Electric Car, it will require an Electric Charge"

    @staticmethod
    def general_description():
        return f"This is the Electric Car which is costier than mechanical one."

print("********")
EV_result = ElectricCar(brand, model, battery_size, fuel_type)
print("Battery Size:",EV_result.battery_size)
print("Description:",EV_result.general_description())

print("********")
print("Result is the instance of Car? = ", isinstance(result, Car))
print("Result is the instance of Electric Car? = ", isinstance(result, ElectricCar))

print("********")
print("EV Result is the instance of Car? = ", isinstance(EV_result, Car))
print("EV Result is the instance of Electric Car? = ", isinstance(EV_result, ElectricCar))

class Engine_info:
    def Engine(self):
        return f"This is Mechanical Engine used for Car using {fuel_type}"

class Battery_info:
    def Battery(self):
        return f"Battery size of the Car: {battery_size}"

class ElectricCarTwo(Car, Engine_info, Battery_info):
    pass

second_result = ElectricCarTwo(brand, model, fuel_type)
print(second_result.Engine())
print(second_result.Battery())
