# Q: Add a class variable to Car that keeps track of the number of cars created.'

fuel_type = str(input("Enter the type of the fuel (e.g. petrol, diesel or CNG): "))

class Car:
    total_car = 0
    def __init__(self, brand, model, fuel_type):
        self.__brand = brand
        self.model = model
        self.fuel_type = fuel_type
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " private"

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def get_fuel_type(self):
        return f"Fuel Type: {self.fuel_type}"

result = Car("Mahindra", "Scorpio", fuel_type)
print(result.full_name())
print(result.get_brand())
print(result.get_fuel_type())

Car("Tata", "Harrier", fuel_type)
Car("Suzuki", "Brezza", fuel_type)

print(Car.total_car)

