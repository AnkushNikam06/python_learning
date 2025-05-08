# Q: Choose a mode of transportation based on the distance (e.g. <3km: Walk, 3-15km: Bike. >15km: Car)

travel = int(input("Enter the distance you wish to travel in km: "))

if travel < 3:
    transportation = "Walking"

elif travel <= 15:
    transportation = "Bike"

else:
    transportation = "Car"

print("You can cover this distance by:", transportation)
