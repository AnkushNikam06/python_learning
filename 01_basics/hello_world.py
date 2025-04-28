print("Hello world!")

# Section1: Function
# Next steps
# Open the terminal and run the following command:
# cd 01_basics
# python3 hello_world.py ...(python3 <file_name>)

def world(hello_world):
    print(hello_world)

world("Hello Python")


# Section2: Importing modules
# If you import the module which is hello_world and if you make any changes in the same module, then when you try to run the module again, it will not reflect the changes.
# You have to import the module again. OR 
# You can use the reload function to reload the module.
asia = "INDIA"
europe = "UK"
africa = "NIGERIA"

# Section3: Use reload
# from importlib import reload
# reload(hello_world)
# This will reload the module and reflect the changes made in the module.
# when you will run the module again, it will reflect the changes made in the module.
# cmd: hello_world.asia (from above example)
