# Create a Dog class:
# It should have an attribute name and breed.
# It should have a method bark() that prints "Woof!".
# Create two Dog objects with different names and breeds.
# Call the bark() method on each object.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"Woof!"
    
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Luna", "German Shepherd")

print(dog1.bark())
print(dog2.bark())
