# Q: Grade Calculator: Assign a letter grade based on a student's score: A (90-100), B(80-89), C(70-79), D(60-69), E(Below 60)

marks = int(input("Enter the marks obtained by the student: "))

if marks > 100:
        print("InvalidValue:Please verify your Grade")
        exit()

if marks >= 90:
        Grade = "A"
elif marks >= 80:
        Grade = "B"
elif marks >= 70:
        Grade = "C"
elif marks >= 60:
        Grade = "D"
else:
        Grade = "E"

print("Grade: ", Grade)
