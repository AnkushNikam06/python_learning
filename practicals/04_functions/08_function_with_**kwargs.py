# Q: Create a function that accepts any number of keyword arguments and print them in the format key:value

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(country="India", continent="Asia")
print_kwargs(country="India")
print_kwargs(country="India", continent="Asia", capital="Delhi")
