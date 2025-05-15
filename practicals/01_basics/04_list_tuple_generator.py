# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

# Accepting a sequence of comma-separated numbers from the user
numbers = input("Enter a sequence of comma-separated numbers: ")

List = numbers.split(",")
Tuple = tuple(List)

print("List: ", List)
print("Tuple: ", Tuple)
