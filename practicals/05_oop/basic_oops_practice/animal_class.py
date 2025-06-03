# Create a Animal class:
# It should have a method speak() that prints a generic "Animal sound".
# Create a Dog class that inherits from Animal and overrides the speak() method to print "Woof!".
# Create a Cat class that inherits from Animal and overrides the speak() method to print "Meow!".
# Create objects of Dog and Cat and call their speak() methods.

class Animal:
    def speak(self):
        print("Animal Sound")


class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

dog = Dog()
cat = Cat()

dog.speak()
cat.speak()
