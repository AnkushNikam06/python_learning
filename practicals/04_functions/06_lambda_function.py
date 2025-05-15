# Q: Create a lambda function to compute the cube of number.

num = int(input("Enter the number to calculate the cube: "))

cube = lambda num: num ** 3
print(cube(num))
