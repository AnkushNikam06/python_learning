# Q: Suggest an activity based on the weather (e.g. Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman)

# forecast = ("Sunny", "Rainy", "Snowy")
Weather = str(input("Enter the weather: "))

if Weather == "Sunny":
    activity = "Go for a walk"

elif Weather == "Rainy":
    activity = "Read a book"

elif Weather == "Snowy":
    activity = "Build a snowman"

print(activity)

else:
    print("Select a valid Weather")
