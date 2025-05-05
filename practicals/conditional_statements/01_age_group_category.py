# Q: Age Group Category: Classify a person's age group: Child (<13), Teenager(13-19), Adult(20-59), Senior(60+)

age = int(input("Enter the age: "))

if  age < 13:
        print("The user is child")

elif age < 20:
        print("The user is Teenager")

elif age < 60:
        print("The user is Adult")

else:
        print("The user is Senior")
