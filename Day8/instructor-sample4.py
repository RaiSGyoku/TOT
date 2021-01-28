# Private Access Modifiers , accessing private
class Person:
    # constructor
    def __init__(self, name, age):
        # private data members
        self.__PName = name # double underscore for Private
        self.PAge = age

    def displayAge(self):
        # accessing public data member
        print (f"Age {self.PAge}")
    

# creating object for the class
obj = Person("Julien", 20)
print (f"Name: {obj._Person__PName}") # Accessing via _Class__Variable

# calling public member function of the class
obj.displayAge() # public

