# Q: Determine if a year is a leap year. (Leap years are divisible 4, but not try 100 unless also divisible by 400)

year = int(input("Enter the year to check if it is leap year: "))

# leap_year = year/4

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("This is a leap year")

else:
    print("This is not a leap year")
