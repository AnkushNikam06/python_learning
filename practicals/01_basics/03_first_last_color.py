# Q: Write a Python program to display the first and last colors from the list.

colors = str(input("Enter the series of colors separated by commas: "))

colors = colors.split(",")

print("First_color:", colors[0], "and", "Last_color:", colors[-1])
