# Q: Customize a coffee order: "Small", "Medium" or "Large" with an option for "Extra shot" of espresso

order = str(input("Enter the order size you want to order e.g. Small/Medium or Large: "))
extra_shot = input("Do you want an extra shot with coffee? (Yes/No): ")

if extra_shot.lower() == "yes":
    extra_shot = "True"
else:
    extra_shot = "False"

if extra_shot == "True":
    coffee = order + " Coffee with an extra shot"

else:
    coffee = order + " coffee"

print(coffee)
