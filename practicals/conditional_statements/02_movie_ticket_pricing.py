# Q: Movie tickets priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday

age = int(input("Enter the age: "))
day = str(input("Enter the day: "))

price = 12 if age >= 18 else 8

if day == "Wednesday":
        price -= 2

print("Movie ticket price for you is $", price)
