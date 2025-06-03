# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.

name = str(input("Enter the name of person: "))
country = str(input("Enter the country name where person resides: "))
birth_year = input("Enter the Date of birth (YYYY-MM-DD): ")

import datetime
today = datetime.date.today()

class Person:
    def __init__(self, name, country, birth_year):
        self.name = name
        self.country = country
        self.birth_year = datetime.datetime.strptime(birth_year, "%Y-%m-%d").date()

    def person_age(self):
        today = datetime.date.today()
        age = today.year - self.dob.year
        if (today.month, today.day) < (self.birth_year.month, self.birth_year.day):
            age -=1
        return age
    
person = Person(name, country, birth_year)
print(f"{person.name} from {person.country} is {person.person.age()} years old.")
