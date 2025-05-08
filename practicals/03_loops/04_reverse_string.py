# Q: Reverse a string using a loop

input_string = str(input("Enter a string you wish to revert: "))
reversed_string = ""

for char in input_string:
    reversed_string =  char + reversed_string 

print(reversed_string)
