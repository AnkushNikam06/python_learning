# Q: Determine if a fruit is ripe, overripe or unripe based on its color (e.g. mango:green - unripe, yellow-ripe, brown-overripe)

fruit = str(input("Enter the fruit name: "))

if fruit == "mango":
    color = str(input("Enter the color of fruit: "))

    if color == "green":
        print("unripe")

    elif color == "yellow":
        print("ripe")
    
    elif color == "brown":
        print("overripe")
    
    else:
        print("Enter the valid color of fruit")

else:
    print("The fruit is not a mango")
