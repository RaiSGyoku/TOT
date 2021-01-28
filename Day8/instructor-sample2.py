# Public Access Modifiers

class Person:
    # constructor
    def __init__(self, name, age):
        # public data members
        self.PName = name
        self.PAge = age

    def displayAge(self):
        # accessing public data member
        print (f"Age {self.PAge}")

person1 = Person("jasper", 24)
Person.displayAge(person1)