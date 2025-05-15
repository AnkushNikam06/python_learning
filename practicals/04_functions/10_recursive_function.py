# Q: Create a recursive function to calculate the factorial of a number

n = int(input("Enter the number to calculate factorial: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(n))
