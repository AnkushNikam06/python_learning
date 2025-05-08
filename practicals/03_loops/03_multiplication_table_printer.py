# Q: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

number = int(input("Enter the number you want to create a table: "))

for i in range(1, 11):
    if i == 5:
        continue
    table = number * i
    print(number, "x", i, "=", table)
