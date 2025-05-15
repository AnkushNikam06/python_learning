# Q: Write a function that greets a user. If no name provided, it should greet with a default name.

default_name = "user"
username = str(input("Enter the name of the user: "))

def greet(username):
    if username != "":
        print("Welcome", username)
    else:
        print("Welcome", default_name)

greet(username)
