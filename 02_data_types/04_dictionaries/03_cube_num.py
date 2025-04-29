# This is a file created to work on the practicals of the course. This is a course based on dictionary index squaring using range. 
# You can simply create a calculator using this code.

n = int(input("Enter the range value: "))
cube_num = {n: n**3 for n in range(n)}

print("The cube of the range value is: ",cube_num)
