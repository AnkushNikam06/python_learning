# Q: Compute the factorial of a number using a while loop

number = int(input("Enter a number to calculate factorial: "))
factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print("Factorial is:", factorial)
