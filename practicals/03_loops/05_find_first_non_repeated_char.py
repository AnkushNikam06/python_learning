# Q: Given a string, find the first non-repeated character.

input_string = str(input("Enter the string: "))

for char in input_string:
    if input_string.count(char) == 1:
        print("The first non-repeated character is ", char) 
        break
