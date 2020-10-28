# How to define a person that has first name, last name and age?

person_list = ["Pepa", "Novak", 23]
person_list_name = person_list[0] # No semantics

person_dictionary = { "first_name": "Pepa", "last_name": "Novak", "age": 23 }
person_dictionary_name = person_dictionary["first_name"] # No way to define function, must rember the strings

# Objects = Data together
# Class = Prescription of shape
class PersonData:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

# Instance of a class = specific data in prescribed shape
pepa = PersonData("Pepa", "Novak", 23)
pepa_name = pepa.first_name

print(pepa_name)
print(pepa.__dict__["first_name"]) # Back to the dictionary...
pepa.favourite_language = "F#" # Assigning undefined variable at first
print(pepa.favourite_language)

def can_drink_alcohol(person):
    return person.age >= 18

print(can_drink_alcohol(pepa))

# Objects = Data + Functions

class PersonWithFunctions:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def can_drink_alcohol(self):
        return self.age >= 18

petr = PersonWithFunctions("Petr", "Novak", 12)
print(petr.can_drink_alcohol())

petr.age = -5 # How to prevent this?

# Objects = private Data + public Functions ?
# Encapsulation: protecting private state, ensuring it is valid

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.set_age(age)

    def can_drink_alcohol(self):
        return self.get_age() >= 18

    def get_age(self):
        return self.__age

    def set_age(self, newAge):
        assert newAge > 0
        self.__age = newAge

pavel = Person("Pavel", "Dvorak", 50)
print(pavel.get_age())
pavel.set_age(51)
print(pavel.get_age())
print(taky_pavel.get_age())
pavel.set_age(-1) # What happens?
print(pavel.__age) # What happens?

# OOP: much more to come!
